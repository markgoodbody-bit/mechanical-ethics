# Claude Review Prompt — ME Book Architecture v0.1

Mark here. Please review this Mechanical Ethics architecture PR before we start prose drafting:

Repository: `markgoodbody-bit/mechanical-ethics`
Branch / PR: `me-book-architecture-v0-1`

Files to review:

- `00_CURRENT_SURFACE/ME_BOOK_ARCHITECTURE_v0_1/README.md`
- `00_CURRENT_SURFACE/ME_BOOK_ARCHITECTURE_v0_1/ME_BOOK_ARCHITECTURE_v0_1_2026_06_27.md`

Task: hostile-but-fair architecture review only.

Context:

TRACE v0.6 is now treated as structurally coherent, transmissible, testable, and not validated. Major TRACE rewrites are paused as a workflow decision only. Decision advantage remains unproven and no STRONG_SIGNAL is claimed.

This PR starts the new Mechanical Ethics side. It is not book prose. It is a planning/control surface to define scope, structure, TRACE→ME interface, router states, honesty rules, and build order before drafting begins.

Current intended split:

```trace
TRACE := how_to_see_transitions_under_uncertainty
ME := what_follows_after_honest_seeing
```

Critical constraints:

- ME must be one human-facing book with numbered parts, chapters, and sections.
- Do not use Roman numerals.
- ME should start from the simplest middle-out premise: something is here, perceives partially, can change something, does not know everything, and time passes.
- Old ME books are reference/quarry only, not the new structure.
- TRACE outputs are read-only for ME.
- ME may prescribe, but every prescription must trace back to structural pressure.
- ME must have fail states such as HOLD, ESCALATE, UNRESOLVED_VALUE_CRUX, or REGRESSION_RISK.
- Dirty conflicts must not be made clean by protocol.
- This is not validation and not a final moral theory.

Please check:

1. Is the one-book scope too broad, too thin, or workable?
2. Does the architecture preserve strict middle-out build order?
3. Does the structure answer what people are actually asking ME to answer?
4. Does the TRACE→ME interface remain clean, or does ME leak back into TRACE?
5. Does the plan accidentally create an automatic moral engine?
6. Are ME fail states strong enough?
7. Is the dirty-conflict section honest enough, or still too clean?
8. Does old Book I / II / III material leak too much structure into the new book?
9. Does the architecture overclaim anything about TRACE, AI review, validation, or decision advantage?
10. What is merge-blocking before the first prose skeleton?

Return exactly:

- `MERGE_AS_IS`, `PATCH_THEN_MERGE`, or `DO_NOT_MERGE`
- one-paragraph reason
- exact patch text if needed

Do not rewrite the whole book.
Do not expand into prose.
Do not propose a different project.
Only identify architecture defects, boundary defects, or narrow patch-before-merge fixes.
