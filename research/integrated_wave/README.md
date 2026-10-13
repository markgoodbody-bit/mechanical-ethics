# ME v0.9 integration wave — a consolidated review candidate

13 October 2026. Codex Windows, under [COM major-wave dispatch](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6151183484).

This checkout brings the existing mathematics, executable cases, editorial
judgements and human companion into one reviewable source package. The complete
released **ME v0.8 book remains the human baseline**, with all original figures,
PDF, safety note, author note and history. The new material is research alongside
that book, not a quietly substituted edition. TRACE v0.4 remains a separate work.

## What changed, and what did not

Before: separate branches required reviewers to reconstruct the relationship
between a policy enumerator, a journalled game, a simultaneous-tick lab, a
mathematical reference and several competing human openings.

After: those owner sources are assembled unchanged in one isolated draft branch,
with an explicit selection/contradiction map, cross-lane seam tests and one
repeatable custody/regression entry point. Git ancestry retains each contributor;
the custody check compares actual working-file blobs, not just section headings.

No existing algorithm or released text was rewritten. No claim that combining
these sources validates them. No release, public website, provider call or human
participant is part of this package. The complete PR59 alternative manuscript is
an external editorial comparison, not silently adopted as the book.

## Read in this order

1. [Complete released book](../../MECHANICAL_ETHICS.md). Start with its entity-first
   opening, Leah/Mia, timing, and Part VI; retain the original voice and scenes.
2. [Consolidated architecture and decision map](ARCHITECTURE.md). This selects the
   defensible kernel and identifies discrepancies instead of averaging them away.
3. [Framework editorial reconciliation](../ME_V0_9_HUMAN_EDITORIAL_RECONCILIATION_FW_20261013.md).
   It proposes a short formation bridge rather than another complete rewrite.
4. [Optional short offline human companion](../offline_review/human_review_offline.html).
   This is the Build PR63/64 Workshop-first alternative, not the full book.
5. [Claude mathematical reference](../ME_V0_9_MATH_KERNEL_CC.md), then the relevant
   executable case. Readers do not need to run a solver to understand the book.

The archaeology and retention maps are supporting custody, not mandatory reading
for a person with an urgent practical problem.

## One integrated source check

From this Git checkout, Python 3.10+ and Git, no dependency install:

```text
python -m research.integrated_wave.check_wave
```

The check verifies every released file against v0.8 and every selected research
carrier against its immutable owner head, then runs the five existing suites,
integration seam tests, three negative-control scripts and deterministic HTML
generation check. It stops on source mismatch, failure or timeout. The pinned Git
objects must be present; a shallow/exported copy may return custody UNKNOWN.
Untracked files are not an authenticated part of custody. Git filters are applied
so Windows CRLF does not manufacture a source-drift allegation.

The three inherited mutation scripts have different detection criteria. Navigator
and Claude count test failure or exception; the game requires assertion failures.
Their results must remain separately reported, not pooled into an invented
universal mutation score. Browser, field, outsider-use and bibliographic checks
are separate, not reproduced by this command.

## Review and release gates

This is a **defensible source consolidation**, not a finished v0.9 replacement
manuscript. A whole successor still needs human editorial selection and semantic
retention review; byte preservation of v0.8 proves it remains available, not that
a compressed companion carries every meaning.

Wave-level peer review should challenge the concrete choices in ARCHITECTURE:
whether the kernel preserves positive formation and ordinary low-reserves cases;
whether any claimed remedy has operational evidence; whether standing/collision
or floors were smuggled in; whether scale transfer preserves the property at
issue; and whether the extra machinery buys anything over ordinary thought.
The strongest valid outcome may be to keep v0.8 and publish no successor.

Earned result: one traceable source package and reproducible checks.
Provisional idea: the short formation bridge may make an existing distinction
easier to find. Wording improvement: epistemic guarantee and actual-world
hardening are explicitly separated. Process improvement: owners remain visible
while review no longer requires navigating several stacks. Unresolved problem:
normative foundation, practical benefit, reader burden, and legitimate release.
