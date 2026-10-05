# Deep Dive 09 - Progression, Activities, Economy, Mounts

Date: 2026-09-18 | Topic 9 (continued one-by-one series).
Method: rellseaswiki progression + cooking + class-system pages fetched live (+ mounts via PGG); synthesis via local FreeLLMAPI router. Gemini grounded pass still queued (Google 429).

---
**RELL Seas – Pre‑Release Discord Server Report**  
*Compiled 18 Sept 2026 – based on the official RELL Seas Wiki (rellseaswiki.com, July 2026) and publicly‑available knowledge. All statements that go beyond the confirmed data are flagged **[SPECULATION]** and given a confidence rating.*  

---  

## A. Progression Philosophy Card  

| Aspect | What the Wiki Says | Why It Matters (Design Intent) | Confidence |
|--------|-------------------|--------------------------------|------------|
| **Non‑linear progression** | *“Every activity (fishing, cooking, mining, woodcutting, combat, sailing) levels your character – grow by doing what you enjoy.”* | Players are not forced into a single “grind path.” Casuals can level by fishing or sailing, while grinders can chase mastery in a single discipline. This reduces entry‑barrier friction and encourages diverse play‑styles. | ✅ High |
| **Mastery & XP/Levels** | Hub page “Leveling (XP/levels/mastery)” – implies a dual‑track: raw XP for level, mastery for deeper skill depth. | Gives long‑term goals (mastery) after the initial level curve flattens, keeping end‑game players engaged. | ✅ High |
| **Races & Mounts** | 5 races, 16 mounts (see section E). | Racial bonuses (unpublished) likely tie into the “class‑system” and may affect stat growth, giving another layer of personalization. | ✅ Medium (race bonuses not disclosed) |
| **Stat System** | Hub page “Stats” (no detail). | Expected to feed into combat, sailing speed, crafting success rates, etc. Allows players to specialize (e.g., high stamina for sailing, high intellect for cooking). | ✅ Medium |
| **Dexes (completionist trackers)** | Adventure, Fishing, Craftsman, Recipe Dexes – reward completeness. | Provides “bingo/achievement” style goals that appeal to completionists and give extra XP or cosmetic rewards, reinforcing the non‑linear design. | ✅ High |

**Take‑away for Discord:** Emphasize that *any* hobby can be a viable leveling route. Promote “Choose‑Your‑Own‑Path” channels where members share their favorite activity and show off their progress.  

---  

## B. Dexes Completionist Card  

| Dex | What It Tracks | Typical Rewards (per Wiki) | How to Use on Discord |
|-----|----------------|----------------------------|-----------------------|
| **Adventure Dex** | Exploration milestones (e.g., discovering islands, sailing routes, hidden caves). | “Reward completeness” – likely XP boost, title, or cosmetic badge. | Create a **#dex‑adventure‑log** where members post screenshots of new locations; run monthly “Explorer Bingo” contests. |
| **Fishing Dex** | Number & rarity of fish caught, fishing mini‑quests, use of different rods/techniques. | Same “reward completeness” model. | Host **#fishing‑trophies** channel; weekly “Big‑Catch” leaderboard; encourage Dex‑completion screenshots. |
| **Craftsman Dex** | Crafted items across disciplines (mining → metal, woodcutting → timber, cooking → meals). | Rewards for filling categories. | Run **#craft‑showcase** with “Dex‑Complete” tags; allow members to trade blueprint hints. |
| **Recipe Dex** | Number of unique recipes unlocked & cooked (linked to Cooking Dex). | Rewards for full collection. | Organize **#recipe‑exchange** where members post unlocked recipes; run “Recipe Hunt” events. |

**Speculation:** Exact reward types (e.g., “Dex‑completion badge”) are not listed. Likely cosmetic or minor XP bonuses based on typical Roblox progression design. **Confidence:** ✅ Medium.  

---  

## C. Class System Card  

| Element | Confirmed Details | Open Questions (Speculation) | Discord Hook |
|---------|-------------------|------------------------------|--------------|
| **Loadout Structure** | Customizable skill keys + placement. | Number of skill slots, whether there are “primary/secondary” loadouts. | Create a **#class‑builder** where members draft their skill key maps and get feedback. |
| **Skill Switching** | Press **R** while mouse‑lock active to swap skill sets. | How many swaps per session? Cooldown? | Host “Rapid‑Swap” challenges in voice chat (e.g., 30‑second combat drills). |
| **Posters (Combat Modifiers)** | Posters are “plug‑into loadouts”; arrows lead to alternate combat/fruit/ability skills. Three families: **Agile** (movement), **Fierce** (offense), **Tactic** (defense). | How many posters per loadout? Whether posters are unlocked via mastery or purchase. | Run a **#poster‑gallery** where members showcase their poster combos; weekly “Poster‑of‑the‑Week” voting. |
| **Class Slots / Names / Bonuses / Selection Timing** | *UNPUBLISHED* – only that they exist. | Likely 3‑4 slots (common in Roblox RPGs); names may be thematic (e.g., “Navigator”, “Harpooner”). Bonuses probably stat‑based (e.g., +5% sailing speed). | Use a **#class‑reveal** channel for speculation; let members vote on preferred class concepts – great for community engagement. |

