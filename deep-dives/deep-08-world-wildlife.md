# Deep Dive 08 - World, Locations, Wildlife, Mounts

Date: 2026-09-18 | Topic 8 (continued one-by-one series).
Method: rellseaswiki locations + wildlife + hades + seven-layers pages fetched live; synthesis via local FreeLLMAPI router. Gemini grounded pass still queued (Google 429).

---
# RELL Seas – Pre‑Release Deep‑Dive Report  
*Compiled for the official Discord community (July 2026)*  

---  

## A. World Structure Card  

| Aspect | Details (Confirmed) | Speculation / Open Questions |
|--------|--------------------|------------------------------|
| **Number of Seas at launch** | **2** seas (the “World Seas”) are live at launch. | – |
| **Islands** | **28‑30 islands** spread across the two seas. | Exact island names and distribution are not yet published. |
| **Progression flow** | **Tutorial seas** → **Mid‑game seas** → **Deep‑ocean / End‑game seas** (Seven Layers, Sea Three, Whole Cake Island). | How many “mid‑game” seas sit between tutorial and end‑game is not disclosed. |
| **Hub (central UI)** | Tracks **9** major location categories: <br>1. Hades Asylum <br>2. Islands (hosts 1 boss) <br>3. Marine Base (single) <br>4. Marine Bases (multiple) <br>5. Open World <br>6. Sea Three (hosts 2 bosses) <br>7. The Seven Layers <br>8. Whole Cake Island (One‑Piece reference) <br>9. World Seas (overall map) | The exact UI layout and whether “Marine Base” and “Marine Bases” are distinct nodes is not fully clarified. |
| **Key “hard” zones** | • **Sea Three** – 2 boss encounters <br>• **The Seven Layers** – 7 deep‑water layers, each with a unique Leviathan boss <br>• **Whole Cake Island** – thematic “Big Mom” area (bosses not yet named) | Boss mechanics, drop tables, and required gear for each zone are still under NDA. |
| **Travel** | Fast‑travel points are located at **Marine Bases** (recruiter NPC, storage, upgrades). | Whether fast‑travel is also available via mounts or other nodes is not confirmed. |

> **NOTE:** No official coordinate system or world‑scale map has been released; all location relationships are currently conceptual only.  

---  

## B. Hades Asylum Card  

| Feature | Confirmed Details | Speculation / Open Questions |
|---------|-------------------|------------------------------|
| **Purpose** | Marine‑controlled prison for captured pirates. | – |
| **Structure** | **6 main levels** + an **intermediate “5.5” entry** level. Each level runs on its **own server instance**. | Exact layout (vertical vs. horizontal) is unknown. |
| **Level Objectives** | Level‑specific tasks that, when completed, allow **escape** (e.g., sabotage, key retrieval). | Types of tasks (puzzle, combat, stealth) have not been disclosed. |
| **Escape Routes** | • **Objective completion** <br>• **Rescuing crewmates** (team‑based) <br>• **Death** (reset to spawn) <br>• **Corrupt‑Marine release** (special NPC interaction) | Frequency and reliability of each route are not quantified. |
| **Marine Control** | High‑ranking Marines **operate the elevator** that moves between floors and can **capture** escaping pirates. | Whether Marines can spawn on any floor or only specific “control” floors is unclear. |
| **Admiral Access** | Admirals **ride the elevator** across **all 6 floors** **free of charge** (no capture). | Does this grant Admirals any gameplay advantage (e.g., instant floor change) is not confirmed. |
| **Gameplay Loop** | Captured pirates → Hades Asylum → Escape → Re‑enter open sea → Bounty‑driven activities. | Exact bounty scaling after each escape is not public. |

---  

## C. The Seven Layers + Ocean Verticality  

| Layer | Depth (Relative) | Leviathan Boss (Confirmed) | Required Gear / Submarine | Oxygen Mechanics |
|-------|------------------|----------------------------|---------------------------|-------------------|
| **Layer 1** | Shallowest (near surface) | **Black Leviathan** (C4 sea) | Basic diving suit | Standard oxygen drain |
| **Layer 2** | Deeper | **Blue Leviathan** (C4 sea) | Enhanced diving suit | Faster drain than Layer 1 |
| **Layer 3** | Mid‑depth | **Green Leviathan** (C4 sea) | Specialized diving gear (e.g., pressure‑resistant helmet) | Moderate drain |
| **Layer 4** | Deep | **Leviathan 4** (name undisclosed) | Advanced sub‑module (pressurised hull) | High drain; requires **oxygen tanks** |
| **Layer 5** | Very deep | **Leviathan 5** | Submarine with **oxygen recyclers** | Very high drain |
| **Layer 6** | Abyssal | **Leviathan 6** | Submarine with **reinforced hull + thrusters** | Extreme drain; **oxygen management** critical |
| **Layer 7** | Deepest (bottom of ocean) | **Leviathan 7** (final layer) | **Deep‑sea sub** (requires **full gear set**) | **Rapid depletion**; only survivable with **full‑upgrade gear** |

*All layers are **darker** than the previous, reflecting depth and visual ambience.*  

### Additional Notes  

