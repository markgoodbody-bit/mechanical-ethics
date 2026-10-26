# Casebook PDF — 26 October 2026

[Download the PDF](https://github.com/markgoodbody-bit/mechanical-ethics/raw/refs/heads/main/casebook/pdf/Mechanical_Ethics_Casebook_2026-10-26.pdf) · [Casebook contents](../README.md) · [HTML reader](../reader/README.md) · [Main book](../../working-editions/v1.0/README.md)

60 A4 pages with selectable text, a linked contents page, PDF bookmarks and external source links. Includes two historical studies, one constructed employment study, comparative analysis, source receipts and editorial history: twelve source documents in all. The subsequently returned GitLab draft is not included.

This is a reading format of the integrated casebook, not a new release of Mechanical Ethics, an amendment to its frozen manuscript, or evidence of field efficacy. Existing repository rights and third-party source rights remain unchanged.

## Exact edition

- Integrated repository anchor: `9f2a2f79118320211c7d62ab22e1ee494afb283f`.
- Underlying twelve-document source snapshot: `0a281d0dd729a0110d5c2c5ecd358502da413821`.
- Preserved HTML input: `source-reader.html`, SHA-256 `e534524f3ea9f2317cbbeacbe27d396ed1d4736cefee8673b31f1fe1cde31a0e`.
- Published PDF: 301381 bytes, SHA-256 `a237befcb01dd6626de90db92968eaa23e6f428d6efa0829f90a77d5b0ec951f`.

The PDF retains the dated source and editorial wording. The online HTML reader may receive newer navigation links; that does not silently change this PDF snapshot.

## Rebuild

Python 3, WeasyPrint 70.0, its platform text-rendering dependencies, and DejaVu Serif/Sans/Sans Mono fonts are required. Install the pinned Python dependency from `requirements.txt`, then run:

```sh
python casebook/pdf/build_pdf.py --output /tmp/Mechanical_Ethics_Casebook.pdf
```

The builder rejects a changed HTML input. It does not fetch remote sources. Exact PDF bytes may depend on font and rendering-library versions; the committed file hash identifies the delivered edition. Regeneration is a document-format operation, not renewed source verification.

## Checks and limits

All sixty pages were rendered and visually inspected in contact sheets, with a full-size table inspection. Contents links, bookmarks and selectable text are present. The first render exposed a stylesheet-precedence conflict; corrected by embedding the final print stylesheet after the reader styles, then rerendered and inspected. No new primary-source research, independent factual audit, screen-reader/PDF-UA acceptance or mobile-browser test was performed.

The repository publication adds download navigation; the three study texts, frozen book, release assets and tags are unchanged.
