# Review — build/phase-5-blueprint.md
VERDICT: NEEDS REVISION (single pass; per AGENTS.md no second pass permitted without owner request)

Provenance: content below is the `@reviewer` verdict returned verbatim 2026-10-06 (one pass only). The reviewer was instructed to return text only and write no files; this file saves that verbatim text unedited. Builder applied MUST-FIX items directly (feasible role-assignment mechanism, free-tier-constrained helper-bot list with native-only fallback, real ticket/DM report workflow) and did not re-invoke the reviewer.

---

VERDICT: NEEDS REVISION

STRONG:
- All 10 required blueprint sections are present and broadly “buildable” (channels/roles/bots/onboarding/launch week/weekly routine/disclaimer/safety/left-outs/freshness flags), matching the Phase 5 brief + skill checklist.
- Constraints are explicitly honored in multiple places: fan-run disclaimer placement + “no official assets” rule (§7), English-only launch + no non‑EN spaces (§1/§9), no paid roles/no P2W optics (§2), no public mod summary beyond private log (§0/§8/§9).
- Snapshot-dependent facts are correctly quarantined into a dedicated re-check list (§10) and even includes a “don’t cite in server copy” guardrail for the counts claim (item 8).

WEAK:
- **Buildability risk / likely incorrect Discord mechanics:** “Verify email (Medium level) → auto-promote to Watchkeeper” (§4, line 85) is not a native Discord automation. Verification level doesn’t trigger role assignment; this needs a concrete, feasible mechanism (or be reframed as manual).
- **Bot capability risk / free-tier risk:** “ONE helper bot (Carl-bot)… forum auto-archive nudges / expiry DM… label template enforced by helper-bot prompt” (§3, lines 71–78) reads like assumed features. Carl-bot may not support these exact flows (and some may be premium), which threatens the “free + solo operator” constraint.
- **Report-flow feasibility:** “message-react ‘report’ → lands in private queue” (§8, line 120) is not a Discord-native pathway; without a specific bot/modmail setup, this is likely non-functional.
- **Source-discipline edge:** “custom ‘EAC price’ / ‘release date stated as fact’ phrases routed to … reframe queue” (§3, line 72) implies confident detection/enforcement logic but isn’t tied to an insight card or a proven tool capability; also risks false positives and “censorship” optics.
- **Comment-sentiment tension not surfaced:** Findings argue for PT/FR hubs with native-speaker mods (comment-sentiment-findings §5.5), while this blueprint chooses English-only + locked translation blurb (§0/§1). That’s fine per owner directive, but the blueprint should explicitly note it as an intentional override of research due to operability.

MUST-FIX:
- Replace/clarify the **email-verified → role auto-promotion** claim with a mechanism that actually exists (or mark it as manual).
- Verify and constrain the **helper-bot feature list** to what is definitely possible on a free plan; otherwise specify “custom bot in Phase 6” (but that affects scope).
- Fix the **reaction-based report pipeline** to a real workflow (e.g., ModMail bot, slash command, or “DM Keeper” fallback) that works without live staffing.

QUESTIONS FOR OWNER:
- Are you willing to run/maintain a **custom lightweight bot** (to guarantee role gating + report intake + expiry nudges), or must Phase 6 be strictly “no-code / off-the-shelf free bots only”? This choice is hard to unwind later.

---

Builder fixes applied (no second reviewer pass):
- Role assignment now feasible: verification gates chatting only; Watchkeeper via helper-bot autorole on onboarding completion with Keeper batch-grant fallback; <1-day accounts stay Castaway.
- Helper-bot list constrained to free-tier definite (welcome-DM/reaction-role/autorole); forum auto-archive is native, expiry/label prompts marked best-effort with native + Keeper fallback; no custom bot at launch (added to left-outs).
- Report flow now real: helper-bot ticket command (/report, Phase 6 to confirm free-tier name) OR DM Keeper, async queue, no reaction pipeline.
- AutoMod keyword flag softened to best-effort with card cites (INS-015/016/001/007/054/128) and false-positive review; sentiment §5.5 override noted explicitly in left-outs.
- Owner question answered in blueprint default: strictly off-the-shelf free bots only, no custom bot (reversible later if owner requests).
