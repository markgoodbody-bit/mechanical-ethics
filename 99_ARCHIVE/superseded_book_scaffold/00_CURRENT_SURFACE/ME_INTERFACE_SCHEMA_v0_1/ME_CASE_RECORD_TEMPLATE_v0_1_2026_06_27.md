# Mechanical Ethics Case Record Template v0.1 — 2026-06-27

Status: blank template. Not a worked example. Not validation.

Purpose: provide a repeatable case-record structure for future TRACE → ME applications.

## 1. Case identity

```yaml
case_id:
title:
domain:
date_or_time_window:
decision_or_question_on_the_table: # the live choice ME is asked to inform; router finding must refer to this
prepared_by:
review_status: draft | reviewed | contested
source_status: public_record | private_record | mixed | hypothetical | unknown
```

## 2. Minimum viable case record

Required to run a worked example:

```yaml
minimum_viable_case_record:
  decision_or_question_on_the_table:
  transition_description:
  affected_scope_minimum: at_least_one
  future_space_comparison_for_that_scope:
  at_least_one_clock_using_TRACE_bands:
  first_gates_results:
  router_finding:
  prescription_audit:
```

All other sections should be filled when known. Mark `missing` or `unknown`; never silently fill.

## 3. TRACE input summary

This section is read-only from the TRACE case map. If no TRACE case map exists, mark the field `missing`, not assumed.

```yaml
transition_description:
  start_state:
  change_or_proposed_change:
  end_state_or_expected_end_state:
  action:
  inaction_or_delay_option:
  mechanism:

trace_status_label: UNKNOWN | COMPRESSION_ONLY | CONTAMINATED_SIGNAL | PARTIAL_SIGNAL | STRONG_SIGNAL | REGRESSION
trace_confidence:
unknowns_and_disputes:
```

## 4. Actor map

```yaml
actors:
  - actor_id:
    role: initiator | designer | operator | maintainer | reviewer | beneficiary | delegated_system | blocker | other
    control_description:
    benefit_or_incentive:
    evidence:
```

## 5. Affected scope map

```yaml
affected_scopes:
  - scope_id:
    scope_type: person | group | animal | ecosystem | institution | future_persons | artificial_system | disputed | other
    affected_how:
    continuation_interest:
    vulnerability_or_dependency:
    participation_or_consent_status:
    protection_reasons:
    disputed_status:
```

## 6. Future-space comparison

```yaml
future_space:
  - scope_id:
    O_change: expanded | narrowed | mixed | unchanged | unknown | incomparable
    R_change: expanded | narrowed | mixed | unchanged | unknown | incomparable
    I_change: expanded | narrowed | mixed | unchanged | unknown | incomparable
    overall_comparison: expanded | narrowed | mixed | unchanged | unknown | incomparable
    confidence:
    reason:
```

No scalar subtraction unless a domain-specific measurement model is explicitly supplied and audited.

## 7. Clocks — read-only TRACE input

Clocks in the TRACE input use TRACE bands, not ME `clock_fit`.

```yaml
loss_clock:
  T_det_band: IMMEDIATE | SHORT | MEDIUM | LONG | GENERATIONAL | UNKNOWN
  T_det_confidence: OBSERVED | INFERRED_STRONG | INFERRED_WEAK | UNKNOWN
  T_route_band: IMMEDIATE | SHORT | MEDIUM | LONG | GENERATIONAL | UNKNOWN
  T_route_confidence: OBSERVED | INFERRED_STRONG | INFERRED_WEAK | UNKNOWN
  T_corr_band: IMMEDIATE | SHORT | MEDIUM | LONG | GENERATIONAL | UNKNOWN
  T_corr_confidence: OBSERVED | INFERRED_STRONG | INFERRED_WEAK | UNKNOWN
  T_irr_band: IMMEDIATE | SHORT | MEDIUM | LONG | GENERATIONAL | UNKNOWN
  T_irr_confidence: OBSERVED | INFERRED_STRONG | INFERRED_WEAK | UNKNOWN
  timing_relation: correction_before_hardening | correction_after_hardening | mixed | unknown

opportunity_clock:
  T_access_band: IMMEDIATE | SHORT | MEDIUM | LONG | GENERATIONAL | UNKNOWN
  T_access_confidence: OBSERVED | INFERRED_STRONG | INFERRED_WEAK | UNKNOWN
  T_uptake_band: IMMEDIATE | SHORT | MEDIUM | LONG | GENERATIONAL | UNKNOWN
  T_uptake_confidence: OBSERVED | INFERRED_STRONG | INFERRED_WEAK | UNKNOWN
  T_integrate_band: IMMEDIATE | SHORT | MEDIUM | LONG | GENERATIONAL | UNKNOWN
  T_integrate_confidence: OBSERVED | INFERRED_STRONG | INFERRED_WEAK | UNKNOWN
  T_opp_band: IMMEDIATE | SHORT | MEDIUM | LONG | GENERATIONAL | UNKNOWN
  T_opp_confidence: OBSERVED | INFERRED_STRONG | INFERRED_WEAK | UNKNOWN
  timing_relation: opportunity_before_expiry | opportunity_after_expiry | mixed | unknown
```

## 8. ME clock-fit interpretation

`ME_clock_fit` is derived by ME from TRACE clock bands and timing relation. It is not TRACE-emitted.

```yaml
ME_clock_fit:
  loss_clock_fit: likely_in_time | borderline | likely_too_late | already_too_late | unknown
  opportunity_clock_fit: likely_in_time | borderline | likely_too_late | already_too_late | unknown
  derivation_note:
```

## 9. Channels

