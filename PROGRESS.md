# Progress

Read this first, every session. Update it at the end of every session.

## Status
- Setup (AGENTS.md, agents, skills, fact-ledger): done
- Phase 1 — Shard digests: 12/12 shards done (S01–S12)
- Phase 2 — Synthesis: done (reviewed 3 passes; final: brief criteria PASS, AGENTS must-fix citations corrected)
- Phase 3 — Concepts: not started (CHECKPOINT — owner go-ahead required before starting)
- Phase 4 — Stress test: not started
- Phase 5 — Blueprint: not started
- Phase 6 — Discord setup script: not briefed yet
- Models: builder = opencode/muse-spark-1.3-contributor-free (temporary); reviewer = vercel/openai/gpt-5.2 (permanent); fact-checker = opencode/muse-spark-1.3-contributor-free with bash:allow

## Next action
Phase 2 complete and reviewed — CHECKPOINT. Owner reviews build/phase-2-synthesis.md before Phase 3 Concepts begins.

## Open questions / blockers
(none — fact-checker and reviewer smoke tests passed; probe artifacts removed)

## Session log
Append one line per session: `date — phase — what was done — output file`.
- 2026-10-06 — setup fix — moved rell-seas-setup/* to root, migrated agents to permission:, pinned reviewer model, hardened opencode.json, banned fallback answers — no output file
- 2026-10-06 — setup fix — bisected fact-checker spawn failure to `bash: deny`, pinned contributor-free, granular bash ask+ledger-allow, smoke test passed — build/fact-ledger.md
- 2026-10-06 — setup fix — reviewer bash:allow + probe passed, ledger junk removed, repeat smoke test passed (duplicate row noted) — build/fact-ledger.md
- 2026-10-06 — setup fix — reviewer moved to vercel/openai/gpt-5.2 with bash:deny, probe passed (spawn-kill is contributor-free-specific) — no output file
- 2026-10-06 — Phase 1 S01 — shard digest (INS-001–INS-014) — build/digests/shard-S01-digest.md
- 2026-10-06 — Phase 1 S02 — shard digest (INS-015–INS-029) — build/digests/shard-S02-digest.md
- 2026-10-06 — Phase 1 S03 — shard digest (INS-030–INS-041) — build/digests/shard-S03-digest.md
- 2026-10-06 — Phase 1 S04 — shard digest (INS-042–INS-054) — build/digests/shard-S04-digest.md
- 2026-10-06 — Phase 1 S05 — shard digest (INS-055–INS-066) — build/digests/shard-S05-digest.md
- 2026-10-06 — Phase 1 S06 — shard digest (INS-067–INS-080) — build/digests/shard-S06-digest.md
- 2026-10-06 — Phase 1 S07 — shard digest (INS-081–INS-092) — build/digests/shard-S07-digest.md
- 2026-10-06 — Phase 1 S08 — shard digest (INS-093–INS-104) — build/digests/shard-S08-digest.md
- 2026-10-06 — Phase 1 S09 — shard digest (INS-105–INS-115) — build/digests/shard-S09-digest.md
- 2026-10-06 — Phase 1 S10 — shard digest (INS-116–INS-128) — build/digests/shard-S10-digest.md
- 2026-10-06 — Phase 1 S11 — shard digest (INS-129–INS-139) — build/digests/shard-S11-digest.md
- 2026-10-06 — Phase 1 S12 — shard digest (INS-140–INS-152) — build/digests/shard-S12-digest.md
- 2026-10-06 — Phase 2 — master synthesis (14 needs, 11 conflicts, 10 gaps; @reviewer 3 passes) — build/phase-2-synthesis.md
- 2026-10-06 — Phase 2 review record — recovered @reviewer verdict (needs revision) to build/reviews/ — build/reviews/phase-2-synthesis.md
