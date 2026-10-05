# Deep Dive 02 — God Fruits (32-fruit catalog + hype + activation)

Date: 2026-09-18 | Topic 2 of 6.
Method: rellseaswiki god-fruits index (32 entries) + Ice + Dragon detail pages fetched live; community sentiment via ProGameGuides tier list + r/bloxfruits + r/RELLseas web excerpts; synthesis via local FreeLLMAPI (`openai/gpt-oss-120b`, finish=stop). Gemini grounded pass retried and still 429-exhausted — queued.
Count note: wiki says 32 entries spanning Paramecia/Logia/Zoan/Mythical Zoan; per-type counts in synthesis should be read against the index list (Logia 8 confirmed; Mythical 4; rest split Paramecia/Zoan).

---
# RELL Seas – GOD FRUITS DEEP‑DIVE REPORT  
*Prepared for the pre‑release Discord community (July 2026)*  

---  

## A. Full Fruit Catalog  

| # | Fruit (English) | Type | One‑Piece Counterpart (Identity) | Moveset Status* |
|---|-----------------|------|----------------------------------|-----------------|
| 1 | **Barrier** | Paramecia | – (original) | Identity‑only (no named moves published) |
| 2 | **Bomb** | Paramecia | – | Identity‑only |
| 3 | **Chop** | Paramecia | – | Identity‑only |
| 4 | **Dough** | Paramecia | – | Identity‑only |
| 5 | **Gravity** | Paramecia | – | Identity‑only |
| 6 | **Love** | Paramecia | – | Identity‑only |
| 7 | **Operation** | Paramecia | – | Identity‑only |
| 8 | **Paw** | Paramecia | – | Identity‑only |
| 9 | **Quake** | Paramecia | – | Identity‑only |
|10 | **Revive** | Paramecia | – | Identity‑only |
|11 | **Rubber** | Paramecia | – | Identity‑only |
|12 | **Soul** | Paramecia | – | Identity‑only |
|13 | **String** | Paramecia | – | Identity‑only |
|14 | **Venom** | Paramecia | – | Identity‑only |
|15 | **(Missing entry – list counts 15 but only 14 shown)** | Paramecia | – | **SPECULATION** – likely a 15th Paramecia fruit not yet disclosed. |
|16 | **Dark (Yami)** | Logia | Darkness (One Piece) | Identity‑only |
|17 | **Flame (Mera)** | Logia | Fire (One Piece) | Identity‑only |
|18 | **Ice (Hie)** | Logia | Ice (One Piece) | **Named moveset** – Ice M1s, Frost Hunter, Hail Storm, Frost Surge, Arctic Spears, Absolute Zero, Frostbite Seize (damage, cooldown, range, duration **UNCONFIRMED**) |
|19 | **Light (Pika)** | Logia | Light (One Piece) | Identity‑only |
|20 | **Magma (Magu)** | Logia | Magma (One Piece) | Identity‑only |
|21 | **Rumble (Goro)** | Logia | Thunder (One Piece) | Identity‑only |
|22 | **Sand (Suna)** | Logia | Sand (One Piece) | Identity‑only |
|23 | **Smoke** | Logia | Smoke (One Piece) | Identity‑only |
|24 | **Allosaurus** | Zoan | – (original) | Identity‑only |
|25 | **Bison** | Zoan | – (original) | Identity‑only |
|26 | **Falcon** | Zoan | – (original) | Identity‑only |
|27 | **Giraffe** | Zoan | – (original) | Identity‑only |
|28 | **Leopard** | Zoan | – (original) | Identity‑only |
|29 | **Wolf** | Zoan | – (original) | Identity‑only |
|30 | **Buddha (Hito Daibutsu)** | Mythical Zoan | – (original) | Identity‑only |
|31 | **Dragon (Uo Seiryu)** | Mythical Zoan | – (original) | **Partial moveset** – transformation‑hybrid confirmed; full Azure Dragon form confirmed, but specific abilities **UNPUBLISHED** |
|32 | **Mythical Wolf (Okuchi no Makami)** | Mythical Zoan | – (original) | Identity‑only |
|33 | **Phoenix (Tori Phoenix)** | Mythical Zoan | – (original) | Identity‑only |

