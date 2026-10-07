#!/usr/bin/env python3
"""Phase 6a live execution — RELL Seas Discord setup via direct REST.

ONE script for all Discord API calls. Loads DISCORD_BOT_TOKEN and
DISCORD_SERVER_ID from .env internally. Never prints the token or
request headers. Prints only HTTP status, endpoint path, and
Discord's error code/message.

Modes:
  --preflight (default, read-only): Phase 0 checks only.
  --execute: re-runs preflight first (refuses to continue on failure),
             then Phases 1-7.

Safety: idempotent (lookup by exact name + parent before create;
skip-if-matches, stop-if-differs, never delete/overwrite), 429-aware
(wait retry_after, retry once, stop if >120s), 0.5s pause between
writes, GET-after-create verification, any other failure is a hard
stop with no rollback/cleanup/deletion.

Spec source: build/phase-6a-dry-run.md + build/phase-5-blueprint.md.
Only blueprint-exact text is posted (the fan-run disclaimer line);
anything not worded in the blueprint is an owner to-do, not invented.
"""

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# --------------------------------------------------------------------------
# Named Discord constants (no magic numbers)
# --------------------------------------------------------------------------
API_BASE = "https://discord.com/api/v10"

# Channel types
CH_GUILD_TEXT = 0
CH_GUILD_VOICE = 2
CH_GUILD_CATEGORY = 4
CH_GUILD_FORUM = 15

# Permission flags
PERM_ADMINISTRATOR = 1 << 3
PERM_VIEW_CHANNEL = 1 << 10
PERM_SEND_MESSAGES = 1 << 11
PERM_READ_MESSAGE_HISTORY = 1 << 16
PERM_SEND_MESSAGES_IN_THREADS = 1 << 38

# Verification levels
VERIFY_MEDIUM = 2

# AutoMod trigger types / presets / action types / event types
AM_KEYWORD = 1
AM_SPAM = 3
AM_KEYWORD_PRESET = 4
AM_MENTION_SPAM = 5
AM_PRESET_PROFANITY = 1
AM_PRESET_SLURS = 3
AM_EVENT_MESSAGE_SEND = 1
AM_ACTION_BLOCK = 1
AM_ACTION_ALERT = 2

# Forum 7-day auto-archive (minutes)
ARCHIVE_7_DAYS = 10080

# Write pacing + rate-limit ceiling (seconds)
WRITE_PAUSE = 0.5
RETRY_AFTER_MAX = 120

# Discord requires callers to identify with a User-Agent; urllib's default
# (Python-urllib/...) trips edge bot-protection, so identify the setup bot.
USER_AGENT = "DiscordBot (rell-seas fan-run community setup, phase-6a)"

# Bot identity expected by the brief
EXPECTED_BOT_USERNAME = "RELL Seas Setup Bot"

# Fan-run disclaimer — exact blueprint wording (brief Phase 3). Never rephrase.
DISCLAIMER = (
    "FAN-RUN \u2014 This is a fan-run community, not official. "
    "Not affiliated with the RELL Seas developers. "
    "No official assets used here. Treat everything as community "
    "discussion unless a Keeper post links a primary source."
)

# --------------------------------------------------------------------------
# Intended build (from dry-run plan + blueprint; neutral choices noted)
# --------------------------------------------------------------------------
# Roles: name -> {color (neutral choice, plan leaves unspecified),
#                 permissions (plan specifies none beyond Solo Banner's
#                 "no extra permissions", so all guild-wide 0)}.
INTENDED_ROLES = {
    "Castaway": {"color": 0x95A5A6, "permissions": 0},
    "Watchkeeper": {"color": 0x5DADE2, "permissions": 0},
    "Solo Banner": {"color": 0xAAB7B8, "permissions": 0},
    "Beacon": {"color": 0xF5B041, "permissions": 0},
    "Elder": {"color": 0xAF7AC5, "permissions": 0},
    "Keeper": {"color": 0xE74C3C, "permissions": 0},
}
# Ladder, bottom-up position numbers (all must land below the bot role).
# Solo Banner is holdable flair, parked just above @everyone.
INTENDED_ROLE_ORDER = [
    "Solo Banner",
    "Castaway",
    "Watchkeeper",
    "Beacon",
    "Elder",
    "Keeper",
]

INTENDED_CATEGORIES = [
    "LIGHTHOUSE ENTRY",
    "WATCH DECK",
    "MILESTONE BOARD",
    "HEARTH",
    "OCEAN & HELP",
    "COMMUNITY CRAFT",
    "SAFETY",
]

