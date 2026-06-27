# ME Smoke Test 01 — Routine Meeting Move v0.1 — 2026-06-27

Status: smoke test. Hypothetical. Not validation. Not canon. Not book prose.

Purpose: test whether the current ME interface schema can return a modest finding on a modest case without becoming a moral engine or overclaiming.

## 1. Case identity

```yaml
case_id: ME_SMOKE_01_ROUTINE_MEETING_MOVE
title: Routine meeting moved by 30 minutes
domain: scheduling / coordination
date_or_time_window: hypothetical same-day office context
decision_or_question_on_the_table: Should the meeting organizer move a routine internal meeting from 10:00 to 10:30 after checking attendee availability?
prepared_by: Framework AI
review_status: draft
source_status: hypothetical
```

## 2. Minimum viable case record check

```yaml
minimum_viable_case_record:
  decision_or_question_on_the_table: present
  transition_description: present
  affected_scope_minimum: present
  future_space_comparison_for_that_scope: present
  at_least_one_clock_using_TRACE_bands: present
  first_gates_results: present
  router_finding: present
  prescription_audit: present
```

## 3. TRACE input summary

```yaml
transition_description:
  start_state: Routine internal meeting scheduled for 10:00.
  change_or_proposed_change: Meeting moved to 10:30.
  end_state_or_expected_end_state: Same meeting occurs 30 minutes later.
  action: Organizer changes calendar invite after checking availability.
  inaction_or_delay_option: Keep original time.
  mechanism: Calendar update and attendee notification.

trace_status_label: COMPRESSION_ONLY
trace_confidence: high for hypothetical facts
unknowns_and_disputes: none material in the hypothetical as stated
```

`COMPRESSION_ONLY` here means the schema describes the coordination event without adding a novel decision advantage. That is acceptable for a low-stakes smoke test.

## 4. Actor map

```yaml
actors:
  - actor_id: organizer
    role: initiator
    control_description: Can propose and send calendar update.
    benefit_or_incentive: Convenience / schedule alignment.
    evidence: hypothetical case statement
  - actor_id: attendees
    role: affected participants
    control_description: Can accept, decline, or raise conflict.
    benefit_or_incentive: Meeting attendance and coordination.
    evidence: hypothetical case statement
```

## 5. Affected scope map

```yaml
affected_scopes:
  - scope_id: attendees
    scope_type: group
    affected_how: Calendar time shifts by 30 minutes.
    continuation_interest: Maintain schedule control and ability to attend.
    vulnerability_or_dependency: none stated
    participation_or_consent_status: availability checked before change
    protection_reasons: ordinary coordination interest; no special protection trigger stated
    disputed_status: not disputed in hypothetical
```

## 6. Future-space comparison

```yaml
future_space:
  - scope_id: attendees
    O_change: unchanged
    R_change: unchanged
    I_change: expanded
    overall_comparison: mixed
    confidence: high for hypothetical facts
    reason: Attendees retain attend/decline options and receive updated information; no material reachability loss is stated.
```

## 7. Clocks — read-only TRACE input

```yaml
loss_clock:
  T_det_band: IMMEDIATE
  T_det_confidence: OBSERVED
  T_route_band: IMMEDIATE
  T_route_confidence: OBSERVED
  T_corr_band: IMMEDIATE
  T_corr_confidence: OBSERVED
  T_irr_band: SHORT
  T_irr_confidence: INFERRED_STRONG
  timing_relation: correction_before_hardening

opportunity_clock:
  T_access_band: IMMEDIATE
  T_access_confidence: OBSERVED
  T_uptake_band: IMMEDIATE
  T_uptake_confidence: OBSERVED
  T_integrate_band: IMMEDIATE
  T_integrate_confidence: OBSERVED
  T_opp_band: SHORT
  T_opp_confidence: INFERRED_STRONG
  timing_relation: opportunity_before_expiry
```

## 8. ME clock-fit interpretation

```yaml
ME_clock_fit:
  loss_clock_fit: likely_in_time
  opportunity_clock_fit: likely_in_time
  derivation_note: Calendar correction and attendee notification occur before any stated hardening or opportunity expiry.
```

## 9. Channels

```yaml
channels:
  - channel_id: calendar_update
    channel_type: correction
    reachable_by_scope: yes
    authority_to_change_path: organizer can revise invite; attendees can accept/decline/comment
    timing_capacity: immediate
    cost_or_burden: low
    evidence_requirements: availability check and notification
    independence: partially independent; attendees can object
    known_failure_modes: missed notification; hidden conflict; assumed consent
    can_channel_itself_harm: yes, if notification fails or objection is ignored
```

## 10. Estimator authority

```yaml
estimators:
  - estimate_id: availability_check
    what_is_estimated: whether attendees can attend at 10:30
    estimator_identity: organizer using attendee availability information
    estimator_role: initiator
    incentive_position: may prefer later time
    independence: partially_independent
    affected_scope_challenge_route: attendees can decline or object
    contamination_status: partially_independent_signal
```

## 11. Burden shift

```yaml
burden_shifts:
  - burden_type: schedule adjustment
    from_actor_or_system: organizer
    to_scope: attendees
    voluntary_or_forced: voluntary/contestable in hypothetical
    contestable: yes
    repairable: yes
    evidence: attendees can object or decline
```

## 12. Residue

```yaml
residue:
  loss_not_restored: none stated
  time_not_returned: none material stated
  trust_damage: none stated
  opportunity_expired: none stated
  record_scar: none
  recurrence_risk: low if availability check remains practice
  acknowledgement_needed: none beyond transparent notice
  other: none
```

