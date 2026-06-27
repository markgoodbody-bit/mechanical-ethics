# TRACE Current State v0.6 — 2026-06-27

Status: working TRACE artifact, not validation.

This note freezes where TRACE currently stands before beginning the separate Mechanical Ethics artifact.

## 1. Split now in force

```trace
TRACE_artifact :=
  pre-prescriptive minimal-value grammar
  for transitions under uncertainty

Mechanical_Ethics_artifact :=
  later prescriptive layer:
  what should follow if TRACE's description is accepted
```

TRACE is the descriptive / field-inspection side. Mechanical Ethics is not yet built in this repo as a separate artifact.

## 2. Current TRACE master packet shape

The current packet separates jobs that earlier drafts mixed:

```trace
TRACE_Master_Packet_v0_6 :=
  motivation_layer
  + cold_test_card
  + decision_delta_battery
  + case_record_template
  + trust/audit_ledger
  + ME_boundary_stub
  + review_prompts
```

The motivation layer can carry the “After the Apocalypse” / transmission frame.

The cold-test card must not carry mythology, care-language, validation claims, or emotional staging.

## 3. Current operational spine

```trace
transition
-> affected scopes
-> future-space comparison
-> preference-gradient / local reward pull
-> loss clock
-> opportunity clock
-> correction channel usability
-> estimator authority
-> burden shift
-> residue
-> router/status label
```

Future-space is compared qualitatively as:

```trace
F_x(t) := (O_x(t), R_x(t), I_x(t))

O := option topology
R := practical reachability
I := usable navigational information
```

Do not use fake scalar subtraction or undefined alpha/beta/gamma weights.

## 4. Two clocks

Loss-side clock:

```trace
T_det + T_route + T_corr < T_irr
```

Opportunity-side clock:

```trace
T_access + T_uptake + T_integrate < T_opp
```

The most likely decision-relevant contribution is forced dual-clock attention: checking both whether correction arrives before loss hardens and whether access arrives before opportunity expires.

## 5. Estimator authority rule

Every clock-band estimate should record who set it.

```yaml
estimator_identity:
estimator_role:
estimator_incentive:
estimator_independence:
affected_scope_challenge_route:
contamination_flag:
```

Rule:

```trace
if estimator_is_assessed_actor:
  estimate_status := CONTAMINATED_SIGNAL by default
```

The assessed actor may still be right. The point is that the estimate is not independent.

## 6. Scope handling

Use unordered scope reasons, not a worth ladder.

```trace
scope_reasons :=
  affected
  continuing
  preference_bearing
  vulnerable_or_dependent
  domain_protected
  disputed_or_unknown
```

Uncertainty should not demote a scope. It should be recorded.

## 7. Router brakes

TRACE must be able to return:

```trace
UNKNOWN
COMPRESSION_ONLY
PARTIAL_SIGNAL
STRONG_SIGNAL
REGRESSION
CONTAMINATED_SIGNAL
```

It must also route out of cases where the crux is not timing, future-space, correction, opportunity, or estimator authority.

Value-crux exit:

```trace
if case_crux in {desert, legitimacy, punishment, dignity, recognition, moral_status, value_priority, justification_of_loss}:
  TRACE_status := UNKNOWN or COMPRESSION_ONLY
  unless TRACE reveals a specific inspection delta
```

## 8. Current review signal

Observed so far:

```trace
AI_reconstruction_signal := present
cross_language_reconstruction_candidate := present
low_fit_COMPRESSION_ONLY_cases := present
high_fit_PARTIAL_SIGNAL_candidate := present
STRONG_SIGNAL := none
validation := false
```

The project has passed the “is this basically coherent?” gate.

It has not passed the “does this reliably improve decisions?” gate.

## 9. Current best description

TRACE v0.6 is best understood as:

```trace
structurally_coherent
+ transmissible
+ testable
+ not_validated
+ good_enough_to_pause_major_rewrites
```

Further work on TRACE should mostly be testing, case records, and minor repairs.

The next major build should be the separate Mechanical Ethics artifact.

## 10. Wall rule

Name who sets each clock, and cut the myth from cold tests — otherwise a cold test measures framing and assertions, not grammar.
