# Mechanical Ethics Repo Hygiene / Archive Audit — 2026-07-01

Status: audit scaffold only. No deletion. No theory rewrite.

Branch: `repo-hygiene-archive-audit-2026-07-01`

## Purpose

Clean the public reader path while preserving provenance.

The current repository front door publishes the narrow Correction Window Test v0.1 and explicitly says this is not the whole Mechanical Ethics / TRACE framework. Cleanup must protect that narrow public-facing status.

```trace
repo_hygiene_goal :=
  keep_public_diagnostic_clear
  + protect_book_track
  + preserve_history
  + reduce_reader_confusion
  + no_silent_claim_expansion
```

## Do not move without explicit review

```trace
do_not_move :=
  README.md
  + quick_reference.md
  + test/
  + worksheet/
  + examples/
  + glossary.md
  + method/
  + falsifiers/
  + 02_ME_BOOK_PUBLICATION_TRACK/
```

The book publication track is active. Do not archive live book chapters or current Claude reviews unless Mark explicitly asks.

## Likely archive candidates

These categories are likely archive-only if present and superseded:

```trace
archive_candidates :=
  old_framework_builds
  + superseded_book_drafts_outside_active_book_track
  + old_review_packets
  + deprecated_exports
  + stale relay prompts
  + old combined PDFs
  + prior diagnostics replaced by Correction Window Test v0.1
  + proof/validation-seeming material now demoted
```

## Proposed archive structure

```text
99_ARCHIVE/
  README.md
  old_framework_builds/
  superseded_book_drafts/
  old_review_packets/
  deprecated_exports/
  stale_relay_prompts/
  prior_diagnostics/
  uncertain_do_not_move_yet/
```

## Classification rule

```trace
classification :=
  KEEP_LIVE
  | ARCHIVE_ONLY
  | UNCERTAIN_DO_NOT_MOVE
```

Default to `UNCERTAIN_DO_NOT_MOVE` when provenance, current references, or status are unclear.

## Claude/Fable audit prompt

```text
ROLE: repo hygiene auditor

Repo:
markgoodbody-bit/mechanical-ethics

Task:
Do not review or validate the theory.
Do not rewrite prose.
Do not optimise for neatness over provenance.

The public front door is the Correction Window Test v0.1. The ME book track is active and should not be buried.

Identify which files/folders should remain in the live reader path and which look superseded, duplicate, historical, deprecated, or archive-only.

Return:
1. keep-live list
2. archive-candidate list
3. do-not-move warnings
4. README/front-door defects
5. recommended archive structure
6. anything that looks dangerous to move
```

## Next action

Run an inventory/classification pass before moving files. Do not bulk-archive from memory.
