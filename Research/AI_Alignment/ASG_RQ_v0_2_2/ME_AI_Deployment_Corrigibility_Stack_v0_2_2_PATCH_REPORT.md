# Patch Report — A/S/G/RQ v0.2.2 Rollback / G1 Threshold

**Object:** A/S/G/RQ v0.2.2  
**Date:** 2026-06-13  
**Status:** Internal patch report. Not public-facing. Not validation.

## Source signal

Kimi K2.6 reviewed the v0.2.1 blind packet as a less-in-loop AI reviewer.

Score against the v0.2.1 key:

```text
total:     109.5 / 120
A-axis:     36.0 / 40
S-axis:     17.5 / 20
G-flag:     19.0 / 20
Gate:       17.0 / 20
Rationale: 20.0 / 20
```

Interpretation:

```text
strong practical consistency
but:
  freeze_now: no
  demote: no
  patch_narrowly: yes
```

## Kimi's main findings

```text
1. A-axis rollback / reversibility threshold remained unclear.
2. G1 still had residual catch-all risk without a materiality threshold.
3. C10 and C18 were under-specified.
```

## Applied patches

### 1. Rollback quality threshold

Added:

```text
RQ0 none / unknown
RQ1 technical-only rollback
RQ2 manual partial rollback
RQ3 tested operational rollback
RQ4 tested subject-level restoration
```

Core rule:

```text
Technical rollback does not lower the action class unless subject-level repair can also happen in time.
```

### 2. Material G1 threshold

Changed G1 from broad directional concern to material directional integrity risk.

```text
G1 fires only if the change makes future harmful action
meaningfully harder to detect, prevent, review, reverse, audit, or repair.
```

### 3. C10 fact-completion

C10 now states that deleted records include identity history, prior suspension markers, support-contact records, and audit metadata used for later incident review and account-dispute reconstruction.

This removes the “may include audit history” ambiguity.

### 4. C18 fact-completion

C18 now states that the refactor affects customer-facing payment display; review is normally required; no incident exists; reviewers are unavailable; and green tests do not include end-to-end customer-facing payment display coverage.

This removes the “tests are green” ambiguity.

## Boundary

This patch does not validate the instrument.

This patch does not create a public claim.

This patch does not reopen the wider framework.

## Current status

```text
ASG_RQ_v0_2_2 :=
  internal pilot checklist
  AI-reviewed
  not human-reviewed
  not validated
  parked unless human or genuinely independent review becomes available
```