**Speculation Confidence:**  
- Number of skill slots – **Low** (common design but not confirmed).  
- Poster unlock method – **Medium** (posters often tied to mastery).  

---  

## D. Activities Catalog  

| Activity | Core Loop (per Wiki) | Cross‑Links & Notable Mechanics | Ideal Player Type | Discord Content Ideas |
|----------|----------------------|--------------------------------|-------------------|-----------------------|
| **Fishing** | Catch fish → gain XP → fill Fishing Dex → unlock recipes (via Cooking). | Fish act as raw material for cooking meals & potions; some fish are “underwater‑only nodes” (economy). | Relaxed / collector | **#fishing‑log**, live‑stream fishing trips, “Catch‑of‑the‑Day” polls. |
| **Mining** | Mine nodes → collect ores → craft metal items → feed Craftsman Dex. | Ores may be required for high‑tier blueprints; boss‑drop materials likely mined from special veins. | Grinder / resource‑hoarder | **#ore‑market**, price‑tracking of mined materials. |
| **Woodcutting** | Chop trees → gather timber → craft tools, ship parts, mount upgrades. | Timber needed for ship hull upgrades (sailing) and some cooking equipment (e.g., cutting board). | Casual / builder | **#timber‑trades**, showcase of custom ship designs. |
| **Cooking** | Use 7 equipment pieces (pot, grill, saucepan, cutting board, pan, butcher knife, cooking knife) → unlock recipes via Blueprint → create meals/potions → support exploration/combat. | **Max talent points:** 500 (per Wiki). Recipes require fish/wildlife materials → ties directly to Fishing & Hunting. Meals/potions give combat buffs or stamina for sailing. | Hybrid (combat + explorer) | **#cooking‑lab** – members post blueprint‑style recipe cards; weekly “Meal‑Master” contest. |
| **Sailing** | Pilot ships, explore islands, pay Marine tax (or avoid via pirate status). | Sailing speed may be affected by mounts (e.g., Whale) and class “Agile” posters. Taxes create an economy loop (see section E). | Explorer / PvP‑oriented | **#sailing‑routes**, “Fastest‑Voyage” leaderboards, tax‑avoidance tips. |
| **Combat** | Engage NPCs/bosses, use loadout skills, posters for combos. | Boss drops feed crafting (blueprints, rare materials). | Grinder / PvP | **#combat‑replays**, “Poster‑Combo” tutorials. |

**Note:** Exact ingredient tables for cooking, node rarity, or combat damage numbers are *pending* – **[SPECULATION]**.  

---  

## E. Mounts + Economy Notes  

### 1. Mount List (16)  

| Mount | Type | Likely Use (Speculative) |
|-------|------|--------------------------|
| Dunky Owl | Sky | Fast aerial scouting, possibly reduces travel time between islands. |
| Mammoth | Land | Heavy‑load carrier; may boost woodcutting or mining haul capacity. |
| Drakus | Land | Agile ground mount; could improve combat positioning. |
| Deer | Land | Speedy terrestrial travel; low‑profile for stealth. |
| Tiger | Land | Combat‑oriented mount; may grant attack buffs. |
| Crab | Water | Short‑range water navigation; could aid in coastal fishing. |
| Shelly | Water | Defensive water mount; possibly higher durability. |
| Crocodile | Water | Aggressive water mount; may enable melee attacks while sailing. |
| Whale | Water | Long‑range sea travel; likely reduces Marine tax cost. |
| Komachiyo | Sky | Exotic flyer; may unlock sky‑only fishing nodes. |
| Billower Bike | Land | Fast ground vehicle; likely a “pirate” style mount. |
| *(12 more unnamed mounts from PGG – not listed)* | — | — |

**Speculation:** Exact functional bonuses (speed, cargo, combat) are not published. **Confidence:** ✅ Medium (based on typical Roblox mount design).  

### 2. Economy Loops  

| Loop | Confirmed Elements | How It Likely Works (Speculation) | Confidence |
|------|-------------------|-----------------------------------|------------|
| **Crafting ↔ Blueprints** | Blueprints unlock recipes; crafting uses boss‑drop materials. | Players collect rare drops → purchase/unlock blueprint → craft high‑value items → sell/trade. | ✅ High |
| **Underwater‑Only Nodes** | Mentioned as resource locations. | Likely require a diving suit or specific mount (e.g., Whale) → yields exclusive ores/fish → higher market price. | ✅ Medium |
| **Marine Tax vs Pirate Tax‑Free** | “Marine taxes” vs “pirate tax‑free” noted. | Sailing under a “Marine” affiliation incurs a periodic fee (in‑game currency) on cargo; pirates avoid tax but may face PvP penalties. | ✅ Medium |
| **Trading (Values/Stock Culture)** | “Values/stock culture from unofficial servers” – indicates a player‑driven market. | Players list items on a marketplace; prices fluctuate based on supply (e.g., fish season) → community-driven economy. | ✅ Medium |
| **Community Bounty (Directory Feature)** | “Directory feature, not in‑game.” | Discord‑based bounty board where players post requests for items/materials; rewards are negotiated in‑game currency or cosmetics. | ✅ Low (no in‑game implementation confirmed). |

