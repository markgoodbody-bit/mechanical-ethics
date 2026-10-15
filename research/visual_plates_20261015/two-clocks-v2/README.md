# Two Clocks: sparse v2 candidate

Responds to human feedback in [COM828 c6194085474](https://github.com/markgoodbody-bit/COM/issues/828#issuecomment-6194085474). This is one alternative figure, not another book proof. The original three-plate set, PR76 and Build's A4 PDF remain unchanged.

Start with [the actual before/after at equal width](before-after.png), then [the editable SVG](two-clocks-v2.svg), [colour PNG](two-clocks-v2.png) or [neutral monochrome PNG](two-clocks-v2-mono.png). The before image is cropped from the exact reviewed A4 page 3, not recreated from a different font or enlarged screenshot. Only the existing public diagram region is included, not the private book prose.

The alternative removes the repeated heading, bold labels, acknowledgement, duplicate explanation and UNKNOWN card. It retains six regular labels at a **larger** intended size (11.91pt rather than 10.32pt at 126mm width), one start, two tracks, actual-payment dots and separate loss ticks. Graphic height falls from 106.4mm to 54.6mm. Labels are reduced, not shrunk. The [editorial note](editorial-note.md) supplies a two-sentence book caption, accessible alternatives and an explicit account of the precision that remains in the body.

## Reproduce with existing tools only

Run `node render.mjs` with existing Sharp available (or point `SHARP_MODULE` to its installed module directory). Then `python -X utf8 verify_and_compare.py --before-pdf PATH --verify-sources` with installed Pillow, pdfplumber and pypdfium2, plus existing GitHub read access for the optional source check. The source-PDF hash must match `80fce3d8640bb12b4f561aed729aafbaf07f4cd6f77dc3a58d156bde6a460646`, otherwise comparison stops. No PDF is authored or modified. The local default is the already-downloaded exact review copy.

The [check receipt](checks.json) records extraction, geometry, negative controls, bounds, original preservation and exact file hashes. Rendering uses installed Arial as a working proof; no final-font claim or font distribution. The source SVG and PNGs are user-viewable without a local server. No browser-policy workaround or dependency installation.

## Stop

Optional human-review candidate. No insertion into DEV2, new page-3 typesetting, main merge, release, hosting, provider use or spend. Physical print, actual comprehension, assistive technology and final approval remain untested. Mark chooses whether this is the right direction; Build's prose calibration continues separately.
