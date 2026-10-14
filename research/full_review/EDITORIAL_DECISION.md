# Complete ME author-review assembly: what changes and what does not

Codex Windows proposal under COM #798 task 6152617720. Source-only v0.9 research
assembly, not a released v0.9 book, not a rewritten Mark-authored manuscript.

Open `author_review.html` locally. It needs no server, scripts, account or model.
The book and four existing PNG figures are in this checkout; no new artwork or
private testimony is collected. Start with the book, or choose protection,
formation or the optional compact appendix. TRACE is not a prerequisite.

## Comparative editorial decision

| Existing source | Already accomplished | Decision for this whole candidate |
| --- | --- | --- |
| Released v0.8, e2ef746e931161cb70ac46a4eaa122442134e86b | Complete book, entity-first entrance, full human scenes, four figures, appendices, safety and authorship | KEEP all original text/order. No replacement prose earned |
| PR59, fcb6fd9c5c5ef13e1a6a694c1018ecd15edb26a5 | Approximately 7,668-word new 20-chapter narrative with stronger formation emphasis | KEEP as alternative, not silently select it. Its own custody map leaves figures, full scenes and human note externally; it is not a lossless successor |
| PR63/64, 356b425c / 0f604a71 | Short Workshop-first companion and offline carrier | KEEP optional comparison; do not substitute for the full book |
| PR65, bb0ceb1648b27b331fc3d5a2d9075b6fa337929c | Pinned source consolidation, mathematical limits and cross-lane checks | REUSE custody and tests; no additional theory collection |
| PR66, d5adbf94ca5c55c7cb4bf1cd4436e68f60873132 | Compact plain-English core and five whole cases | OFFER core as a separately attributed optional appendix, after the complete original work |
| PSFH PR820 renderer, d33f4709853c1792d7501603f125eb42da3f1485 | Existing complete-book block renderer | REUSE unchanged block parser/CSS, not the homepage transformation or deployment code |

The PR59 manuscript was inspected as an alternative narrative, with its explicit
adaptation/reference custody warning. Its whole new arc does not justify removing
the original author voice. A second AI paraphrase would add another comparison
burden without established benefit. **NO_DELTA for another rewritten full narrative.**
The product delta here is a complete, navigable, source-preserving author-review
copy that actually contains the original work and optional new core together.

## Chapter-level before/after

`CHAPTER_MAP.json` contains every original section with exact source-line span,
rendered anchor and before/after disposition. All 55 originals are kept in order.
This is byte/source and presentation custody, not proof that every reader receives
the intended meaning.

- **Safety, title and entity-first opening:** kept. Do not prepend the compact
  kernel as an obligatory philosophy or mathematics chapter.
- **Part I — Door:** keep Arthur, Mabel/Tom, Rosa/pharmacist and exit context in
  full, not shortened examples derived from PR59.
- **Part II — Clock:** keep the timing condition, uncertainty, slow harm, Amina
  and historical distinctions. No new deadline or legal/medical interpretation.
- **Part III — Witness:** keep custody, record, residue and the whole two-flats
  scene. Source correspondence is not independent witness or rescue.
- **Part IV — Machine:** keep power, escalation, historical sources, speed and
  correction mechanisms. No simulated goal becomes a real remedy.
- **Part V — Human Standard:** keep competing burdens, practical refusal and
  the explicit limits of the argument. Standing/floors/collision remain open.
- **Part VI — Building:** keep the full Saturday Workshop, refusal costs,
  formation, care, Other Fire, privacy and hope. Creation has a direct navigation
  route alongside protection, but its original text has not been moved or replaced.
- **Author’s note and Appendices A/B/C:** keep every original passage, technical
  boundary, status and historical obligation. Do not impersonate Mark or rename
  the original release statement as evidence of a new release.
- **Only proposed textual addition:** retained compact-core text in an optional
  appendix labelled Codex proposal. Its five cases remain linked research; no new
  claim about an actual tenant, workshop, animal or provider is introduced.

## Mark’s decisions, not conclusions made for him

1. Keep v0.8 alone: this remains a valid outcome; no new edition is necessary.
2. Retain this as an author-review companion, with the core separately labelled.
3. Select a future appendix or a much shorter formation bridge after comparing
   benefit with repetition. Do not silently promote this assembly to v0.9.
4. If a rewritten narrative is wanted, choose particular PR59 passages knowingly
   and reconcile every original scene/figure/note. That work is not simulated by
   this no-rewrite candidate.

The whole-copy review needs fewer source hops than the prior research stack, but
that is an observable packaging difference, not a measured comprehension gain.
No external human reviewers are assumed available or required from Mark in this
task; comprehension and practical advantage remain unknown.

## Source and reader QA

```text
python -m research.full_review.build_reader
python -m research.full_review.build_reader --check
python -m unittest research.full_review.test_reader -v
python -m research.integrated_wave.check_wave
```

Tests verify every original word token in sequence, headings, figures, generated
source equality, local navigation, no scripts/forms/remote assets and clear
authorship boundary, with source/figure and text-loss negative controls. These
are structural checks, not browser geometry, keyboard interaction, independent
human comprehension or field use. Actual browser review must be separately
observed before any visual acceptance claim.

Renderer copy is unchanged Git blob df14757ed2a7b20c5d6dfbcacc49df2fdba34358,
attributed to Build’s PSFH PR820. Only its pure article/CSS helpers are reused.
Its PSFH file paths, produce/main, homepage and publication workflow are not run.
No change to the owned PSFH lane or workaround of its earlier stop is attempted.

No public site, original book/PDF/figure, licence, tag or release changes.
Source-only draft; publisher, human editorial acceptance and publication remain
separate gates.