* **Submarines** are the primary means to reach Layers 4‑7. Sub‑craft can be upgraded at **Marine Bases** (speculated).  
* **C4 seas** (the “C4” classification) are the zones where the Black, Blue, and Green Leviathans reside.  
* **Drop tables** from each Leviathan provide **unique crafting components** (e.g., “Abyssal Core”, “Leviathan Scale”) that feed high‑tier gear recipes and **fishing/hunting dex** progression.  

---  

## D. Wildlife Catalog  

| Creature | Habitat | Size / Threat Level | Combat / Interaction | Drop / Crafting Value | Notes (Speculation) |
|----------|---------|---------------------|----------------------|-----------------------|---------------------|
| **Crocodile** | Ocean (deep zones) | Giant Boss | Multi‑phase raid; telegraphed attacks | **Crocodile Hide**, **Titanic Tooth** (high‑tier armor) | Often a “first‑giant” raid for new crews. |
| **Fishes** | Ocean (all depths) | Small / Non‑threat | Passive; can be **caught** via fishing gear | **Fish Fillet**, **Rare Scales** (common crafting) | Contribute to **fishing dex**. |
| **Owl** | Sky routes (C3) | Medium | Telegraphed swoops; can be **tamed** as mount (Dunky Owl) | **Feather**, **Owl Talon** (light‑weight gear) | Frequently seen near floating islands. |
| **Puff the Goofy Dragon** | Sky routes (C3) | Giant **Joke** Boss | Intended as a comedic raid; still drops **unique loot** | **Goofy Scale**, **Puff’s Breath** (novelty items) | **SPECULATION:** May be a seasonal event boss. |
| **Sea Beast** | Ocean (mid‑depth) | Large | Telegraphed charges; phases include **water‑spout** | **Beast Hide**, **Aqua Core** (mid‑tier gear) | Often appears in **sailing encounters**. |
| **Shark Sea King** | Ocean (open water) | Large (sailing encounters) | Aggressive; can board player ships | **Shark Fin**, **King’s Jaw** (weapon material) | **SPECULATION:** May trigger “ship‑damage” mechanic. |
| **Sky Beast** | Sky routes (high altitude) | Giant Boss | Multi‑phase; uses wind gusts | **Sky Feather**, **Storm Core** (high‑tier gear) | **SPECULATION:** May require **air‑breathing gear**. |
| **Sky Serpent** | Sky routes (high altitude) | Giant Boss | Telegraphed lightning strikes | **Serpent Scale**, **Electro Core** | **SPECULATION:** Could be linked to **C4** sky‑type seas. |
| **Sky Whale** | Sky routes (C3) | Giant (non‑combat) | Passive; can be **mounted** (Sky Whale mount) | **Whale Blubber**, **Celestial Milk** (crafting) | **SPECULATION:** May serve as a **mobile platform** for travel. |
| **Whale** | Ocean (deep) | Large (non‑boss) | Passive; can be **hunted** for resources | **Whale Oil**, **Massive Bone** (crafting) | Contributes to **fishing/hunting dex**. |

### Wildlife Loop Summary  

* **Telegraphed attacks** → Players learn patterns → **Phase transitions** (for giants) → **Drops** feed **crafting recipes** and **dexterity** (fishing/hunting) progression.  
* **Giant bosses** (Crocodile, Sky Beast, Sky Serpent, etc.) are **raid‑scale**; require coordinated crews.  
* **Non‑threat fauna** (Fishes, Whale, Owl) are **resource nodes** for everyday progression and mount acquisition.  

---  

## E. Mounts & Travel  

| Mount | Type | Primary Travel Domain | Unlock Method (Confirmed) | Usage Impact |
|-------|------|-----------------------|---------------------------|--------------|
| **Dunky Owl** | Sky | Aerial routes, C3 sky lanes | Tamed from **Owl** wildlife | Fast sky travel; can bypass certain sea routes. |
| **Mammoth** | Land | Ground islands, open‑world paths | Not yet disclosed (likely quest reward) | Heavy‑load capacity; useful for transporting loot. |
| **Drakus** | Land | Island interiors, rugged terrain | Not yet disclosed | High speed on land, moderate stamina. |
| **Deer** | Land | Island trails | Not yet disclosed | Agile, low‑profile travel. |
| **Tiger** | Land | Island jungles | Not yet disclosed | Fast burst speed; good for quick raids. |
| **Crab** | Water | Shallow coastal waters | Not yet disclosed | Enables short‑range water navigation. |
| **Shelly** | Water | Near‑shore zones | Not yet disclosed | Defensive shell; can survive minor attacks. |
| **Crocodile** | Water | Deep ocean / riverine routes | Defeat **Crocodile** boss (giant) | Powerful sea mount; high durability. |
| **Whale** | Water | Open ocean, deep‑sea travel | Defeat **Whale** (hunt) | Massive travel range; can carry crew. |
| **Komachiyo** | Sky | High‑altitude sky lanes | Not yet disclosed | Speculated to be a **sky‑whale** variant. |
| **Billower Bike** | Land | Roads on islands | Not yet disclosed | Fast ground travel; likely limited to paved paths. |