# Channels: (name, type, category, slowmode, archive, tags, overwrites-key)
# Overwrites resolved in code from role IDs; keys:
#   open      = no overwrites (everyone default)
#   readonly  = @everyone deny SEND (Keeper allow view/send/history)
#   keeper    = @everyone deny SEND, allow view/history/threads (Keeper full)
#   scamwatch = keeper + @everyone explicitly allowed thread replies
#   private   = @everyone deny VIEW (Keeper only)
INTENDED_CHANNELS = [
    ("read-first-rules", CH_GUILD_TEXT, "LIGHTHOUSE ENTRY", 0, None, None, "readonly"),
    ("welcome-in-pt-fr-es", CH_GUILD_TEXT, "LIGHTHOUSE ENTRY", 0, None, None, "readonly"),
    ("watch-deck", CH_GUILD_TEXT, "WATCH DECK", 60, None, None, "open"),
    ("lantern-room", CH_GUILD_TEXT, "WATCH DECK", 60, None, None, "open"),
    ("milestone-board", CH_GUILD_TEXT, "MILESTONE BOARD", 0, None, None, "keeper"),
    ("receipts-and-rumors", CH_GUILD_TEXT, "MILESTONE BOARD", 0, None, None, "open"),
    ("introductions", CH_GUILD_TEXT, "HEARTH", 0, None, None, "open"),
    ("tenure-and-returns", CH_GUILD_TEXT, "HEARTH", 0, None, None, "open"),
    ("finder", CH_GUILD_FORUM, "HEARTH", 0, ARCHIVE_7_DAYS, ["solo-welcome"], "open"),
    ("ocean-joy", CH_GUILD_TEXT, "OCEAN & HELP", 0, None, None, "open"),
    ("help-desk", CH_GUILD_FORUM, "OCEAN & HELP", 0, ARCHIVE_7_DAYS, None, "open"),
    ("patient-craft", CH_GUILD_TEXT, "COMMUNITY CRAFT", 0, None, None, "open"),
    ("creator-mirror", CH_GUILD_TEXT, "COMMUNITY CRAFT", 0, None, None, "open"),
    ("scam-watch-and-report", CH_GUILD_TEXT, "SAFETY", 0, None, None, "scamwatch"),
    ("mod-action-log", CH_GUILD_TEXT, "SAFETY", 0, None, None, "private"),
]

# AutoMod rules: name -> spec. flag_only rule uses ALERT only, never BLOCK.
INTENDED_AUTOMOD = [
    {
        "name": "Long Watch - slurs and profanity",
        "trigger_type": AM_KEYWORD_PRESET,
        "metadata": {"presets": [AM_PRESET_PROFANITY, AM_PRESET_SLURS]},
        "actions": ["block+alert"],
    },
    {
        "name": "Long Watch - spam shield",
        "trigger_type": AM_SPAM,
        "metadata": {},
        "actions": ["block+alert"],
    },
    {
        "name": "Long Watch - mention flood",
        "trigger_type": AM_MENTION_SPAM,
        "metadata": {"mention_total_limit": 7},
        "actions": ["block+alert"],
    },
    {
        "name": "Long Watch - scam bait",
        "trigger_type": AM_KEYWORD,
        "metadata": {
            "keyword_filter": [
                "*free robux*",
                "*free eac*",
                "*eac giveaway*",
                "*robux giveaway*",
            ]
        },
        # Blueprint-named bait phrases only; lookalike domains + slur
        # variants are an owner to-do (freshness flag: refresh blocklist).
        "actions": ["block+alert"],
    },
    {
        "name": "Long Watch - unsourced claims flag",
        "trigger_type": AM_KEYWORD,
        "metadata": {"keyword_filter": ["*eac price*", "*release date*"]},
        # Blueprint-named assertion types only; FLAG-ONLY, never blocked.
        "actions": ["alert"],
    },
]


class HardStop(Exception):
    """Any failure other than a handled rate limit. No retries, no cleanup."""


class Discord:
    def __init__(self, token, log):
        self._token = token
        self._log = log

    def _scrub(self, text):
        # Belt-and-braces: the token must never reach any output.
        try:
            return str(text).replace(self._token, "[REDACTED]")
        except Exception:
            return "<unprintable error>"

    def request(self, method, path, body=None, write=False):
        url = API_BASE + path
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Content-Type", "application/json")
        req.add_header("User-Agent", USER_AGENT)
        # Token travels only in the request header object, never in output.
        req.add_header("Authorization", "Bot " + self._token)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                status = resp.status
                payload = json.loads(resp.read().decode() or "null")
        except urllib.error.HTTPError as e:
            try:
                raw = e.read().decode(errors="replace")
            except Exception:
                raw = ""
            try:
                err = json.loads(raw or "{}")
            except Exception:
                err = {}
            # Exact state for the report: Discord errors are JSON with
            # code/message; anything else (e.g. a proxy block page) is
            # reported by shape only, scrubbed, truncated. Never headers.
            detail = (
                "code=%s message=%s"
                % (err.get("code", "?"), self._scrub(err.get("message", "?")))
                if err
                else "non-json-body len=%d head=%s"
                % (len(raw), self._scrub(raw[:160]))
            )
            if e.code == 429 and write:
                retry_after = float(err.get("retry_after", 0) or 0)
                print(
                    "RATE LIMIT path=%s status=429 retry_after=%s"
                    % (path, retry_after),
                    flush=True,
                )
                if retry_after > RETRY_AFTER_MAX:
                    raise HardStop(
                        "429 retry_after=%s exceeds %ss; stopping. path=%s"
                        % (retry_after, RETRY_AFTER_MAX, path)
                    )
                time.sleep(retry_after)
                # Retry exactly once; a second 429 is a hard stop.
                req2 = urllib.request.Request(url, data=data, method=method)
                req2.add_header("Content-Type", "application/json")
                req2.add_header("User-Agent", USER_AGENT)
                req2.add_header("Authorization", "Bot " + self._token)
                try:
                    with urllib.request.urlopen(req2, timeout=30) as resp2:
                        status2 = resp2.status
                        payload2 = json.loads(resp2.read().decode() or "null")
                except urllib.error.HTTPError as e2:
                    try:
                        raw2 = e2.read().decode(errors="replace")
                    except Exception:
                        raw2 = ""
                    try:
                        err2 = json.loads(raw2 or "{}")
                    except Exception:
                        err2 = {}
                    detail2 = (
                        "code=%s message=%s"
                        % (
                            err2.get("code", "?"),
                            self._scrub(err2.get("message", "?")),
                        )
                        if err2
                        else "non-json-body len=%d head=%s"
                        % (len(raw2), self._scrub(raw2[:160]))
                    )
                    raise HardStop(
                        "HTTP %s path=%s %s (after 429 retry)" % (e2.code, path, detail2)
                    )
                print("OK path=%s status=%s (after 429 retry)" % (path, status2), flush=True)
                if write:
                    time.sleep(WRITE_PAUSE)
                return status2, payload2
            raise HardStop("HTTP %s path=%s %s" % (e.code, path, detail))
        except HardStop:
            raise
        except Exception as e:
            raise HardStop("TRANSPORT path=%s error=%s" % (path, self._scrub(e)))
        print("OK path=%s status=%s" % (path, status), flush=True)
        if write:
            time.sleep(WRITE_PAUSE)
        return status, payload

    def get(self, path):
        return self.request("GET", path)[1]

    def post(self, path, body):
        return self.request("POST", path, body, write=True)[1]

    def patch(self, path, body):
        return self.request("PATCH", path, body, write=True)[1]

    def put(self, path, body):
        return self.request("PUT", path, body, write=True)[1]


