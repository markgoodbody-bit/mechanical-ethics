# Claude Review Prompt — ME Interface Schema v0.1

Mark here. Please review this Mechanical Ethics interface schema before we use it for worked examples or opening prose.

Repository: `markgoodbody-bit/mechanical-ethics`
Branch / PR: `me-interface-schema-v0-1`

Files to review:

- `00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/README.md`
- `00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/TRACE_ME_INTERFACE_SCHEMA_v0_1_2026_06_27.md`
- `00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/ME_CASE_RECORD_TEMPLATE_v0_1_2026_06_27.md`

Task: hostile-but-fair interface/schema review only.

Context:

The merged ME architecture and skeleton established:

- one human-facing book;
- middle-out origin;
- TRACE-owned shared primitives;
- interface plumbing moved out of the human argument spine;
- router outputs are findings, not authorizations;
- dirty conflicts remain dirty;
- Part 11 frames legitimacy/coercion/desert rather than solving them;
- no validation claim.

This PR adds the operator-support interface that Part 14 / appendices can use. It must not become the book's human spine and must not redefine TRACE.

Please check:

1. Does the schema preserve `TRACE_description != ME_permission`?
2. Does it keep TRACE outputs read-only?
3. Does it accidentally redefine TRACE-owned primitives?
4. Does it turn router states into authorizations despite saying they are findings?
5. Does the case-record template force enough evidence without becoming impossible to use?
6. Does contaminated signal handling correctly demote evidential authority rather than moral standing?
7. Does the dirty-conflict section still avoid cleaning sacrifice?
8. Does responsibility attachment avoid hindsight blame?
9. Does legitimacy/coercion remain an open value-crux where appropriate?
10. Are there missing fields required before worked examples can be run?
11. Is anything merge-blocking before a first worked-example or opening-page seed?

Return exactly:

- `MERGE_AS_IS`, `PATCH_THEN_MERGE`, or `DO_NOT_MERGE`
- one-paragraph reason
- exact patch text if needed

Do not rewrite the schema wholesale.
Do not propose finished prose.
Do not expand into new doctrine.
Only identify boundary, usability, schema, or honesty defects.
