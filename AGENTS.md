# AGENTS.md — RELL Seas Discord Build

Read this file at the start of every session, before anything else. If anything here conflicts with a phase brief, this file wins.

## What this project is
A FAN-RUN (not official) Discord server for RELL Seas, an unreleased Roblox naval RPG. The server must be free, feel premium, and never look pay-to-win. Launch scope is English-only. The owner is a capable coder but new to running a Discord community, so you (the agent) are the domain expert here — see "How to make decisions" below.

## Source hierarchy — never invent a fact
1. `insights/` cards (152, each with a `discord_decision`) are where player-need decisions come from. Cite by card id.
2. For any game-mechanics number or fact, cite ONLY the Appendix V tail of the relevant `deep-dives/deep-0N-*.md` file. Never cite deep-dive body text — it is an unverified snapshot.
3. `findings/comment-sentiment-findings.md` is the weighted verdict and wins any conflict with other findings memos.
4. Never read or cite: `../rell-seas-trash/`, `youtube-api-key.md`, or raw comment text. Quote card id + row ids, never "vibes."
5. Never publish or invent unreleased numbers: damage, cooldowns, rarity odds, tax rates, drop rates.
6. Anything date-sensitive, live, or possibly changed since the research snapshots must go through `@fact-checker` before you rely on it. You do not have direct web access — `youcom_*` and `playwright_*` tools are restricted to the fact-checker subagent on purpose. Don't try to route around this. If a `@fact-checker` call fails for any reason, STOP and report it as blocked — never answer the question yourself, with or without a disclaimer. No fallback answers, ever. Fact-checker runs with bash:allow due to a tier constraint; its edit and tool restrictions are enforced by convention, not by permission.

## How to make decisions
The owner is not a Discord power user. For every design choice:
- Propose ONE default with a one-line reason. Don't hand back an unprioritized menu.
- If you use a Discord-specific term (forum channel, onboarding screen, AutoMod, verification level, etc.), explain it in one line the first time.
- Decide the small stuff yourself and move on: channel names, role colors, bot copy, emoji choices.
- Escalate to the owner only at the three checkpoints (end of Phase 2, end of Phase 4, and the final blueprint in Phase 5) and for anything genuinely hard to reverse once real members join, or that depends on the owner's taste rather than the research.
- Think like someone who has to keep this server healthy, not just launch it: moderation load, what day-one feels like when it's nearly empty, what a lean team of one can actually sustain.

## Non-negotiable constraints
- Free. No paywalls, no cosmetic framing that reads as pay-to-win.
- Feels premium without money gates — structure, identity, and status systems do that work instead.
- Fan-run disclaimer must be visible in the design; no reuse of official game assets.
- Sized for one operator who can check in every 10–15 minutes, not sit in the server all day. Automation (AutoMod, a verification level, a clear rules/report flow, a mod-action log) carries the load by default — don't propose anything that needs live human moderation to function at launch.
- No custom age-verification system — if a concept seems to need one, flag it to the owner rather than deciding it yourself; general game-discussion content shouldn't need this at all.

## Session and token discipline
- One phase = one session. Do the phase's defined task, write its output file, update `PROGRESS.md`, and stop. Do not continue into the next phase on your own.
- In Phase 1, one shard per session — never the whole bank at once, even though it would fit in context.
- Only write inside `build/` (plus updating `PROGRESS.md` at the repo root). Everything in `insights/`, `deep-dives/`, `findings/`, `caribbros/`, `ideas/`, `tasks/`, and the root stats files is read-only input — never edit it.
- Never call a `youcom_*` or `playwright_*` tool yourself. Delegate to `@fact-checker` with one question at a time.
- Reasoning effort by phase: low/standard for shard digests, max for synthesis (Phase 2), concepts (Phase 3), and the blueprint (Phase 5); high for the stress test (Phase 4).
- `@reviewer` (a different model) checks every phase from Phase 2 onward before you report to the owner. Run it; don't skip it.
- Reviewer runs exactly ONE pass per phase. Apply its MUST-FIX items directly. Do not re-invoke @reviewer to confirm the fixes were sufficient — that is a second paid pass and is not permitted without the owner's explicit request.
- Every phase's git add must include build/reviews/<phase-file>.md and any new build/fact-ledger.md entries from that session — not just the primary output file.

## Secrets
Never read, print, cat, grep, or source .env, and never run env or printenv. The only code allowed to load .env is the Phase 6a execution script (build/scripts/phase6a_execute.py), which loads it internally and must never print it. If a secret appears in any output, stop and tell the owner.

## Where to look
- `README.md` — the original research map and its own reading order.
- `PROGRESS.md` — current status; read this every session.
- `build/briefs/phase-N-*.md` — the brief for whatever phase is next.
- `build/skills/*.md` — the method for that phase; read the one the brief points to.
- `build/fact-ledger.md` — already-verified facts; check before asking `@fact-checker` the same question twice.

## Phase 6a live execution is authorized only as defined in build/briefs/phase-6a-live-execution.md. Phase 6b (custom bot) is not briefed; do not start it.
