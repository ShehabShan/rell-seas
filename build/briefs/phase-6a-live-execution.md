# PHASE 6a: LIVE EXECUTION BRIEF

## Authorization
The owner approved the Phase 5 blueprint (final checkpoint) and authorizes live creation of the structure in `build/phase-6a-dry-run.md` on the Discord server whose ID is in `.env`. This brief overrides the "dry run only" restriction in `build/briefs/phase-6a-server-build.md` for this task only.

Not authorized: invites, announcements, launch-week posts, bot hosting, Phase 6b, or anything not listed in the dry-run plan.

## Secret handling (hard rules)
- You never read `.env`. No `cat`, `grep`, `head`, `source`, `env`, `printenv`, and no read tool on it. The token must never enter your context.
- All Discord API calls go through ONE script you write: `build/scripts/phase6a_execute.py`. The script loads `DISCORD_BOT_TOKEN` and `DISCORD_SERVER_ID` from `.env` internally and sends the header `Authorization: Bot <token>`.
- The script never prints, logs, or writes the token or request headers. Catch exceptions so tracebacks and response dumps cannot include headers. Print only the HTTP status, the endpoint path, and Discord's error code and message.
- Never put the token on a command line. Never use curl with it.
- If the token ever appears in any output, stop and tell the owner at once. Do not repeat it.
- The script file contains no secrets and may be committed. The execution log contains IDs only.

## Script requirements
- Two modes: `--preflight` (read-only, the default) and `--execute`. `--execute` re-runs preflight first and refuses to continue if it fails.
- Idempotent. Before creating anything, look it up by exact name (and parent for channels). If it exists and matches, skip it and record its ID. If it exists but differs, stop and report. Never delete or overwrite anything.
- Rate limits: on HTTP 429, wait the given `retry_after` and retry once. If `retry_after` exceeds 120 seconds, stop. Pause about 0.5 seconds between writes.
- After every create, GET that object and compare it to intent: name, type, parent, topic, slowmode, permission overwrites (allow and deny bits), role color and permissions. Any mismatch means stop.
- Use named constants for Discord permission flags, never magic numbers.
- Any failure other than a handled rate limit is a hard stop. No automatic retries, no rollback, no cleanup, no deletion. Report the exact state and wait.
- Append progress to `build/phase-6a-execution-log.md` as you go (type, name, ID, status), so a cut-off session still leaves a record.

## Order of operations

### Phase 0: Preflight (read-only)
1. GET `/users/@me`. The username should be "RELL Seas Setup Bot". Otherwise stop.
2. GET the guild with counts. Report name, member count, and features. If the member count is above 5, stop (likely the wrong server).
3. The guild features must include `COMMUNITY`. Forum channels and Onboarding both require it. If it is missing, stop and tell the owner to enable Community in Server Settings first. Do not try to enable it through the API.
4. GET channels and roles. Expected pre-existing items: default "Text Channels" and "Voice Channels" categories with `#general` and a General voice channel, any channels Discord's Community wizard created (rules, moderators-only, community-updates), `@everyone`, and the bot's own role. Record them in the log as "pre-existing". Do not modify or delete them. Anything else unexpected means stop.
5. Confirm the bot's role has Administrator. Otherwise stop.

If preflight is clean, continue to Phase 1 in the same session. If any stop condition triggers, report and end.

### Phase 1: Roles
Create Castaway, Watchkeeper, Solo Banner (flair, no extra permissions), Beacon, Elder, Keeper, using the values in `build/phase-6a-dry-run.md`. Where the plan leaves a value unspecified (such as color), choose a neutral value and note it in the log. Do not invent permissions beyond the plan. Then set the order Keeper (top) > Elder > Beacon > Watchkeeper > Castaway, all below the bot's own role, and verify the positions.

### Phase 2: Categories
Create the 7 categories in blueprint order. Verify each and record its ID.

### Phase 3: Channels
Create the 14 channels plus the private mod-action-log, each under its correct category, using role IDs from Phase 1 in permission overwrites exactly as the plan specifies. Check the private mod-action-log twice: `@everyone` must be explicitly denied View Channel, and only Keeper can see it. Verify slowmode and forum settings where specified.

Topics and pins: post and pin text only where the plan specifies it, and use the blueprint's exact wording. The disclaimer line is:

> FAN-RUN — This is a fan-run community, not official. Not affiliated with the RELL Seas developers. No official assets used here. Treat everything as community discussion unless a Keeper post links a primary source.

Do not rephrase it. If a required text is not in the blueprint, do not write one. List it under "owner to-do" in the report.

### Phase 4: AutoMod
Create the rules from blueprint §8. The flag-only rule (unsourced claims and rumors) must use the alert action pointed at the mod-action-log channel and must NOT block the message. The rules for spam, slurs, and scam-link patterns DO block. Do not merge these two behaviors. GET each rule and verify its action list matches this split.

### Phase 5: Verification level
Set Medium. GET and verify.

### Phase 5b (soft): Community channel pointers
Try pointing the rules channel at `#read-first-rules` and the Community updates channel at the private mod-action-log. If the API rejects either, report it and leave the defaults. Do not treat this as a failure.

### Phase 6 (soft): Onboarding
Check the prerequisite (enough default channels where `@everyone` can view and send). If met, configure the required "accept the rules" prompt linked to grant Watchkeeper, the default channels, and the disclaimer on the welcome screen. If the prerequisite is not met or the call fails, retry at most once, then report "onboarding needs manual setup in the dashboard" and continue. This and Phase 5b are the only soft-fail points. Everything else is a hard stop.

### Phase 7: Final verification
GET the guild's channels, roles, and AutoMod rules. Cross-check the complete list against `build/phase-6a-dry-run.md`. Report anything missing or mismatched, and any plan item that cannot be done through the API.

### Phase 8: Log and report
- Finish `build/phase-6a-execution-log.md` with every created item and its real Discord ID, plus the pre-existing items and onboarding status.
- State in the log that the token never appeared in any output or file.
- Commit and push the log and the script. Nothing else, and never `.env`.
- Report in under 200 words: preflight result, counts created, soft-fails, any hard stop with the exact error, final verification result, owner to-do list.
