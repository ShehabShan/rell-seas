# Skill: Blueprint Writer

Used in Phase 5, once, after the owner has picked a concept.

## Input
The chosen concept from `build/phase-4-stress-test.md`, plus anything the owner added when choosing it.

## Output — `build/phase-5-blueprint.md`
The actual buildable spec:
- **Categories and channels**, each with its one-line purpose.
- **Role ladder**, with what each role is for and roughly what it can do.
- **Bots and automation**, what each one handles (spam, bad language, raids, verification, welcome flow) — favor automation over anything needing a human online.
- **Onboarding/verification flow** for a new member's first five minutes.
- **Launch-week content plan** — what posts/events happen in the first 7 days so the server doesn't feel empty.
- **A weekly routine** sized to the owner's actual time (occasional 10–15 minute check-ins), not a full-time-moderator workload.
- **Fan-run disclaimer** — exact placement (e.g., server description, a pinned message, a rules-channel line).
- **Safety baseline** — AutoMod/verification-level settings, report flow, mod-action log; explicitly confirm no custom age-verification is needed, or flag it to the owner if something in the chosen concept seems to require one.
- **What we left out and why** — the lean-launch doctrine made real: name what's deliberately not at launch.
- **Freshness flags** — a short list of every fact this blueprint depends on that should go through `@fact-checker` again right before the owner actually launches (dates, counts, release status).

## Rules
- This is the last research-side phase. Do not write or touch anything Discord-API-related, `.env`, or the bot token — that's Phase 6, separately briefed.
- Write it so the owner can hand it to Phase 6 (or do it by hand) without re-deriving anything.
