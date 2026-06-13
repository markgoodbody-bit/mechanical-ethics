# Correction Window Test v0.1

**Can the safeguard actually fix the error before it is too late?**

Many systems claim to have safeguards: appeals, reviews, audits, dashboards, human oversight, complaint routes, or rollback procedures.

This test asks one narrow question:

> If the system is wrong, can the affected person get correction before the consequence becomes hard to reverse?

This is a diagnostic tool, not a governance framework, ethics theory, certification scheme, or AI-alignment solution.

## Use the tool

1. Read the [`quick reference`](quick_reference.md).
2. Read the [`Correction Window Test`](test/correction_window_test_v0_1.md).
3. Use the [`worksheet`](worksheet/correction_window_worksheet_v0_1.md).
4. Compare your result with the [`worked examples`](examples/README.md).

## The five checks

1. **Decision** — what does the system do, rank, approve, refuse, flag, route, or trigger?
2. **Affected person** — who carries the consequence?
3. **Too-late point** — when does the consequence become hard to reverse?
4. **Actual fix mechanism** — what can pause, stop, reverse, repair, or compensate?
5. **Timing fit** — can that mechanism act before the too-late point?

## Working result labels

- **Live protection** — the fix can still change the live path in time.
- **Partial protection** — some real protection exists, but timing, authority, evidence, access, or resources are incomplete.
- **After-the-fact review** — the route can expose, compensate, or prevent recurrence, but usually arrives after the original consequence has hardened.
- **False safeguard** — the safeguard exists in name, policy, dashboard, or process, but lacks a meaningful fix mechanism.
- **Unknown** — the available evidence does not show enough to classify it.

## Example set

- [`Live protection: Payment Hold With Live Challenge`](examples/live_protection_payment_hold.md)
- [`Partial / mixed: Benefits Suspension or Recovery`](examples/full_worksheet_benefits_suspension.md)
- [`After-the-fact review: Hiring Rejection After Role Filled`](examples/after_the_fact_hiring_rejection.md)
- [`False safeguard: Dashboard Without a Brake`](examples/full_worksheet_false_safeguard_dashboard.md)
- [`Unknown: Private Risk Scoring With Missing Records`](examples/unknown_private_scoring.md)

## Usage constraints

This repository does **not** claim that:

- Mechanical Ethics / TRACE is validated;
- this is a reliability-tested instrument;
- this is a complete ethics framework;
- this is an AI governance framework;
- this solves AI alignment;
- this proves a system is safe, fair, lawful, legitimate, or aligned.

Use it as a structured diagnostic for one failure mode: a claimed safeguard that cannot correct a harmful error before the consequence hardens.

## Support files

- [`glossary.md`](glossary.md) — working definitions.
- [`method/`](method/) — method notes and caveats.
- [`falsifiers/`](falsifiers/) — what would weaken or break the approach.
- [`LICENSE`](LICENSE) — reuse terms for original text and documentation.

## Current status

Public v0.1 diagnostic. Not externally validated. Not ready to be treated as a finished governance method.

Formal citation and DOI are not yet assigned. Original text and documentation are licensed under CC BY 4.0 unless a file says otherwise.
