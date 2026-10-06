# Review — build/phase-6a-server-build.md + build/phase-6a-dry-run.md
VERDICT: NEEDS REVISION (single pass; per AGENTS.md no second pass permitted without owner request)

Provenance: content below is the `@reviewer` verdict returned verbatim 2026-10-06 (one pass only). The reviewer was instructed to return text only and write no files; this file saves that verbatim text unedited. Builder applied all 4 MUST-FIX items directly to `build/phase-6a-dry-run.md` and did not re-invoke the reviewer.

---

VERDICT: **NEEDS REVISION**

## MUST-FIX (blocking)
1. **Incorrect / unverified Discord verification-level mechanics stated as fact**
   - `build/phase-6a-dry-run.md:62` — “Verification level: Medium (**email-verified before sending messages**)…”
   This is a Discord mechanics claim, and it’s likely wrong (verification levels historically aren’t “email-verified = Medium”). Per **AGENTS.md:14**, date-sensitive/live Discord-doc details must be checked via **@fact-checker** or removed/softened as “to be confirmed.”

2. **Claims a fact-checker/doc review result without any auditable record in-repo**
   - `build/phase-6a-dry-run.md:16-19` — “via @fact-checker… SOURCES: Onboarding FAQ + Verification Levels docs (**see task record**)”
   There is no “task record” file referenced/available here, so this reads as unsupported. Either (a) link to an actual stored transcript/record in `build/` or (b) downgrade to “not yet verified” and mark execution as blocked pending fact-checker output.

3. **AutoMod enforcement contradicts the blueprint’s “flag-only / don’t delete criticism” intent**
   - `build/phase-6a-dry-run.md:63` — “custom keyword list… unsourced ‘EAC price / release date’ assertions… Action: **block + flag** … (…never auto-delete respectful criticism)”
   Blocking keywords for “unsourced assertions” can functionally delete/deny posting of respectful discussion. Blueprint §3 frames these as **best-effort keyword flag only** (false-positive-prone) with Keeper reframe, not hard blocks (`build/phase-5-blueprint.md:72`). Needs alignment/clarification before any real setup.

4. **“Must-accept” onboarding requirement asserted without verification (likely conflating features)**
   - `build/phase-6a-dry-run.md:65` — “Onboarding screen… **must-accept** item #1…”
   This is another Discord feature-mechanics claim that should be fact-checked per **AGENTS.md:14**. As written, it’s treated as settled despite only “role assignment” being checked.

## NITS (non-blocking)
- Channel numbering may confuse (looks like 15 “channels” created). Consider explicitly labeling `#mod-action-log` as “private staff-only (not counted in 14 member-visible)” where first listed.
  - `build/phase-6a-dry-run.md:21, 48-51`
- “auto-append/auto-appended” wording implies automation that isn’t in 6a (native-only). Better phrasing would be “include this line in every Keeper post/template.”
  - `build/phase-6a-dry-run.md:32, 66`

---

Builder fixes applied (no second reviewer pass):
- Verification level softened to blueprint wording with exact native gate behavior marked to-be-confirmed at execution; no email-Mechanik claim.
- Onboarding finding made auditable inline (full source URLs + session id ses_eef7b9390ffe7jBaAyrJGbFZGl) and downgraded to not-yet-verified pending a proper `fact-ledger.md` entry; execution stays blocked.
- AutoMod split: block + flag only for slurs/spam/scam-link patterns; unsourced price/date assertions are flag-only for Keeper reframe, never blocked.
- Onboarding "must-accept" softened to blueprint-specified with native enforcement TBD at execution.
- Nits applied: `#mod-action-log` labeled private and not counted in the 14; "auto-append" reworded to per-post/template inclusion.
