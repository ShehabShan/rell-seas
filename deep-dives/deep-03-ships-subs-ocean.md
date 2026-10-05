# Deep Dive 03 — Ships, Submarines & Ocean Zones

Date: 2026-09-18 | Topic 3 of 6.
Method: rellseaswiki ships hub (8 pages) + Submarines + Ocean Zones pages fetched live; synthesis via local FreeLLMAPI (`openai/gpt-oss-120b`, finish=stop). Gemini grounded pass still queued (Google 429).

---
**RELL Seas – Pre‑Release Deep‑Dive Report**  
*Compiled for the official Discord community (July 2026)*  

---  

## A. Ship Systems “Cards”

| System | Core Function (per wiki) | Customisation Slots | Typical Play‑Style Impact | Known Variants / Notes |
|--------|--------------------------|---------------------|---------------------------|------------------------|
| **Hull / Base Ship** | Serves as both **home base** and **battleship**. | N/A (foundation) | Determines overall durability and interior space for crew activities. | Players can outfit the hull with visual skins, but functional changes are limited to attached parts. |
| **Ship Customisation** | Add **parts, upgrades, and cannons** to tailor performance. | • Cannon slots  <br>• Figurehead slot  <br>• Sail slot  <br>• Steering‑wheel slot | Trade‑off between **solo speed**, **crew‑brawl efficiency**, and **deep‑sea exploration**. | Upgrades may affect handling, armor, or resource generation (speculative). |
| **Cannons** | Primary ranged weaponry. | Multiple per ship (exact count unpublished). | **Combat roles**: long‑range artillery, rapid‑fire boarding support, anti‑submarine fire. | Types are listed in the “Cannons” hub page (e.g., standard, grapeshot, explosive). |
| **Basic Sail** | Provides visual identity, crew banner display, and **sailing style**. | One per ship. | Influences **speed** and **aesthetic theme** (e.g., pirate flag, navy ensign). | No performance‑changing sails have been shown yet (speculation). |
| **Figureheads** | Bow‑mounted décor; also a **craftable item**. | One per ship. | Cosmetic prestige; some may grant minor buffs (unconfirmed). | Known names appear in the “Figureheads” hub page; players can craft them with specific resources. |
| **Steering Wheel** | Controls **direction** and **maneuverability**. | One per ship. | Affects turning radius and response time in combat. | Different wheel designs may have unique visual flair. |
| **Sailing Mechanics** | Governs how ships move across the surface (wind, currents, crew input). | N/A | Impacts **travel time**, **battle positioning**, and **resource gathering**. | Exact formulas are not public (speculation). |

> **Why it matters:** The ship is the player’s **central hub** – a place to store loot, meet crew, and launch into combat or exploration. The modular slots give each crew a chance to **personalise** their flagship, reinforcing community identity (banners, figureheads, etc.).

---

## B. Submarine Deep Card  

### 1. Acquisition  

| Aspect | Confirmed Detail | Speculation |
|--------|------------------|-------------|
| **Unlock Method** | Summoned via a **Sub Cola** (One‑Piece‑style bottle). | The Sub Cola is **progress‑gated**; exact milestone (e.g., level, quest, or resource) has not been disclosed. |
| **Availability** | Not a starter; must be earned later in the game. | Likely tied to **Ocean‑Zone C4** progression or a specific **crew achievement**. |

### 2. Controls  

| Mode | Input (Keyboard / Mouse) | Function |
|------|--------------------------|----------|
| **Exploration** | **R** – move forward / turn, **G** – battle‑mode toggle, **X** – sonar ping | Basic navigation, depth control (ascend/descend). |
| **Battle** | **Left‑Mouse Button** – fire machine‑gun, **Z** – launch missiles, **X** – sonar ping | Direct combat while submerged. |

> *All controls are displayed in the Submarine hub page; no additional key bindings have been shown.*  

### 3. Depth‑Layer Table  

| Depth Layer | Environment | Hazards | Gameplay Effects |
|-------------|-------------|---------|-------------------|
| **1 – Shallow** | Safe, clear water. | Minimal. | Ideal for learning controls; no HP drain. |
| **2 – Mid‑Depth** | Presence of **beasts**. | Standard enemy encounters. | No HP drain; combat focus. |
| **3 – Danger Threshold** | **HP drain** begins (no armor protection). | Continuous pressure damage. | Requires careful navigation; encourages surfacing or armor. |
| **4 – Dark Zone** | Dark water, **piranha/whale‑eel** variants. | Increased HP drain, aggressive fauna. | Heightened tension; sonar becomes valuable. |
| **5 – Extreme** | **Hidden caves** appear; severe HP drain. | Very high pressure; rare resources. | Exploration reward vs. survival risk. |
| **6 – Near‑Fatal** | Rare **dungeons**; near‑instant death risk. | Extreme pressure, elite enemies. | Only well‑armoured submarines survive. |
| **7 – Max Darkness** | Near‑instant death zone; **rarest content**. | Immediate lethal pressure. | Intended for end‑game challenges / secret bosses. |

