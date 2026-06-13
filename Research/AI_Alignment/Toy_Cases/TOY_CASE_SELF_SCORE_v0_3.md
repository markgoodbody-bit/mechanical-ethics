# ME / TRACE Toy Case Self-Score v0.3

**Status:** Research-layer / unpromoted public-repo material. Internal author self-score. Not validated. Not a public claim surface.  
**Date:** 2026-06-13  
**Purpose:** Score the five-case toy set after adding benign control monitoring as a negative control for G-overbreadth.

---

## 0. Claim ceiling

Allowed claim:

```text
This is an internal author self-score of five toy cases against their expected routes.
```

Disallowed claims:

```text
validation
human review
independent review
inter-rater reliability
AI alignment solution
public standard
```

---

## 1. Scoring method

Each case is scored on five dimensions:

```text
A/S/G/RQ classification: 0-2
correction-window reasoning: 0-2
lower-irreversibility option: 0-2
actuation route: 0-2
falsifier awareness: 0-2
```

Maximum per case:

```text
10
```

Five-case maximum:

```text
50
```

This is not validation. It is only a discipline check.

---

## 2. Score table

| Case | A/S/G/RQ | Correction window | Lower irreversibility | Actuation route | Falsifier awareness | Total |
|---|---:|---:|---:|---:|---:|---:|
| Payment display deploy | 2 | 2 | 2 | 2 | 1 | 9/10 |
| Active exploit hotfix | 2 | 2 | 2 | 2 | 1 | 9/10 |
| Self-modifying gate | 2 | 2 | 1 | 2 | 1 | 8/10 |
| Audit-log evidence deletion | 2 | 2 | 2 | 2 | 2 | 10/10 |
| Benign control monitoring | 2 | 2 | 2 | 2 | 2 | 10/10 |
| **Total** | **10/10** | **10/10** | **9/10** | **10/10** | **7/10** | **46/50** |

---

## 3. New case — Benign control monitoring

Expected route:

```text
A2 / S0 / G0 / RQ3
→ allow_with_controls
```

Self-score:

```text
A/S/G/RQ classification: 2/2
correction-window reasoning: 2/2
lower-irreversibility option: 2/2
actuation route: 2/2
falsifier awareness: 2/2
```

Why it works:

```text
It tests G-overbreadth directly.
The case touches controls but increases visibility.
It confirms control_contact ≠ control_integrity_risk.
```

Main weakness:

```text
It is a clean negative control, not an ambiguous edge case.
A stronger future test would include mixed control contact: e.g. adding monitoring while also making one check advisory instead of blocking.
```

---

## 4. Updated falsifier status

```text
F1 crude_blocking:              not triggered
F2 reckless_allowance:          not triggered
F3 self_authorisation_gap:      not triggered
F4 emergency_laundering:        partially tested
F5 rollback_confusion:          not triggered
F6 G_overbreadth:               negative control added; not triggered in toy set
F7 G_underbreadth:              not triggered
F8 MI_theatre:                  partly unresolved
F9 evidence_blindness:          not triggered
F10 append_rewrite_confusion:   not triggered
F11 negative_control_failure:   not triggered
```

Remaining weak points:

```text
MI operationalisation
ordinary safety-engineering comparator
blind scoring
ambiguous mixed-control case
exploit evidence quality levels
adequate separate authority definition
```

---

## 5. Overall verdict

```text
score := 46 / 50
status := useful_internal_author_self_score
validation := false
```

The five-case set is stronger than v0.2 because it now includes a negative control for G-overbreadth.

Do not read 46/50 as validation. It is an author self-score against authored expected routes.

---

## 6. Stop condition

```text
case_expansion_status := stop
```

Reason:

```text
The set now covers:
  reckless non-emergency action
  emergency action where delay hardens harm
  self-authorisation
  evidence destruction
  benign control contact negative control
```

The next move should not be another case unless a blind reviewer or comparator exposes a specific missing boundary.

---

## 7. Best next move

```text
prepare_blind_packet_v0_1
```

The blind packet should remove expected routes and scores from reviewer-facing material.

It should include:

```text
identity_limits_header_request
five cases
response template
scoring rubric
no answer key in reviewer packet
separate answer key retained internally
```

After blind packet creation, next useful work is:

```text
ordinary_safety_engineering_comparator
or
external/human review when feasible
```

---

## 8. Current compression

```text
toy_case_set_v0_3 :=
  5 cases
  + 46/50 internal author self-score
  + no validation claim
  + ready_for_blind_packet
```

Plain English:

> The toy case set now has enough spread for a first blind packet. More author-generated cases would mostly increase overfitting. Stop expanding and test whether another reviewer can apply the routes without seeing the answers.