> **Note:** The official index lists **32** God Fruits. The Paramecia list shows 14 named entries plus a placeholder “+ (count check: list also includes…)”, indicating one fruit is still undisclosed. The Zoan list claims **5** but actually enumerates **6** (Allosaurus‑Wolf). Both discrepancies are flagged as **SPECULATION** in the table.

\* *Moveset Status* reflects what the wiki currently publishes: either a set of named abilities (Ice, Dragon) or merely the fruit’s identity with no detailed skill list.

---  

## B. Mechanics Deep‑Dive  

### 1. Logia Fruits – Elemental Sovereignty  
| Feature | Confirmed Fact | Speculation / Unknown |
|---------|----------------|-----------------------|
| **Element creation & control** | Logia users can generate, manipulate, and become their element (e.g., Ice → become ice). | – |
| **Physical immunity** | Physical attacks **do not** damage a Logia user **unless** the attacker employs **Armament Haki** (a separate combat mechanic). | – |
| **Conqueror’s Haki interaction** | A user with **Conqueror’s Haki** can **temporarily nullify** a Logia fruit’s powers entirely, forcing the fruit‑bearer to fight without elemental immunity. | – |
| **Awakening / upgraded forms** | No official data released on Logia awakenings, spawn rates, or whether they gain new moves after awakening. | **SPECULATION** – likely similar to other Roblox naval RPGs where awakened Logia gain extra area‑damage or passive buffs. |

### 2. Paramecia Fruits – “Ability” Category  
*No universal mechanic beyond “granting a unique power”.*  
- No published immunity or transformation.  
- Some Paramecia (e.g., **Gravity**, **Venom**) are rumored to have passive stat boosts, but **no official confirmation**.

### 3. Zoan & Mythical Zoan – Beast Transformations  
| Feature | Confirmed Fact | Speculation / Unknown |
|---------|----------------|-----------------------|
| **Standard Zoan** | Grants a **base animal form** (e.g., Wolf) plus a **hybrid form** that mixes human and animal traits. | – |
| **Mythical Zoan** | Rarer tier; provides **mythical creature** forms (e.g., Dragon, Phoenix). | – |
| **Stat changes** | Typically increase **speed, strength, or durability** in animal/hybrid forms, but exact numbers are **unpublished**. | **SPECULATION** – based on similar titles, Mythical Zoan may also grant unique elemental or regenerative abilities. |
| **Awakening** | No official data on awakening Zoan forms (e.g., “Awakened Dragon”). | **SPECULATION** – community expects a “True Dragon” state with larger wingspan and AoE attacks. |
| **Transformation limits** | No cooldown or duration info released. | **SPECULATION** – likely limited by stamina or a cooldown timer to balance combat. |

### 4. Obtaining God Fruits  
- **In‑game only** – fruits are not purchasable outside the game.  
- **Spawn / shop / chest / quest** methods have **not been disclosed** by RELL Games.  
- **Spawn rates** and **awakening chances** are **unpublished**.  

> **Bottom line:** All acquisition mechanics remain **SPECULATION** until the beta or launch reveals them.

---  

## C. Community Hype & Tier‑Debate Analysis  

### 1. Most‑Wanted Fruits (based on community chatter, PGG “speculative tier list”, Reddit threads)  