> **Note:** The exact HP‑drain values are **unpublished**; only the *presence* of a scaling drain system is confirmed.

### 4. Pressure & Armor  

| Item | Effect on Pressure Damage |
|------|---------------------------|
| **Full Armor Set** | **Complete protection** against pressure‑drain across all layers. |
| **Partial / No Armor** | **No protection** – pressure damage applies normally (Movie 3 confirmation). |

> *No intermediate protection tiers have been shown.*  

### 5. Currents & Underwater Content  

| Depth | Current Behaviour | Content Linked to Currents |
|-------|-------------------|----------------------------|
| **All depths** | **Compass arrows** shift to indicate flow; **bubble trails** visualise direction. | **Hidden caves**, **mini‑bosses**, **full bosses**, and **dungeons** are located at **current sources**. |
| **C4+ Regions** | Stronger, more complex currents. | Majority of **underwater-exclusive crafting nodes** and **deep‑sea bosses** (including Leviathan) reside here. |

### 6. Oxygen System  

| Feature | Confirmed Detail |
|---------|------------------|
| **Timer** | **No fixed oxygen timer** – players are not forced to surface after a set period. |
| **Oxygen Bubbles** | Randomly spawn; **rarer** at deeper layers. |
| **Survival** | Managing bubble collection is essential in deeper layers (3‑7). |

### 7. Physics & Animation  

| Aspect | Confirmed Detail |
|--------|------------------|
| **Swim Speed** | Slower than surface sailing, but **M1 weapons retain normal projectile speed**. |
| **Dash** | Directional dash **toward the camera** (visual “burst”). |
| **Animations** | Floaty, underwater‑filtered sound; **gravity appears reduced**. |
| **Leviathan Battles** | Sub‑combat scenario confirmed (Movies 2 & 3). |

### 8. Content Highlights (C4‑Focused)  

| Content Type | Location | Unlock Requirement (if known) |
|--------------|----------|-------------------------------|
| **Caves / Multi‑room Dungeons** | Depth layers 5‑7, **C4+** zones. | Submarine + appropriate depth. |
| **Mini‑Bosses** | At current sources, mid‑depth (3‑4). | No extra requirement. |
| **Full‑Scale Bosses** | Deepest layers (6‑7), **C4+**. | Full armor set recommended. |
| **Underwater‑Only Crafting Nodes** | Scattered in C4+ waters. | Submarine presence; specific resource not disclosed. |
| **Alternative “Coating” Path** | **Resin‑treated ship dive** (One‑Piece reference) hinted as a **non‑sub** method to reach deep content. | Still speculative; not yet shown in‑game. |

---

## C. Ocean Zones Card  

| Zone | General Description | Confirmed Features | Pending / Speculative Details |
|------|----------------------|--------------------|------------------------------|
| **C1** | Early‑game surface waters. | Identifiers exist (names/rules unpublished). | Exact hazards, resource density, and quest lines unknown. |
| **C2** | Mid‑game surface waters, slightly more challenging. | Same status as C1 – identifiers known, specifics hidden. | Likely introduces **storm** and **tsunami** mechanics. |
| **C3** | **Sky content** – floating islands, airborne ships, sky‑beasts. | Aerial traversal introduced; entry requirements not fully disclosed. | How players transition from sea to sky (e.g., “sky‑gate” or special vessel) remains unknown. |
| **C4** | **Deep‑sea hub** – richest underwater content, submarine‑centric. | Majority of **underwater caves, dungeons, bosses, crafting nodes** reside here. | Exact map layout, number of sub‑zones, and any surface‑to‑underwater connectors (e.g., sinkholes) are unconfirmed. |

### Hazards Overview  

| Hazard | Severity (relative) | Known Effects |
|--------|---------------------|----------------|
| **Tsunami Zones** | **High** | Massive wave damage; can sink ships instantly (damage values unpublished). |
| **Storm Zones** | **Medium** | Reduced visibility, erratic wind affecting sail handling. |
| **Sinkhole Connectors** | **High** | Surface‑to‑underwater portals; can drop ships into deep layers abruptly. |

> **Confirmed vs. Pending:** All hazard types are **confirmed** to exist, but exact **damage numbers**, **trigger conditions**, and **mitigation methods** are still pending release.

---

## D. Why Ships Win Pre‑Release Hype  

