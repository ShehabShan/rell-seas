# Review — build/phase-2-synthesis.md
VERDICT: needs revision

Provenance: content below is the `@reviewer` verdict returned verbatim 2026-10-06 (single bounded pass). The reviewer was instructed to write this path directly; local verification (unchanged mtime/md5 13:58:18) showed its sandbox write does not propagate to this workspace, so the returned verbatim text is saved here unedited. Builder added nothing except this header.

STRONG:
- Ranked needs are clearly labeled (N1–N12) and usually anchored with concrete volumes (e.g., INS-015 vol 7728 in N1; sentiment topic/cluster volumes throughout), matching Phase-2’s ranked-needs requirement.
- Conflicts are explicitly enumerated (C1–C11) with a stated winner/handling rule and rationale; C7 correctly applies AGENTS.md hierarchy by letting `comment-sentiment-findings.md` override `discord-architecture-research.md`.
- Gaps section is comprehensive and appropriately treats uncertain items as RUMOR/UNVERIFIED/SPECULATION (e.g., G3/G4), aligning with source discipline.

WEAK:
- **Server-design leakage:** N12 includes solution-structures: “ticket routing” and “charter-with-appeals” (line 39–40); N11 similarly lists “closed-loop response posts” / “weekly small updates” (line 37). Phase-2 brief says “No server design yet,” so even as provenance this is too implementation-shaped.
- **Unsourced mechanics/access digit claim:** G2 states “16+-vs-9+ age split” (line 68). Even framed as a gap, this is a specific mechanics/access-number claim not traceable to an Appendix V tail per AGENTS.md §Source hierarchy #2; should be removed or de-numeralized.
- **Potential “rumor digit” repetition:** N4 mentions “iPhone-7/8 folk benchmark” and N4 also cites “700-day-revamp meme” (line 19). If these are rumor-number tokens, the phase-2 output should avoid repeating them (your own rule: no repeated rumor digits) or clearly mark them as non-actionable shorthand without propagating specifics.
- **Ranking rule ambiguity:** Method says ranking uses sentiment weighted order as tiebreak (line 7). Brief asks “ranked by volume where possible”; consider explicitly stating where sentiment order overrides volume order (which specific needs swapped) to keep the ranking audit-friendly.

MUST-FIX before the owner sees this:
- Remove or rephrase all solution/structure mentions (tickets, pinning, charters, weekly updates, “somewhere for salt to go”) so Phase 2 is strictly needs/outcomes.
- Remove the explicit “16+-vs-9+” numeric split (and any similar access numbers) unless backed by Appendix V; keep as “age-restriction rumors/confusion exist” and retain as a gap.

QUESTIONS FOR OWNER:
- None (this file should not force taste decisions), but confirm whether they want Phase-2 to include cross-cutting “enablers” (N13–N14) as non-ranked items, or keep strictly to a single ranked list.
