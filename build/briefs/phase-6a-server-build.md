# PHASE 6a — Server Build (safety-gated: dry-run first)

Scope: one session. Safety-gated: dry-run plan only, no live execution without explicit owner confirmation.

Input: `build/phase-5-blueprint.md` (final spec — Long Watch + borrowings, §§1–4, 7–8).

Scope (exactly as specced in blueprint, no re-derivation):
- Create 7 categories / 14 member-visible channels + private `#mod-action-log` (staff-only), with purposes, slowmode, forum/auto-archive settings per blueprint §1/§3.
- Create 5-rung role ladder (Castaway / Watchkeeper / Beacon / Elder / Keeper) + Solo Banner optional flair, per §2. No paid roles.
- Set Medium verification level at launch (High on raid signal preset), per §3/§8. Verification gates chatting only, assigns no role by itself.
- Configure AutoMod: presets ON + custom keyword list per §8 (slur variants, lookalike-link domains, "free Robux/EAC giveaway" bait; action = block + flag to private log).
- Configure Discord native onboarding flow per §4 (fan-run + rules + English-only + report path must-accept; lands as Castaway).
- Does NOT include bot code or hosting (that's 6b). Helper-bot free-tier confirmation (welcome-DM / reaction-role / autorole) is a 6b question; 6a uses native-only + Keeper batch-handling fallback.

Constraints (AGENTS.md wins on any conflict):
- Must not touch `.env` or print the token anywhere, including in any output file or commit. Refer to token only as `[REDACTED]`.
- Dry-run plan only in this phase. Do not create anything in the live server yet.
- Date-sensitive / live Discord-docs question (onboarding auto-role) goes through `@fact-checker`, one question at a time. No fallback answers.
- Only write inside `build/` (plus `PROGRESS.md` update).

Skill: none (build from blueprint spec directly).
Output: `build/phase-6a-dry-run.md` (full would-create list; explicit "nothing created live" statement).
Reasoning effort: standard.
Reviewer: yes — run `@reviewer` one pass before reporting (AGENTS.md: every phase from Phase 2 onward, exactly one pass).

Definition of done:
- Tooling for Discord API reported (MCP / discord.py / discord.js / direct REST).
- Onboarding-role-assignment finding reported (from current Discord docs via fact-checker) before any autorole planning.
- `build/phase-6a-dry-run.md` saved; live server untouched; `.env` unread.
- Under-150-word report: tooling, finding, dry-run saved, nothing created live.
