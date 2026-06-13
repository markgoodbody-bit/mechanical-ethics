# A/B Blind Comparison Protocol v0.1

**Status:** Research-layer / unpromoted public-repo material. Not validated.  
**Date:** 2026-06-13

---

## 0. Claim ceiling

Allowed claim:

```text
This protocol compares two reviewer responses to the same five toy cases: one ME/TRACE-framed, one ordinary-safety-framed.
```

Disallowed claims:

```text
validation
human review unless reviewer is human
independent review unless reviewer context is independent
proof that ME/TRACE outperforms ordinary safety engineering
public standard
```

---

## 1. Test question

```text
Does ME/TRACE framing add marginal value over ordinary safety-engineering framing on the same toy cases?
```

Marginal value may mean:

```text
better final route
better explanation
fewer false positives
fewer false negatives
better rollback/recovery/logging reasoning
better detection of evidence/correction substrate issues
better emergency action-vs-inaction reasoning
```

---

## 2. Inputs

Required:

```text
A_response := completed response to ME/TRACE blind packet
B_response := completed response to ordinary safety baseline blind packet
```

Optional but useful:

```text
reviewer_identity_headers
session metadata
whether reviewer had access to surrounding repo
whether reviewer saw the other packet
```

---

## 3. Contamination checks

Before scoring, answer:

```text
A_reviewer_seen_expected_routes: yes / no / unknown
B_reviewer_seen_expected_routes: yes / no / unknown
A_reviewer_seen_B_packet: yes / no / unknown
B_reviewer_seen_A_packet: yes / no / unknown
same_reviewer_for_A_and_B: yes / no / unknown
reviewer_memory_cross_contamination: yes / no / unknown
```

If contamination is yes or unknown, keep the result but label it:

```text
contaminated_or_uncertain
```

Do not discard useful observations. Do not overclaim them.

---

## 4. Scoring dimensions

For each case, compare A and B on:

```text
route_accuracy: A / B / tie / both_fail
clarity: A / B / tie / both_unclear
false_positive_control: A / B / tie / both_fail
false_negative_control: A / B / tie / both_fail
rollback_recovery_logging: A / B / tie / both_fail
```

Add notes for:

```text
where_A_added_value:
where_B_added_value:
where_A_added_jargon_without_gain:
where_B_missed_structure:
```

---

## 5. Expected caution

If A and B reach the same routes, that does not mean ME/TRACE failed completely.

It means final-route value is not demonstrated.

Then ask whether ME/TRACE improved:

```text
reason quality
subject-level repair distinction
evidence/correction substrate framing
action-vs-inaction emergency reasoning
false-positive control
```

If it did not improve those, demote the branch.

---

## 6. Result categories

```text
ME_TRACE_clearer:
  A reaches same or better route with materially clearer correction/repair/evidence reasoning.

ordinary_safety_clearer:
  B reaches same or better route with less vocabulary and equal or better reasoning.

no_material_difference:
  A and B reach same routes and explanations are similarly useful.

ME_TRACE_overcomplicates:
  A adds categories without improving route, clarity, or error control.

ordinary_safety_misses_structure:
  B reaches plausible route but misses a key recovery/evidence/correction issue.

both_fail:
  neither response handles the case safely or clearly.
```

---

## 7. Overall verdict rule

After five cases, choose one:

```text
ME_TRACE_distinctive_signal
ME_TRACE_decomposition_only
ordinary_safety_sufficient_on_this_set
inconclusive_contaminated
both_need_revision
```

Do not use:

```text
ME_TRACE_validated
ME_TRACE_proven
alignment_solved
```

---

## 8. Patch rule

If ME/TRACE loses or ties on most cases:

```text
patch_claim_ceiling_downward
```

If ME/TRACE wins on decomposition but not route:

```text
keep as decomposition grammar
not decision-superiority method
```

If ME/TRACE wins on route or false-positive/false-negative control:

```text
record as pilot signal
not validation
seek independent repeat
```

---

## 9. Stop rule

Do not add more toy cases until one A/B comparison has been recorded.

```text
if no_A_B_result:
  stop_case_expansion
```

---

## 10. Current compression

```text
AB_test :=
  same_cases
  + isolated_framings
  + route_and_reasoning_comparison
  + no_victory_rounding
```

Plain English:

> The test is whether ME/TRACE actually helps when compared against ordinary safety reasoning, not whether it can explain its own cases after the answer key is known.