```yaml
channels:
  - channel_id:
    channel_type: correction | opportunity | appeal | review | compensation | repair | disclosure | pause | other
    reachable_by_scope:
    authority_to_change_path:
    timing_capacity:
    cost_or_burden:
    evidence_requirements:
    independence:
    known_failure_modes:
    can_channel_itself_harm: yes | no | unknown
```

## 10. Estimator authority

```yaml
estimators:
  - estimate_id:
    what_is_estimated:
    estimator_identity:
    estimator_role:
    incentive_position:
    independence: independent | partially_independent | assessed_actor | unknown
    affected_scope_challenge_route:
    contamination_status: independent_signal | partially_independent_signal | contaminated_signal | unknown
```

If the assessed actor sets a material clock, mark contaminated unless independently supported.

## 11. Burden shift

```yaml
burden_shifts:
  - burden_type:
    from_actor_or_system:
    to_scope:
    voluntary_or_forced:
    contestable:
    repairable:
    evidence:
```

## 12. Residue

```yaml
residue:
  loss_not_restored:
  time_not_returned:
  trust_damage:
  opportunity_expired:
  record_scar:
  recurrence_risk:
  acknowledgement_needed:
  other:
```

## 13. ME intake status

```yaml
me_intake:
  status: usable | usable_with_unknowns | needs_more_TRACE_mapping | hold_due_to_missing_material_field
  material_unknowns:
  contaminated_estimates:
  disputed_facts:
```

## 14. First gates

```yaml
first_gates:
  do_not_hide_loss:
    result: pass | fail | uncertain | not_applicable
    answered: yes | no | not_applicable
    reason:
  do_not_erase_affected_scopes:
    result: pass | fail | uncertain | not_applicable
    answered: yes | no | not_applicable
    reason:
  do_not_treat_uncertainty_as_certainty:
    result: pass | fail | uncertain | not_applicable
    answered: yes | no | not_applicable
    reason:
  do_not_pretend_repair_where_residue_remains:
    result: pass | fail | uncertain | not_applicable
    answered: yes | no | not_applicable
    reason:
  do_not_let_correction_channels_become_harm_carriers:
    result: pass | fail | uncertain | not_applicable
    answered: yes | no | not_applicable
    reason:
  do_not_let_assessed_actor_set_every_clock:
    result: pass | fail | uncertain | not_applicable
    answered: yes | no | not_applicable
    reason:
  do_not_use_emergency_to_launder_prior_failure:
    result: pass | fail | uncertain | not_applicable
    answered: yes | no | not_applicable
    reason:
```

Consistency rule: if any first gate is `fail` and `answered: no`, router finding cannot be `NO_STRUCTURAL_OBJECTION_FOUND`.

## 15. Protection and scope findings

```yaml
protection_findings:
  - scope_id:
    finding: protection_triggered | precaution_triggered | standing_unresolved | no_protection_reason_found
    reasons:
    uncertainty_modifier:
```

## 16. Duties

```yaml
duty_records:
  - duty: disclose | preserve_evidence | slow_or_pause | independent_review | keep_challenge_live | repair_path | compensate | record_residue | prevent_recurrence | escalate | hold
    structural_pressure:
    affected_scope:
    obligated_actor:
    timing:
    evidence_basis:
    uncertainty_status:
    residue_status:
```

## 17. Dirty conflict check

```yaml
dirty_conflict:
  status: yes | no | unknown
  losses_by_path:
  nonparticipants:
  least_reachable_scopes:
  least_repairable_losses:
  minimum_floor_issue:
  declared_value_tilt_used:
  residue_after_forced_loss:
```

Dirty conflict must not be recorded as clean.

## 18. Responsibility attachment

```yaml
responsibility_attachment:
  - actor_id:
    visibility:
    decision_time_evidence:
    action_relevance:
    role_connection:
    meaningful_control:
    capacity_to_act:
    finding: no_attachment_found | weak_attachment | material_attachment | strong_attachment | unresolved_due_to_missing_evidence
    reason:
```

## 19. Legitimacy and coercion

```yaml
legitimacy_and_coercion:
  authority_basis:
  affected_scope_recognition:
  reason_giving:
  contestability:
  burden_accounting:
  correction_capacity:
  expiry_or_review:
  independent_challenge:
  finding: structurally_supported | structurally_defective | unresolved_value_crux | outside_ME_current_scope
```

## 20. ME router finding

```yaml
me_router_finding: NO_STRUCTURAL_OBJECTION_FOUND | PROCEED_ONLY_WITH_NAMED_CONSTRAINTS | PAUSE | HALT | ESCALATE | REPAIR_REQUIRED | COMPENSATION_REQUIRED | INDEPENDENT_REVIEW_REQUIRED | HOLD | UNRESOLVED_VALUE_CRUX | REGRESSION_RISK
named_constraints:
reason:
actor_responsibility_remaining:
gate_router_consistency_checked: yes | no
```

Router finding is not permission to act. If any failed gate remains unanswered, do not use `NO_STRUCTURAL_OBJECTION_FOUND`.

## 21. Prescription audit

```yaml
prescription_audit:
  decision_or_question_on_the_table:
  trace_facts_read:
  trace_primitives_used_without_redefinition:
  value_priority_added_by_ME:
  scopes_protected_and_why:
  uncertainties_remaining:
  contaminated_clocks_or_estimates:
  duties_and_structural_pressure:
  dirty_or_unrepaired_loss:
  residue_persisting:
  responsibility_remaining:
  laundering_risk:
  first_gate_failed_and_unanswered:
  no_objection_finding_avoided_if_required:
  fail_state_considered:
```

## 22. Reviewer notes

```yaml
reviewer_notes:
  non_independence_flags:
  objections:
  patch_needed:
  status: draft | revise | usable_for_worked_example | do_not_use
```
