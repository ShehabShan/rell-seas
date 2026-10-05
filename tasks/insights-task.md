# Insight Bank Task — Discord build thinking (target 150–250 sharp cards)

> Supersedes `comment-task.md` row-canonical plan (archived as background). We do NOT preserve every comment. We mine the 42,629 quality rows + 168 clusters for actionable user thinking and drop the rest (logged). End state: insight cards with decisions, not a comment record.

## 1. Goal
Produce an insight bank the Discord blueprint can build from directly: each card = one distinct piece of user thinking (complaint/request/question/fear/want with specifics) + evidence + volume + a server decision. Complaints with specifics first; praise kept only for loyalty/rivalry signals; generic hype/first/emoji-only/off-topic dropped.

## 2. Inputs (read-only)
- `comments_quality.jsonl` — 42,629 `quality_unique` (score order, 28,564 zero-like) + 168 `cluster` (5 examples each). Use as evidence pool.
- Existing findings for triangulation (do not redo; CWD is `rell-seas/` so paths below are root-relative): `findings/comment-sentiment-findings.md` (weighted verdict wins), `findings/yt-comment-findings.md` (Part B multilingual), `findings/caribbros-research.md` (dev tone/history), `findings/reddit-threads.md`/`findings/reddit-findings.md` (triggers), `deep-dives/deep-01..10` Appendix V (verified facts — never contradict; cite spec vs rumor correctly).
- Likes are tiebreak/voice-picking only. Zero-like substance is equal. PT/FR/ES kept (summarize in English, 1–2 verbatim per language where wording carries culture).

## 3. Outputs (all in `insights/`)
- `insights/insights.jsonl` — one JSON per card (final concat, sorted by shard then card id).
- `insights/insights.md` — readable version grouped by shard (same content, markdown).
- `insights/dropped.log` — counts + reasons per shard (`generic-praise N`, `first/emoji-only N`, `off-topic N`, `vague-restatement N`, sample ids) — no full-text dump.
- `insights/insights.stats.md` — input 42,629+168 → cards N, dropped M by reason, language split, top-10 cards by volume.
- Per-shard work files: `insights/shard_S01.jsonl` (+ matching `.md` section appended to `insights.md` by the session).

## 4. Card schema (every card must have all fields)
`{card_id (INS-001…), shard, title (≤10 words), user_thinking (2–5 sentences: what they believe/want/fear + why), evidence (3–8 verbatim quotes; each {text VERBATIM, commentId, likeCount, lang, videoId}), volume {merged_rows, cluster_weights_cited}, discord_decision (one specific action: add FAQ/containment channel/event/rule/content angle/tone law — or explicit "no action" with reason), confidence (high/med/low), sources (row ids + finding/deep cites)}`.
Rules: `text` byte-identical (never retype from memory — copy via script); every factual claim cites row ids; volume = counted not vibes; each card states its decision; cross-language duplicates become one card with per-language evidence (not separate cards) unless the thinking genuinely differs by region.