def load_env(root):
    env = {}
    for line in (root / ".env").read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip("\"'")
    token = env.get("DISCORD_BOT_TOKEN", "")
    server = env.get("DISCORD_SERVER_ID", "")
    if not token or not server:
        raise HardStop("MISSING .env keys: need DISCORD_BOT_TOKEN + DISCORD_SERVER_ID")
    return token, server


def log_line(log_path, text):
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(log_path, "a") as f:
        f.write("%s %s\n" % (stamp, text))
    print("LOG %s" % text, flush=True)


# --------------------------------------------------------------------------
# Phase 0: Preflight (read-only)
# --------------------------------------------------------------------------
def preflight(api, guild_id, log_path):
    log_line(log_path, "PREFLIGHT start")
    me = api.get("/users/@me")
    username = me.get("username", "?")
    print("PREFLIGHT bot_user=%s" % username, flush=True)
    log_line(log_path, "PREFLIGHT bot_user=%s status=bot-identity" % username)
    if username != EXPECTED_BOT_USERNAME:
        raise HardStop(
            "bot username is '%s', expected '%s'; stopping (wrong token/server?)"
            % (username, EXPECTED_BOT_USERNAME)
        )

    guild = api.get("/guilds/%s?with_counts=true" % guild_id)
    gname = guild.get("name", "?")
    members = guild.get("approximate_member_count", "?")
    features = guild.get("features", [])
    print("PREFLIGHT guild=%s members=%s features=%s" % (gname, members, ",".join(features)), flush=True)
    log_line(
        log_path,
        "PREFLIGHT guild name=%s members=%s features=%s status=guild-info"
        % (gname, members, ",".join(features)),
    )
    if isinstance(members, int) and members > 5:
        raise HardStop("member count %d above 5; likely wrong server; stopping" % members)
    if "COMMUNITY" not in features:
        raise HardStop(
            "guild lacks COMMUNITY feature; owner must enable Community in "
            "Server Settings first (API cannot enable it); stopping"
        )

    channels = api.get("/guilds/%s/channels" % guild_id)
    roles = api.get("/guilds/%s/roles" % guild_id)

    expected_names = {
        "Text channels",
        "Voice channels",
        "general",
        "General",
        "rules",
        "moderator-only",
        "moderators-only",
        "community-updates",
    }
    for c in channels:
        log_line(
            log_path,
            "PRE-EXISTING channel type=%s name=%s id=%s status=pre-existing"
            % (c.get("type"), c.get("name"), c.get("id")),
        )
        if c.get("name") not in expected_names:
            raise HardStop(
                "unexpected pre-existing channel '%s' (id=%s); stopping "
                "rather than touching an unknown server state"
                % (c.get("name"), c.get("id"))
            )

    bot_role = None
    for r in roles:
        managed = bool(r.get("managed"))
        log_line(
            log_path,
            "PRE-EXISTING role name=%s id=%s managed=%s status=pre-existing"
            % (r.get("name"), r.get("id"), managed),
        )
        if r.get("name") == "@everyone":
            continue
        if not managed:
            raise HardStop(
                "unexpected unmanaged role '%s' (id=%s); stopping" % (r.get("name"), r.get("id"))
            )
        tags = r.get("tags") or {}
        if str(tags.get("bot_id")) == str(me.get("id")):
            bot_role = r
    if bot_role is None:
        raise HardStop("bot role not found among guild roles; stopping")
    perms = int(bot_role.get("permissions", "0"))
    if not (perms & PERM_ADMINISTRATOR):
        raise HardStop("bot role '%s' lacks Administrator; stopping" % bot_role.get("name"))
    print(
        "PREFLIGHT bot_role=%s position=%s admin=yes"
        % (bot_role.get("name"), bot_role.get("position")),
        flush=True,
    )
    log_line(
        log_path,
        "PREFLIGHT bot_role=%s id=%s position=%s administrator=yes status=clean"
        % (bot_role.get("name"), bot_role.get("id"), bot_role.get("position")),
    )
    log_line(log_path, "PREFLIGHT result=clean")
    print("PREFLIGHT result=clean", flush=True)
    return {"me": me, "guild": guild, "channels": channels, "roles": roles, "bot_role": bot_role}


