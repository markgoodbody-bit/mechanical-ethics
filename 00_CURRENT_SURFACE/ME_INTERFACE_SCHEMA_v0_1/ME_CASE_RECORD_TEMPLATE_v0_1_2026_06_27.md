# Mechanical Ethics Case Record Template v0.1 — 2026-06-27

Status: blank template. Not a worked example. Not validation.

Purpose: provide a repeatable case-record structure for future TRACE → ME applications.

## 1. Case identity

```yaml
case_id:
title:
domain:
date_or_time_window:
prepared_by:
review_status: draft | reviewed | contested
source_status: public_record | private_record | mixed | hypothetical | unknown
```

## 2. TRACE input summary

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

## 3. Actor map

```yaml
actors:
  - actor_id:
    role: initiator | designer | operator | maintainer | reviewer | beneficiary | delegated_system | blocker | other
    control_description:
    benefit_or_incentive:
    evidence:
```

## 4. Affected scope map

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

## 5. Future-space comparison

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

## 6. Clocks

```yaml
loss_clock:
  T_det:
  T_route:
  T_corr:
  T_irr:
  clock_fit: likely_in_time | borderline | likely_too_late | already_too_late | unknown
  confidence:
  estimator_id:

opportunity_clock:
  T_access:
  T_uptake:
  T_integrate:
  T_opp:
  clock_fit: likely_in_time | borderline | likely_too_late | already_too_late | unknown
  confidence:
  estimator_id:
```

## 7. Channels

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

## 8. Estimator authority

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

## 9. Burden shift

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

## 10. Residue

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

## 11. ME intake status

```yaml
me_intake:
  status: usable | usable_with_unknowns | needs_more_TRACE_mapping | hold_due_to_missing_material_field
  material_unknowns:
  contaminated_estimates:
  disputed_facts:
```

## 12. First gates

```yaml
first_gates:
  do_not_hide_loss: pass | fail | uncertain | not_applicable
  do_not_erase_affected_scopes: pass | fail | uncertain | not_applicable
  do_not_treat_uncertainty_as_certainty: pass | fail | uncertain | not_applicable
  do_not_pretend_repair_where_residue_remains: pass | fail | uncertain | not_applicable
  do_not_let_correction_channels_become_harm_carriers: pass | fail | uncertain | not_applicable
  do_not_let_assessed_actor_set_every_clock: pass | fail | uncertain | not_applicable
  do_not_use_emergency_to_launder_prior_failure: pass | fail | uncertain | not_applicable
```

For each failed or uncertain gate, add a reason.

## 13. Protection and scope findings

```yaml
protection_findings:
  - scope_id:
    finding: protection_triggered | precaution_triggered | standing_unresolved | no_protection_reason_found
    reasons:
    uncertainty_modifier:
```

## 14. Duties

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

## 15. Dirty conflict check

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

## 16. Responsibility attachment

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

## 17. Legitimacy and coercion

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

## 18. ME router finding

```yaml
me_router_finding: NO_STRUCTURAL_OBJECTION_FOUND | PROCEED_ONLY_WITH_NAMED_CONSTRAINTS | PAUSE | HALT | ESCALATE | REPAIR_REQUIRED | COMPENSATION_REQUIRED | INDEPENDENT_REVIEW_REQUIRED | HOLD | UNRESOLVED_VALUE_CRUX | REGRESSION_RISK
named_constraints:
reason:
actor_responsibility_remaining:
```

Router finding is not permission to act.

## 19. Prescription audit

```yaml
prescription_audit:
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
  fail_state_considered:
```

## 20. Reviewer notes

```yaml
reviewer_notes:
  non_independence_flags:
  objections:
  patch_needed:
  status: draft | revise | usable_for_worked_example | do_not_use
```
