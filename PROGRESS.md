# Progress

Read this first, every session. Update it at the end of every session.

## Status
- Setup (AGENTS.md, agents, skills, fact-ledger): done
- Phase 1 — Shard digests: 12/12 shards done (S01–S12)
- Phase 2 — Synthesis: done (reviewed 3 passes; final: brief criteria PASS, AGENTS must-fix citations corrected)
- Phase 3 — Concepts: done (reviewed 3 passes; final: PASS) — G7 resolved per owner directive (English-only + static PT/FR/ES blurb + partner-not-poach, no ongoing non-EN moderation)
- Phase 4 — Stress test: done (@reviewer 1 pass, PASS, MUST-FIX none) — Long Watch recommended (27), Crucible runner-up (24), Ledger 23, Harbor 22
- Phase 5 — Blueprint: done (@reviewer 1 pass, NEEDS REVISION, MUST-FIX 3 applied directly, no second pass) — Long Watch + Crucible/Harbor/Ledger borrowings, G7 generic + human-checked, private-log-only
- Phase 6 — Discord setup script: 6a dry-run done (brief + plan, @fact-checker onboarding finding, @reviewer 1 pass NEEDS REVISION with 4 MUST-FIX applied, no second pass); no live creates, `.env` unread
- Models: builder = opencode/muse-spark-1.3-contributor-free (temporary); reviewer = vercel/openai/gpt-5.2 (permanent); fact-checker = opencode/muse-spark-1.3-contributor-free with bash:allow

## Next action
Phase 4 complete and reviewed (PASS) — CHECKPOINT: owner chooses the concept (or asks for changes) before Phase 5.
Phase 5 complete and reviewed (1 pass, MUST-FIX applied) — FINAL CHECKPOINT: owner approves blueprint (or asks for changes) before any Phase 6 brief. Do not start Discord setup.

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
- 2026-10-06 — Phase 3 — four concepts (Ledger House / Crucible / Harbor / Long Watch; @reviewer 3 passes, final PASS) — build/phase-3-concepts.md
- 2026-10-06 — Phase 3 review record — saved @reviewer final verdict (PASS) to build/reviews/ — build/reviews/phase-3-concepts.md
- 2026-10-06 — Phase 4 — stress test (4 concepts × 6 rubric rows, Long Watch recommended; @reviewer 1 pass PASS) — build/phase-4-stress-test.md
- 2026-10-06 — Phase 4 review record — saved @reviewer verdict (PASS, MUST-FIX none) to build/reviews/ — build/reviews/phase-4-stress-test.md
- 2026-10-06 — Phase 5 — final blueprint (Long Watch + borrowings, G7 generic + human-checked, private-log-only; @reviewer 1 pass NEEDS REVISION, 3 MUST-FIX applied, no second pass) — build/phase-5-blueprint.md
- 2026-10-06 — Phase 6a — server-build brief + dry-run plan (no MCP/discord.py/discord.js → direct REST for execution; onboarding auto-role NO per in-session check ses_eef7b9390ffe7jBaAyrJGbFZGl, ledger pending; @reviewer 1 pass NEEDS REVISION, 4 MUST-FIX applied; live untouched, .env unread) — build/phase-6a-dry-run.md