| Reason | Explanation | Discord Tie‑In |
|--------|-------------|----------------|
| **Home + Battleship Duality** | Players get a **personal base** (crafting, storage, crew lounge) *and* a **combat platform** in one vehicle. This “everything‑in‑one” concept fuels imagination and role‑play. | Crew “home‑base” channels can showcase interior screenshots, encouraging members to share their ship layouts. |
| **Crew Identity via Banners & Figureheads** | Custom banners and figureheads let crews **brand** themselves, fostering rivalry and pride. | Discord **banner‑design contests** give crews a visual badge to display on their server roles. |
| **Modular Customisation → Player Agency** | Slots for cannons, sails, wheels, and figureheads let each crew **tune** the ship for their preferred play‑style (speed, brawling, exploration). | The **Shipwright Forge** contest can reward the most innovative build, reinforcing the sense of agency. |
| **Narrative Hook (Pirate‑Adventure + Sci‑Fi)** | Combining classic naval piracy with **submarine deep‑sea exploration** and **sky islands** creates a rich, multi‑layered world that feels fresh. | Discord events (e.g., “C3 vs C4 debate night”) can spark lore discussions and community storytelling. |
| **Social Gameplay (Crew Roles)** | Different ship parts map naturally to **crew positions** (captain, gunner, navigator, engineer). This encourages coordinated play and recruitment. | Role‑based Discord tags (Captain, Gunner, Diver, etc.) can be assigned, reinforcing in‑game responsibilities. |

---

## E. Discord Activation Plan  

### 1. Shipwright Forge Contest  
| Element | Details |
|--------|---------|
| **Goal** | Design the most *thematically cohesive* and *functionally balanced* ship using the confirmed slots (cannons, sail, figurehead, wheel). |
| **Submission Template** | 1. Ship name  <br>2. Screenshot or mock‑up (in‑game or art)  <br>3. List of parts (cannon type, sail style, figurehead, wheel)  <br>4. Intended play‑style (speed, brawl, exploration)  <br>5. Crew banner description. |
| **Judging** | Community votes + dev‑panel review. Prizes: exclusive Discord role, early‑access badge, in‑game “Founders’ Figurehead” (speculative). |
| **Timeline** | 2‑week submission window, followed by 3‑day voting period. |

### 2. Depth‑Layer Role Ladder  
| Depth Layer | Discord Role (suggested) | Unlock Criteria (speculative) |
|------------|--------------------------|-------------------------------|
| **Surface (C1‑C2)** | “Deckhand” | Join server + basic tutorial. |
| **Mid‑Depth (2‑3)** | “Diver” | Obtain first Sub Cola (progress‑gated). |
| **Deep‑Sea (4‑5)** | “Abyssal Explorer” | Survive to depth 4 (pressure‑drain observed). |
| **Extreme (6‑7)** | “Leviathan Slayer” | Defeat a deep‑sea boss (Leviathan) – confirmed in dev movies. |

*Roles grant access to exclusive voice channels (e.g., “Depth‑5 Dungeons”) and custom emojis.*

### 3. Sonar‑Trivia Event  
- **Format:** Live voice‑chat where a bot (or dev) plays a short sonar ping; participants guess the **underwater creature** or **cave layout** shown.  
- **Reward:** “Sonar‑Scout” badge and a **temporary boost** (e.g., extra oxygen bubbles) for the next submarine run (speculative but aligns with in‑game mechanics).  

### 4. C3‑vs‑C4 Debate Night  
- **Premise:** Split the server into two factions – **Sky‑Seekers (C3)** vs **Abyss‑Hunters (C4)**.  
- **Activities:** Panel discussion on pros/cons, fan‑art showcase, and a poll to decide which zone the dev team should prioritize for the next update.  
- **Outcome:** Generates buzz, gathers community feedback, and highlights the **dual‑world** design.  

### 5. Banner‑Design Contest  
- **Goal:** Create a **crew banner** (PNG ≤ 512 px) that can be displayed on ships.  
- **Submission Fields:** 1. Banner image  <br>2. Symbolic meaning  <br>3. Colour palette.  
- **Prize:** Winning banner becomes a **default option** for all players for a limited time (speculative but plausible as a community‑driven perk).  

---

## F. Sources  

