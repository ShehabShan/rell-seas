# Review — build/phase-6c-content.md

VERDICT: NEEDS REVISION (single pass; per AGENTS.md no second pass permitted without owner request)

Provenance: content below is the `@reviewer` verdict returned verbatim 2026-10-07 (one pass only). The reviewer was instructed to return text only and write no files; this file saves that verbatim text unedited. Builder applied all 4 MUST-FIX items directly to `build/phase-6c-content.md` and did not re-invoke the reviewer.

---

VERDICT: **NEEDS REVISION**

MUST-FIX (blocking)

1) **Non-permitted game/timeline fact (“2019”)**
- `build/phase-6c-content.md:122` — “**2019 veterans**” is a game-adjacent factual claim (timeline) and violates the phase constraint that the **only** allowed game fact is “still unreleased” with VERIFIED ledger backing. Remove the year and keep it yearless (e.g., “early-watch veterans”) or otherwise de-factualize.

2) **Day 1 VERIFIED milestone post lacks the actual source links it tells users to check**
- `build/phase-6c-content.md:190-196` — Post says “Sources: official Roblox listing + release tracker… check the linked sources” but **does not include URLs**. For paste-ready content and “VERIFIED ledger backing,” include the two URLs from `build/fact-ledger.md` (CHECKED 2026-10-07) directly in the post and cite the ledger Q/date.

3) **Launch-week plan violates Phase 6c brief “one seed post per day for 7 days”**
- `build/phase-6c-content.md:185-271` — Includes multiple days with **second posts** (Day 1 second post, Day 6 second post, Day 7 second post). The brief requires **exactly 7** day seeds (one/day). Either consolidate to one post/day or explicitly re-scope the extras as “setup/admin” outside the “one seed per day” requirement (but as written, it’s non-compliant).

4) **AutoMod proposals: item without source + not clearly a “scam-link/fake-giveaway pattern”**
- `build/phase-6c-content.md:312-314` — #12 “Unsourced ‘price / release date’ assertions…” has **no source URL** and is more of a moderation workflow than a scam-link pattern. Brief requires **each** proposal have a source (fact-checker/ledger-backed) and be a scam/giveaway pattern. Remove it or replace with a sourced, pattern-based scam lure.

NITS (non-blocking)

- `build/phase-6c-content.md:40-41`, `56-57`, `201-206` — Repeats an operational promise “cleared every 10–15 minutes.” Blueprint mentions this cadence, but in member-facing copy it creates expectation debt; consider softening (“as soon as we can”).
- `build/phase-6c-content.md:64-65` — “A /report command is planned/coming later” reads like a promise; safer as “may be added later.”
- `build/phase-6c-content.md:80-81` — “Threads close after 7 quiet days” assumes the forum auto-archive is set to 7 days (blueprint intent). Since this doc must match live channel settings, ensure Phase 6a execution actually set it.

---

Builder fixes applied (no second reviewer pass):
- "2019 veterans" + Day-7 "2019" de-factualized (both spots); "both-Shinobi-Lives" kept as community identity from insight cards.
- Day-1 milestone post now carries both source URLs inline + ledger Q/date.
- Launch week restructured to exactly 7 day-seeds; Keeper intro moved to "Setup posts (NOT day seeds)" and creator mirror marked WITHHELD; Day-7 lantern-room question folded into the Day-7 seed.
- AutoMod #12 removed (11 proposals, all sourced); unsourced-claim handling noted as manual Keeper work, not keyword filtering.
- Nits applied: check-in promises softened to "at the next check-in", /report as "may be added later", forum-type + 7-day auto-archive added to owner dashboard to-dos.
