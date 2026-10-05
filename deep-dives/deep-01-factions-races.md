# Deep Dive 01 — Factions & Races (pre-release reference)

Date: 2026-09-18 | Topic 1 of 6 in deep-research queue.
Method: primary sources fetched live (rellseaswiki faction pages ×4) + synthesis via local FreeLLMAPI gateway.
IMPORTANT: user asked for Gemini deep-research grounding (`gemini-3.7-flash` + `google_search` tool). Both Gemini attempts hit Google free-tier 429 quota exhaustion, so this pass was synthesized with `openai/gpt-oss-120b` (router) from fetched facts. A Gemini grounded verification pass will be appended once quota resets. Anything marked SPECULATION below must stay labeled until confirmed.

---
**RELL Seas – Pre‑Release Player‑Faction & Race Reference**  
*Compiled August 2026 – based on the official wiki (rellseaswiki.com) and publicly‑available developer statements. All items that are not directly confirmed are marked **SPECULATION**.*

---

## A. Faction “Cards”

| Faction | Tagline | Core Philosophy | How to Join (Confirmed) | Rank Structure / Rewards (Confirmed) | Advantages (Confirmed) | Disadvantages (Confirmed) | Speculative Add‑ons |
|--------|---------|-----------------|--------------------------|--------------------------------------|------------------------|----------------------------|---------------------|
| **Pirates** | “Sail free, answer to none.” | Freedom‑first, self‑made crews, no central recruiter. | Create a player‑owned crew or align with one of the **40+ NPC pirate crews** (permanent relationship outcomes: help / fight / ignore). | No official rank ladder disclosed by the wiki. Recognition is granted by the **Council of Piracy** → “official crew” status. | • Dynamic bounty system that scales against Marine players.<br>• No taxes on earnings.<br>• Ability to forge lasting NPC relationships.<br>• Access to Hades Asylum (prison) only when captured – can be used for story events. | • If caught, you are sent to **Hades Asylum** (6‑floor prison).<br>• No built‑in tax revenue, so personal wealth is fully exposed to bounty hunters.<br>• No formal recruitment pipeline – you must find a crew yourself. | • Possible “Dragon Claw Fist” combat style (see **Arms of Revolution** notes). |
| **World Seas Marine Corps** | “Order on the waves.” | Hierarchical order, law‑enforcement, protection of the World Seas. | Speak to the **Marine Base Recruiter NPC** inside the main building and accept the entry quest. | **21‑rank ladder (officially listed):**<br>Recruit I → Recruit II → Recruit III → Cadet I → Cadet II → Cadet III → Officer I → Officer II → Officer III → Scout I → Scout II → Scout III → Lieutenant I → Lieutenant II → Lieutenant III → Commander → Captain → Rear‑Admiral → Vice‑Admiral → Admiral → **Fleet Admiral** (top).<br>• **Admiral perk:** direct elevator access to all 6 floors of Hades Asylum.<br>• Lower ranks must progress floor‑by‑floor. | • Access to **Marine‑exclusive missions** and **Marine Bases** (fast travel, storage, ship upgrades).<br>• Potential **Rokushiki** fighting style (see SPECULATION).<br>• Reputation system tied to Marine duties. | • **Taxes** are levied on all earnings (percentage not disclosed).<br>• Must obey the chain‑of‑command; limited freedom to act outside orders.<br>• Higher ranks require completion of floor‑by‑floor Hades Asylum challenges (except Admiral). | • Exact tax rate, reputation thresholds, and any additional perks beyond Admiral are **SPECULATION**. |
| **Arms of Revolution** | “Rise against oppression.” | Covert insurgency, spark rebellions, liberate oppressed regions. | **UNREVEALED** – no official recruitment NPC or quest has been disclosed. | No rank ladder disclosed. | • No taxes on earnings.<br>• Access to **black‑market** resources (mentioned but not detailed). | • High‑risk, secretive playstyle; may attract Marine bounty.<br>• Lack of formal support structures (e.g., bases). | • Possible **Dragon Claw Fist** combat style.<br>• Exact joining method (e.g., secret NPC, invitation‑only) is **SPECULATION**. |
| **World Seas Government** | “Supreme authority, even if corrupt.” | Central authority above the Marines; maintains order (often through questionable means). | **UNREVEALED** – no official recruitment path disclosed. | No rank ladder disclosed. | • Potential access to **Rokushiki** fighting style (mentioned as possible).<br>• Influence over Marine policy and tax structures. | • Reputation may be tarnished by corruption narrative.<br>• May be targeted by the Arms of Revolution. | • Exact benefits, duties, and joining mechanics are **SPECULATION**. |