# --------------------------------------------------------------------------
# Phase 1: Roles
# --------------------------------------------------------------------------
def ensure_roles(api, guild_id, log_path, bot_role):
    existing = {r["name"]: r for r in api.get("/guilds/%s/roles" % guild_id)}
    ids = {}
    for name, spec in INTENDED_ROLES.items():
        if name in existing:
            r = existing[name]
            if int(r.get("color", 0)) != spec["color"] or int(r.get("permissions", "0")) != spec[
                "permissions"
            ]:
                raise HardStop(
                    "role '%s' exists but differs (color/permissions); "
                    "refusing to overwrite; id=%s" % (name, r.get("id"))
                )
            print("SKIP role exists+matches name=%s id=%s" % (name, r.get("id")), flush=True)
            log_line(log_path, "ROLE name=%s id=%s status=skipped-exists" % (name, r.get("id")))
            ids[name] = r["id"]
            continue
        created = api.post(
            "/guilds/%s/roles" % guild_id,
            {
                "name": name,
                "color": spec["color"],
                "permissions": str(spec["permissions"]),
                "hoist": False,
                "mentionable": False,
            },
        )
        # GET-after-create verification.
        check = {r["name"]: r for r in api.get("/guilds/%s/roles" % guild_id)}.get(name)
        if (
            check is None
            or int(check.get("color", -1)) != spec["color"]
            or int(check.get("permissions", "-1")) != spec["permissions"]
        ):
            raise HardStop("role '%s' verify mismatch after create; stopping" % name)
        print("CREATED role name=%s id=%s" % (name, check["id"]), flush=True)
        log_line(
            log_path,
            "ROLE name=%s id=%s color=%s permissions=%s status=created"
            % (name, check["id"], spec["color"], spec["permissions"]),
        )
        ids[name] = check["id"]
        _ = created

    # Order Keeper(top) > Elder > Beacon > Watchkeeper > Castaway, below bot.
    # Order Keeper(top) > Elder > Beacon > Watchkeeper > Castaway, all below
    # the bot's own role. Fresh roles land at the bottom, so the bot role is
    # included in the bulk move at the top; then positions are verified.
    payload = [{"id": ids[n], "position": i + 1} for i, n in enumerate(INTENDED_ROLE_ORDER)]
    payload.append({"id": bot_role["id"], "position": len(INTENDED_ROLE_ORDER) + 1})
    api.patch("/guilds/%s/roles" % guild_id, payload)
    verify = {r["name"]: r for r in api.get("/guilds/%s/roles" % guild_id)}
    positions = {n: int(verify[n]["position"]) for n in INTENDED_ROLE_ORDER}
    bot_pos = int(verify[bot_role["name"]]["position"])
    ladder_ok = (
        positions["Keeper"]
        > positions["Elder"]
        > positions["Beacon"]
        > positions["Watchkeeper"]
        > positions["Castaway"]
    )
    below_bot = all(p < bot_pos for p in positions.values())
    if not ladder_ok or not below_bot:
        raise HardStop("role order verify failed: %s; stopping" % positions)
    print("ROLES ordered positions=%s bot_below_ok=yes" % positions, flush=True)
    log_line(log_path, "ROLES order=%s status=verified (Solo Banner flair parked lowest)" % positions)
    return ids


# --------------------------------------------------------------------------
# Phase 2: Categories
# --------------------------------------------------------------------------
def ensure_categories(api, guild_id, log_path):
    channels = api.get("/guilds/%s/channels" % guild_id)
    by_name = {}
    for c in channels:
        if c.get("type") == CH_GUILD_CATEGORY:
            by_name.setdefault(c.get("name"), []).append(c)
    ids = {}
    for name in INTENDED_CATEGORIES:
        if name in by_name:
            if len(by_name[name]) > 1:
                raise HardStop("duplicate category '%s'; stopping" % name)
            c = by_name[name][0]
            print("SKIP category exists name=%s id=%s" % (name, c["id"]), flush=True)
            log_line(log_path, "CATEGORY name=%s id=%s status=skipped-exists" % (name, c["id"]))
            ids[name] = c["id"]
            continue
        created = api.post(
            "/guilds/%s/channels" % guild_id, {"name": name, "type": CH_GUILD_CATEGORY}
        )
        check = api.get("/channels/%s" % created["id"])
        if check.get("name") != name or check.get("type") != CH_GUILD_CATEGORY:
            raise HardStop("category '%s' verify mismatch; stopping" % name)
        print("CREATED category name=%s id=%s" % (name, check["id"]), flush=True)
        log_line(log_path, "CATEGORY name=%s id=%s status=created" % (name, check["id"]))
        ids[name] = check["id"]
    return ids


