# Insight bank — what this folder is

User-thinking data for building the RELL Seas Discord server. NOT a comment record: 42,629 quality-filtered comments were mined down to **152 sharp insight cards**. Everything generic (praise, "first", emoji-only, off-topic, vague restatements) was dropped and logged, not kept.

## Files
- `insights.jsonl` — the bank: 152 cards (INS-001…INS-152), machine-readable. Each card = one distinct piece of user thinking + 3–8 verbatim evidence quotes (with commentId/likes/lang/videoId) + volume signal + exactly one `discord_decision` (the server action it demands, or explicit no-action + reason).
- `insights.md` — same 152 cards, readable, grouped by shard (topic).
- `insights.stats.md` — counts: 152 cards, 694 evidence quotes (en 555 / pt 93 / fr 40 / es 6), per-shard yields, top-10 cards by volume, quality gates, verification log.
- `shard_S01…S12.jsonl` — per-topic work files (release-date, movie/EAC, platform, monetization, combat, rivalry, crews, ships/bosses, memes, trust/mod, PT-FR-ES audit, loyalty). Sum = 152.
- `dropped.log` — what was dropped and why (counts + reasons + sample ids per shard, no full-text dump).

## How it was built (chain, all upstream in trash or root)
273,756 raw comments (YT 210K + CaribBros 63K) → exact/near-dup collapse + theme clustering → 159K uniques → quality filter (length + question/keyword/longform, likes tiebreak only) → 42,629 rows → 12 topic shards, AI-synthesized into cards, meme families capped at 5 variants, PT/FR/ES evidence preserved. Build scripts and pools lived in `work/` (trashed after acceptance); raw inputs in `rell-seas-trash/`.

## How to use it
Start from a card's `discord_decision`, not from raw comments. Top-volume cards first (open-testing honesty, rivalry clock, combat accuracy, fruit rarity — see stats top-10). Check `confidence` and evidence before building a channel/rule/event from any card. For mechanics facts (fruit counts, Haki cards, ranks), cite `deep-dives/` Appendix V, never a comment.
