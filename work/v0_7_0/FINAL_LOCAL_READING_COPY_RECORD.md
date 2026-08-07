# Mechanical Ethics v0.7.0 — verified local reading copy record

## Status

```text
LOCAL_READING_COPY
CC_REVIEW_INTEGRATED
NOT_REPOSITORY_BASELINE
NOT_RELEASED
NOT_CANON
NOT_VALIDATED
NOT_PUBLICATION_READY
```

The frozen v0.6.3 source and PDFs on `main` are unchanged. This record preserves the result of local editorial and PDF work; it does not add the v0.7.0 source or PDF to the repository.

## Source

```text
file: MECHANICAL_ETHICS_HUMAN_READER_v0_7_0_CC_INTEGRATED_WORKING_CANDIDATE.md
SHA-256: b4c78b46aaf8aa3e8d2df5ddf2915cdd52aff77b170802fd6956e2bd6e631fff
words: 13,752 by whitespace split
frozen v0.6.3 words: 13,851
delta: -99
```

## Reading-copy PDF

```text
file: Mechanical_Ethics_v0_7_0_CC_INTEGRATED_READING_COPY.pdf
SHA-256: b42dc5f244871e0787c980f820ac0cf30a945dabc268a1c400b8ada52b4ed43d
size: 583,095 bytes
pages: 34
geometry: all A4
```

## Toolchain

```text
Python 3.13.5
Pandoc 3.1.11.1
WeasyPrint 68.0
```

The reproducible build retains the source, CSS, build script, four figure assets, manifest, verification record, and generated PDF.

## Verification

- All 34 pages rendered with Poppler at 200 DPI.
- All 34 pages rendered with PDFium at 144 DPI.
- The corrected Conclusion equation page was inspected in both renderers.
- All four figure captions occur once.
- No extracted word box exceeds page bounds.
- No raw TeX, MathML annotation, or unconverted dollar expression remains.
- Contents includes `The Door Out` and `When One Case Is Not Enough`.
- The CC-retained distributed-responsibility paragraph is present.
- The appended second closing and asserted collective inspection right are absent.

## Render defects found and repaired

1. Contents chapter numbers resetting to `1`.
2. The last `Door Out` sentence orphaned on another page.
3. Conclusion equations exposing raw TeX/MathML annotations.
4. The Saturday Workshop heading orphaned on an otherwise blank page.

The long Workshop scene now splits across pages 25–26 with its heading and opening together.

## CC route

```text
COM task: ME-V070-CC-001
COM issue: markgoodbody-bit/COM#34
CC return comment: 5216186980
CC-reviewed head: baa179d9ca8c096f48f608f6f301deca63526b6f
Framework integration decision: comment 5216210790
```

CC returned `NARROW`: retain distributed responsibility, narrow meaningful exit and collective correction, and discard the appended human closing. Agreement is not validation; CC identity/model/provider fields remain self-reported.