# --------------------------------------------------------------------------
# Phase 3: Channels
# --------------------------------------------------------------------------
def build_overwrites(kind, everyone_id, keeper_id):
    E = {"id": everyone_id, "type": 0}
    K = {"id": keeper_id, "type": 0}

    def ow(base, allow=0, deny=0):
        o = dict(base)
        o["allow"] = str(allow)
        o["deny"] = str(deny)
        return o

    view = PERM_VIEW_CHANNEL | PERM_READ_MESSAGE_HISTORY
    send = view | PERM_SEND_MESSAGES
    if kind == "open":
        return []
    if kind == "readonly":
        return [
            ow(E, allow=view, deny=PERM_SEND_MESSAGES),
            ow(K, allow=send | PERM_SEND_MESSAGES_IN_THREADS),
        ]
    if kind == "keeper":
        return [
            ow(E, allow=view, deny=PERM_SEND_MESSAGES),
            ow(K, allow=send | PERM_SEND_MESSAGES_IN_THREADS),
        ]
    if kind == "scamwatch":
        # Keeper-post-only at top level; members may reply in threads.
        return [
            ow(
                E,
                allow=view | PERM_SEND_MESSAGES_IN_THREADS,
                deny=PERM_SEND_MESSAGES,
            ),
            ow(K, allow=send | PERM_SEND_MESSAGES_IN_THREADS),
        ]
    if kind == "private":
        return [
            ow(E, deny=PERM_VIEW_CHANNEL),
            ow(K, allow=send),
        ]
    raise HardStop("unknown overwrite kind '%s'" % kind)


def overwrites_match(actual, expected):
    a = {o["id"]: (int(o.get("allow", "0")), int(o.get("deny", "0"))) for o in (actual or [])}
    e = {o["id"]: (int(o.get("allow", "0")), int(o.get("deny", "0"))) for o in expected}
    return a == e


def ensure_channels(api, guild_id, log_path, cat_ids, role_ids):
    everyone_id = guild_id  # @everyone shares the guild id
    keeper_id = role_ids["Keeper"]
    channels = api.get("/guilds/%s/channels" % guild_id)
    by_key = {}
    for c in channels:
        by_key.setdefault((c.get("name"), c.get("parent_id")), []).append(c)
    ids = {}
    for name, ctype, cat, slowmode, archive, tags, kind in INTENDED_CHANNELS:
        parent = cat_ids[cat]
        expected_ow = build_overwrites(kind, everyone_id, keeper_id)
        topic = DISCLAIMER if name == "read-first-rules" else None
        key = (name, parent)
        if key in by_key:
            if len(by_key[key]) > 1:
                raise HardStop("duplicate channel '%s' under '%s'; stopping" % (name, cat))
            c = by_key[key][0]
            full = api.get("/channels/%s" % c["id"])
            problems = []
            if full.get("type") != ctype:
                problems.append("type")
            if (full.get("topic") or "") != (topic or ""):
                problems.append("topic")
            if int(full.get("rate_limit_per_user", 0) or 0) != slowmode:
                problems.append("slowmode")
            if archive is not None and int(
                full.get("default_auto_archive_duration", 0) or 0
            ) != archive:
                problems.append("archive")
            if not overwrites_match(full.get("permission_overwrites"), expected_ow):
                problems.append("overwrites")
            if ctype == CH_GUILD_FORUM and tags:
                have = {t.get("name") for t in full.get("available_tags", [])}
                if not set(tags) <= have:
                    problems.append("tags")
            if problems:
                raise HardStop(
                    "channel '%s' exists but differs (%s); refusing to overwrite; id=%s"
                    % (name, ",".join(problems), c["id"])
                )
            print("SKIP channel exists+matches name=%s id=%s" % (name, c["id"]), flush=True)
            log_line(log_path, "CHANNEL name=%s id=%s status=skipped-exists" % (name, c["id"]))
            ids[name] = c["id"]
            continue
        body = {"name": name, "type": ctype, "parent_id": parent}
        if slowmode:
            body["rate_limit_per_user"] = slowmode
        if topic:
            body["topic"] = topic
        if ctype == CH_GUILD_FORUM and archive:
            body["default_auto_archive_duration"] = archive
        if ctype == CH_GUILD_FORUM and tags:
            body["available_tags"] = [{"name": t, "moderated": False} for t in tags]
        if expected_ow:
            body["permission_overwrites"] = expected_ow
        created = api.post("/guilds/%s/channels" % guild_id, body)
        check = api.get("/channels/%s" % created["id"])
        problems = []
        if check.get("name") != name or check.get("type") != ctype:
            problems.append("name/type")
        if check.get("parent_id") != parent:
            problems.append("parent")
        if (check.get("topic") or "") != (topic or ""):
            problems.append("topic")
        if int(check.get("rate_limit_per_user", 0) or 0) != slowmode:
            problems.append("slowmode")
        if not overwrites_match(check.get("permission_overwrites"), expected_ow):
            problems.append("overwrites")
        if problems:
            raise HardStop(
                "channel '%s' verify mismatch (%s); stopping" % (name, ",".join(problems))
            )
        print("CREATED channel name=%s id=%s" % (name, check["id"]), flush=True)
        log_line(
            log_path,
            "CHANNEL name=%s id=%s parent=%s slowmode=%s overwrites=%s status=created"
            % (name, check["id"], cat, slowmode, kind),
        )
        ids[name] = check["id"]

    # Private mod-action-log double-check (brief Phase 3).
    modlog = api.get("/channels/%s" % ids["mod-action-log"])
    ow = {o["id"]: o for o in modlog.get("permission_overwrites", [])}
    ev = ow.get(everyone_id)
    kp = ow.get(keeper_id)
    if (
        ev is None
        or not (int(ev.get("deny", "0")) & PERM_VIEW_CHANNEL)
        or kp is None
        or not (int(kp.get("allow", "0")) & PERM_VIEW_CHANNEL)
    ):
        raise HardStop("mod-action-log privacy double-check failed; stopping")
    if len(ow) != 2:
        raise HardStop("mod-action-log has %d overwrites, expected 2; stopping" % len(ow))
    log_line(log_path, "CHANNEL mod-action-log privacy double-check passed status=verified")
    print("PRIVACY mod-action-log double-check passed", flush=True)

    # Disclaimer post + pin in #read-first-rules (only blueprint-exact text).
    rules_ch = ids["read-first-rules"]
    pins = api.get("/channels/%s/pins" % rules_ch)
    if not any(DISCLAIMER == (m.get("content") or "") for m in pins):
        posted = api.post("/channels/%s/messages" % rules_ch, {"content": DISCLAIMER})
        api.request("PUT", "/channels/%s/pins/%s" % (rules_ch, posted["id"]), write=True)
        check_pins = api.get("/channels/%s/pins" % rules_ch)
        if not any(DISCLAIMER == (m.get("content") or "") for m in check_pins):
            raise HardStop("disclaimer pin verify failed; stopping")
        log_line(
            log_path,
            "PIN channel=read-first-rules message_id=%s status=created (disclaimer only)"
            % posted["id"],
        )
        print("PIN disclaimer posted+pinned message_id=%s" % posted["id"], flush=True)
    else:
        log_line(log_path, "PIN channel=read-first-rules status=skipped-exists")
        print("SKIP disclaimer already pinned", flush=True)
    return ids


