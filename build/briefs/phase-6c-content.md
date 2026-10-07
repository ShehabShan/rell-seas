# PHASE 6c: SERVER CONTENT (DRAFT ONLY)

## Scope
Draft every piece of text the live server still needs. This phase writes ONE document for owner review. It makes no Discord calls, does not read `.env`, does not run the execution script, and posts nothing. Posting happens later, after the owner approves the draft.

Input: `build/phase-5-blueprint.md` (rules summary, §7 disclaimer, §8 AutoMod, launch-week plan, channel purposes), `build/phase-6a-execution-log.md` (exact channel names), `build/fact-ledger.md`.
Output: `build/phase-6c-content.md`
Reasoning effort: high. Reviewer: one pass only, per AGENTS.md.

## Voice (default, owner may override at review)
Warm, plain English, short sentences, light nautical flavor at most. Never hype, never promise dates, never imply the server is official. Keep each message short enough to read on a phone in ten seconds.

## What to write
Format the document by destination channel. For each item give the exact channel name, whether it is PINNED, and the paste-ready text.

1. **`#read-first-rules`**: full rules copy. Expand the blueprint's 6-rule summary into clear wording. Keep the substance the blueprint set (evidence-over-insults, rumor labeling, no harassment, English-only, scam rules, and so on). Do not invent new rules. If the blueprint is missing something you think is needed, list it separately under "Proposed additions" for the owner to decide. Keep the existing disclaimer line exactly as pinned.
2. **Report path.** Write the text for how members report a problem. The `/report` bot does not exist yet, so the current path is: message a Keeper directly, or reply in a thread in `#scam-watch-and-report`. Write it so it is easy to update when `/report` exists.
3. **Channel guidelines.** One short pinned message each for `#finder`, `#help-desk`, `#receipts-and-rumors`, `#introductions`, `#tenure-and-returns`, `#patient-craft`, and `#creator-mirror`, plus a one-line description for each remaining channel. Write each from the channel's purpose in the blueprint.
4. **`#welcome-in-pt-fr-es`**: a 3-sentence blurb. Content: this is a fan-run, English-only server, and communities in other languages exist, with no specific servers named. Write the English source, then drafts in Portuguese, French, and Spanish. Mark each translation "NEEDS NATIVE-SPEAKER CHECK. DO NOT POST UNTIL CHECKED."
5. **Launch week.** One seed post per day for 7 days, as the blueprint plans. For each: day, channel, text, and a tag. Day-1 milestone seeds may contain ONLY facts verified by `@fact-checker` this session, each tagged VERIFIED with its ledger entry. Anything else must be clearly labeled as a community rumor or left out. Launch-week posts must not promise release dates, odds, prices, or any stat the project has not verified.
6. **Optional: Server Guide** welcome sign and 3 new-member to-dos (we skipped these in Onboarding).
7. **AutoMod keyword proposals.** Do NOT write slur or profanity lists. Discord's built-in presets cover those. Using `@fact-checker`, propose at most 15 scam-link and fake-giveaway patterns commonly reported against Roblox and Discord communities, each with its source. These are proposals for the owner to approve before anything is added.

## Fact rules
- Every game fact goes through `@fact-checker`, one question per call. Reuse existing ledger entries where they are still current.
- The blueprint §10 freshness list names what to re-check. Check only what this content actually uses, and list anything you left unchecked in the document.
- Never quote player comments. Never use official assets. Never invent numbers.
- `#creator-mirror`: link only creator channels you verified through `@fact-checker`. If you cannot verify a handle, leave a clearly marked placeholder.

## Document layout
Start with a 5-line summary of what is included and what is unverified. Then one section per destination channel. End with an "Owner decisions and to-dos" list (voice changes, proposed rules, translation checks, unverified items).

## Finishing
- Run `@reviewer` once on `build/phase-6c-content.md`. Apply must-fix items directly. Do not run a second review.
- `git add` must include `build/phase-6c-content.md`, `build/reviews/phase-6c-content.md`, and any new `build/fact-ledger.md` entries. Commit and push.
- Update `PROGRESS.md`. Report in under 150 words, with the review attached, and stop. Do not post anything.