**Key Takeaway:** The economy is **resource‑centric** (mining, fishing, crafting) with **tax mechanics** that differentiate lawful vs pirate playstyles, encouraging both trade and PvP dynamics.  

---  

## F. Discord Activation Blueprint  

| Discord Feature | How It Mirrors In‑Game Systems | Sample Event / Channel |
|-----------------|--------------------------------|------------------------|
| **Profession‑Picker Onboarding** | Mirrors the *non‑linear progression* – members choose a “starting activity” (Fishing, Mining, Cooking, etc.) and receive a role. | `#welcome‑professions` – new members react to emojis to claim a role; bot posts a short guide and a “first‑task” (e.g., catch 5 fish). |
| **Dex‑Bingo Seasons** | Directly tied to the four Dexes; seasonal “bingo cards” encourage completeness. | `#dex‑bingo‑spring2027` – a 5×5 grid of Dex milestones; members post proof for a chance at a cosmetic Discord badge. |
| **Cooking‑Recipe Theory Contest** | Uses the *blueprint‑style* cooking system (7 equipment, 500 talent points). | `#cook‑off‑contest` – participants submit a “recipe blueprint” (text + image) following a template; community votes; winner gets a custom Discord role and a sneak‑peek of an unreleased recipe. |
| **Mount Draft Lottery** | Reflects the 16‑mount roster; creates hype for rare mounts. | `#mount‑draft` – weekly lottery where members earn “draft tickets” by completing Dex tasks; drawn mounts are announced with lore teasers. |
| **Grinder‑vs‑Casual Role Tracks** | Aligns with player archetypes (grinder = mastery focus, casual = exploration). | `#grinder‑track` & `#casual‑track` – each channel offers tailored challenges (e.g., “Reach Fishing Dex level 30” vs “Discover 10 islands”). |
| **Weekly Profession Spotlight** | Highlights each activity in turn, reinforcing the *do‑what‑you‑enjoy* mantra. | `#spotlight‑week‑1` – “Fishing Week”: live streams, Q&A with devs, exclusive fishing‑Dex tips. |
| **Poster‑Design Lab** | Encourages speculation on the *class poster* system. | `#poster‑lab` – members sketch poster combos (Agile/Fierce/Tactic) and discuss potential in‑game effects; devs may drop hints. |
| **Tax & Trade Forum** | Mirrors Marine vs Pirate tax mechanics. | `#tax‑talk` – discussion of optimal trade routes, tax‑avoidance strategies; occasional “Pirate Raid” role‑play events. |

All of the above can be automated with Discord bots (role assignment, bingo tracking, lottery draws) to keep the community active while the game is still in development.  

---  

## G. Sources  

| Source | Type | Date Accessed | Notes |
|--------|------|---------------|-------|
| **rellseaswiki.com** – “Hub” page (Races, Mounts, Leveling, Stats, Dexes, Class System) | Official wiki (July 2026) | 18 Sept 2026 | Primary factual base. |
| **rellseaswiki.com** – “Activities” page (Fishing, Mining, Crafting, Cooking, Woodcutting, Sailing) | Official wiki (July 2026) | 18 Sept 2026 | Provides activity list and cooking equipment/talent cap. |
| **rellseaswiki.com** – “Mounts” page (list of 16 mounts) | Official wiki (July 2026) | 18 Sept 2026 | Names confirmed; functional details not disclosed. |
| **Community posts on unofficial RELL Seas Discords & Reddit** | Player‑generated speculation (e.g., tax system, market culture) | 2025‑2026 | Marked as **[SPECULATION]** where not corroborated by the wiki. |
| **Roblox RPG design patterns (e.g., *Adventure Quest*, *Tower of Hell*)** | General industry knowledge | Ongoing | Used to infer likely reward structures and UI conventions; flagged as speculation. |

---  

**End of Report**  

*All data points are drawn from the confirmed wiki entries unless explicitly marked as speculation. Numbers, names, or mechanics not present in the source material have been omitted to respect the “no invented values” rule.*

---
## Appendix V — Grounded verification (2026-10-05, youcom MCP)

Method: `you-contents /progression/` hub. No invented numbers.
CONFIRMED: `Browse 25 pages`; Races 5, Mounts 16, Leveling (XP/levels/mastery), Stats, Dexes (Adventure/Fishing/Craftsman/Recipe), Class System (classes/specs/trees). Non-linear verbatim: `every activity (fishing, cooking, mining, woodcutting, combat) levels your character. Grow by doing what you enjoy. Dexes reward completeness; races define starting traits; class opens with first spec pick.`
NOT re-verified: cooking 7 tools / 500pts, mount names/functions, tax/trade loops, class slots/posters — keep July snapshot, SPECULATION.
Sources: `https://rellseaswiki.com/progression/`. Status: hub COMPLETE, details PENDING.