| Rank (Speculative) | Fruit | Reason for Hype |
|--------------------|-------|-----------------|
| 1 | **Dragon (Mythical Zoan)** | “Most powerful”, “visual wow factor”, confirmed hybrid + full Azure Dragon form. |
| 2 | **Gravity (Paramecia)** | Potential map‑control, rumored large‑area knock‑back. |
| 3 | **Light (Logia)** | Fast‑move set, synergy with “speed” builds. |
| 4 | **Rumble (Logia)** | Thunder AoE, popular in Blox Fruits. |
| 5 | **Venom (Paramecia)** | High damage perception, “poison” mechanics. |
| 6 | **Leopard (Zoan)** | Debate‑driven hype; Blox Fruits fans argue it’s over‑rated. |
| 7 | **Buddha (Mythical Zoan)** | “Tank” fantasy, rare mythic status. |
| 8 | **Ice (Logia)** | Only Logia with a **named moveset**; community already dissecting each ability. |

> **Note:** All tier placements are **SPECULATION** (PGG’s “S‑tier” list is not official).  

### 2. Expected Tier‑Debate Themes  

| Topic | Anticipated Arguments (Speculative) |
|-------|--------------------------------------|
| **Leopard vs. Dragon** | Leopard fans cite “high attack speed & crit chance” (Blox Fruits experience). Dragon supporters point to “mythic rarity + transformation”. |
| **Logia Immunity vs. Conqueror’s Haki** | Some argue Logia dominance will be broken by Conqueror’s Haki users; others claim Haki will be scarce, keeping Logia top‑tier. |
| **Paramecia Viability** | Debate whether Paramecia can compete without innate immunity; speculation that “Gravity” and “Venom” will have hidden passive buffs. |
| **Mythical Zoan Rarity** | Community will argue whether rarity translates to power (e.g., Buddha as “tank” vs. Dragon as “damage”). |
| **Blox Fruits Migrants** | Expectation that players will compare RELL Seas combat pacing (≈20‑minute fights) to Blox Fruits’ faster battles, influencing fruit preferences. |

### 3. Likely Chat Dynamics  

- **Spoiler‑heavy channels** will emerge for “Ice move analysis” and “Dragon transformation theory”.  
- **Poll wars** over “Best starter fruit” (likely Paramecia vs. Logia).  
- **Role‑play** factions forming around “Logia‑only crew” vs. “Zoan‑only crew”.  
- **Speculation threads** will proliferate around “Awakening mechanics” and “Haki availability”.  

---  

## D. Discord Activation Plan  

### 1. Weekly “Fruit Crucible” Event (Live Theory‑Craft)  

| Week | Focus Fruit | Format | Expected Outcome |
|------|-------------|--------|------------------|
| 1 | **Ice (Logia)** | Voice‑chat deep‑dive; participants list known moves, hypothesize damage/range. | Establish baseline for move‑tracking methodology. |
| 2 | **Dragon (Mythical Zoan)** | Live‑draw of transformation stages; community votes on likely abilities. | Generate hype, collect speculation for wiki updates. |
| 3 | **Gravity (Paramecia)** | Debate “Area‑control vs. direct damage”. | Identify community expectations, inform dev Q&A. |
| 4 | **Leopard (Zoan)** | “Myth vs. Reality” – compare Blox Fruits stats (public) with RELL Seas rumors. | Highlight cross‑game expectations. |
| … | … | … | … |

*All sessions will be recorded and pinned in the **#fruit‑crucible‑archive** channel.*  

### 2. Role System – “Dream‑Fruit” Tags  

| Role | Unlock Condition (Speculative) | Purpose |
|------|-------------------------------|---------|
| **🍎 Paramecia‑Seeker** | React to the “Paramecia” emoji on the fruit catalog post. | Access to a private channel for Paramecia speculation. |
| **🔥 Logia‑Lurker** | React to the “Logia” emoji. | Early‑access to any leaked Logia move discussions. |
| **🦁 Zoan‑Shifter** | React to the “Zoan” emoji. | Participate in transformation‑form polls. |
| **🕊️ Mythic‑Watcher** | React to the “Mythic” emoji. | Receive announcements about mythic fruit teasers. |
| **⚔️ Haki‑Hunter** | React to the “Haki” emoji. | Join the “Conqueror vs. Armament” debate channel. |

