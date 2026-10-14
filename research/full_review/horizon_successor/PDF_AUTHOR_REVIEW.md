# Mechanical Ethics — direct author-review PDF (Option B)

**14 October 2026 · unreleased draft · source/product review, not an edition decision**

This deliverable answers [Framework's explicit COM #798 PDF dispatch](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6167273330). Mark asked for an immediately readable **complete book PDF**, produced by the Build aperture rather than the Campfire lead.

## Concrete author reading result

Build assembled a **63-page direct PDF** in its working container and handed the PDF file to Mark in the ChatGPT conversation: `Mechanical_Ethics_Concise_B_Author_Review.pdf`. It is not a public-site URL or a released version. This file is a conversation attachment; GitHub cannot resolve its `sandbox:/` address. Do not infer that a repository-hosted PDF artifact exists from this note.

- **Original source:** full 57-page released v0.8.0 PDF, SHA256 `e9ca37b249b4d915b18e954b6c72ebd999ae4be8ceed2c0aaf395922d0c6b56f`; original Markdown SHA256 `e3267c3e41e7fdfb44c9a9279250a1a7a38d5b9c389a594fef40cfea75fdbe76`.
- **Added content:** one review front page, five B-labelled proposed pages positioned after original `What This Can Build` and before the original `Conclusion`. Proposed source is [BRIDGE_CONCISE.md](BRIDGE_CONCISE.md), SHA256 `0aca01811ac42146841afb193c1b5b06f8c7ce0c271c40b8fdced26c4ac1d067`.
- **Actual handed PDF:** 63 pages; 4 original figures retained; source execution verified every original page's PDF text extraction unchanged; original Conclusion remains the next page after B5. Local PDF SHA256 at final verification: `061c41ec74cbe1fc31dd5311fa8b0d11ba4ba898d69ae0a65054ba224bed949f`.
- **Reading experience:** 6 x 9 inch book geometry, added unambiguous front status sheet, AI-attributed and B-folio proposal pages, preserved original artwork/layout and Contents/page numbering, clickable outline including original sections and B sections.
- **Visual verification:** selected generated pages (cover, original last Part VI, all five proposed pages, original Conclusion and final appendices) were rendered and visually inspected. Full text extraction and all-original-page preservation were checked. This is not independent human comprehension, screen-reader/keyboard testing or print proof.

## Durable source route

[author_review_pdf.py](author_review_pdf.py) is a **source recipe** on draft PR68. Run it from an existing offline Python environment with `reportlab` and `pypdf` already provisioned:

```sh
python research/full_review/horizon_successor/author_review_pdf.py \
  --output /path/to/Mechanical_Ethics_Concise_B_Author_Review.pdf
```

The script accepts the pinned original released PDF and Markdown, inserts only the separately attributed Option B pages, maps original PDF bookmarks to their new page offsets and checks all 57 original PDF pages' extracted text against the result. It refuses a changed original book, changed 57-page boundary, lost proposal heading or absent Conclusion. The source recipe was committed **after** the local direct-PDF build; do not claim a byte-identical GitHub/CI rebuild was observed. The exact local PDF used a Unicode-capable embedded serif font for proposed pages; the repository recipe uses the standard PDF fonts for portability. Appearance equivalence requires a new source build and human review.

**Dependencies:** This recipe does not install packages or run a browser. Do not use GitHub CI or a network package install as a workaround for earlier tool policy refusals. The existing released-PDF builder already uses ReportLab/pypdf; a fully provisioned permitted runner could produce a separately evidenced output and downloadable GitHub artifact in a later authorised wave, but that has not been claimed here.

## Editorial gates

Mark may keep released v0.8 only, accept or rewrite Option B, use the full Option A proposal, or reject both. This PDF is not **Mechanical Ethics v0.9 RELEASED**, not an attribution transfer and not a validation of consequences or moral claims. No release tag, protected merge, hosted source, publication, contact, spending, rights decision or provider state was changed.
