# Phase 6a — Dry-Run Plan (NO live changes)

Date: 2026-10-06. Input: `build/phase-5-blueprint.md` §§1–4, 7–8. Brief: `build/briefs/phase-6a-server-build.md`.
Bot token: `[REDACTED]` (never read, printed, or committed per AGENTS.md + phase-6a brief).

## Safety statement (read first)
- No connection to the live server was made. `.env` was not read. No category, channel, role, or setting was created, modified, or deleted.
- TASK Step 4 asked for a live-connected dry run via bot token; AGENTS.md wins on conflict (never read `.env`; do not touch token/live server). This plan is therefore derived purely from the blueprint spec — the guaranteed-safe dry run.
- Live execution remains blocked until explicit owner confirmation in a new brief.

## Tooling confirmed (TASK Step 2)
- No Discord MCP server configured (`opencode.json` has no `mcp` section; `.opencode/` holds agents only).
- No `discord.py` / `discord.js` installed (`discord.py: False`, `discord.js: false`).
- Available: Python 3.14 + `requests`/`httpx`/`aiohttp`, Node v25, `curl` 8.7.1 → direct Discord REST (`https://discord.com/api/v10`) is what 6a-execution would use. No bot-code dependency for 6a (6b covers hosting).

## Onboarding-role finding (TASK Step 3, via @fact-checker, one question — in-session result, ledger entry pending)
- Q: can Server Settings → Onboarding assign a role automatically on completion, independent of verification level?
- VERDICT: UNVERIFIABLE (docs reviewed, no auto-on-completion role). ANSWER: No — per in-session check, Onboarding grants roles only when a member picks an answer linked to that role; Verification Level is a separate Safety Setup gate on chatting. SOURCES: https://support.discord.com/hc/en-us/articles/11074987197975-Community-Onboarding-FAQ, https://support.discord.com/hc/en-us/articles/216679607-Verification-Levels. CHECKED: 2026-10-06. Session: ses_eef7b9390ffe7jBaAyrJGbFZGl. No `fact-ledger.md` entry was written (ledger is @fact-checker-only) — treat as not-yet-verified and re-confirm via ledger before any execution.
- Consequence for blueprint: the "autorole on verify" replacement does NOT apply. Keep blueprint §3 mechanism: helper-bot autorole grants Watchkeeper on onboarding completion (free-tier, 6b to confirm); guaranteed fallback is Keeper batch-grant on 10–15-min check-ins. No native-only auto-role; no bot code in 6a.

## Would-create list (exact blueprint order; 7 categories / 14 member-visible channels + 1 private staff-only channel not counted in the 14)

### A. LIGHTHOUSE ENTRY (read-only except where noted)
1. `#read-first-rules` (text, read-only) — pin: fan-run disclaimer line 1 + 6 rules + report path + Solo Banner parity line + English-only + generic partner line. Topic mirrors disclaimer.
2. `#welcome-in-pt-fr-es` (text, read-only, locked) — human-checked static PT/FR/ES blurb only (fan-run + English-only scope + generic partner direction + report path). No discussion.

### B. WATCH DECK (slowmode 60s both, from day one)
3. `#watch-deck` (text, slowmode 60s) — grief-humor containment; heckler-fatigue rule pinned.
4. `#lantern-room` (text, slowmode 60s) — earnest waiting / hope talk.

### C. MILESTONE BOARD (strictest scope)
5. `#milestone-board` (text, Keeper-post-only; members discuss in threads) — shipped-only + source link + date-posted + confirmed-vs-rumor label; include "fan curation — check the linked source" line in every Keeper post/template.
6. `#receipts-and-rumors` (text; 30s slowmode preset toggle during spikes) — pinned label template (Confirmed/Rumor + source link or "no source"); evidence-over-insults norm pinned.

### D. HEARTH
7. `#introductions` (text) — template: callsign / sailed-from / solo-or-looking / one ocean joy.
8. `#tenure-and-returns` (text) — tenure honors (no invented lineage) + reunion boards + return doors alongside real milestones only.
9. `#finder` (forum channel, native auto-archive 7 days inactive) — crew/friend finder + Solo Banner opt-in flair + solo-welcome tag; stale threads archive, re-post to re-confirm.

