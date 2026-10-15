# Harmonised companion plates — optional

One paired proposal for [COM828 c6195256238](https://github.com/markgoodbody-bit/COM/issues/828#issuecomment-6195256238), following the provisionally preferred v3 Two Clocks direction. No further timing redesign or book-master edit.

Start with [the equal-width before/after contact sheet](before-after.png). New editable sources: [Who draws the map?](who-draws-the-map.svg) and [Growing room](growing-room.svg). Each has colour, neutral monochrome and 714px book-width PNGs. See [captions, long descriptions and placement advice](captions-and-placement.md) and checks.json for exact evidence/limits.

The map separates the authored account from the visitor's consequence and brings both towards review without showing a verdict. Growing room uses unboxed original line vignettes, a child and adult, the repeated room/glass/pot, a different plant and continuing upkeep. It remains a schematic drawing, not a claim of accomplished learning or finished commissioned narrative art.

## Reproduce

Use existing Sharp with `node render.mjs` (or point `SHARP_MODULE` to its installed path), then existing Python/Pillow with `python -X utf8 check_and_compare.py --verify-sources`. After first rendering, use `--repeat-render --node PATH_TO_EXISTING_NODE` for byte-identity checks. The source check uses existing GitHub read access; no credentials are printed. No package/font install, browser, PDF or external asset required.

The original two PR76 plates and Two Clocks v3 are hash-checked and untouched. New assets are 126mm wide; text remains regular Georgia/Georgia Italic at approximately 11.91pt minimum. Source paths/hashes in the preserved source-map.json remain edition-specific. Build may use these if they aid the current chapter and are explicitly marked optional, or finish the book without them. The human editor has not approved these plates or any final placement.
