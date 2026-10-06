# Fact Ledger

Append-only log of live-verified facts for the RELL Seas Discord build. Written only by `@fact-checker`. Never edit or delete an entry — if a fact changes, add a new entry; the newest `CHECKED` date is the current one.

Entry format:

---
Q: question asked
VERDICT: CONFIRMED | CHANGED | UNVERIFIABLE
ANSWER: ...
SOURCE: ...
CHECKED: date
TAG: VERIFIED | SNAPSHOT | RUMOR
---

---
Q: Is RELL Seas currently released or still unreleased?
VERDICT: CONFIRMED
ANSWER: Still unreleased; the official Roblox listing shows no running experiences and trackers list it as pre-release with no announced launch date.
SOURCE: https://www.roblox.com/games/7089993809/RELL-Seas, https://rellseaswiki.com/release-date/
CHECKED: 2026-10-06
TAG: VERIFIED
---
---
Q: Can Server Settings → Onboarding assign a role automatically when a member completes onboarding, independent of verification level?
VERDICT: CONFIRMED
ANSWER: Yes — Community Onboarding grants the roles linked to a member's chosen answers when they complete onboarding; Verification Levels separately gate sending messages and joining voice, not the role grant.
SOURCE: https://support.discord.com/hc/en-us/articles/11074987197975-Community-Onboarding-FAQ, https://support.discord.com/hc/en-us/articles/216679607-Verification-Levels
CHECKED: 2026-10-06
TAG: VERIFIED
---
---
Q: What is the exact mechanism by which Community Onboarding grants roles — automatic on completion, or only via answer-linked role picks?
VERDICT: CONFIRMED
ANSWER: Only via answer-linked picks — "When a member picks that answer, they will be granted those roles and those channels will be added to their channel list!"; priors read different articles (Onboarding FAQ vs Verification Levels gates chat/voice), so the Onboarding sentence settles it.
SOURCE: https://support.discord.com/hc/en-us/articles/11074987197975-Community-Onboarding-FAQ, https://support.discord.com/hc/en-us/articles/216679607-Verification-Levels
CHECKED: 2026-10-06
TAG: VERIFIED
---
