# Start Here

This repository is a public front door for a practical diagnostic from the Mechanical Ethics / TRACE project.

Start with one question:

> If this system is wrong, can the affected person get correction before the consequence hardens?

That question is the **Correction Window Test**.

## What to read first

1. [`quick_reference.md`](quick_reference.md) — shortest usable version.
2. [`examples/full_worksheet_benefits_suspension.md`](examples/full_worksheet_benefits_suspension.md) — a complete filled worksheet.
3. [`test/correction_window_test_v0_1.md`](test/correction_window_test_v0_1.md) — the test itself.
4. [`worksheet/correction_window_worksheet_v0_1.md`](worksheet/correction_window_worksheet_v0_1.md) — fill this in for a real system.
5. [`faq.md`](faq.md) and [`glossary.md`](glossary.md) — common questions and terms.
6. [`method/method_and_caveats.md`](method/method_and_caveats.md) and [`falsifiers/falsifiers.md`](falsifiers/falsifiers.md) — limits and failure conditions.

## The shortest usable version

A safeguard is only live protection if:

1. the affected person or a legitimate proxy can detect the problem;
2. they have a route to challenge it;
3. the route has authority and resources;
4. the system can pause, reverse, or repair the action;
5. this can happen before the consequence becomes practically irreversible.

If those conditions are absent, the safeguard may still be documentation, review, audit, or after-the-fact accountability. But it should not be described as live protection.

## How this connects to AI

AI systems do not need to be conscious, human-like, or malicious to matter.

They matter when their outputs enter the world as selections: rankings, classifications, recommendations, generated code, risk scores, summaries, flags, refusals, approvals, or actions.

The Correction Window Test asks whether the correction machinery is fast, strong, and accessible enough for those selections.

For AI-specific use, read [`guides/ai_governance_use.md`](guides/ai_governance_use.md).

## How this connects to public services

Public systems often contain formal appeal or complaint routes. The test asks whether those routes can still change the affected person's future in time.

An appeal after eviction, destitution, job loss, medical delay, credit damage, or evidence loss may still matter. It is not the same as live protection.

## How this connects to design

A weak safeguard often has a name but no carrier.

A stronger safeguard usually has notice, evidence access, pause power, reversal power, corrector deadlines, and a route the affected person can trigger.

For design guidance, read [`guides/design_patterns.md`](guides/design_patterns.md).

## Current build status

This is a public v0.1 diagnostic.

The repository now contains:

- a quick reference;
- the test;
- a worksheet;
- a full filled example;
- shorter worked examples;
- AI governance guidance;
- design patterns;
- FAQ and glossary;
- method notes and falsifiers.

Do not treat this repository as proof that the wider framework is correct.
