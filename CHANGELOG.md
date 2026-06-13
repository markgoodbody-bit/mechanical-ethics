# Changelog

## 2026-06-13 — Gemini/Grok pruning pass

Applied the convergent review finding from Gemini and Grok: the diagnostic core is useful, but the repository presentation had become overbuilt.

Removed duplicate or over-expansive material:

- `START_HERE.md`
- `faq.md`
- `SCOPE.md`
- `method/how_to_apply_honestly.md`
- `guides/README.md`
- `guides/ai_governance_use.md`
- `guides/design_patterns.md`

Updated:

- `README.md` to become the single front door and cut the repo-map/syllabus structure;
- `quick_reference.md` with plainer terms: decision, too-late point, actual fix mechanism;
- `test/correction_window_test_v0_1.md` to harden the actual-fix-mechanism requirement;
- `docs/index.md` to remove dead links and bloat;
- `method/README.md` to remove obsolete links;
- `PUBLICATION_STATUS.md` to reflect the pruned state.

Current rule:

- Stop adding files.
- Refine only the test, worksheet, and examples if doing so makes the diagnostic clearer.

Still not claimed:

- validated framework;
- reliability-tested instrument;
- complete ethics framework;
- AI governance framework;
- complete AI-alignment solution;
- full repair-capacity measurement;
- external review completed.

## 2026-06-13 — Claude private-build architecture batch

Applied the remaining high-value recommendations from Claude's private-build architecture pass while preserving the v0.1 claim ceiling.

Added:

- `SCOPE.md`
- `method/how_to_apply_honestly.md`
- `method/README.md`
- `examples/live_protection_payment_hold.md`
- `examples/after_the_fact_hiring_rejection.md`
- `examples/unknown_private_scoring.md`

Updated:

- `test/correction_window_test_v0_1.md` with quick distinction rules for working labels;
- `README.md` with scope, honest-use, and category-example navigation;
- `START_HERE.md` with category examples and scope route;
- `examples/README.md` with working-label coverage;
- `docs/index.md` with scope, honest-use, and category-example links;
- `PUBLICATION_STATUS.md` with architecture-batch status.

Removed:

- `LICENSE_PENDING.md`, now obsolete because `LICENSE` exists.

Current category coverage:

- LIVE PROTECTION — payment hold with live challenge;
- PARTIAL / mixed — benefits suspension or recovery;
- AFTER-THE-FACT REVIEW — hiring rejection after role filled;
- FALSE SAFEGUARD — dashboard without a brake;
- UNKNOWN — private risk scoring with missing records.

Still not claimed:

- validated framework;
- reliability-tested instrument;
- complete AI-alignment solution;
- full repair-capacity measurement;
- external review completed.

Recommended stop condition:

- re-read the whole repo as a stranger before adding more files.

## 2026-06-13 — License and crisp-example patch

Applied the main fixes from Claude Opus second-pass review.

Added:

- `LICENSE`
- `examples/full_worksheet_false_safeguard_dashboard.md`

Updated:

- `README.md` to link both a cautious full worksheet example and a crisp false-safeguard example;
- `START_HERE.md` to include both full examples;
- `examples/README.md` to list both full examples;
- `PUBLICATION_STATUS.md` to remove license as a blocker and mark the repo ready for a small public feedback post within the v0.1 claim ceiling.

Still not claimed:

- validated framework;
- reliability-tested instrument;
- complete AI-alignment solution;
- full repair-capacity measurement;
- external review completed.

Remaining:

- GitHub Pages may still need enabling;
- ICO FOI/EIR CSV and source notes not yet published;
- DOI not issued.

## 2026-06-13 — Stranger-usability expansion

Expanded the public repo while preserving the claim ceiling.

Added:

- `quick_reference.md`
- `glossary.md`
- `faq.md`
- `guides/README.md`
- `guides/ai_governance_use.md`
- `guides/design_patterns.md`
- `examples/full_worksheet_benefits_suspension.md`
- `review_requests/claude_opus_front_door_review.md`

Updated:

- `README.md` with reader paths and expanded navigation;
- `START_HERE.md` with the quick-reference/full-example route;
- `examples/README.md` to identify the full worksheet example as the best first example;
- `docs/index.md` to match the expanded front door;
- `PUBLICATION_STATUS.md` to reflect the expansion and next review path.

Still not claimed:

- validated framework;
- reliability-tested instrument;
- complete AI-alignment solution;
- full repair-capacity measurement;
- external review completed.

## 2026-06-13 — Public front-door cleanup after outside review

Applied front-door cleanup after hostile outside-reader review.

Changed:

- removed `Mechanical_Ethics_v14_trade.pdf` from repository root;
- changed README title to lead with `Correction Window Test v0.1`;
- added a direct worked-example link near the top of the README;
- removed the empty ICO data folder from the README repository map;
- removed private method shorthand from the README front door;
- changed `Result categories` to `Working result labels` in the test;
- removed the notation block from the public test page;
- added `examples/README.md`;
- added issue templates for applying the test and reporting front-door defects;
- updated publication status.

Remaining:

- license still pending at that point;
- GitHub Pages may still need enabling;
- ICO FOI/EIR CSV and source notes not yet published.

## 2026-06-13 — Public front-door rebuild

Initial public rebuild of `markgoodbody-bit/mechanical-ethics` around the Correction Window Test v0.1.

Added:

- `README.md`
- `START_HERE.md`
- `test/correction_window_test_v0_1.md`
- `worksheet/correction_window_worksheet_v0_1.md`
- worked examples for hiring AI, benefits suspension, medical prioritisation, and agentic AI write access
- method and caveat notes
- falsifiers
- ICO FOI/EIR data-surface placeholder
- draft GitHub Pages landing page
- contribution guide
- publication status note
- license pending note

Claim ceiling:

- public diagnostic only;
- no validation claim;
- no reliability-tested instrument claim;
- no AI-alignment-solved claim.

Next intended action:

- add source-checked ICO FOI/EIR data and source notes, or explicitly park that surface.
