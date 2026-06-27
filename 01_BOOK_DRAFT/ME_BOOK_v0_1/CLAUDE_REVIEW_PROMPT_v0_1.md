# Claude Review Prompt — ME Book Draft v0.1

Mark here. Please review the first full wide-pass draft of the Mechanical Ethics book.

Repository: `markgoodbody-bit/mechanical-ethics`
PR: #7 — `Start ME book draft v0.1`
Folder:

```text
01_BOOK_DRAFT/ME_BOOK_v0_1/
```

Files to review:

```text
00_TITLE_AND_CONTROL.md
PART_0_HOW_TO_READ_THIS_BOOK.md
PART_1_THE_ENTITY_THAT_WAKES.md
PART_2_THE_WORLD_THAT_PUSHES_BACK.md
PART_3_LAYERS_OF_ACTION.md
PART_4_HARM_TIME_AND_FUTURE_SPACE.md
PART_5_DESCRIPTION_IS_NOT_PERMISSION.md
PART_6_THE_FIRST_GATES.md
PART_7_PROTECTION_STANDING_AND_SCOPE.md
PART_8_CORRECTION_REPAIR_AND_RESIDUE.md
PART_9_DIRTY_CONFLICTS.md
PART_10_RESPONSIBILITY_AFTER_VISIBILITY.md
PART_11_POWER_LEGITIMACY_AND_COERCION.md
PART_12_CIVILIZATION_UNDER_UNCERTAINTY.md
PART_13_ARTIFICIAL_SYSTEMS_AND_FUTURE_MINDS.md
PART_14_CASE_RECORDS_AND_USE_PROTOCOLS.md
PART_15_LIMITS_FAILURES_AND_OPEN_QUESTIONS.md
STRUCTURAL_REVIEW_v0_1_2026_06_27.md
```

Task: hostile-but-fair structural review only.

Do not line edit.
Do not polish prose.
Do not rewrite chapters.
Do not ask for external validation.
Do not expand into policy programme.

Context:

This is the first full wide-pass book draft after the architecture, skeleton, interface schema, alignment note, and smoke test. It is not canon, not validation, not public release, and not final moral law.

The intended book arc is:

```trace
origin
-> interaction
-> layers
-> future_space_and_time
-> description_not_permission
-> first_gates
-> protection
-> repair_and_residue
-> dirty_conflict
-> responsibility
-> power
-> civilization
-> artificial_systems
-> use_protocols
-> limits
```

Review questions:

1. Does the book preserve the middle-out origin, or does it smuggle ethics/personhood/law too early?
2. Can a TRACE-naive reader follow the human argument without needing the operator schema?
3. Does Part 4 explain TRACE-owned primitives without redefining them?
4. Does Part 5 preserve `description_is_not_permission` without becoming technical plumbing?
5. Are the Part 6 gates earned from Parts 1–5, or do any still feel imported?
6. Does Part 7 avoid hidden worth-ladder/personhood smuggling?
7. Does Part 8 preserve correction/repair/residue distinctions?
8. Does Part 9 keep dirty conflicts dirty, or does it clean sacrifice through procedure?
9. Does Part 10 avoid hindsight blame while preserving answerability?
10. Does Part 11 stay framing-not-solving on legitimacy/coercion/desert/punishment/force?
11. Does Part 12 become manifesto/aphorism, or does it preserve mechanism?
12. Does Part 13 overclaim AI standing or alignment doctrine?
13. Does Part 14 put operator schema in the right place without turning the book into bureaucracy?
14. Does Part 15 name limits clearly enough?
15. What structural defects must be patched before merge as first wide-pass draft?
16. What should be deferred to second-pass prose and not block merge?

Return exactly:

- `MERGE_AS_FIRST_WIDE_PASS`, `PATCH_THEN_MERGE`, or `DO_NOT_MERGE`
- one-paragraph reason
- exact patch text if needed

Remember: this review is useful pressure, not validation.
