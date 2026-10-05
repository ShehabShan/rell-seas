# Comment Sentiment Findings — RELL Seas (Stage-2 synthesis of deduped corpus)

Date: 2026-09-18. Input: `rell-seas/comments_dedupe.cleaned.jsonl` (159,211 unique records in full + 168 theme clusters covering 51,976 records, every record counted once — see `comments_dedupe.stats.md`). Method: clusters ranked by count×(1+avgLikes); top-350 uniques by likes read directly; topic volumes counted over kept records (clusters + unique dup-weights); questions mined (16,031 exemplars, 17,092 volume; top question-words: when 1,554, how 1,221, why 1,151).
Companion docs: `yt-comment-findings.md` (pre-dedupe harvest synthesis), `reddit-findings.md`, `caribbros-research.md`. This doc is the weighted, de-duplicated verdict — where it disagrees with the earlier ones, this one wins.
Caveats: topic volumes overlap (one comment can match two topics); two clusters (`botak` 370, `enyu` 233) are single-video phenomena, flagged below, not general findings.

## 1. Top complaints / pain points (ranked by volume × engagement)

| # | Complaint | Volume signal | Peak like |
|---|-----------|---------------|-----------|
| 1 | **"Trailer for a trailer" with no date** — teaser-for-teaser comms read as disrespect, not hype | cluster 340 @ 25.1 avg likes (highest engagement of any theme) | 3,991 ("Trailer to a Trailer is DIABOLICAL") |
| 2 | **"Open testing" perceived as dishonest** — application-gated testing called "open" | unique 4,696 ("limited to applicants = not open testing") | 4,696 |
| 3 | **Date-baiting / vague timelines** — "M3T" with no M3 date; "80% done, just editing" said before filming started | clusters: date 401, summer-window 223 @ 11.5, never-releasing 307 | 1,963 ("release before summer, I want to play all summer") |
| 4 | **Feeling baited / played with** — notifications that aren't M3; trauma language | cluster 346 @ 7.5 | 2,018 ("i think we just got baited") |
| 5 | **Paid-tester cynicism** — EAC seen as monetized early access, not testing; "charged for testing on Roblox is cheap", comparisons to games accused of scams | cluster 255 (tester-talk) + unique 330 ("closed paid testing… accused of scams like 10 times") | 330 |
| 6 | **Copyright dread** — fear Toei/Bandai or Roblox moderation kills the game; anger at big companies "making examples out of children" | cluster 236 + unique 4,946 | 4,946 |
| 7 | **Aging out while waiting** — fans who had time in 2021–22 are now in college/work; "took so long im in college now", "graduated high school since quarantine" | cluster 265 @ 7.0 + uniques 736/1,035 | 1,035 |
| 8 | **Platform anxiety** — potato-PC/mobile players fear they can't run it; "Mobile players 💀 / PC players 😈"; iPad-only players asking for mobile support | clusters: mobile 650, pc-vs-mobile 246 @ 5.1; topic vols mobile 8.5K, console/PS 6.7K, xbox 4.2K | 1,140 |
| 9 | **No-wiki-needed promise must hold** — the behind-the-scenes line is now a quoted standard; incompleteness felt in newer trailers vs older ones | uniques 3,333 + 315 | 3,333 |
| 10 | **Fake games / scams** — players buying fake "Rell Seas" copies; official warning exists but discovery is the gap | topic vol 4.8K; official anti-scam comment 452 likes | 452 (dev comment) |

## 2. Top requests (what they want)

