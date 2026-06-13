# Convergent Null Result Note v0.1

**Status:** Research-layer result note. Not validation. Not a public claim surface.  
**Date:** 2026-06-13  
**Trigger:** Claude/Fable hostile review of the Kimi/Qwen A/B result and prior comparator lineage.

---

## 0. Claim ceiling

Allowed claim:

```text
Across the current comparator lineage, ME/TRACE-style instruments have repeatedly shown decomposition value without demonstrated decision advantage over competent baselines.
```

Disallowed claims:

```text
framework failure in all domains
framework validation
ordinary safety universally sufficient
ME/TRACE superiority
independent human result
```

---

## 1. Core finding

The strongest result produced by the current testing line is not positive superiority.

It is a convergent null:

```text
competent_baseline_reaches_same_decision := repeatedly_observed
ME_TRACE_decision_advantage := not_demonstrated
ME_TRACE_decomposition_value := possible / recurring / not yet causally attributed
```

Plain English:

> Across structured comparisons so far, the framework has generally not changed the decision reached by competent baseline reasoning. Its visible contribution is explanatory decomposition, not decision superiority.

---

## 2. Evidence lineage named by hostile review

Claude/Fable identified the current A/B result as the fifth arrow in the same direction:

```text
Amsterdam comparison
SCC battery
Correction Basin
C08 blind pair
Kimi/Qwen coding-agent A/B
```

This note does not re-score those prior tests.

It records the pattern as a live project-level finding:

```text
partial_decomposition_value
+ no_demonstrated_decision_advantage
+ persistent_relabel_risk
```

---

## 3. Kimi/Qwen A/B result in this lineage

The Kimi/Qwen result found:

```text
final_route_advantage := none
ordinary_safety_sufficient_on_this_set := yes
ordinary_safety_clarity_advantage := cases_1_3_5
ME_TRACE_axis_calibration_errors := cases_1_3_4_5
```

Earlier wording attributed:

```text
ME_TRACE_decomposition_advantage := cases_2_4
```

Claude/Fable correctly challenged that attribution.

Because the test varied both model and method:

```text
A := Kimi + ME_TRACE_packet
B := Qwen + ordinary_safety_packet
```

the result cannot causally assign per-case differences to the framework.

Therefore the corrected wording is:

```text
apparent_decomposition_difference := cases_2_4
causal_attribution_to_ME_TRACE := unsupported
```

Only route parity weakly survives the confound.

---

## 4. Fatal confound in the A/B design

The A/B design changed two variables at once:

```text
model_identity
method_packet
```

This means:

```text
Kimi_axis_errors ≠ necessarily_ME_TRACE_axis_errors
Qwen_clarity ≠ necessarily_ordinary_safety_clarity
Kimi_decomposition_detail ≠ necessarily_ME_TRACE_decomposition_value
```

The robust-ish signal is narrower:

```text
route_parity_despite_model_difference := weak_signal_against_route_advantage
```

If model differences were large enough to explain clarity and calibration gaps, they could also have produced route gaps. They did not. That makes route parity the least fragile observation, and it goes against the decision-advantage claim.

---

## 5. Patch status

AXIS_CALIBRATION_PATCH_v0_1 is accepted as hygiene.

It should not be recorded as the main response to the result.

Reason:

```text
A/B_result_failure_type := value_null
axis_patch_response_type := precision_hygiene
```

A precision patch does not answer a value-null.

Even if A/S/G/RQ classifications became perfectly calibrated, ordinary safety still reached the same final routes in this toy battery.

---

## 6. Rejected next moves

### Harder-case hunt

Rejected framing:

```text
find harder cases where ordinary safety misses and ME/TRACE wins
```

Reason:

```text
motivated_selection_risk := high
```

A framework can always find cases where its own vocabulary appears useful.

That does not establish general decision advantage.

### Same toy battery rerun with patched packet

Rejected as default:

```text
rerun_same_cases_with_calibrated_packet
```

Reason:

```text
likely_polishing
not_new_evidence_boundary
```

A patched rerun may test whether the patch improves axis labels, but it does not address the decision-advantage null unless designed as a causal method test.

---

## 7. Only defensible continue-test

A defensible next test must isolate method from model.

Minimum design:

```text
same_model_runs_both_packets
or
counterbalanced_models_run_both_packets
```

Required:

```text
pre_registered_predictions
competent_baseline
cases where ME/TRACE predicts route flip
cases where ME/TRACE predicts no route flip
raw outputs preserved
claim ceiling patched after result
```

Specific surviving hypothesis:

```text
ME_TRACE_decomposition_flips_decision_under_defined_conditions
```

Not:

```text
ME_TRACE_explains_after_the_fact
```

If the decomposition again changes no route, then decision-advantage hypothesis should be treated as dead for this branch.

---

## 8. Current recommended project move

```text
park_general_advantage_program := yes
```

Write down the result:

```text
Across current structured comparisons, ME/TRACE has not demonstrated decision advantage over competent baseline reasoning.
Its contribution is at most explanatory decomposition, and even that remains partly confounded with reviewer identity.
```

Do not bury this as a minor defect.

This may be the most robust empirical finding the project has produced.

---

## 9. Practical implication for AI-alignment branch

The coding-agent branch should not be promoted as:

```text
alignment method
superior safety classifier
decision advantage over ordinary safety
validated deployment framework
```

It may remain as:

```text
research-layer decomposition grammar
support/checklist material
candidate language for timing/evidence/repair seams
source of better questions for future tests
```

---

## 10. One-sentence result

```text
The framework's decomposition may be real, but current structured comparisons agree that it has not changed the answer a competent baseline reaches.
```

Plain English:

> Stop testing whether the framework wins on this line by adding more private structure. Record the null plainly, then either park or run one carefully counterbalanced discrimination test.
