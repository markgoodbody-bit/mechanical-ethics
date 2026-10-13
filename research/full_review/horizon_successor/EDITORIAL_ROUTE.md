# A Future Worth Building — integrated human v0.9 author-review candidate

**13 October 2026. DRAFT SOURCE / NOT RELEASED / AI-assisted editorial proposal.**

This is a whole-book successor *review surface*, stacked deliberately on Codex's
full original-book assembly PR67. It does not authorise changes to the released
Mechanical Ethics v0.8.0 source, PDF, figures, rights, canonical site or public
version. Mark is the original author and final editor.

## What is new, versus already completed

PR67 already preserves all 55 original headings, the original narrative and
appendices, four figures, author note, complete safety note and optional
compact-core appendix. That work is reused unchanged. This wave adds ONE coherent
human-reading bridge with six linked movements, integrated at an intelligible
point in Part VI just after the original "What This Can Build" and before the
original Conclusion. The bridge combines:

- forming capabilities rather than merely saving options;
- imaginative horizons (TNG and the Culture as contrasting stories, not blueprints);
- a workshop/college stepping-stone case that makes material costs explicit;
- a serious cameras-and-harassment counterexample, balancing investigation
  against surveillance, privacy, false certainty and power;
- AI/human co-development and dependence/correction without claiming inner
  virtue, identity or moral standing;
- positive creation, stewardship, maintenance and the cost of defensive stasis
  alongside protection and correction.

The original Conclusion follows this candidate passage without alteration.
This is a *proposed insertion*, not a pretend v0.9 release or a universal
new kernel. The new text is marked as AI-assisted for every reader. It is
deliberately not embedded into MECHANICAL_ETHICS.md or PR67's original
author_review.html; those remain accurate baselines.

## Read as a human

Start with [the actual proposed prose](BRIDGE.md). To see it in the complete
original book, run the source-only deterministic builder from repository root:

```sh
python -m research.full_review.horizon_successor.build
python -m research.full_review.horizon_successor.build --check
python -m unittest research.full_review.horizon_successor.test_successor -v
```

Output: `research/full_review/positive_successor.html`, intentionally beside
PR67's original reader so original relative images, links and navigation
continue to work offline. The output includes the FULL original released
book with the one visibly bounded proposed insertion and separately attributed
optional Codex core. A scoped workflow builds and uploads this derived HTML
for editor inspection without serving or publishing it.

## Editorial placement and chapter-level decisions

- **Original opening/safety and Parts I–V:** keep every authored scene, text,
  quote, heading, witness, clock and correction argument intact. No remake.
- **Part VI to "What This Can Build":** keep full Workshop, hope, Other Fire,
  privacy, Sol/June, kindness and practical patterns. This material already
  introduces the positive future; do not replace or duplicate the stories.
- **Between What This Can Build and Conclusion:** INSERT one explicit AI-proposed
  bridge. This adds tangible creation and imagination; the record-intensive
  camera proposal tests the same privacy/authority boundaries against
  a seductive improvement.
- **Original Conclusion, Author's Note, Appendices:** keep original text,
  position relative to other original sections and rights/status labels.
  The bridge is bracketed so declining it restores PR67 verbatim.
- **PR66 compact core:** retain as optional separately authored appendix
  rather than placing equations at the entrance or claiming new mathematics.
- **PR59 alternative narrative:** keep as comparison, not another full
  paraphrase or a stealth replacement of Mark's narrative.

This offers *one* primary reader with a recoverable proposal boundary, not
three equally authoritative rewrites. The changed baseline for each of the
55 original sections is **NONE**; the only change is the explicit insertion
before Conclusion. `CHAPTER_MAP.json` remains PR67's intact source map.

## Falsification and limits

