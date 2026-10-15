# Two Clocks v3: one editorial alternative

Human brief: [COM828 c6194754841](https://github.com/markgoodbody-bit/COM/issues/828#issuecomment-6194754841). Aim: retain v2's clarity while making the diagram less austere, without adding information.

[v2 beside v3 at equal width](v2-v3-equal-width.png) · [editable SVG](two-clocks-v3.svg) · [colour PNG](two-clocks-v3.png) · [neutral monochrome](two-clocks-v3-mono.png) · [caption, accessible alternatives and art direction](art-direction.md).

Both drawings retain ten label words at 126mm intended width. v3 uses regular serif event labels, italic row labels in one aligned column, consistent upper baselines, a restrained copper shared-event mark and fine rounded rules. No decorative motif, extra legend or warning panel. The smallest type is unchanged, approximately 11.91pt; v3 is 59.5mm high against v2's 54.6mm. Caption and mechanics are unchanged. This is a preference candidate, not a finding that beauty or comprehension improved.

## Reproduce with installed tools

`node render.mjs` using existing Sharp (or set `SHARP_MODULE` to its installed path), then `python -X utf8 check_and_compare.py --verify-sources` using existing Pillow and GitHub read access for the optional immutable-source check. After first proofs exist, add `--repeat-render --node PATH_TO_EXISTING_NODE` to check identical repeated output. The script preserves/validates PR76 original and PR77 v2 hashes, checks Georgia regular/italic text bounds, diagram geometry and five negative controls, then makes the equal-width comparison and receipt. No new PDF, browser, installation, external asset, provider call or font-file distribution.

Working fonts: installed Georgia/Georgia Italic, not a claimed final publication selection. SVGs remain live editable text; fallback/platform rendering must be checked at actual production. See checks.json for full hashes and honest untested limits. Mark retains the art decision. Build's literary calibration and the unchanged DEV2 master remain separate.
