# Insights stats

Date: 2026-10-05 (final). Input: `comments_quality.jsonl` = 42,629 quality_unique rows + 168 clusters (total 42,797 rows).
Output: **152 cards** (INS-001..INS-152), **694 evidence quotes** (all byte-identical, script-extracted).
Quality-row coverage: 669 unique rows cited as evidence (1.6% of quality rows).

## Per-shard yields
| shard | topic | cards | evidence quotes | langs | confidence |
|---|---|---|---|---|---|
| S01 | release-date | 14 | 52 | {'en': 43, 'pt': 7, 'es': 1, 'fr': 1} | {'high': 8, 'medium': 6} |
| S02 | movie/EAC | 15 | 66 | {'en': 55, 'fr': 3, 'pt': 8} | {'high': 10, 'medium': 5} |
| S03 | platform | 12 | 46 | {'en': 40, 'pt': 6} | {'high': 3, 'medium': 8, 'low': 1} |
| S04 | monetization | 13 | 62 | {'en': 49, 'pt': 9, 'fr': 3, 'es': 1} | {'high': 4, 'medium': 8, 'low': 1} |
| S05 | combat/fruit | 12 | 60 | {'en': 52, 'fr': 3, 'pt': 5} | {'high': 3, 'medium': 8, 'low': 1} |
| S06 | rivalry | 14 | 76 | {'en': 64, 'pt': 8, 'fr': 4} | {'medium': 9, 'high': 5} |
| S07 | crews/RP | 12 | 58 | {'en': 50, 'pt': 4, 'fr': 4} | {'high': 1, 'medium': 11} |
| S08 | ships/bosses | 12 | 47 | {'en': 44, 'fr': 1, 'pt': 2} | {'medium': 9, 'high': 1, 'low': 2} |
| S09 | memes | 11 | 58 | {'en': 44, 'pt': 7, 'fr': 7} | {'high': 2, 'medium': 7, 'low': 2} |
| S10 | trust/mod | 13 | 65 | {'en': 55, 'fr': 5, 'pt': 5} | {'high': 5, 'medium': 8} |
| S11 | audit | 11 | 42 | {'pt': 31, 'fr': 7, 'es': 4} | {'medium': 11} |
| S12 | loyalty | 13 | 62 | {'en': 59, 'fr': 2, 'pt': 1} | {'high': 5, 'medium': 7, 'low': 1} |

## Dropped / unsampled
Shard keyword pools (S01–S10, S12; overlapping by design): 55389 keyword-matched rows, 6072 pooled for review. Uncited pool rows are bucketed in `dropped.log` (generic-praise / first-emoji-only / off-topic / vague-restatement + deferred + cross-shard-merged, with sample ids, no full-text dump). Unsampled tails (keyword rows never entering pools) are counted per shard in `dropped.log`.
S11 audit pool: 4918 non-EN quality rows (of 42,629); pool reviewed 480.
Generic hype / first-post / emoji-only / off-topic rows were dropped throughout; counts per shard in `dropped.log`.

## Language split (evidence quotes)
Total evidence quotes: 694: en=555, pt=93, fr=40, es=6.
Non-EN input pool: PT 3,649 + FR 1,134 + ES 135 quality rows (S11 audit). Per-card language evidence in `insights.md` headers.
Rule applied: cross-language duplicates became one card with per-language evidence; separate cards only where thinking differs by region (S11: BR money talk, FR IP split, ES margins).

## Top-10 cards by volume (evidence likes + cited cluster weights + merged rows)
| rank | card | title | volume score |
|---|---|---|---|
| 1 | INS-015 | "Open testing" reads as dishonest | 7728 |
| 2 | INS-067 | Race to release is rivalry clock | 7096 |
| 3 | INS-069 | Combat accuracy is the wedge | 6407 |
| 4 | INS-055 | Fruits must be rare and hard | 5970 |
| 5 | INS-059 | Conqueror power fantasy | 5357 |
| 6 | INS-057 | NPC fear plus living world | 5109 |
| 7 | INS-060 | Fruit showcase love and wishlist | 4482 |
| 8 | INS-049 | Copyright dread | 3829 |
| 9 | INS-141 | Craft supremacy signals | 3730 |
| 10 | INS-068 | Better even while unreleased | 3562 |

## Quality gates (final)
- Every quote byte-identical to its source row (script-extracted; 30 random cards re-verified below).
- Every factual claim cites row ids; volumes are counted sums, not estimates.
- Each card has exactly one discord_decision (or explicit no-action + reason).
- Non-EN evidence present where the thinking lives in PT/FR/ES (see per-card langs).
- Meme families: one card max per family, 3–8 variants as evidence (S09).
- Total 152 lands in the 150–250 band.
- Deferred rows from earlier batches (S07/S08/S10/S12 targets) all consumed as evidence; remaining parked rows logged in dropped.log.

## Verification log
- 30 random cards re-verified (text/likes/video/volume/schema): see session report 2026-10-05.
- insights.jsonl sorted by shard then card id; IDs continuous INS-001..INS-152.