# --------------------------------------------------------------------------
# Phase 4: AutoMod
# --------------------------------------------------------------------------
def automod_actions(spec_actions, modlog_id):
    acts = []
    if "block+alert" in spec_actions:
        acts.append({"type": AM_ACTION_BLOCK, "metadata": {}})
        acts.append({"type": AM_ACTION_ALERT, "metadata": {"channel_id": modlog_id}})
    elif spec_actions == ["alert"]:
        acts.append({"type": AM_ACTION_ALERT, "metadata": {"channel_id": modlog_id}})
    else:
        raise HardStop("unknown automod action spec %s" % spec_actions)
    return acts


def automod_match(rule, spec, modlog_id):
    if int(rule.get("trigger_type", -1)) != spec["trigger_type"]:
        return False, "trigger_type"
    want_actions = automod_actions(spec["actions"], modlog_id)
    got = [(a.get("type"), (a.get("metadata") or {}).get("channel_id")) for a in rule.get("actions", [])]
    want = [(a.get("type"), (a.get("metadata") or {}).get("channel_id")) for a in want_actions]
    if got != want:
        return False, "actions"
    meta = rule.get("trigger_metadata") or {}
    if spec["trigger_type"] == AM_KEYWORD_PRESET:
        if sorted(meta.get("presets", [])) != sorted(spec["metadata"].get("presets", [])):
            return False, "presets"
    if spec["trigger_type"] == AM_KEYWORD:
        if sorted(meta.get("keyword_filter", [])) != sorted(
            spec["metadata"].get("keyword_filter", [])
        ):
            return False, "keyword_filter"
    if spec["trigger_type"] == AM_MENTION_SPAM:
        if int(meta.get("mention_total_limit", -1)) != int(
            spec["metadata"].get("mention_total_limit", -1)
        ):
            return False, "mention_total_limit"
    return True, ""


def ensure_automod(api, guild_id, log_path, modlog_id):
    existing = {r["name"]: r for r in api.get("/guilds/%s/auto-moderation/rules" % guild_id)}
    for spec in INTENDED_AUTOMOD:
        name = spec["name"]
        if name in existing:
            ok, field = automod_match(existing[name], spec, modlog_id)
            if not ok:
                raise HardStop(
                    "automod rule '%s' exists but differs (%s); refusing to overwrite; id=%s"
                    % (name, field, existing[name].get("id"))
                )
            # Action-split verification (brief Phase 4).
            types = [a.get("type") for a in existing[name].get("actions", [])]
            if spec["actions"] == ["alert"] and types != [AM_ACTION_ALERT]:
                raise HardStop("flag-only rule '%s' has non-alert actions; stopping" % name)
            print("SKIP automod exists+matches name=%s" % name, flush=True)
            log_line(
                log_path,
                "AUTOMOD name=%s id=%s status=skipped-exists"
                % (name, existing[name].get("id")),
            )
            continue
        body = {
            "name": name,
            "event_type": AM_EVENT_MESSAGE_SEND,
            "trigger_type": spec["trigger_type"],
            "trigger_metadata": dict(spec["metadata"]),
            "actions": automod_actions(spec["actions"], modlog_id),
            "enabled": True,
        }
        created = api.post("/guilds/%s/auto-moderation/rules" % guild_id, body)
        check = api.get(
            "/guilds/%s/auto-moderation/rules/%s" % (guild_id, created["id"])
        )
        ok, field = automod_match(check, spec, modlog_id)
        if not ok:
            raise HardStop("automod rule '%s' verify mismatch (%s); stopping" % (name, field))
        types = [a.get("type") for a in check.get("actions", [])]
        if spec["actions"] == ["alert"] and types != [AM_ACTION_ALERT]:
            raise HardStop("flag-only rule '%s' verify: non-alert actions; stopping" % name)
        if spec["actions"] != ["alert"] and AM_ACTION_BLOCK not in types:
            raise HardStop("block rule '%s' verify: no block action; stopping" % name)
        print("CREATED automod name=%s id=%s" % (name, check["id"]), flush=True)
        log_line(
            log_path,
            "AUTOMOD name=%s id=%s actions=%s status=created"
            % (name, check["id"], ",".join(spec["actions"])),
        )


