# Review — build/phase-2-synthesis.md

VERDICT: needs revision

Scope checked against: build/briefs/phase-2-synthesis.md + AGENTS.md

Transcription note: this record contains the `@reviewer` verdict returned 2026-10-06. The reviewer subagent reported writing this file but the write did not land on disk (sandbox path issue), so the builder transcribed the returned verdict verbatim below. Content is the reviewer's, not the builder's.

## Criteria (PASS/FAIL)

1) Ranked needs with volumes: **PASS** (tiers + volumes; N13–N14 explicitly "not separately ranked").
2) Conflicts named w/ winner+why (digest↔digest and digest↔sentiment): **PASS (with risk)** — table is thorough, but completeness is asserted rather than evidenced.
3) Gaps named: **PASS** (G1–G10).
4) No server design: **PASS** (stays at need/outcome level; no channel/role/bot prescriptions).
5) No invented game numbers; no raw comment quotes; no banned sources; card-id citations: **FAIL** (raw comment quotes present).
6) Sentiment wins conflicts with other findings memos: **PASS** (explicit in C7; uses §6 ambiguity rules in C8–C10).

## STRONG (up to 3)

- Clear tiering and consistent volume anchoring to `comment-sentiment-findings.md` and `insights.stats.md` (e.g., N1/N2/N6).
- Conflict table uses sentiment §6 ambiguity guardrails correctly (C8–C10), preventing common misreads.
- Gaps section correctly quarantines date-sensitive/rumor claims (G2–G5/G9) and warns about `@fact-checker`.

## WEAK (up to 5)

- **Raw comment quotes violate AGENTS.md.** Line 15 repeats "I'll see y'all in 2043" and "friends we made along the way" with like counts (these are raw comment text, even if sourced from sentiment). Must remove/replace with paraphrase + cite sentiment line/section.
- **Another raw-quote-like phrase risk:** Line 55 references QnA mockery context ("Questions, No Answers" appears indirectly in N11 via sentiment, and sentiment includes raw quotes). Keep synthesis quote-free; cite the theme only.
- **Completeness of "every conflict" is not auditable.** The table claims coverage ("every digest-vs-digest…", line 47) but doesn't state how conflicts were enumerated (e.g., "scanned each digest's 'Tensions/Conflicts' section"). This is a risk against the brief's "every conflict" requirement.
- **Non-EN numeric pool claims lack a pointer.** Line 45 ("4,918 non-EN quality rows…", "3,649 PT + 1,134 FR + 135 ES") need an explicit citation anchor (e.g., "from S11 digest header") to avoid looking invented.
- **Robux range repetition is optics-risky.** Line 17 restates "400–1000 Robux" (even labeled speculation). Consider dropping the exact range in Phase 2 to reduce accidental propagation.

## MUST-FIX before the owner sees this

- Remove **all** raw comment quotes from the synthesis (line 15 and any others) and replace with paraphrase + sentiment § reference only.
- Add a 1–2 line note on **how conflicts were enumerated** (so "every conflict" is defensible).
- Add explicit source pointers for the **non-EN pool counts** (line 45 / G7).

## QUESTIONS FOR OWNER

- Do you want the synthesis to **avoid repeating specific rumor numbers entirely** (e.g., "400–1000 Robux") even when labeled rumor, to reduce later leakage into server messaging?
