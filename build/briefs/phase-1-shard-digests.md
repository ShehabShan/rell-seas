# PHASE 1 — Shard Digests

Scope: ONE shard per session. 12 sessions total (S01–S12). Do not do more than one shard in a single session, even though the context would fit — this keeps each session reviewable and cheap.

Input: `insights/shard_S0N.jsonl` (pick the next undone shard — check `PROGRESS.md`)
Skill: `build/skills/shard-digest.md` (read this first)
Output: `build/digests/shard-S0N-digest.md`

## Definition of done
- Every card in the shard is represented in the digest (id, claim, discord_decision, volume, flagged conflicts)
- No invented content; paraphrased, not copied at length
- Shard summary (3–5 lines) written at the end
- `PROGRESS.md` updated: this shard marked done, next shard named

Reasoning effort: low/standard — this is extraction, not judgment.
Reviewer: not needed for this phase.
Stop after one shard. Do not continue to the next shard or the next phase automatically.
