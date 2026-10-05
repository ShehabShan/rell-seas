# Discord Architecture Research — structure doctrine + activity system + Roblox cases

Date: 2026-09-18. Purpose: supply-side research for the pre-release RELL Seas fan Discord (demand-side audience research lives in yt-comment-findings.md, reddit-findings.md, caribbros-research.md). This is RESEARCH, not the blueprint.
Sources: Discord official support docs (community setup, onboarding, verification), The Game Marketer agency guide (ex-Riot/Ubisoft/EA, Aug 2026), Guildbase "20 Ways to Grow 2026", discords.ai wiki set, buildmydiscord guides, top.gg / discordhome / discordforge Roblox listings (member counts Apr-Sep 2026). Synthesized via Gemini.

---
# RELL SEAS DISCORD RESEARCH & ARCHITECTURE DOCUMENT
**Target:** Pre-Release Fan Discord (Roblox) & Future YouTube Channel  
**Context:** ~380K Favorites, Launch Window Sep–Oct 2026, 105K-member existing unofficial community to differentiate from, official RELL Games server to complement.

---

## A. The Common Anatomy

Discord server architecture requires balancing structural discipline with organic community flow. Based on 2026 platform standards, the mechanics of community engineering are categorized below.

### 1. Structure & Permissions Doctrine
*   **The Golden Rule:** Roles first, then categories. Category-level permissions propagate downward, maintaining structural integrity through synced vs. unsynced channels.
*   **Category Discipline:** Limit the server to a maximum of **8 primary categories**. Avoid 1-channel categories as they disrupt mobile scrolling flow.
*   **Naming Convention:** Standardize naming with a clear visual hierarchy (e.g., `📁 ┃ INFORMATION`, `💬 ┃ SOCIAL`).
*   **Order of Operations:** 
    1. Information
    2. Welcome/Onboarding
    3. General/Social
    4. Main Content (The Game)
    5. Sub-Topics
    6. Events
    7. Voice
    8. Staff (Locked)

### 2. The Lean Launch Model (Max 12 Channels)
A dead channel signals an abandoned community. **Start lean.** 
*   **Category 1 (Info):** `#announcements`, `#patch-notes`, `#rules`
*   **Category 2 (Social):** `#general`, `#introduce-yourself`
*   **Category 3 (Game/Content):** `#media-clips`, `#gameplay-tips`
*   **Category 4 (Utility):** `#bug-reports`, `#feedback-suggestions`
*   **Category 5 (Voice):** `General` voice channel, `Game Sessions` voice channel.
*   *Note on Memes/Rants:* Omit entirely until the community actively demands them. Archive any channel that remains dead for 2+ weeks.

### 3. Role Hierarchy & Sweet Spot (~10 Roles)
1.  **Owner** (Invisible/Protected accounts)
2.  **Admin** (Minimum necessary accounts)
3.  **Moderator** (Moderation permissions, explicitly separated from admin power)
4.  **Support** (Community helpers / ticket handlers)
5.  **Event Team** (Hosts, community managers)
6.  **Bots** (Automated integrations)
7.  **VIP** (Content creators, early boosters, special contributors)
8.  **Member** (Auto-assigned post-onboarding)
9.  **New/Unverified** (Restricted view until onboarding is complete)
10. **Opt-in / Interest / Faction Roles** (Used for targeted pings, preventing spammy `@everyone` alerts while building user identity).

### 4. Bot Stack & Automation
*   **Native First:** Maximize Discord’s built-in **AutoMod** before adding third-party bloat.
*   **Core 3–4 Additions:**
    *   *MEE6 or Dyno:* Leveling and basic automod.
    *   *Carl-bot:* Reaction roles, starboard, and event triggers.
    *   *Giveaway Boat:* Community engagement engines.
    *   *Statbot:* Server analytics and growth tracking.
    *   *DISBOARD / Sesh / ProBot:* Bumping, scheduling, and economy loops.
*   *Real-World Reference:* Mega-trading server *Eclipse* (770K members) relies on a lean, high-reliability stack: Appy, ProBot, Giveaway Boat, and Arcane.