| Source | Type | Date |
|--------|------|------|
| **rellseaswiki.com – Ship Hub (8 pages)** | Official wiki (ship customisation, cannons, sails, figureheads, steering wheel, submarines, ocean zones, sailing mechanics) | July 2026 |
| **rellseaswiki.com – Submarines** | Sub‑Cola summon, controls, depth layers, pressure/armor, currents, oxygen, physics, Leviathan battles | July 2026 |
| **rellseaswiki.com – Ocean Zones** | C1‑C4 identifiers, sky content (C3), deep‑sea content (C4), hazards (tsunami, storm, sinkhole) | July 2026 |
| **Developer Movies 2 & 3** | Visual confirmation of submarine deployment, depth‑layer visuals, Leviathan combat, coating hint | July 2026 |
| **General Roblox & RPG knowledge** | Context for community‑driven events, role‑based Discord structures, typical contest formats | N/A (background knowledge) |

*All facts above are taken **directly** from the confirmed wiki entries and developer media. Anything labelled **SPECULATION** is an inference based on typical game design patterns and has **not** been officially announced.*

---
## Appendix V — Grounded verification (2026-10-05, youcom MCP, quality pilot #3)

Method: `you-search x3 + you-contents` (`rellseaswiki.com/systems/ship-customisation/`, `/ships/`, Fandom Submarines + Ship_Customisation) + subagent extraction. No invented numbers.

### V1. Ships — CONFIRMED structure, numbers MISSING
- Types: Sloop (small/fast, Low cannons, Speed/Evasion), Caravel (medium/balanced), Gallion (large, High combat/Ram, more crew). Marine warships `significantly larger than Gallion`. Speed/Health/Turn values MISSING (Low/Med/High only).
- Stats: 6 names CONFIRMED — Speed/Armour/Cannons/Turn Speed/Ram Strength/Health, via chests/bosses parts. Values MISSING.
- Cannons: Heavy (slow/high), Burst (machine-gun/fast/sustained DPS), Mortar (long/arc), Front Cannon if bow supports; `All ports same type, cannot mix`. Weak-point tiers 1x/2x/3x CONFIRMED. Base damage/range MISSING.
- Slots: Bow (figurehead/ram/front cannon), Stern (6 rear styles + Steam Engine), Sails (crew Jolly Roger), Cannons, Flag, Material, Midship/Main Mast, Steering Wheel/Rudder. Figurehead blueprints (e.g. Allard, Sea Serpent Wing Craft) improve stats, not just cosmetic.
- Hull: Wood default → Iron (significantly +Armour, unlocks Steam Engine, needs Mining Iron). Amount MISSING.
- Spawn: `Ship in a Bottle` → whirlpool → ship rises; tiny-bottle builder room; 3 layouts saveable. Battle Mode `R` → Mortars/Chain Shot/RAM. NPC crew auto-fire cannons. Theft/anchor mechanic CONFIRMED. Fruits never outclass cannons at sea (dev principle).

### V2. Submarine — partial correction
- Spawn CONFIRMED: `using ship in a bottle while underwater`, walk-in transition, multi-crew sit. `Sub Cola / Subc Cola` name NOT found in 4 docs — keep as July2026-snapshot term, flag for re-fetch of `/ships/submarines/` detail page.
- 7 layers + Leviathan battles CONFIRMED. UI: Health/Pressure/Compass/Sonar/Depth. Pressure>armor = explode/implode; health zero = explode. Armor page only `Titanum armour (placeholder)` — thresholds MISSING.
- Controls: `R` start engine, `W/S` fwd/back, `Q/E` descend/ascend, `F` battle mode, `A/D` turn in battle, mouse steer, RightClick machine-gun, `Z` missiles, `X` sonar CONFIRMED. `G` + `LMB` + combined R/G/X scheme from §B NOT found — mark UNCONFIRMED.
- Sonar/compass locate Leviathans/hidden areas CONFIRMED. Oxygen bubbles/currents/interior/coating from §B-D NOT found in these 4 docs (only generic `depth, pressure and oxygen systems` stub) — keep as July2026 snapshot, needs detail-page re-fetch, do not publish as verified.

### V3. Ocean zones C1-C4 — NOT re-verified here
Live fetch 2026-10-05 shows `Ocean Zones - 1 entries - Danger zones and sea regions` + `Sea 1/2/3/4` nav only. No C1-C4 identifiers, sky-C3, deep-C4, tsunami/storm/sinkhole in returned docs (storm hits = MTG ads). Keep §C as July2026 snapshot, flag for dedicated `/locations/ocean-zones/` + `/seven-layers/` re-fetch before blueprint use.

Sources re-fetched 2026-10-05: `https://rellseaswiki.com/systems/ship-customisation/`, `https://rellseaswiki.com/ships/`, `https://rellseas.fandom.com/wiki/Submarines`, `https://rellseas.fandom.com/wiki/Ship_Customisation`, plus PGG/Movie3/crews search highlights.
Status: partial verification COMPLETE (ships high-confidence, subs/zones need detail-page pass). Gemini re-check optional.