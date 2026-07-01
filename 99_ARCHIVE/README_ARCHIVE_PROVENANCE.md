# Archive Provenance

This file records archive moves made during repo hygiene.

Archive moves are not deletion in intent. They preserve the original material under `99_ARCHIVE/` and remove it from the live reader path only after the original path is no longer part of the public front-door surface.

## Applied moves — 2026-07-01 (Claude/Opus atomic pass)

Applied on branch `repo-hygiene-archive-audit-2026-07-01` (PR #27) using `git mv`, atomically, after full recursive tree verification of the source path (tracked and untracked; no untracked files were present, so no partial-move risk). Git recorded all entries as renames.

```text
00_CURRENT_SURFACE/ -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/   (13 files)
```

### Full file-level record

```text
00_CURRENT_SURFACE/ME_BOOK_ARCHITECTURE_v0_1/ARCHITECTURE_ALIGNMENT_NOTE_2026_06_27.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_BOOK_ARCHITECTURE_v0_1/ARCHITECTURE_ALIGNMENT_NOTE_2026_06_27.md
00_CURRENT_SURFACE/ME_BOOK_ARCHITECTURE_v0_1/CLAUDE_REVIEW_PROMPT_v0_1.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_BOOK_ARCHITECTURE_v0_1/CLAUDE_REVIEW_PROMPT_v0_1.md
00_CURRENT_SURFACE/ME_BOOK_ARCHITECTURE_v0_1/ME_BOOK_ARCHITECTURE_v0_1_2026_06_27.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_BOOK_ARCHITECTURE_v0_1/ME_BOOK_ARCHITECTURE_v0_1_2026_06_27.md
00_CURRENT_SURFACE/ME_BOOK_ARCHITECTURE_v0_1/README.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_BOOK_ARCHITECTURE_v0_1/README.md
00_CURRENT_SURFACE/ME_BOOK_SKELETON_v0_1/CLAUDE_REVIEW_PROMPT_v0_1.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_BOOK_SKELETON_v0_1/CLAUDE_REVIEW_PROMPT_v0_1.md
00_CURRENT_SURFACE/ME_BOOK_SKELETON_v0_1/ME_BOOK_SKELETON_v0_1_2026_06_27.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_BOOK_SKELETON_v0_1/ME_BOOK_SKELETON_v0_1_2026_06_27.md
00_CURRENT_SURFACE/ME_BOOK_SKELETON_v0_1/README.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_BOOK_SKELETON_v0_1/README.md
00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/CLAUDE_REVIEW_PROMPT_v0_1.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/CLAUDE_REVIEW_PROMPT_v0_1.md
00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/ME_CASE_RECORD_TEMPLATE_v0_1_2026_06_27.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/ME_CASE_RECORD_TEMPLATE_v0_1_2026_06_27.md
00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/README.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/README.md
00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/TRACE_ME_INTERFACE_SCHEMA_v0_1_2026_06_27.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/TRACE_ME_INTERFACE_SCHEMA_v0_1_2026_06_27.md
00_CURRENT_SURFACE/ME_SMOKE_TEST_CASES_v0_1/ME_SMOKE_TEST_01_ROUTINE_MEETING_MOVE_v0_1_2026_06_27.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_SMOKE_TEST_CASES_v0_1/ME_SMOKE_TEST_01_ROUTINE_MEETING_MOVE_v0_1_2026_06_27.md
00_CURRENT_SURFACE/ME_SMOKE_TEST_CASES_v0_1/README.md -> 99_ARCHIVE/superseded_book_scaffold/00_CURRENT_SURFACE/ME_SMOKE_TEST_CASES_v0_1/README.md
```

### Pre-move gate checks (all passed)

```text
repo                   = markgoodbody-bit/mechanical-ethics
branch                 = repo-hygiene-archive-audit-2026-07-01 (PR #27, draft, open)
tree clean before move = yes
README signpost        = "Other material in this repository" present
full recursive tree    = verified (13 tracked files == 13 files on disk)
untracked files        = none under 00_CURRENT_SURFACE (no partial-move risk)
destination collision  = none
do-not-move paths       = all confirmed present after move (README.md, quick_reference.md, test/,
                          worksheet/, examples/, glossary.md, method/, falsifiers/, tools/, Research/,
                          01_BOOK_DRAFT/, 02_ME_BOOK_PUBLICATION_TRACK/, PUBLICATION_STATUS.md,
                          CHANGELOG.md, CONTRIBUTING.md, LICENSE)
```

## Not yet approved (unchanged)

```text
01_BOOK_DRAFT/ME_BOOK_v0_1/ -> 99_ARCHIVE/superseded_book_draft/ME_BOOK_v0_1/
```

Book material requires explicit Mark confirmation before moving. Not moved in this pass.
`02_ME_BOOK_PUBLICATION_TRACK/` is active and was not touched.

## Application note

The earlier connector-only view could not expose a full recursive file tree, so the move was deferred. This pass was run against a local git clone, where the full tree was verified and the move was performed atomically with `git mv`. That blocker is resolved for this path.

Status: applied and committed on branch `repo-hygiene-archive-audit-2026-07-01`. PR #27 left as draft; not marked ready; not merged.