### 5. Onboarding & Conversion Friction
Native Community Onboarding should be restricted to **2 steps max** (e.g., rules agreement + 1 platform/interest role). Every additional layer exponentially drops conversion rates:
*   Reaction gates: ~5% drop
*   CAPTCHA tests: ~10% drop
*   Q&A blocks: ~15% drop
*   Full applications: ~35% drop
*   Voice interviews: ~60% drop
*   **Welcome Best Practices:** Keep welcome messages under 300 words with functional channel mentions. Gate the server so unverified accounts see *only* the start-here channel.

---

## B. What Discord Is Made For

Discord is built for **conversation**, not broadcasting. Servers structured like press-release RSS feeds inevitably fail. 

### 1. The Presence Principle
Member count is vanity. True health is measured by **weekly communicators** (a healthy baseline is 3–10% of total members) and **7-day/30-day retention** (good 30-day retention exceeds 40%). Presence beats announcements—developers and staff visibly chatting and joining voice channels builds intrinsic community trust.

### 2. Event Cadence Table
Servers with regular recurring events see up to **3x higher retention**.

| Frequency | Event Type | Purpose | Effort Level |
| :--- | :--- | :--- | :--- |
| **Daily** | Trivia, Polls, Theory Prompts | Low-barrier engagement hooks | Low |
| **Weekly** | Game nights, watch parties, voice hangouts | Building core social bonds | Medium |
| **Monthly** | Tournaments, community showcases | Driving competitive energy | High |
| **Quarterly** | Major milestones, live dev Q&As | Celebrating community history | Very High |

### 3. Social Bonds & Gamification
*   **The Friendship Factor:** People stay for friends, not content. Prioritize member spotlights, icebreaker prompts, and small sub-topic interest groups. Give the community real ownership over sub-channels and event formatting.
*   **Leveling/XP Mechanics:** Boosts retention by 40–60%, *provided* rewards are tied to constructive contribution (helping peers, welcoming new users, sharing quality media) rather than raw message spam.

### 4. The Feedback Engine
*   Implement strict structural templates for feedback channels (Requiring: What, Why, and Trade-off).
*   **Close the loop publicly:** Explicitly credit community members when their feedback is implemented (*"You asked, here it is"* is the single most powerful tool for reviving dead servers).
*   Never delete respectful criticism; instead, address it transparently. Utilize gated tester roles to isolate and manage playtest feedback securely.

### 5. Moderation Philosophy
*   Rely on fast, quiet timeouts paired with a direct DM explaining the infraction. Avoid public drama or power-tripping.
*   Leave visible, neutral notes where content was removed for violating standards.
*   **The Scaling Rule:** Massive communities (50K+) can run smoothly on as few as **3 veteran volunteer mods** if behavioral culture is locked down during week one.

### 6. Health Metrics & Benchmarks

| Metric | Unhealthy | Healthy / Benchmark |
| :--- | :--- | :--- |
| **Daily Active Communicators** | < 1% of total | 3% – 10% of total |
| **30-Day Retention** | < 15% | > 40% |
| **Replies per Message** | < 0.5 (monologue style) | > 1.5 (active dialogue) |
| **DISBOARD Bumps** | < 1 / day | 5+ / day (+30-50% profile views) |

---

## C. Roblox Case Studies

An analysis of top-tier Roblox spaces highlights how successful infrastructure directly maps to game identity:

```
[Official Mega-Server: Blox Fruits (3.5M+)] ──> Massive scale, high utility, centralized updates
[Trading/Utility Hubs: Eclipse / Bloxy (500K-700K+)] ──> 24/7 self-running bots, stock feeds, zero staff overhead
[Niche Activity Hubs: Sea Hunters (30K)] ──> Micro-focus on a single gameplay loop
```

*   **Blox Fruits (3.5M+):** Relies on massive utility pillars—strategy tips, trading hubs, raid coordination, and rapid announcements.
*   **Eclipse & Bloxy (534K – 770K Trading Hubs):** Built entirely around 24/7 autonomous mechanics: live stock notifiers, automated matchmaking, trading feeds, daily automated giveaways, and strict SFW enforcement. These require almost zero active staff intervention.
*   **Sea Hunters (30K):** Proves that a hyper-niche focus (anchored around a single in-game maritime activity) can build a fiercely loyal community.
*   **Brookhaven (253K):** Centers around visual assets, fan art galleries, building guides, and bug reporting.
*   **The Common Pattern:** Successful Roblox servers combine **utility** (trading, stock bots, LFG/crew coordination, private server links) with a **speculation space**, creator content integration, and automated giveaways.

