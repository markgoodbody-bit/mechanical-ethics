# Archive Provenance

This file records archive moves made during repo hygiene.

Archive moves are not deletion in intent. They preserve the original material under `99_ARCHIVE/` and remove it from the live reader path only after the original path is no longer part of the public front-door surface.

## Pending low-risk moves from Claude/Fable audit — 2026-07-01

```text
00_CURRENT_SURFACE/ -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/
```

This was classified as a low-risk archive candidate by the Claude/Fable hygiene audit and approved by Mark for the next pass.

## Not yet approved

```text
01_BOOK_DRAFT/ME_BOOK_v0_1/ -> 99_ARCHIVE/superseded_book_draft/ME_BOOK_v0_1/
```

Book material requires explicit Mark confirmation before moving.

## Applied moves

None yet.

## Application note

The current connector view has not exposed a full recursive file tree for this path. Do not perform partial directory moves. Apply only when exact file list/tree entries are available, or when using local git so the move can be performed atomically with `git mv`.