# --------------------------------------------------------------------------
# Phase 5 / 5b / 6 / 7
# --------------------------------------------------------------------------
def ensure_verification(api, guild_id, log_path):
    guild = api.get("/guilds/%s" % guild_id)
    if int(guild.get("verification_level", -1)) == VERIFY_MEDIUM:
        log_line(log_path, "VERIFY level=Medium status=skipped-exists")
        print("SKIP verification already Medium", flush=True)
        return
    api.patch("/guilds/%s" % guild_id, {"verification_level": VERIFY_MEDIUM})
    check = api.get("/guilds/%s" % guild_id)
    if int(check.get("verification_level", -1)) != VERIFY_MEDIUM:
        raise HardStop("verification level verify failed; stopping")
    log_line(log_path, "VERIFY level=Medium status=set+verified")
    print("VERIFY set to Medium, verified", flush=True)


def soft_community_pointers(api, guild_id, log_path, chan_ids):
    # Soft-fail point: API rejection is reported, defaults left alone.
    try:
        api.patch("/guilds/%s" % guild_id, {"rules_channel_id": chan_ids["read-first-rules"]})
        check = api.get("/guilds/%s" % guild_id)
        if str(check.get("rules_channel_id") or "") != str(chan_ids["read-first-rules"]):
            raise HardStop("rules channel pointer verify mismatch")
        log_line(
            log_path,
            "COMMUNITY rules_channel=read-first-rules id=%s status=set" % chan_ids["read-first-rules"],
        )
        print("COMMUNITY rules channel pointed at read-first-rules", flush=True)
    except HardStop as e:
        log_line(log_path, "COMMUNITY rules_channel status=soft-fail (%s); defaults kept" % e)
        print("SOFT-FAIL rules channel pointer: %s" % e, flush=True)
    try:
        api.patch(
            "/guilds/%s" % guild_id, {"public_updates_channel_id": chan_ids["mod-action-log"]}
        )
        check = api.get("/guilds/%s" % guild_id)
        if str(check.get("public_updates_channel_id") or "") != str(chan_ids["mod-action-log"]):
            raise HardStop("updates channel pointer verify mismatch")
        log_line(
            log_path,
            "COMMUNITY updates_channel=mod-action-log id=%s status=set" % chan_ids["mod-action-log"],
        )
        print("COMMUNITY updates channel pointed at mod-action-log", flush=True)
    except HardStop as e:
        log_line(log_path, "COMMUNITY updates_channel status=soft-fail (%s); defaults kept" % e)
        print("SOFT-FAIL updates channel pointer: %s" % e, flush=True)


def soft_onboarding(api, guild_id, log_path, role_ids, chan_ids):
    # Soft-fail point: at most one retry, then manual-setup report.
    try:
        return _onboarding_attempt(api, guild_id, log_path, role_ids, chan_ids, attempt=1)
    except HardStop as e:
        log_line(log_path, "ONBOARDING attempt=1 status=failed (%s); retrying once" % e)
        print("ONBOARDING attempt 1 failed, retrying once: %s" % e, flush=True)
        try:
            return _onboarding_attempt(
                api, guild_id, log_path, role_ids, chan_ids, attempt=2, minimal=True
            )
        except HardStop as e2:
            log_line(
                log_path,
                "ONBOARDING status=soft-fail (onboarding needs manual setup in the dashboard; %s)"
                % e2,
            )
            print("SOFT-FAIL onboarding needs manual setup in the dashboard", flush=True)
            return "manual"


def _onboarding_attempt(api, guild_id, log_path, role_ids, chan_ids, attempt, minimal=False):
    current = api.get("/guilds/%s/onboarding" % guild_id)
    log_line(
        log_path,
        "ONBOARDING attempt=%d current enabled=%s prompts=%d status=read"
        % (attempt, current.get("enabled"), len(current.get("prompts", []))),
    )
    # Prerequisite: enough default-eligible channels where @everyone can view+send.
    channels = api.get("/guilds/%s/channels" % guild_id)
    eligible = []
    for c in channels:
        if c.get("type") != CH_GUILD_TEXT:
            continue
        denied = 0
        for o in c.get("permission_overwrites", []) or []:
            if o.get("id") == guild_id and int(o.get("type", 0)) == 0:
                denied = int(o.get("deny", "0"))
        if not (denied & (PERM_VIEW_CHANNEL | PERM_SEND_MESSAGES)):
            eligible.append(c)
    if len(eligible) < 3:
        raise HardStop("only %d @everyone view+send channels; prerequisite not met" % len(eligible))
    defaults = (
        [chan_ids["introductions"], chan_ids["watch-deck"]]
        if minimal
        else [
            chan_ids["read-first-rules"],
            chan_ids["introductions"],
            chan_ids["watch-deck"],
        ]
    )
    body = {
        "default_channel_ids": defaults,
        "enabled": True,
        "prompts": [
            {
                "title": "Do you accept the rules?",
                "single_select": True,
                "required": True,
                "in_onboarding": True,
                "type": 0,
                "options": [
                    {
                        "title": "I accept the rules",
                        "description": "Accept the rules in #read-first-rules, join as Watchkeeper.",
                        "channel_ids": [],
                        "role_ids": [role_ids["Watchkeeper"]],
                    }
                ],
            }
        ],
    }
    updated = api.put("/guilds/%s/onboarding" % guild_id, body)
    prompts = updated.get("prompts", []) or []
    linked = any(
        role_ids["Watchkeeper"] in (opt.get("role_ids") or [])
        for p in prompts
        for opt in p.get("options", [])
    )
    if not updated.get("enabled") or not linked:
        raise HardStop("onboarding verify failed (enabled/link)")
    log_line(
        log_path,
        "ONBOARDING attempt=%d enabled=yes watchkeeper-linked=yes defaults=%s status=set+verified"
        % (attempt, ",".join(defaults)),
    )
    print("ONBOARDING configured (attempt %d), verified" % attempt, flush=True)
    return "auto"


