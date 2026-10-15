# Three visual plates — optional v1.0 review candidates

Original vector design for COM828 task `CODEX-ME10-THREE-VISUAL-PLATES-20261015` (comment 6192355018). These are **conceptual diagrams**, not finished narrative illustrations, not a new theory, and not manuscript insertions. Mark selects art direction; Framework owns interpretation/placement; Build owns DEV2 prose. The three diagrams have no borrowed assets, outside clipart, external fonts, raster tracing or model-provider calls.

Before: concepts existed in the text and in a proposed visual memo, without actual plates.
After: three editable SVG candidates, colour and monochrome PNGs, a contact sheet, captions and long descriptions, source anchors, and reproducible checks. No manuscript text changes. The later UK English/A4 brief is reflected in the style sheet and provisional ink/teal palette; this handoff contains figure assets, not a new PDF or locked book design.

## Review

- [Three-plate contact sheet](contact-sheet.png)
- [Two clocks](01-two-clocks.svg) · [PNG](01-two-clocks.png) · [monochrome](01-two-clocks-mono.png)
- [Who draws the map?](02-who-draws-the-map.svg) · [PNG](02-who-draws-the-map.png) · [monochrome](02-who-draws-the-map-mono.png)
- [Growing room](03-growing-room.svg) · [PNG](03-growing-room.png) · [monochrome](03-growing-room-mono.png)
- [Captions, long descriptions and falsifiers](captions.md)
- [One-page visual specification](style-guide.md)
- [Exact edition/source map](source-map.json)
- [Generated verification receipt and hashes](checks.json)

View source SVGs directly or PNGs; no browser/server is needed for the delivered raster review. No browser restriction was bypassed. The PNG width is 1488px, approximately 300dpi at the SVG's intended 126mm book width. A 714px-wide review copy simulates 144dpi display sampling at that width; this is not a physical print or reader study. SVG text is real editable text, with title/description alternatives. Font rendering can change if Arial/Helvetica is unavailable: re-render on the publication system before use.

## Reproduce without installation

1. Run `python -X utf8 make_plates.py` with an existing Python 3 runtime.
2. Run `node render.mjs` with an existing Sharp installation resolvable by Node, or set `SHARP_MODULE` to that existing module's path.
3. Run `python -X utf8 test_plates.py` with existing Pillow. It verifies SVG safety, labels/bounds with installed Arial, source-custody anchors (optional live `--verify-sources`), semantic geometry invariants, exact regenerated SVGs and raster metadata/hash stability.

No dependency installer is invoked. Windows review used bundled Python 3.12.14 / Node / Sharp plus installed Arial. Font files are not copied. A publisher should check its own font licences and final output; this project does not determine rights for a future edition.

## Stop rule / limitations

Optional review candidates only. No automatic insertion, public host, book release, protected merge, outreach or spending. The timeline is deliberately unscaled and synthetic: its geometry encodes ordering, not measured durations or a known case. A challenge route is proposed, not established safe/usable or shown to deliver a remedy. The third plate depicts one possible development, not an efficacy result. The diagrams do not replace the surrounding qualifications. Actual novice comprehension, assistive-technology use, physical printing and WCAG/PDF-UA conformance remain untested. Reconcile edition-specific captions against DEV2 at placement; do not silently carry DEV1 references into a changed edition.