## 5. Shards (claim whole shard, not row ranges; ~12–20 cards each → 150–250 total)
| shard | topics (seed clusters/keywords) | status | session | date | cards | notes |
|---|---|---|---|---|---|---|
| S01 | release-date/window (release/game/when, coming/out/when, date/release/movie, YEAR/release/seas, please/release/rell) | done | 2026-10-05 S01+S02+S03 batch | 2026-10-05 | 14 (INS-001..014, 52 quotes, EN41/PT9/ES1/FR1) | kw 2897 rows, pool 502, seed-w 8307; numerology merged into S02-INS-023 |
| S02 | movie-3/EAC/testing (movie/release/not, EAC/tester/CC/open-testing, QNA) | done | 2026-10-05 S01+S02+S03 batch | 2026-10-05 | 15 (INS-015..029, 66 quotes, EN53/FR5/PT8) | kw 3868 rows, pool 606, seed-w 3585; absorbs frame-math from S01 |
| S03 | platform/mobile/xbox/pc/console (mobile/game/play, xbox/game/mobile) | done | 2026-10-05 S01+S02+S03 batch | 2026-10-05 | 12 (INS-030..041, 46 quotes, EN25/PT17/FR4) | kw 2296 rows, pool 576, seed-w 3166 |
| S04 | monetization/price/codes/scam (code/shindo/new, price/robux, scam/fake, got/scammed) | done | 2026-10-05 S04+S05+S06 batch | 2026-10-05 | 13 (INS-042..054, 62 quotes, EN49/PT9/FR3/ES1) | kw 4455 rows, pool 603, seed-w 1902 |
| S05 | combat/haki/fruit/builds (haki/armament/conquerors, gear/blox/fruits, fruit/race/boss names, bloodline/rework/pls) | done | 2026-10-05 S04+S05+S06 batch | 2026-10-05 | 12 (INS-055..066, 60 quotes, EN52/FR3/PT5) | kw 19320 rows, pool 611, seed-w 4556; boss-AI rows deferred to S08 |
| S06 | rivalry/migration (better/blox/fruits, piece/one/rell, more/seas/blox, update/shindo/life, peak/seas/rell, looks-good/fire/praise → keep only signals) | done | 2026-10-05 S04+S05+S06 batch | 2026-10-05 | 14 (INS-067..080, 76 quotes, EN64/PT8/FR4) | kw 10131 rows, pool 609, seed-w 6805; GAG thinking merged into INS-040 |
| S07 | crews/social/RP/jobs (crew, crew-finder, language crews, profession/job, RP) | done | 2026-10-05 S07+S08+S09 batch | 2026-10-05 | 12 (INS-081..092, 58 quotes, EN50/PT4/FR4) | kw 1582 rows, pool 456, seed-w 490 (2 crew clusters only; keywords carried RP/jobs) |
| S08 | ships/subs/ocean/bosses/events (ship, submarine, depth, boss, sea beast, event) | done | 2026-10-05 S07+S08+S09 batch | 2026-10-05 | 12 (INS-093..104, 47 quotes, EN44/FR1/PT2) | kw 4256 rows, pool 599, seed-w 374 (no ship/sub/boss cluster exists; keyword-only + 6 deferred rows used) |
| S09 | memes/mega-threads (gta/before/seas, YEAR jokes, it's/not/bro, real/seas/rell, botak/enyu → one card per family max, 3–5 variants as evidence) | done | 2026-10-05 S07+S08+S09 batch | 2026-10-05 | 11 (INS-105..115, 58 quotes, EN44/PT7/FR7) | kw 3178 rows, pool 589, seed-w 5926; trailer/santa/notify merged into S02; first-spam dropped per gate |
| S10 | trust/comms/moderation (trailer-for-trailer, baited, vague-dates, toxicity/mute/ban, QNA-mockery) | done | 2026-10-05 FINAL batch | 2026-10-05 | 13 (INS-116..128, 65 quotes) | kw 2132 rows, pool 497; QNA/trailer merged into S02 cards |
| S11 | PT/FR/ES audit (eu/não/jogo + all non-EN substance; ensures per-card language evidence, no separate cards unless thinking differs) | done | 2026-10-05 FINAL batch | 2026-10-05 | 11 (INS-129..139, 42 quotes, all non-EN) | non-EN input 4,918 rows (PT 3,649/FR 1,134/ES 135); audit in stats.md |
| S12 | loyalty/praise signals (dev work ethic, Shindo coexistence/nostalgia, rivalry confidence — keep signals only, drop generic hype) | done | 2026-10-05 FINAL batch | 2026-10-05 | 13 (INS-140..152, 62 quotes) | kw 1248 rows, pool 438, seed-w 4001 |

Seed cluster refs (top by weight): real/seas/rell 791, release/game/when 704, mobile/game/play 650, haki/armament/conquerors 614 (avgLikes 7.4), gear/blox/fruits 579, xbox/game/mobile 572, movie/release/not 572, gta/before/seas 510 (7.8), YEAR/release/seas 484 (12.9), code/shindo/new 478, better/blox/fruits 454. Full list: extract from `comments_quality.jsonl` type=cluster.

## 6. Per-session protocol
1. Read this file + `insights/` current state. Claim oldest `pending` shard (row edit only).
2. Pull evidence read-only: seed clusters (theme_terms above) + keyword query over quality rows (script it, e.g. token match) + top-by-score sample + lang-stratified sample. Never hand-copy text — extract via script to preserve verbatim.
3. Synthesize that shard's cards (12–20): merge same-thinking rows into one card, keep distinct specifics separate (400 vs 1000 Robux, mobile vs Xbox, EAC-error vs EAC-ban = separate cards). Quote count mixed 3–8 as the card needs (AI decides).
4. Drop the rest of the shard's rows with reasons into `dropped.log` (counts + sample ids, not full text).
5. Write `insights/shard_SXX.jsonl` + append shard section to `insights/insights.md`; update ledger row (`done`, counts, notes); spot-check 5 cards (evidence verbatim + row ids resolve + volume math).
6. Report: shard done, cards added, dropped by reason, running total vs 150–250 target, pending shards, another session needed?

## 7. Quality gates (per shard + final)
- Every quote byte-identical to source row (script-extracted, spot-verified).
- Every factual claim has row ids; volumes are sums, not estimates.
- Each card has exactly one `discord_decision` (or explicit no-action + reason).
- Language: non-EN evidence present where the thinking lives in PT/FR/ES.
- Meme families ≤5 variants total across S09.
- Running total visible in ledger; final must land 150–250. If a shard yields <10 or >25 cards, re-judge the bar (too strict/loose) before closing.
- Final session: concat shards → `insights.jsonl` + `insights.md`, write `insights.stats.md` (input → cards/dropped, language split, top-10 by volume, per-shard yields), verify counts + 30 random cards.

## 8. Progress log (append, newest bottom)
- 2026-10-05 batch S01+S02+S03: 41 cards (INS-001..041), 164 verbatim quotes, all spot-checks pass (15/15: text/likes/video/volume/schema). Running total 41/150–250 (pace projects ~164). Shards pending: S04–S12 (9). Another session needed: yes — suggest S04+S05+S06 next.
- 2026-10-05 batch S04+S05+S06: 39 cards (INS-042..080), 198 verbatim quotes, spot-checks pass (15/15 new + 9/9 rebuilt). Running total 80/150–250 (pace projects ~160). Shards pending: S07–S12 (6). Another session needed: yes — suggest S07+S08+S09 next. Notes: lang detector hardened (EN-colliding markers removed, verified clean); boss-AI rows deferred to S08, leak/rot/grief rows to S10, craft/grief rows parked for S12; GAG thinking merged into INS-040 (no duplicate card).
- 2026-10-05 FINAL batch S10+S11+S12: 37 cards (INS-116..152), 169 verbatim quotes, spot-checks pass (15/15 + 9/9 + 30/30 final). FINAL TOTAL 152/150–250. insights.jsonl (sorted shard→id, continuous) + insights.stats.md written; all deferred rows consumed; ledger complete — no further sessions needed for the bank.