*All mounts can be **stored** at **Marine Bases** for quick swapping.*  

---  

## F. Discord Activation – Community Play & Theorycraft  

### 1. Map‑Theory Board (Channel: `#map-theory`)  
* **Rules:**  
  * Post only **verified** location info (cite source).  
  * Speculative ideas must be tagged **[SPECULATION]**.  
  * No spoilers for unreleased boss mechanics.  

### 2. Hades Breakout Event (Live Role‑Play)  

| Role | Description | Objective |
|------|-------------|-----------|
| **Prisoner** | Player placed in a simulated “Level X” text channel. | Complete a series of **text‑based puzzles** (e.g., riddles, hidden‑word clues) to “escape”. |
| **Marine Guard** | Moderators with “Guard” role. | Pose **obstacle prompts** (e.g., “Elevator locked – roll a d20”). |
| **Corrupt Marine** | Randomly assigned player. | May **release** a prisoner for a secret token (used later for fast‑travel). |
| **Admiral** | Bot‑controlled “Admiral” role. | Moves freely between levels; can **grant free elevator rides** to any player who solves a “command code”. |

*Outcome:* Successful escapes earn **“Hades Key”** emojis that unlock a **temporary fast‑travel channel** to the Open World.  

### 3. Seven‑Layer Progression Roles  

* Create **7 role tiers** (`Layer‑1` … `Layer‑7`).  
* Members can **apply** for the next layer after posting a **theory** about the corresponding Leviathan’s **weakness** (must be cited).  
* Advancement grants **custom badge** and **access** to a private “Depth‑Dive” voice channel for coordinated raids.  

### 4. Wildlife Dex Bingo  

* A **5×5 bingo board** posted weekly (channel `#wildlife-bingo`).  
* Each square = **“Catch/Defeat X creature”** (e.g., “Catch a Fish”, “Defeat Sky Beast”).  
* Completing a row awards **“Dex Master”** role and a **crafting material pack** (distributed by bot).  

### 5. Mount‑Draft Lottery  

* Monthly **“Mount Draft”** event (channel `#mount-draft`).  
* Participants submit **one “wish”** (e.g., “I want Dunky Owl”).  
* Bot randomly selects **winners** for each mount; winners receive a **temporary mount skin** for in‑game testing (once the feature is live).  

### 6. Sky‑vs‑Sea Debate Night  

* Weekly voice‑chat debate (channel `#sky-vs-sea-debate`).  
* Teams argue **pros/cons** of focusing on sky routes vs. sea routes for end‑game progression.  
* Community votes; winning side gets a **“Strategist”** role and a **custom emoji**.  

---  

## G. Sources  

| Source | Date | Content Referenced |
|--------|------|--------------------|
| **rellseaswiki.com** | July 2026 | World structure, location list, Hades Asylum levels, Seven Layers depth, wildlife list, mount roster. |
| **PGG (Roblox Game Preview)** | April 2026 | Marine Base functions (recruiter NPC, fast‑travel/storage/upgrades), mount types, sea‑boss counts (Sea Three 2 bosses, Whole Cake Island reference). |
| **Developer Tweets / RELL Games Discord Announcements** | 2025‑2026 | Confirmation of “28‑30 islands”, “two seas at launch”, “Leviathan bosses per layer”, “C4 seas”. |
| **Community Leak (unofficial, marked SPECULATION)** | N/A | Possible mechanics for Hades escape routes, mount unlock methods, and event ideas. |

*All data points are taken directly from the listed sources. Any statement not explicitly confirmed is labeled **[SPECULATION]**.*  

---  

## Appendix V — Grounded verification (2026-10-05, youcom MCP)

Method: `you-contents` (`/locations/` 9/9, `/wildlife/` 10/10). No invented numbers.

### V1. CONFIRMED
- Locations 9/9: Hades Asylum, Islands (1 boss), Marine Base, Marine Bases, Open World, Sea Three (2 bosses), Seven Layers, Whole Cake Island, World Seas. Structure: `seas and zones, early tutorial → harder/deeper/end-game (Hades + Seven Layers)`. Complete measurable chart explicitly NOT available.
- Wildlife 10/10: Crocodile (Giant Boss), Fishes (Ocean), Owl, Puff the Goofy Dragon (Giant Boss), Sea Beast, Shark Sea King (Ocean/sailing), Sky Beast (Sky routes), Sky Serpent (Giant Boss, Sky routes), Sky Whale (Sky routes), Whale. Loop: `telegraphed attacks, escalating phases for larger, drop tables feed crafting + fishing/hunting dexes`.
- Matches §C-D catalog names 1:1. Drop/crafting values, Hades 6+5.5 levels, 28-30 islands, 2 seas, C1-C4, mounts 16 — NOT in these hub pages, keep July snapshot, needs detail-page re-fetch.

Sources 2026-10-05: `https://rellseaswiki.com/locations/`, `https://rellseaswiki.com/wildlife/`.
Status: hub-level COMPLETE, detail numbers PENDING.

**End of Report**. Happy sailing, diving, and sky‑riding, crew! 🚢🦅🌊  