### E. OCEAN & HELP
10. `#ocean-joy` (text) — showcase tagged confirmed-or-community-wish; comparison overflow rule pinned.
11. `#help-desk` (forum channel, native auto-archive 7 days) — one question per thread; sourced-only answers, unknowns marked.

### F. COMMUNITY CRAFT
12. `#patient-craft` (text) — patience/myth/slang with author credit; new entries only with substance/sources.
13. `#creator-mirror` (text) — sourced creator mirrors in English with credit frames; corrections welcomed.

### G. SAFETY
14. `#scam-watch-and-report` (text, Keeper-post-only + thread replies) — pinned single report/appeals path + genuine-link list; victim guidance (official support + evidence preservation, never passwords/tokens).
- (private, not counted in the 14) `#mod-action-log` (private, staff-only, NOT member-visible) — every AutoMod hit + Keeper action; no public summary.

## Roles would-create (5 rungs + 1 flair + bots, no paid roles)
- `Castaway` (new) — read entry + introductions only until onboarding + verification gate passes; <1-day accounts stay here.
- `Watchkeeper` — default citizen (post in Watch/Hearth/Ocean/Help/Craft + open finder/help threads + react). Grant path: helper-bot autorole on onboarding completion (6b to confirm free-tier) OR Keeper batch-grant on check-ins.
- `Solo Banner` — optional self-assign flair, equal standing, holdable alongside Watchkeeper/Beacon.
- `Beacon` — earned (steady/kind/evidence-honest; helpers recognized). Grants: showcase-thread creation in `#patient-craft`, pre-queue-free `#creator-mirror` posts.
- `Elder` — earned, rare (long tenure + sustained Beacon steadiness; never purchasable).
- `Keeper` — operator + rare deputies only (post milestone/scam-watch, manage AutoMod queue, grant Beacon/Elder, private log).
- Bots — `AutoMod` (system) + one helper bot in 6b (welcome-DM / reaction-role / autorole; free-tier to confirm).

## Settings would-apply
- Verification level: Medium at open (blueprint §3/§8 wording; exact native gate behavior to be confirmed from current Discord docs at execution); preset raise to High on raid/bait spike. Assigns no role by itself.
- AutoMod: presets ON (profanity/slurs, spam/mention-flood, scam-link patterns) + custom keyword list per blueprint §8 (slur variants, lookalike-link domains, "free Robux/EAC giveaway" bait). Action for those: block + flag to `#mod-action-log`. Unsourced "EAC price / release date" assertions: flag-only (false-positive-prone) for Keeper reframe to `#receipts-and-rumors` with a rumor label — never blocked or auto-deleted for respectful criticism, per blueprint §3.
- Slowmode: 60s `#watch-deck` + `#lantern-room` day one; 30s `#receipts-and-rumors` toggle on spikes.
- Onboarding screen (native; blueprint-specified must-accept item #1 = fan-run disclaimer — exact native enforcement to be confirmed at execution): fan-run notice + 6 rules summary + English-only + report path → lands as Castaway.
- Server description first line = fan-run disclaimer copy (§7); `#read-first-rules` pinned line 1 + topic; include alongside-claim line in milestone/scam-watch Keeper posts; asset rule ("no official game art/logos").
- Permissions: `#milestone-board` + `#scam-watch-and-report` Keeper-post-only; `#welcome-in-pt-fr-es` locked read-only; `#mod-action-log` staff-only.
- Out of scope for 6a (deferred to 6b): helper-bot install/config/hosting, `/report` ticket command name confirmation, expiry/label-prompt automation (best-effort only; native auto-archive + Keeper batch-handling are the guaranteed fallback).

## Execution precondition (blocked until owner says go)
Live run would use direct REST with token `[REDACTED]`, creating items in the order above, verifying each GET-after-POST, then stopping for owner review. Not started. Nothing to roll back — nothing was created.