1. **Rare fruits, hard to get** (unique 2,994 + 692; fruit topic 48.5K — largest topic in corpus): "praying fruits are ACTUALLY rare… that's what made early GPO good." Directly validates the devs' hard-fruit stance; the server should quote it back.
2. **NPC fear/respect + living world** (unique 4,116): notorious pirates with high bounty should frighten NPCs; ocean/island life over pure powers (726: "needs to be about the ocean not only fruits"). Simulation-depth hunger, not power-fantasy hunger.
3. **Non-P2W oath kept** (1,742: "'non-pay-to-win, PLEASE keep your word, I will be quoting this'"): cosmetics-only acceptable, power-selling is the red line. Price/paid topic 11.8K, free 7.0K.
4. **Haki depth + accuracy** (cluster 614 @ 7.4; haki topic 19.1K): Armament/Conqueror/Observation theorycraft, Haki-first meta belief, "Shanks builds would go crazy" (4,845 on a meme video).
5. **Bosses harder and aggressive** (540 + 736): less backdash-cowardice, fewer rest periods, faster — "bosses feel scared of the player."
6. **Crew-finding, incl. non-English** (topic 4.4K; clusters 264 + 226): "montando uma crew… mande o dc", "imagine you and me become crewmates", grandkids-in-my-crew jokes. Matchmaking is wanted infrastructure.
7. **Build library** (Bartolomeo counter-guides, Mochi grind plans, outfit-affects-Gear-4 hopes at 340, race-not-behind-spinwheel praise at 317).
8. **Ocean/ships/submarine life** (topic 5.4K), professions/jobs RP (cross-ref reddit-findings), newspapers-from-sky info systems (337).
9. **Mobile/Xbox ports + optimization proof** (see §1.8; "extra optimized for mobile" claims circulate unverified — pin only confirmed statements).
10. **Straight answers, labeled content** ("Not movie 3 is devious but im just happy to get some news" 2,823): honesty outperforms hype; teasers should be labeled sneak-peeks, never date-implying.

## 3. Top praise (what's genuinely loved)

- **Dev work ethic worship** (cluster 248 @ 22.0 avg likes — the most-liked positive theme): "12–16 hours a day… THANK YOU", "hardest working devs on Roblox rn" (337), veterans "since 2018/2021" tearing up at progress (64–455). Loyalty reservoir is enormous — and perishable (see §1.7).
- **Animation/visual supremacy** (looks-good cluster 439; peak 402; fire 397; "devs get lost in their own map" 5,799; One-Piece-games-curse破碎 "WE MAKING IT OUT" 2,815; Mochi ult / buzzcut frame-by-frame love 448).
- **"In on the joke" dev tone** ("i appreciate you too, baka" 2,089; milk-cow skit tolerated): self-aware humor is forgiven and loved — but only attached to real information (contrast: QNA mocked as "Questions, No Answers").
- **Rivalry confidence** ("better than Blox Fruits by all means"; "RELL SEAS WILL SAVE US FROM GROW A GARDEN" 3,012; fruit-comparison topic 35.4K): the audience recruits itself against competitors — give them shareable comparison assets, not attack lines.
- **Shindo coexistence, not replacement** (topic 23.8K; "Shindo was a childhood well spent" 3,123; codes-helpfulness): the devs' other game is a trust anchor. Never frame Seas as abandoning Shindo players.

## 4. The release-date dynamic (standalone)

**Size.** The date family is the largest emotional throughline: YEAR-anchored jokes 484 @ 12.9, release-when 704, movie-release 572, coming-out 437, date-please 401, never-releasing 307, summer-window 223 @ 11.5 — roughly 3,000+ clustered records plus a long tail of one-off year jokes (2030/2040/2043/2048/2099 all attested; "I'll see y'all in 2043" 4,301; "friends we made along the way" 4,807). The Stage-1 keyword check (~3%) undercounted by an order of magnitude because of year-number and PT/FR variety ("te vejo em 2026 🫡", timestamp-detective work like "video length 26:27 = delayed to 2027").

**Expression.** Three registers: (a) meme-coping (year jokes, GTA-6-before-Seas 510 @ 7.8 — the single most-liked joke format), (b) earnest pleading (summer-window cluster: "release before summer, I want to play all summer" 1,963 — the emotional core is *seasonal life plans*, not impatience), (c) forensic accountability (timeline audits, "add a month then add three", checklist-frame analysis, three-hour "calculations" played half-straight at 88 likes).

**Triggers.** Spikes attach to: date-shaped content with no date (M3T), post-announcement silence, "soon"-language, comparisons (Shindo updating while Seas waits; Blox Dragon rework racing Seas), and microlinguistics ("80% done, just editing" → later revealed pre-filming). Pride ("GOLDEN AGE… WE HAVE MADE IT" 5,675) flips to salt within one dateless drop — the hype→salt cycle is ~days, not weeks.

