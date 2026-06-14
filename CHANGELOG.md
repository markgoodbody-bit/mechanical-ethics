# Changelog

## 2026-06-14 — Structural boundary cleanup after Gemini review

Applied the remaining public-readiness patch after Gemini identified structural boundary leaks.

Changed:

- Created `Research/AI_Deployment/` as the clean research-layer path.
- Created `Research/AI_Deployment/ME_TRACE_AI_Deployment_Notes_v0_1.md` as the clean filename for the unpromoted AI deployment note.
- Removed the old alignment-labelled top-level research entry points.
- Removed old alignment-labelled toy-case, self-score, blind-review, and comparator scaffolding files from the public repo path that were no longer needed for the v0.1 public diagnostic surface.
- Created clean example filenames:
  - `examples/partial_protection_benefits_suspension.md`
  - `examples/false_safeguard_dashboard_without_brake.md`
- Removed old scaffold-style example filenames.
- Updated root `README.md`, `examples/README.md`, and `PUBLICATION_STATUS.md` to point at the clean public surface and research-layer boundary.

Boundary preserved:

- Public front door remains the root `README.md`.
- Public object remains the **Correction Window Test v0.1**.
- Research-layer AI deployment notes are machine-room material only.
- No validation claim is made.
- No reliability-tested instrument claim is made.
- No AI-governance framework claim is made.
- No AI-alignment solution claim is made.
- No decision-advantage claim is made for ME/TRACE over ordinary safety reasoning.

Stop condition:

- Do not add new examples, theory files, public pages, issue templates, or review prompts in this pass.
- Change the public diagnostic again only if worksheet use shows the test itself needs sharpening.

## 2026-06-14 — Boundary hygiene pass after external audit

Applied a narrow public-readiness patch after hostile-but-constructive external audit.

Changed:

- `README.md` states that the repository publishes one narrow diagnostic from the broader Mechanical Ethics / TRACE work and is not the framework itself.
- `README.md` distinguishes the five checks from the five result labels.
- Public example label wording uses **PARTIAL PROTECTION** consistently.
- `PUBLICATION_STATUS.md` states that unpromoted research-layer notes are not part of the v0.1 public diagnostic surface.
- The AI deployment research note was rewritten in plain English and marked as machine-room material only.

## 2026-06-13 — Pruning and public-front-door stabilization

Applied convergent external review findings that the diagnostic core was useful but the repository presentation had become overbuilt.

Removed duplicate or over-expansive material, including extra start pages, FAQ/scope pages, guides, review prompts, issue templates, Pages drafts, archive material, and placeholder data surfaces.

Updated:

- `README.md` to become the single public front door;
- `quick_reference.md` with plainer terms: decision, too-late point, actual fix mechanism;
- `test/correction_window_test_v0_1.md` to harden the actual-fix-mechanism requirement;
- `examples/README.md` to cover all five working labels;
- `method/README.md` to remove obsolete links;
- `PUBLICATION_STATUS.md` to reflect the pruned state.

Still not claimed:

- validated framework;
- reliability-tested instrument;
- complete ethics framework;
- AI governance framework;
- complete AI-alignment solution;
- full repair-capacity measurement;
- external review completed.

## 2026-06-13 — Public front-door rebuild

Initial public rebuild of `markgoodbody-bit/mechanical-ethics` around the Correction Window Test v0.1.

Added the root README, test, worksheet, examples, method notes, falsifiers, publication-status note, and reuse licence.

Claim ceiling:

- public diagnostic only;
- no validation claim;
- no reliability-tested instrument claim;
- no AI-alignment-solved claim.