def final_verification(api, guild_id, log_path, role_ids, cat_ids, chan_ids):
    channels = api.get("/guilds/%s/channels" % guild_id)
    roles = api.get("/guilds/%s/roles" % guild_id)
    rules = api.get("/guilds/%s/auto-moderation/rules" % guild_id)
    have_channels = {c.get("name") for c in channels}
    have_roles = {r.get("name") for r in roles}
    have_rules = {r.get("name") for r in rules}
    missing = []
    for name, _ctype, _cat, _sm, _arch, _tags, _kind in INTENDED_CHANNELS:
        if name not in have_channels:
            missing.append("channel:" + name)
    for name in INTENDED_CATEGORIES:
        if name not in have_channels:
            missing.append("category:" + name)
    for name in INTENDED_ROLES:
        if name not in have_roles:
            missing.append("role:" + name)
    for spec in INTENDED_AUTOMOD:
        if spec["name"] not in have_rules:
            missing.append("automod:" + spec["name"])
    if missing:
        raise HardStop("final verification missing: %s" % ", ".join(missing))
    log_line(
        log_path,
        "FINAL channels=%d roles=%d automod=%d missing=none status=verified"
        % (len(channels), len(roles), len(rules)),
    )
    print(
        "FINAL verified channels=%d roles=%d automod=%d" % (len(channels), len(roles), len(rules)),
        flush=True,
    )
    api_impossible = [
        "full 6-rules/report-path/parity/partner text (not worded in blueprint; owner to-do)",
        "PT/FR/ES blurb translation (needs human check; owner to-do)",
        "milestone-board Day-1 seeds (need freshness re-check; not authorized this session)",
        "helper-bot welcome-DM/reaction-role (Phase 6b scope)",
        "scam lookalike-domain + slur-variant keyword extension (blocklist refresh; owner to-do)",
    ]
    for item in api_impossible:
        log_line(log_path, "API-IMPOSSIBLE/TODO %s" % item)
    _ = (role_ids, cat_ids, chan_ids)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preflight", action="store_true")
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()
    mode = "execute" if args.execute else "preflight"

    root = Path(__file__).resolve().parents[2]
    log_path = root / "build" / "phase-6a-execution-log.md"
    if not log_path.exists():
        with open(log_path, "w") as f:
            f.write("# Phase 6a execution log\n\n")
            f.write("Spec: build/phase-6a-dry-run.md + build/phase-5-blueprint.md.\n")
            f.write("Entries append as the run goes, so a cut-off session keeps a record.\n\n")

    try:
        token, guild_id = load_env(root)
    except HardStop as e:
        print("HARD STOP preflight error=%s" % e, flush=True)
        return 1
    api = Discord(token, log_path)
    # Drop the in-memory token reference as soon as the client owns it.
    del token

    log_line(log_path, "RUN mode=%s start" % mode)
    try:
        pf = preflight(api, guild_id, log_path)
    except HardStop as e:
        log_line(log_path, "HARD STOP phase=preflight error=%s" % e)
        print("HARD STOP phase=preflight error=%s" % e, flush=True)
        return 1

    if mode == "preflight":
        log_line(log_path, "RUN mode=preflight done; no writes performed")
        log_line(
            log_path,
            "SECRET-HYGIENE token never appeared in any output or file (preflight)",
        )
        print("PREFLIGHT DONE no-writes", flush=True)
        return 0

    try:
        role_ids = ensure_roles(api, guild_id, log_path, pf["bot_role"])
        cat_ids = ensure_categories(api, guild_id, log_path)
        chan_ids = ensure_channels(api, guild_id, log_path, cat_ids, role_ids)
        ensure_automod(api, guild_id, log_path, chan_ids["mod-action-log"])
        ensure_verification(api, guild_id, log_path)
        soft_community_pointers(api, guild_id, log_path, chan_ids)
        onboarding = soft_onboarding(api, guild_id, log_path, role_ids, chan_ids)
        log_line(log_path, "ONBOARDING final=%s" % onboarding)
        final_verification(api, guild_id, log_path, role_ids, cat_ids, chan_ids)
    except HardStop as e:
        log_line(log_path, "HARD STOP phase=execute error=%s (no rollback/cleanup per brief)" % e)
        print("HARD STOP phase=execute error=%s" % e, flush=True)
        return 1

    log_line(log_path, "RUN mode=execute done status=complete")
    log_line(log_path, "SECRET-HYGIENE token never appeared in any output or file")
    print("EXECUTE DONE complete", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