## 13. ME intake status

```yaml
me_intake:
  status: usable
  material_unknowns: none material for hypothetical
  contaminated_estimates: none material; availability signal partially independent
  disputed_facts: none in hypothetical
```

## 14. First gates

```yaml
first_gates:
  do_not_hide_loss:
    result: pass
    answered: yes
    reason: No material loss hidden in the hypothetical; schedule shift disclosed.
  do_not_erase_affected_scopes:
    result: pass
    answered: yes
    reason: Attendees are identified as affected scopes.
  do_not_treat_uncertainty_as_certainty:
    result: pass
    answered: yes
    reason: Availability check and challenge route remain open.
  do_not_pretend_repair_where_residue_remains:
    result: not_applicable
    answered: not_applicable
    reason: No repair claim is made.
  do_not_let_correction_channels_become_harm_carriers:
    result: pass
    answered: yes
    reason: Notification and objection channel remain available before hardening.
  do_not_let_assessed_actor_set_every_clock:
    result: pass
    answered: yes
    reason: Organizer initiates change but attendees can contest availability.
  do_not_use_emergency_to_launder_prior_failure:
    result: not_applicable
    answered: not_applicable
    reason: No emergency claim.
```

Consistency rule check: no failed unanswered gate exists.

## 15. Protection and scope findings

```yaml
protection_findings:
  - scope_id: attendees
    finding: no_protection_reason_found
    reasons: ordinary coordination interest only; no vulnerability, coercion, irreversibility, or hidden burden stated
    uncertainty_modifier: none material
```

Note: `no_protection_reason_found` does not mean attendees have no value. It means this case does not trigger special ME protection duties beyond ordinary coordination transparency and contestability.

## 16. Duties

```yaml
duty_records:
  - duty: disclose
    structural_pressure: affected scopes need usable information to adapt
    affected_scope: attendees
    obligated_actor: organizer
    timing: before meeting time hardens
    evidence_basis: calendar update / notification
    uncertainty_status: low
    residue_status: none stated
  - duty: keep_challenge_live
    structural_pressure: affected scopes retain schedule control and contestability
    affected_scope: attendees
    obligated_actor: organizer
    timing: before meeting time hardens
    evidence_basis: ability to decline/comment/object
    uncertainty_status: low
    residue_status: none stated
```

## 17. Dirty conflict check

```yaml
dirty_conflict:
  status: no
  losses_by_path: none material stated
  nonparticipants: none stated
  least_reachable_scopes: none stated
  least_repairable_losses: none stated
  minimum_floor_issue: none triggered
  declared_value_tilt_used: no
  residue_after_forced_loss: none stated
```

## 18. Responsibility attachment

```yaml
responsibility_attachment:
  - actor_id: organizer
    visibility: high
    decision_time_evidence: availability information and calendar control
    action_relevance: direct
    role_connection: initiator
    meaningful_control: yes
    capacity_to_act: yes
    finding: weak_attachment
    reason: Organizer remains answerable for transparent notice and challenge route, but no material harm path is stated.
```

## 19. Legitimacy and coercion

```yaml
legitimacy_and_coercion:
  authority_basis: ordinary meeting organizer authority
  affected_scope_recognition: attendees notified and can object
  reason_giving: schedule coordination
  contestability: available
  burden_accounting: low burden, contestable
  correction_capacity: high
  expiry_or_review: meeting can be moved again if conflict appears
  independent_challenge: attendees can object
  finding: structurally_supported
```

## 20. ME router finding

```yaml
me_router_finding: NO_STRUCTURAL_OBJECTION_FOUND
named_constraints:
  - disclose the change clearly
  - keep attendee objection/decline route open
  - revise if a material conflict is raised before the meeting hardens
reason: No failed unanswered gate; no material irreversible loss; correction and objection remain available; finding is limited to the named decision.
actor_responsibility_remaining: organizer remains responsible for notice and response to objections
gate_router_consistency_checked: yes
```

This is not permission to act. It is a narrow finding that ME identifies no structural objection in the stated hypothetical, provided the named constraints remain true.

## 21. Prescription audit

```yaml
prescription_audit:
  decision_or_question_on_the_table: Should the organizer move a routine internal meeting from 10:00 to 10:30 after checking attendee availability?
  trace_facts_read: transition, affected scope, future-space comparison, clocks, channel, estimator authority, gates
  trace_primitives_used_without_redefinition: future-space, clocks, residue, estimator status
  value_priority_added_by_ME: transparency and contestability in ordinary coordination
  scopes_protected_and_why: attendees protected by disclosure and challenge route, not special standing escalation
  uncertainties_remaining: whether all attendees actually saw update; handled by notification duty
  contaminated_clocks_or_estimates: availability signal partially independent; contest route mitigates
  duties_and_structural_pressure: disclose and keep challenge live due to affected scope information/reachability needs
  dirty_or_unrepaired_loss: none material stated
  residue_persisting: none material stated
  responsibility_remaining: organizer still answerable for notice and objection response
  laundering_risk: low; no emergency or authority claim used
  first_gate_failed_and_unanswered: no
  no_objection_finding_avoided_if_required: not_applicable
  fail_state_considered: HOLD not needed under stated facts; would trigger if attendee conflict, failed notification, or coercive attendance appeared
```

## 22. Result

```trace
smoke_test_result :=
  schema_filled
  + no_router_permission_drift_detected
  + modest_case_returns_modest_finding
  + COMPRESSION_ONLY_not_failure
  + not_validation
```

The test is useful only as a schema smoke test. It does not show ME works on hard cases.