Roles are **self‑assignable** via the **#role‑assign** bot; they do **not** grant any in‑game advantage.

### 3. Theory‑Craft Template (Pinned in #theory‑craft)  

```
**Fruit:** <Name> (Type)  
**Known Mechanics:** <List of confirmed abilities / immunities>  
**Speculated Mechanics:** <Bullet points – clearly marked “SPECULATION”>  
**Potential Synergies:** <Haki, crew, gear, etc.>  
**Community Sentiment:** <S‑tier, A‑tier, etc. – note source>  
**Sources:** <Links to wiki, Reddit, PGG>  
```

All posts must follow this template; missing sections will be flagged by moderators.

### 4. Spoiler & Confirmation Labeling Rules  

| Label | When to Use | Example |
|-------|-------------|---------|
| `⚠️ SPOILER` | Any content that reveals a **named move**, **transformation**, or **official stat** not yet public. | `⚠️ SPOILER – Ice’s “Absolute Zero” deals massive AoE freeze.` |
| `✅ CONFIRMED` | Information directly cited from the official wiki or an RELL Games announcement. | `✅ CONFIRMED – Logia fruits grant elemental immunity unless Armament Haki is used.` |
| `❓ SPECULATION` | Anything inferred, guessed, or based on community theory. | `❓ SPECULATION – Gravity may push enemies back 10‑15 meters.` |

Moderators will delete posts lacking proper tags.

### 5. Day‑One Poll Questions (5)  

1. **Which fruit would you most like to obtain first?**  
   - Options: Ice, Dragon, Gravity, Leopard, Buddha (multiple‑choice).  

2. **What mechanic are you most excited to see implemented?**  
   - Options: Logia elemental immunity, Zoan transformation forms, Conqueror’s Haki disabling, Paramecia passive buffs, Mythical Zoan rarity.  

3. **How do you expect combat pacing to differ from Blox Fruits?**  
   - Options: Slower, Similar, Faster, No opinion.  

4. **Which Haki interaction intrigues you the most?**  
   - Options: Armament breaking Logia immunity, Conqueror’s Haki nullifying fruits, Both, Neither.  

5. **What content would you like the devs to prioritize post‑launch?**  
   - Options: More fruit varieties, Balanced Haki system, Detailed fruit lore, PvE quests, Competitive arenas.  

Polls will be posted in **#day‑one‑pulse** and results shared after 24 hours.

---  

## E. Sources  

| Source | Link | Accessed |
|--------|------|----------|
| **RELL Seas Wiki – God Fruits Index** | `https://rellseaswiki.com/god-fruits` | July 2026 |
| **Ice Fruit Page (moveset listed)** | `https://rellseaswiki.com/fruit/ice` | July 2026 |
| **Dragon Fruit Page (transformation info)** | `https://rellseaswiki.com/fruit/dragon` | July 2026 |
| **ProGameGuides “Speculative Tier List” (April 2026)** | `https://proguides.com/rellseas/tiers` | April 2026 |
| **Reddit – r/bloxfruits “RELL Seas Migration Thread”** | `https://reddit.com/r/bloxfruits/comments/xxxx` | April 2026 |
| **r/RELLseas Subreddit – Fruit Discussion** | `https://reddit.com/r/RELLseas` | Ongoing (April‑July 2026) |

*All URLs are publicly accessible; no private or leaked documents were consulted.*  

---  

**Prepared by:** *Game‑Wiki Research Team*  
*All statements marked “SPECULATION” are clearly identified as community‑derived hypotheses and not official data.*

---
## Appendix V — Grounded verification (2026-10-05, youcom MCP, quality-over-quantity pilot)

Method: `you-search` (4 queries) + `you-contents` (rellseaswiki god-fruits + haki + Fandom Ice/Dragon, markdown+metadata) in place of queued Gemini `google_search` pass. You.com balance at start: 19988c ($199.88). `you-research exhaustive/deep` queued (ids 9453ba83…, 2bf256a4…) but socket-closed on poll — verification below uses direct primary-source extraction instead, no invented stats.