**Design consequence.** Your server must never manufacture dates: quote rough windows verbatim with source + slip-tag; run monthly prediction rituals (locked answers, post-release reveal) to *contain* date energy; keep a meme-channel pressure valve so salt doesn't flood feedback channels.

## 5. Direct Discord-design implications

1. **Pinned FAQ channel is mandatory.** The same five questions repeat forever: mobile support? Xbox/console? free or paid/how much Robux? EAC = what/when/how to become tester? release date? (16K question exemplars; when/how/why/get top question-words.) Answer with sourced dev quotes only; mark speculation.
2. **Verified-links + scam-watch channel.** Fake games steal money *and* trust; the official warning (452 likes) proves demand. Pin the real game link (ID 70899…), publish a scam-spotting masterpost, route victim help via tickets.
3. **Containment architecture.** Meme/salt channel with rules (seasposting model) + prediction-ritual channel + evidence/detective board (checklist frames, backend watches, audio-clip forensics with SPECULATION tags) + wishlist/feedback with template (what/why/trade-off). Salt kept out of serious channels by design, not by bans.
4. **Crew finder with language filter.** EN/PT (and FR) crew posts recur; r/RELLseas already centralizes recruiting in a weekly megathread — copy the cadence (weekly refresh) and add language tags.
5. **Language hubs (PT ≥ FR).** PT clusters (398 + 383) plus FR/ES/VI/ID traces; small-creator sections run on PT questions; "botak" episode proves SEA presence. At minimum: PT + FR social channels with native-speaker mods; never machine-translate rules.
6. **EAC trust kit.** Tester cynicism is the #1 trust risk at launch: day-one EAC survival guides, "what testers wish they knew", bug-report templates, and explicit paid-vs-free difference tables. Position the server as tester-friendly before EAC lands.
7. **Feedback loop, publicly closed.** "You asked → it's in" posts revive dead rooms; never delete respectful criticism; recruit veteran volunteer mods (appreciation cluster shows the culture rewards recognition — spotlight helpers, not just chatters).
8. **Reactivation engine for aged-out fans.** The "in college now" cohort is your launch-day spike: keep a low-pressure alumni role + "I was here since quarantine" identity hooks + comeback events tied to real milestones (M3, EAC), never to invented dates.
9. **Creator symbiosis.** Small creators live off frame-detective work and checklist analysis — feed them (sneaks-vault, timestamped breakdowns); they recruit for you. Credit, don't compete.
10. **Tone law.** Project-manager voice (progress bars, phases, "combat team is refining X"), never hype-man ("soon"); dev/staff visible presence in chat and voice beats announcements; self-aware humor only when attached to substance.

## 6. Source comparison + ambiguities

- **yt-research vs caribbros are different windows, overlapping now.** cb spans 2022–2026 (dev-channel history: Shindo codes/OST/old sneaks); yt concentrates 2023–2026 with Jul–Sep 2026 peaks. Unique volume 140K (yt) vs 29K (cb); top-100 liked uniques go 97–3 to yt — big-creator videos mint the most-endorsed opinions, cb holds dev-directed loyalty + history. 17 shared videos (10,127 shared comments) merged, not double-counted.
- **cb skews devotional** (appreciate-cluster 81 of 248 from cb; encouragement, patience pleas); **yt skews forensic and comparative** (timeline audits, Blox rivalry, bug-pointing). Design for both: a warmth space AND an evidence space.
- **Ambiguities.** (a) `scammed/baited` cluster is ~80% trailer-disappointment ("got baited"), ~20% literal fraud — don't cite it as fraud volume. (b) `real seas rell` (791) is an authenticity chant/hype, not a question. (c) `nah bro blox` (255 @ 32.2) is a reply-guy artifact — its score rides one 8,056-like copyright-video comment; treat as medium, not top, signal. (d) PT price talk ("400–1000 Robux") is pooled speculation, never confirmed — label as rumor in any FAQ. (e) Sentiment proportions from the earlier harvest memo (30/40/20/10 hype/fatigue/frustration/humor) are directionally right but were unweighted; weighted ranking in §1 supersedes them.
