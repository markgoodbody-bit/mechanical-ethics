# Portable casebook reader

Open `index.html` in a browser. It includes all twelve Markdown documents from
commit `6f20b3a1927266df5ab38ccd6730ddbb5d9726e7`: chapters, source
receipts and editorial history. Reading and internal navigation work without a
server or connection; external references require a connection. No JavaScript,
telemetry, remote fonts, embedded images or live-status claims are included.

This is a dated v0.1 review snapshot, not a new edition of the frozen book.
Both finite cross-case reviews and CC's narrow legal wording answers are
integrated at this snapshot. Later Markdown changes do not silently update this file.

## Rebuild

With Python 3 and pandoc 3.1.3, run `python casebook/reader/build_reader.py` from
the repository root. The source manifest locks the file list, bytes and hashes.
A changed source stops the build. For a new snapshot, deliberately review and
repin the commit and manifest, then regenerate and check the output. The
manifest verifies source identity; it does not establish factual truth.

## Verification and limits — 26 October 2026

All twelve source files matched their exact GitHub commit readbacks before
rendering. The generated document was checked for unique IDs, all internal
fragment destinations, twelve included articles, no scripts or remote assets,
and deterministic regeneration. The source-change guard was exercised with a
temporary altered copy and rejected it. Original files remained unchanged.

Actual browser testing was attempted using headless Playwright in the Build
workspace. Launch failed because its Chromium executable was absent. No browser
was downloaded, and no desktop or VM controls were used. Therefore visual,
mobile, keyboard and assistive-technology acceptance remain NOT_RUN. Responsive
CSS, focus styling, skip navigation and scrollable tables are implemented;
implementation alone is not a claim that those journeys passed.

No Workshop installation, VM change, hosting deployment or merge is included.

Technical revision: superseded introductory scene and exercises are excluded.
The model sections are authored analysis, not new empirical data.

During this revision, the first build stopped on an editorial note's link to a
superseded exercise. The generator now maps only the two explicitly excluded
historical documents to commit-pinned external sources; unknown unbundled links
still fail. The rebuilt twelve-document edition passed internal-link and
reproducibility checks. These historical links require a connection.