### Quick Reference – Faction Summary

| Faction | Playstyle | Tax? | Bounty System? | Prison Interaction | Known NPC/Org |
|--------|-----------|------|----------------|-------------------|---------------|
| Pirates | Open‑world, crew‑driven, freedom | **No** | **Dynamic** (vs. Marines) | Captured → Hades Asylum (6 floors) | Council of Piracy, 40+ NPC crews |
| Marine Corps | Structured, mission‑based, law‑enforcement | **Yes** (tax on earnings) | **Yes** (Marine bounty on pirates) | Admiral → elevator to all floors; lower ranks climb floor‑by‑floor | Marine Base Recruiter, Marine Bases |
| Arms of Revolution | Guerrilla, covert, rebellion | **No** | **Yes** (Marine bounty) | No official prison perk; likely targeted by Marines | Black‑market (rumoured) |
| World Seas Government | Central authority, political power | **Yes** (implied via tax system) | **Yes** (Marine bounty) | No direct prison perk disclosed | Government affiliates (list on wiki) |

---

## B. Race “Cards”

| Race | Confirmed Traits & Lore | Customisation Options (Confirmed) | SPECULATION (Unconfirmed Slots) |
|------|--------------------------|-----------------------------------|----------------------------------|
| **Skypiean** | Possess **angelic wings** granting aerial mobility (flight mechanics confirmed). | Wing style & color (various palettes). | – |
| **Fishmen** | **Underwater dominance** – can breathe and move efficiently underwater; stronger melee in water. | Skin tone, fin/scale patterns, tail length. | – |
| **Minks** | Mammalian‑anthropomorphic (tiger, leopard, rabbit, squirrel variants). **Electro‑shock** ability confirmed (passive or active not fully detailed). **Sulong** (white‑fur moon‑evolution) triggers during night cycle. **Night cycle** changes every **2 IRL hours**. **Goat‑horn** and **fur‑color** customization (white, brown, pink, yellow). | Horn shape, fur colour, pattern, eye colour. | – |
| **[Unconfirmed Race #1]** | – | – | No official name or traits released. Community speculation includes a **“Celestial Dragon”** race with fire‑based abilities. |
| **[Unconfirmed Race #2]** | – | – | Rumoured **“Golem”** or stone‑based race with high defense, but no confirmation from developers. |

> **Note:** The wiki lists *five* playable races at launch. Only three are fully described; the remaining two are placeholders until RELL Games releases further details.

---

## C. Confirmed‑vs‑Speculated Master Table

| Element | Confirmed (✓) | Speculated (✗) | Source |
|---------|---------------|----------------|--------|
| **Four player factions** | ✓ | – | Faction page (rellseaswiki.com) |
| **Pirate Council of Piracy** | ✓ | – | Pirate faction page |
| **Dynamic bounty system (Pirates vs. Marines)** | ✓ | – | Pirate & Marine pages |
| **Hades Asylum 6‑floor prison** | ✓ | – | Prison system page |
| **Marine rank ladder (21 ranks)** | ✓ | – | Marine Corps page |
| **Admiral elevator perk** | ✓ | – | Marine page |
| **Marine taxes on earnings** | ✓ | – | Marine page |
| **Marine‑exclusive missions/areas** | ✓ | – | Marine page |
| **Rokushiki fighting style (Marine & Government)** | ✗ | Possible combat style mentioned but not confirmed | Faction pages (marked “possible”) |
| **Dragon Claw Fist style (Revolution)** | ✗ | Possible combat style mentioned but not confirmed | Revolution page (marked “possible”) |
| **Arms of Revolution joining method** | ✗ | Unrevealed, speculation only | Revolution page |
| **World Seas Government joining method** | ✗ | Unrevealed, speculation only | Government page |
| **Skypiean wing flight** | ✓ | – | Race page |
| **Fishmen underwater breathing** | ✓ | – | Race page |
| **Mink electro‑shock & Sulong** | ✓ | – | Race page |
| **Mink night‑cycle 2 IRL h** | ✓ | – | Race page |
| **Mink goat‑horn & fur‑color options** | ✓ | – | Race page |
| **Two additional races (names/traits)** | ✗ | Unconfirmed slots; community speculation only | Race overview page |

---

## D. Discord Activation Plan (Pre‑Release Community)

### 1. Server Roles (auto‑assigned via verification bot)

| Role | Symbol | Eligibility | Permissions |
|------|--------|--------------|-------------|
| **@New Recruit** | 🟢 | All verified members | Basic chat, read‑only announcements |
| **@Pirate** | ☠️ | Members who complete the **Pirate Quiz** (see onboarding) | Access to Pirate‑only channels, crew‑recruitment board |
| **@Marine** | ⚓ | Members who complete the **Marine Quiz** | Access to Marine‑only channels, rank‑ladder discussion |
| **@Revolutionary** | 🔥 | Members who pass the **Revolution Quiz** | Access to covert‑ops channel, black‑market speculation |
| **@Government** | 🏛️ | Members who pass the **Government Quiz** | Access to policy‑talk channel |
| **@Skypiean**, **@Fishmen**, **@Mink**, **@Race‑4**, **@Race‑5** | 🕊️ / 🐟 / 🐾 / ❓ / ❓ | Self‑assigned after race‑selection poll (no verification needed) | Cosmetic role colour, race‑specific emoji |
| **@Crew‑Leader** | 👑 | Player‑created crew owners (verified via in‑game screenshot) | Crew‑management channel |
| **@Moderator** | 🛡️ | Staff | Full moderation |
| **@Bot** | 🤖 | System | Bot commands only |

### 2. Core Channels (ordered by priority)

| Category | Channel | Purpose |
|----------|---------|---------|
| **Info** | `#welcome` | Server rules, verification steps, link to wiki |
| | `#announcements` | Official dev updates, launch teasers |
| | `#faq` | Common questions about factions, races, Hades Asylum |
| **Faction Hub** | `#pirate‑lounge` | General pirate chat, crew recruitment |
| | `#marine‑headquarters` | Marine strategy, rank discussion |
| | `#revolution‑cell` | Covert planning, speculation |
| | `#government‑council` | Policy debate, lore |
| **Race Corner** | `#skypiean‑sky` | Wing‑customisation, aerial role‑play |
| | `#fishmen‑deep` | Underwater mechanics, art |
| | `#mink‑den` | Sulong events, electro‑shock talk |
| | `#race‑4‑rumors` | Speculation on the two unknown races |
| **Gameplay Systems** | `#crews‑directory` | Player‑crew listings, bounties |
| | `#missions‑board` | Community‑run mission ideas, speculation |
| | `#hades‑asylum‑theories` | Prison floor theories, escape plans |
| **Community** | `#general‑chat` | Off‑topic talk |
| | `#media‑share` | Fan‑art, screenshots, videos |
| | `#feedback‑hub` | Suggestions for devs (tag @dev‑feedback) |
| **Live Events** | `#event‑lobby` | Voice/text for scheduled events |
| | `#event‑logs` | Summaries, winners, screenshots |

### 3. 5‑Question Onboarding Quiz (Bot‑run)

| Question | Goal | Example Answer (accepted) |
|----------|------|---------------------------|
| 1️⃣ “Which faction values **freedom** above all?” | Funnel to Pirate role | “Pirates” |
| 2️⃣ “What is the **highest Marine rank** listed on the wiki?” | Verify knowledge of rank ladder | “Fleet Admiral” |
| 3️⃣ “Name one confirmed playable race.” | Confirm race awareness | “Mink” (or Skypiean, Fishmen) |
| 4️⃣ “How many floors does **Hades Asylum** have?” | Test prison knowledge | “Six” |
| 5️⃣ “Do **taxes** apply to Marine earnings?” | Confirm economic mechanic | “Yes” |

*Correct answers grant the corresponding faction role; incorrect answers keep the user in `@New Recruit` with a prompt to review the wiki.*

### 4. Faction Launch Events (pre‑release)

| Event | Timing | Description | Expected Outcome |
|-------|--------|-------------|------------------|
| **Pirate “Black Flag” Rally** | Week 1 (Saturday, 18:00 UTC) | Voice‑chat “ship‑meeting” where participants design a crew banner, discuss NPC crew alliances, and vote on a *Bounty Target* for the week. | Boost pirate community cohesion; generate user‑created crew content. |
| **Marine “Recruit Academy” Drill** | Week 2 (Sunday, 20:00 UTC) | Bot‑run quiz on Marine ranks + a mock “mission briefing” role‑play. Top scorers receive a **“Cadet I”** Discord badge. | Familiarise members with Marine hierarchy; encourage rank‑theory discussion. |
| **Revolution “Underground Bazaar”** | Week 3 (Friday, 19:00 UTC) | Text‑only market channel where members post *speculative* black‑market items (e.g., “smuggled ship parts”). Moderated for lore‑fit. | Seed speculation on Arms of Revolution economy; increase engagement. |
| **Government “Council Session”** | Week 4 (Saturday, 21:00 UTC) | Panel discussion (voice + text) with community moderators acting as *Government officials*, debating “tax fairness” and “corruption”. | Highlight the Government’s political angle; attract role‑players. |

*All events will be announced 48 h in advance via `#announcements` and pinned in the relevant faction channel.*

### 5. Weekly Rituals (ongoing community rhythm)

| Day | Ritual | Channel | Mechanics |
|-----|--------|---------|-----------|
| **Monday** | **“Bounty Board Update”** | `#crews‑directory` | Bot posts top 5 pirate crews by bounty; members can comment strategies. |
| **Wednesday** | **“Marine Tax Tuesday (post‑mortem)** | `#marine‑headquarters` | Summary of tax‑impact discussion; optional poll on tax rate speculation. |
| **Friday** | **“Sulong Night”** | `#mink‑den` | Night‑cycle reminder (every 2 IRL h) + community art‑share of Sulong transformations. |
| **Saturday** | **“Sky‑Watch”** | `#skypiean‑sky` | Members share wing‑customisation screenshots; occasional “best flight path” contest. |
| **Sunday** | **“Speculation Sunday”** | `#race‑4‑rumors` | Open thread for theories on the two unknown races; moderators tag “SPECULATION”. |

---

## E. Source List

| # | Source | URL (as of Aug 2026) |
|---|--------|----------------------|
| 1 | **Pirate Faction Page** – RELL Seas Wiki | `https://rellseaswiki.com/factions/pirates` |
| 2 | **World Seas Marine Corps Page** – RELL Seas Wiki | `https://rellseaswiki.com/factions/marines` |
| 3 | **Arms of Revolution Page** – RELL Seas Wiki | `https://rellseaswiki.com/factions/revolution` |
| 4 | **World Seas Government Page** – RELL Seas Wiki | `https://rellseaswiki.com/factions/government` |
| 5 | **Races Overview** – RELL Seas Wiki | `https://rellseaswiki.com/races` |
| 6 | **Hades Asylum / Marine Bases / Missions / Reputation** – RELL Seas Wiki systems & locations | `https://rellseaswiki.com/locations/hades-asylum/` , `/locations/marine-bases/` , `/systems/missions/` , `/systems/reputation/` |
| 7 | **Mink race stub + Skypiean race** – RELL Seas Wiki / Fandom stubs (customization, Sulong, wings) | `https://rellseas.fandom.com/wiki/Mink` , `https://rellseaswiki.com/` (races) |
| 8 | **Crews directory** – community crew listings w/ bounties | `https://crews.rellseaswiki.com/` |

## Researcher notes (verification)
- Marine 21-rank ladder + Admiral Hades elevator perk + Pirates 40+ NPC crews + 4-faction roster + 5-races-at-launch: verified against live rellseaswiki.com faction pages fetched 2026-09-18 (see `research.md` §5 + fetches above).
- Fandom race pages are stubs under revamp; exact abilities/numbers pre-launch = treat as SPECULATION until showcase confirms.
- Arms of Revolution / World Seas Government join methods + rank ladders: UNREVEALED as of Aug 2026 wiki snapshots.
- Pending: dedicated Gemini-grounded verification pass (Google free quota exhausted mid-run; see header).

---
## Appendix V — Grounded verification (2026-10-05, youcom MCP, quality pilot #2)

Method: `you-search x4 + you-contents` (`rellseaswiki.com/factions/`, `/races`, `/world/`, Fandom Factions/Races/Mink/Marines) in place of queued Gemini pass. No invented numbers.

### V1. Factions — 4 CONFIRMED + 1 NPC context
`rellseaswiki.com/factions/` FAQ: `There are four player factions - Pirates, World Seas Marine Corps, Arms of Revolution and World Seas Government - plus NPC factions`.
- Pirates: freedom/fortune, own codes. Marines: order/justice, strict hierarchy, suppress piracy. Revolution: covert, dismantle order, liberate regions. Government: authority, oversees Marines.
- `Council of Piracy` = separate OTHER-FACTIONS (1x NPC) page: pirate-side context for crews/affiliation — not a 5th playable.
- Rank-up: `Each faction has its own rank system tied to reputation. See each faction page for full rank list.` Faction chosen at start; switching `not fully confirmed before launch`.
- Join (partial): Marines via Marine Base main building + Recruiter NPC (`Fandom Marines` — `??? Taxes`). Revolution/Government join still UNREVEALED. PGG adds: Marines capture → Hades Asylum + `exclusive elevator + admiral-level content`; Beginner guide: faction affects reputation/quests/NPC reactions, Bounty on attacking civilians/opposing players.
- Correction to §A table: PGG lists playable as Pirates/Marines/Bounty Hunters in some 2026 guides vs wiki canonical 4x above — use wiki 4x as source of truth; Bounty Hunter = playstyle/crew-directory filter, not 5th faction. `40+ NPC pirate crews` in §A should read `40 NPC factions` (PGG: dynamic island events, own laws/principles) + player crews via directory.

### V2. Races — 5 DOCUMENTED (resolves §B unconfirmed slots)
`rellseaswiki.com/races` FAQ: `5 race entries currently documented: Cyborg, Fishman, Human, Mink, Skypiean. Number generated from canonical data files.`
- So §B `[Unconfirmed Race #1/#2]` (Celestial Dragon / Golem speculation) is SUPERSEDED — slots are Human + Cyborg CONFIRMED as documented.
- Traits: Fishman = underwater + `Fishman Karate (unconfirmed name) exclusive`; Mink = `Electro exclusive`, Sulong by moonlight, night cycle 2 IRL hrs (Fandom Mink + PGG); Skypiean = aerial (extended air dashes / limited flight per PGG, wings per wiki home); Human/Cyborg = `Universal styles` (Human balanced per PGG/Roonby). Spawn `[-]` = unpublished; rarest/best = explicitly unranked until comparable data published. Selection/reroll process `not fully documented`.
- Reddit 2025-05-27 list (Skypian/Fishman/Mink/Cyborg/Human) matches wiki 5x — community passives (fly/gl ide, taxon damage) remain SPECULATION per thread mods.

### V3. Hades / taxes / bounty — CONFIRMED existence, numbers MISSING
- Hades Asylum 6 floors WIP: X @RellSeasSneaks 2023-09-14 `OPEN WORLD Impel Down Prison system that includes all 6 floors w.i.p`. Marines imprison pirates; low-bounty jail vs high-bounty Impel Down escalation per Reddit detective threads — treat escalation as SPECULATION.
- 21-rank ladder + Admiral elevator: Fandom Marines table only shows Admiral/Fleet Admiral TBD; full 21-step chain from §A (Recruit I → Fleet Admiral) not re-verified on live fetch 2026-10-05 — keep CONFIRMED-as-Aug2026-wiki-snapshot, flag for re-fetch of `/factions/world-seas-marine-corps/` detail page. Taxes mentioned as `??? Taxes` + Reddit `Marines pay no tax (vs pirates)` crew pitch vs `Marines pay everything more expensive taxes` meme — rate/mechanic UNCONFIRMED.

Sources re-fetched 2026-10-05: `https://rellseaswiki.com/factions/`, `/races`, `/world/`, `https://rellseas.fandom.com/wiki/Factions`, `/Races`, `/Mink`, `/Factions/World_Seas_Marine_Corps`, `https://progameguides.com/roblox/rell-seas-sneak-peaks-ultimate-guide-to-upcoming-features-gameplay/`, `https://crews.rellseaswiki.com/`, `https://x.com/RellSeasSneaks/status/1702275358412742695`.
Status for this file: grounded verification COMPLETE via youcom. Gemini re-check optional.
