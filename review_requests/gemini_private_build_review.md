# Gemini Private-Build Review Request

Please review this public GitHub repository as a private build pass, not a launch review:

https://github.com/markgoodbody-bit/mechanical-ethics

## Context

The current object is **Correction Window Test v0.1**.

It is a practical diagnostic asking whether a safeguard can correct a harmful error before the consequence becomes hard to reverse.

The author does **not** want public feedback yet and is not asking whether to post it publicly. Treat this as private architecture, structure, and discipline review.

## Claim ceiling

Do not treat the repository as:

- a validated framework;
- a reliability-tested instrument;
- a complete ethics framework;
- an AI alignment solution;
- a finished governance methodology;
- evidence that Mechanical Ethics / TRACE is proven.

The allowed claim is narrower:

> The Correction Window Test is a v0.1 diagnostic for checking whether safeguards can correct harmful errors before consequences harden.

## Your review stance

Please be hostile but useful.

Focus on:

- repo architecture;
- stranger navigation;
- scope control;
- bloat risk;
- category coverage;
- worked-example quality;
- claim ceiling leaks;
- whether files sharpen the diagnostic or merely enlarge the project.

Do not praise the ambition. Do not recommend public posting. Do not rewrite the whole theory.

## Files to inspect first

Start with:

- `README.md`
- `SCOPE.md`
- `quick_reference.md`
- `test/correction_window_test_v0_1.md`
- `examples/README.md`
- category examples under `examples/`
- `method/how_to_apply_honestly.md`
- `falsifiers/falsifiers.md`
- `guides/ai_governance_use.md`
- `guides/design_patterns.md`

Flag anything you cannot access or verify.

## Review questions

1. Does the repo still work as a 60-second public front door, or has it become too large?
2. Does `SCOPE.md` adequately control the claim ceiling?
3. Does the README route a stranger well, or is it now over-supplied?
4. Do the five working-label examples genuinely clarify LIVE, PARTIAL, AFTER-THE-FACT, FALSE SAFEGUARD, and UNKNOWN?
5. Which example is weakest and why?
6. Is the distinction between PARTIAL and AFTER-THE-FACT clear enough?
7. Does `method/how_to_apply_honestly.md` add discipline or duplicate other files?
8. Do the AI governance and design-pattern guides imply more operational readiness than the evidence supports?
9. What should be cut, merged, renamed, or moved to archive?
10. What should be added next, if anything?
11. What should definitely not be added yet?
12. What is the biggest bloat or theory-creep risk?

## Please end with

A. Verdict on private-build state

B. Strongest file

C. Weakest file

D. Biggest overclaim or ceiling leak

E. Biggest usability defect

F. One file to cut or merge

G. One file to improve first

H. One missing worked example, if any

I. Recommended next commit batch, capped at no more than 5 files

J. Stop condition before adding more

## Required discipline

If the repo is already sufficient for the current object, say so.

If adding more would make it worse, say so.

Treat repo growth as a cost, not a sign of progress.
