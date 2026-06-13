# Correction Window Test v0.1

**A safeguard is not real protection unless it can still change the outcome before the harm becomes hard to reverse.**

This repository is a public front door for a small diagnostic tool from the Mechanical Ethics / TRACE project.

The **Correction Window Test** asks a practical question about AI systems, automated decisions, public services, institutions, and governance processes:

> If the system is wrong, can the affected person detect, challenge, and correct the error before the consequence hardens?

This is not a claim that Mechanical Ethics is validated. It is not a complete moral theory. It is not a claim to have solved AI alignment. It is a way to inspect whether a safeguard is live protection or only paperwork after the fact.

## Start here

1. Read the [`quick reference`](quick_reference.md).
2. See a cautious filled worksheet: [`Benefits Suspension or Recovery`](examples/full_worksheet_benefits_suspension.md).
3. See a crisp filled worksheet: [`Dashboard Without a Brake`](examples/full_worksheet_false_safeguard_dashboard.md).
4. Read the [`Correction Window Test`](test/correction_window_test_v0_1.md).
5. Use the [`worksheet`](worksheet/correction_window_worksheet_v0_1.md) on one real system.
6. Check the [`FAQ`](faq.md), [`glossary`](glossary.md), [`method and caveats`](method/method_and_caveats.md), and [`falsifiers`](falsifiers/falsifiers.md).

If you find a defect, open an issue or apply the worksheet to a concrete case and show where it fails.

## Why this matters

Many systems say they have safeguards: appeals, audits, human oversight, risk reviews, complaint routes, dashboards, escalation processes, model cards, governance boards, or logs.

Those safeguards may still fail if they cannot act in time.

A review after the job is filled, the benefit is stopped, the account is closed, the model output has propagated, the deadline has passed, or the evidence is lost may still matter. It may expose the failure. It may compensate. It may prevent recurrence.

But it is no longer live protection.

## The test in one sentence

**Can correction reach the affected person before the consequence becomes practically irreversible?**

## Reader paths

### I want the shortest version

Read the [`quick reference`](quick_reference.md).

### I want to use the tool

Use the [`worksheet`](worksheet/correction_window_worksheet_v0_1.md) and compare against the [`cautious full example`](examples/full_worksheet_benefits_suspension.md) and the [`crisp false-safeguard example`](examples/full_worksheet_false_safeguard_dashboard.md).

### I work on AI governance

Read [`Using the Correction Window Test in AI Governance`](guides/ai_governance_use.md).

### I design safeguards

Read [`Design Patterns for Live Correction`](guides/design_patterns.md).

### I want to criticise the approach

Read [`falsifiers`](falsifiers/falsifiers.md) and open a front-door defect issue.

## Core concepts

- **Selection** — where a system chooses or recommends a path that affects the world.
- **Affected person** — the person or group whose options, burden, standing, or future changes.
- **Harm hardening** — the point where the consequence becomes difficult, costly, or impossible to reverse.
- **Correction window** — the time between first possible error and practical hardening.
- **Carrier** — the real mechanism that can stop, pause, reverse, compensate, or repair the action.
- **Evidence** — the record that lets an affected person or reviewer show what happened.
- **Standing** — who is allowed to trigger challenge or protection.

See [`glossary.md`](glossary.md) for working definitions.

## Repository map

- [`quick_reference.md`](quick_reference.md) — short card for applying the test.
- [`test/correction_window_test_v0_1.md`](test/correction_window_test_v0_1.md) — the main test.
- [`worksheet/correction_window_worksheet_v0_1.md`](worksheet/correction_window_worksheet_v0_1.md) — a fill-in worksheet for applying the test.
- [`examples/`](examples/) — worked examples, including full worksheet examples.
- [`guides/`](guides/) — AI governance use and design patterns.
- [`faq.md`](faq.md) — common questions.
- [`glossary.md`](glossary.md) — working definitions.
- [`method/`](method/) — method notes, caveats, and publication discipline.
- [`falsifiers/`](falsifiers/) — what would weaken or break the claims.
- [`PUBLICATION_STATUS.md`](PUBLICATION_STATUS.md) — what is public, incomplete, or still pending.

The ICO FOI/EIR public-record surface is staged but not yet published as data. It is tracked in publication status, not presented here as a usable front-door object.

## What this project is not

This repository does **not** claim:

- that Mechanical Ethics is validated;
- that AI alignment is solved;
- that one worksheet can settle ethics;
- that faster review is always better;
- that every harm is reducible to timing;
- that every safeguard must block action absolutely;
- that public-record surfaces prove the whole framework.

The narrow claim is this:

> A system that cannot detect, pause, challenge, or correct a harmful error before practical hardening should not describe that safeguard as live protection.

## Intended users

This is for people looking at:

- AI deployment and AI governance;
- automated public-service decisions;
- benefit, tax, credit, hiring, health, policing, or education systems;
- appeals and complaint routes;
- audit and oversight processes;
- institutional risk controls;
- public-record research.

The best way to use this repository is to pick one real system and apply the worksheet.

## Current status

**Status:** public rebuild / v0.1 front door.

The Correction Window Test is a practical diagnostic. It is ready for use as a thinking tool. It is not reliability-tested as an instrument.

The public-record data surface is being separated from theory claims. Data, caveats, and falsifiers should remain inspectable without requiring belief in Mechanical Ethics.

## Suggested citation for now

Goodbody, Mark. *Correction Window Test v0.1*. Mechanical Ethics / TRACE public working repository.

Formal citation and DOI are not yet assigned. Original text and documentation are licensed under CC BY 4.0 unless a file says otherwise.