---

## D. Pre-Release Playbook

1.  **Timing:** Open the server 3 to 6 months prior to launch. The conversations held in the first few weeks permanently set the server's cultural DNA. Soft-launch with a small group to tune the culture before opening the floodgates.
2.  **Sharp Niche:** Avoid generic "gaming community" positioning. Define the space precisely—e.g., *"Pre-release theory-crafting & launch-day crew finder for RELL Seas."*
3.  **Signature Experience:** Provide one unmissable element competitors lack (e.g., an exclusive asset tracker, a weekly dev-lore breakdown, or a specialized crew-matching system).
4.  **Content Loop:** Distribute dev-update clips, behind-the-scenes assets, and screenshots to Reddit and TikTok, driving traffic directly into the Discord. Use the server as a centralized hub for beta/playtest access.
5.  **Anti-Patterns to Avoid:**
    *   Building 25 channels for your first 50 members.
    *   Going completely silent for 2 weeks.
    *   Blindly copying another game's structure instead of tailoring it to RELL Seas' specific gameplay loops.
    *   Scaling member count before the internal culture is stable.
    *   Over-moderating into a cold, corporate atmosphere.

---

## E. Bridge to RELL Seas: Strategic Implications

Mapping the research data against the known facts of the RELL Seas ecosystem yields strategic imperatives for our server design:

1.  **Differentiate from the Official Hub:** The official RELL Games Discord (~1M members) is massive, corporate, and support-depleted. Our fan server must feel intimate, highly interactive, and peer-driven rather than an announcement broadcast feed.
2.  **Harness Breadcrumb Culture:** RELL Games drops information infrequently and cryptically. The server must be architected as a **theory-crafting engine** where tiny screenshots or developer comments are dissected line-by-line.
3.  **Capitalize on Scam Fear:** Given the history of Roblox trading and high-stakes item economies, verification systems and security education channels must be prominent to alleviate community anxiety around scams.
4.  **Crew-Forming Architecture:** Because RELL Seas is an open-world anime sea game (similar to *One Piece* tropes), crew and fleet recruitment must be a core pillar of the server utility long before launch.
5.  **Shindo Coexistence:** A significant portion of the audience comes from *Shindo Life*. Channel culture should gracefully bridge past RELL fandom into the new IP without letting old habits cannibalize new discussion.
6.  **Small-Creator Symbiosis:** Position the server as a launchpad for emerging YouTube creators covering RELL Seas. Provide dedicated content-sharing zones to build early, loyal influencer advocacy.
7.  **Lean Pre-Launch Setup:** Restrict launch to under 12 channels to ensure maximum chat density per channel during the pre-release drought.
8.  **Automated Utility Focus:** Implement automated trackers, RSS feeds for developer socials, and update alerts early so the server feels alive 24/7 without burning out the moderation team.
9.  **Scheduled Rituals:** Institute a weekly theory or countdown ritual to combat the months-long wait until the Sep–Oct 2026 launch window.
10. **Feedback Loop Integration:** Establish clean suggestion templates early to make the community feel their voices are heard by passionate fans (and potentially seen by developers).
11. **Strict Onboarding Discipline:** Keep the native onboarding flow under 2 steps to maximize conversion from incoming TikTok and YouTube traffic.
12. **Opt-In Pings over Broadcasts:** Utilize role-gated notification pings for dev logs and media drops to prevent notification fatigue and mass leaves.
13. **Leveling Tied to Contribution:** Reward theory-crafting and welcoming behavior via automated XP rather than raw message spam.
14. **Voice Infrastructure for Crews:** Prepare scalable voice channels for crew voice communication during playtests and launch day.
15. **Transparent Moderation:** Adopt a fast-timeout, quiet-DM moderation stance to keep public channels clean and free of toxic power struggles.
16. **Archival Discipline:** Aggressively archive dead pre-release speculation channels post-launch to keep the server clean and dynamic.
17. **Evergreen Resource Hubs:** Build pinned guides and mechanic breakdowns early; these rank well and feed organic discovery over the multi-month pre-release runway.