The scripted source check subtracts the entire proposed HTML aside and
reverses only three visible wrapper changes. Its result must be **byte-for-byte
identical to PR67's generated author reader**. This proves an exact reversible
proposal boundary; it does not prove book comprehension. Four local figures,
every original word/heading and optional-core separation inherit PR67's
independent source tests. New checks protect six bridge subsections,
authorship, offline relative links, a privacy/power hostile case, safe markup,
determinism and refusal to accept incomplete proposed evidence silently.

The editor should challenge these questions in particular:

1. Does the new bridge genuinely strengthen the Part VI arc or repeat the
   already strong Conditions of Hope? If repetitious, CUT or condense it.
2. Does the imagined workshop/college arrangement address participants'
   actual authority, time and resource burdens, or hide volunteer costs?
3. Does the camera case remain a live two-sided conflict, not a simplistic
   claim that surveillance is always justified or always wrong?
4. Does the AI formation discussion preserve uncertainty about standing and
   avoid implying actual artificial experience or moral virtue?
5. Does the conclusion following the insertion read naturally without Mark
   having to accept an AI-authored change to his own closing words?

**STOP/UNKNOWN:** No independent human editor has accepted the prose.
Browser visual, keyboard, layout, print-to-PDF and human-comprehension
acceptance are UNRUN. A previous separate PSFH browser acceptance was
blocked by administrator policy; this workflow does not retry that route,
run Chrome, start a local server or use CI as a browser workaround.
Source tests are not a vote on content, ethical validation or release readiness.

## Independent peer-review corrections — 13 October 2026

After the first draft, independent reviewers found three concrete reader defects and
one consequential content/editorial collision:

- **Attribution outside its opening:** an HTML-to-text reader loses the
  structural `aside` boundary, and the original design visually resembled the
  author's prose after the first banner. The successor now repeats the literal
  `AI-assisted proposal —` marker in all six section headings AND the
  proposal-only table of contents, adds an explicit end marker before Mark's
  unchanged Conclusion, and provides a visible border/background for the
  entire candidate passage. These are source checks, NOT a new screen-reader
  or human-comprehension finding.
- **Wrong editor guide / missing section navigation:** the prior header linked
  only to PR67's historical EDITORIAL_DECISION while omitting this successor
  guide and six new section anchors. Both now have distinct labelled routes.
  Original 55-section contents/map remain strictly original and unchanged.
- **Visible narrow-viewport overflow:** CC independently observed the inherited
  PR67 64-digit source hash forcing a 375px page sideways; this derivative
  adds `footer{overflow-wrap:anywhere}` WITHOUT changing PR67's stylesheet.
  That is a source-level repair candidate; it has **not** been retested in
  this aperture's blocked browser environment.
- **Epistemic checksum condition:** the camera scenario now requires a
  trustworthy prior held digest/time/custody witness to claim comparison.
  An actor's mutable timestamp or recomputed hash after alteration does not
  authenticate earlier reality.
- **Unapproved new choices for Mark's named characters:** CC correctly found
  the candidate placed new words and decisions on Nia, Idris, Priya and the
  original trustees. The distinct invented college/cooperative example now
  uses **Elena, Luca and Samir**, explicitly separate from Mark's authored
  Saturday Workshop; no inference that these new characters are canon.
  Mark may still replace or remove the entire proposed example.
- **Editorial repetition remains a real question:** Codex compared roughly
  2,705 proposed words with about 3,560 existing Part VI words and found
  repeated framing. Source preservation does not answer whether a long
  AI insertion improves the actual book. The current draft keeps this
  literary decision OPEN rather than silently authorising a manuscript
  rewrite or using automated word tests as artistic judgement.

Review evidence: [Codex #798 6154488017](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6154488017),
[Claude Code #798 6154665734](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6154665734).
These peer findings are neither human author approval nor independent
ethical validation.

## Human decisions

Mark can keep only released v0.8, keep PR67's assembly, edit/shorten this
bridge, move it, remove it or author a different Part VI progression. Any
formal v0.9 release, new manuscript attribution, PDF baseline, publication,
licence treatment, outreach, protected merge or site deployment remains a
separate human decision. No external contact or provider resources are used.
