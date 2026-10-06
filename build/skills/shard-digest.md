# Skill: Shard Digest

Used in Phase 1. One shard, one session, one output file.

## Input
One file: `insights/shard_S0N.jsonl`. Each line is one insight card (fields roughly: card id, the thinking/claim behind it, supporting quote references, a volume/count, language tags, and a `discord_decision`).

## What to do
1. Read the shard file.
2. For every card, pull out: the card id, a one-sentence paraphrase of its core claim (not a copy of the original quotes), its `discord_decision`, its volume if present, and whether it's tagged with a non-English language.
3. If two cards in this shard point to opposite `discord_decision`s on the same topic, flag it as a conflict — name both card ids, don't resolve it (that's Phase 2's job).
4. Do not editorialize, rank, or propose server design here. This phase is extraction only.

## Output — `build/digests/shard-S0N-digest.md`
A tight list or table, one row per card:
`CARD-ID | one-line claim | discord_decision | volume | flags`

End with a 3–5 line "Shard summary" naming the 2–3 dominant themes in this shard.

## Rules
- Paraphrase; never quote original comment text at length.
- Every card in the shard must appear in the digest — don't skip low-volume cards, just keep their row short.
- Keep the whole digest well under the length of the source shard.