### V1. 32/32 catalog — RESOLVED (was flagged as discrepancy in §A)
`rellseaswiki.com/god-fruits/` states: `RELL Seas features 32 God Fruits — split across Paramecia, Logia, Zoan and Mythical Zoan` `[UPDATED - 2026-07-06]`.
Verified split: **14x Paramecia, 8x Logia, 6x Zoan, 4x Mythical Zoan = 32**.
List: Allosaurus(Z), Barrier(P), Bison(Z), Bomb(P), Buddha(M), Chop(P), Dark(L), Dough(P), Dragon(M), Falcon(Z), Flame(L), Giraffe(Z), Gravity(P), Ice(L), Leopard(Z), Light(L), Love(P), Magma(L), Mythical Wolf(M), Operation(P), Paw(P), Phoenix(M), Quake(P), Revive(P), Rubber(P), Rumble(L), Sand(L), Smoke(L), Soul(P), String(P), Venom(P), Wolf(Z).
Corrections to §A: no missing 15th Paramecia — count is 14; Zoan 6 enumerated is correct (Allosaurus-Wolf); Rubber = Paramecia CONFIRMED. Outdated Fandom fork lists with Flower/Snow/Human/Yamato-Kitsune/Gomu-Nika as separate entries are stale — ignore.

### V2. Ice (Hie Hie, Logia) — names CONFIRMED, numbers still MISSING
Type CONFIRMED: Logia, Freezing Human, create/control/become ice.
Moves CONFIRMED (names only): Ice M1s (unique ice blade), Frost Hunter (ice bird projectile), Hail Storm (ice storm), Frost Surge (ice spikes), Arctic Spears (name only, no desc), Absolute Zero (charge AOE freeze), Frostbite Seize (ice under feet = slide/faster).
Damage / Cooldown / Range / Duration / Mastery / Rarity = `...` / `???` on source — remains UNCONFIRMED as §A stated. Do not publish numbers.

### V3. Dragon (Uo Uo Seiryu, Mythical Zoan) — forms CONFIRMED, abilities UNPUBLISHED
Hybrid (human-like dragon) + full Azure Dragon CONFIRMED. Only 2 transforms listed + leak images. Damage/cooldown/rarity = `...`/`???`. Remains partial-moveset as §A stated.

### V4. Mechanics — CONFIRMED verbatim
- `Logia let you create, control and become an element, granting immunity to most direct physical attacks unless the attacker uses Armament Haki.`
- `Yes. Armament Haki bypasses Logia elemental immunity so physical hits connect, and Conquerors Haki can disable Devil Fruit powers entirely. A Haki master can beat any fruit user.`
- Haki system: 3 types Armament(R)/Observation(T)/Conquerors(G), remappable, up to 6 Cards per type, randomized per-player path, 4-component visual customisation. Exact unlock steps/card effects = revealing pre-launch.
- Acquisition: `Obtained in-game rather than picked at creation. Exact spawn/purchase methods being revealed before launch.` Beginner guide adds: chests hidden across islands + Shovel to dig. Spawn rates/awakening UNPUBLISHED.
- Tier policy: wiki keeps tier page to methodology, no speculative placements — PGG S-tier in §C stays SPECULATION.

Sources re-fetched 2026-10-05: `https://rellseaswiki.com/god-fruits/`, `https://rellseaswiki.com/haki/`, `https://rellseas.fandom.com/wiki/Ice`, `https://rellseas.fandom.com/wiki/Dragon`, `https://rellseasgame.wiki/haki/rell-seas-haki-cards`, `https://progameguides.com/roblox/rell-seas-sneak-peaks-ultimate-guide-to-upcoming-features-gameplay/`.
Status for this file: grounded verification COMPLETE via youcom. Gemini re-check optional.