# TRACE → Mechanical Ethics Interface Schema v0.1 — 2026-06-27

Status: operator-support surface. Not book prose. Not canon. Not validation.

Purpose: define how Mechanical Ethics consumes a TRACE case record without rewriting TRACE, and how ME produces findings, duties, constraints, holds, escalations, and residue records without pretending to authorize action automatically.

## 1. Boundary rule

```trace
TRACE := descriptive_case_map
ME := prescriptive_interpretation_layer

TRACE_description != ME_permission
ME_router_output != permission_to_act
TRACE_outputs_are_read_only := true
```

Plain English:

TRACE may tell ME what is visible in the transition. ME may say what duties, constraints, holds, escalations, or repair obligations follow under ME's own rules. Neither layer removes responsibility from the actor.

## 2. Single-source primitive rule

```trace
shared_primitives_are_TRACE_owned := true

TRACE_owned_shared_primitives :=
  future_space
  + O_R_I
  + loss_clock
  + opportunity_clock
  + residue
  + estimator_status
```

ME may quote and explain these for a human reader. ME may not redefine them. If a definition in ME diverges from canonical TRACE, the TRACE definition governs.

## 3. TRACE input packet

A complete TRACE input packet should provide the following fields where known. Missing fields are allowed, but they must be marked unknown rather than silently filled.

```trace
TRACE_input_packet :=
  case_identity
  + transition_description
  + actor_map
  + affected_scope_map
  + future_space_comparison
  + clocks
  + correction_and_opportunity_channels
  + estimator_authority
  + burden_shift
  + residue
  + status_label
  + confidence
  + unknowns_and_disputes
```

### 3.1 Case identity

```trace
case_identity :=
  case_id
  + title
  + domain
  + date_or_time_window
  + source_status
  + prepared_by
  + review_status
```

### 3.2 Transition description

```trace
transition_description :=
  start_state
  + change_or_proposed_change
  + end_state_or_expected_end_state
  + action
  + inaction_or_delay_option
  + mechanism
```

Inaction is a transition if it changes the future-space of affected scopes.

### 3.3 Actor map

```trace
actor_map :=
  initiators
  + designers
  + operators
  + maintainers
  + reviewers
  + beneficiaries
  + delegated_systems
  + blockers_or_gatekeepers
```

Actor map records position and control. It does not assign blame by itself.

### 3.4 Affected scope map

```trace
affected_scope_map :=
  scope_id
  + scope_type
  + affected_how
  + continuation_interest
  + vulnerability_or_dependency
  + participation_or_consent_status
  + protection_reason
  + disputed_status
```

Scope reasons are not a worth ladder. ME may later assign protection duties, but the TRACE record does not decide final standing.

### 3.5 Future-space comparison

```trace
future_space_comparison :=
  scope_id
  + O_change
  + R_change
  + I_change
  + comparison_status
  + confidence
  + reason
```

Allowed comparison statuses:

```trace
comparison_status :=
  expanded
  | narrowed
  | mixed
  | unchanged
  | unknown
  | incomparable
```

No fake scalar subtraction. ME must not net one scope's expansion against another scope's contraction without an explicit ME audit chain.

### 3.6 Clocks

```trace
clocks :=
  loss_clock
  + opportunity_clock
```

Loss clock:

```trace
loss_clock :=
  T_det
  + T_route
  + T_corr
  + T_irr
  + clock_fit
  + confidence
```

Opportunity clock:

```trace
opportunity_clock :=
  T_access
  + T_uptake
  + T_integrate
  + T_opp
  + clock_fit
  + confidence
```

Clock fit values:

```trace
clock_fit :=
  likely_in_time
  | borderline
  | likely_too_late
  | already_too_late
  | unknown
```

### 3.7 Correction and opportunity channels

```trace
channel_record :=
  channel_id
  + channel_type
  + reachable_by_scope
  + authority_to_change_path
  + timing_capacity
  + cost_or_burden
  + evidence_requirements
  + independence
  + known_failure_modes
```

A channel can itself become a harm carrier if it consumes time, burden, evidence, or reachability faster than it repairs the path.

### 3.8 Estimator authority

```trace
estimator_authority :=
  estimate_id
  + what_is_estimated
  + estimator_identity
  + estimator_role
  + incentive_position
  + independence
  + affected_scope_challenge_route
  + contamination_status
```

Contamination values:

```trace
contamination_status :=
  independent_signal
  | partially_independent_signal
  | contaminated_signal
  | unknown
```

Default rule:

```trace
if estimator_is_assessed_actor:
  contamination_status := contaminated_signal by default
```

ME consequence:

```trace
CONTAMINATED_SIGNAL_response :=
  demote_evidential_authority
  + require_independent_check_if_material
  + restrict_irreversible_action_if_unchecked
  + preserve_challenge_route
  - demote_moral_standing_by_default
```

### 3.9 Burden shift

```trace
burden_shift :=
  burden_type
  + from_actor_or_system
  + to_scope
  + voluntary_or_forced
  + contestable
  + repairable
  + evidence
```

### 3.10 Residue

```trace
residue :=
  loss_not_restored
  + time_not_returned
  + trust_damage
  + opportunity_expired
  + record_scar
  + recurrence_risk
  + acknowledgement_needed
```

Residue is not erased by correction unless a specific residue element is actually repaired.

### 3.11 TRACE status label

```trace
TRACE_status_label :=
  UNKNOWN
  | COMPRESSION_ONLY
  | CONTAMINATED_SIGNAL
  | PARTIAL_SIGNAL
  | STRONG_SIGNAL
  | REGRESSION
```

ME must not treat `STRONG_SIGNAL` as permission. ME must not treat `COMPRESSION_ONLY` as failure. ME must not treat `UNKNOWN` as automatic paralysis where reversible action or evidence-gathering remains possible.

## 4. ME interpretation layers

ME reads the TRACE packet through ordered interpretation layers.

```trace
ME_layers :=
  intake_integrity_check
  -> protection_and_scope_check
  -> uncertainty_and_reversibility_check
  -> first_gates_check
  -> duty_derivation
  -> dirty_conflict_check
  -> responsibility_attachment_check
  -> legitimacy_and_coercion_check
  -> router_finding
  -> residue_ledger_update
  -> prescription_audit
```

### 4.1 Intake integrity check

Questions:

1. Is the TRACE packet complete enough to read?
2. Which fields are unknown?
3. Which estimates are contaminated?
4. Which facts are disputed?
5. Which definitions are TRACE-owned and therefore not editable by ME?

Possible output:

```trace
intake_output :=
  usable
  | usable_with_unknowns
  | needs_more_TRACE_mapping
  | hold_due_to_missing_material_field
```

### 4.2 Protection and scope check

Questions:

1. Which scopes have protection reasons?
2. Which scopes are vulnerable, dependent, nonparticipating, or unable to contest?
3. Which scope statuses remain disputed?
4. Does uncertainty increase caution?

Output:

```trace
scope_output :=
  protection_triggered
  | precaution_triggered
  | standing_unresolved
  | no_protection_reason_found
```

### 4.3 Uncertainty and reversibility check

Questions:

1. Is the proposed action reversible, partially reversible, or irreversible?
2. Are relevant clocks unknown or contaminated?
3. Would action close a correction or opportunity window?
4. Would delay itself narrow future-space?

Rule:

```trace
if data_status == UNKNOWN
and action_irreversible == true:
  default := HOLD_OR_ESCALATE
```

This is a default, not an absolute ban. Emergency or dirty-conflict conditions may override only through an explicit audit chain.

### 4.4 First gates check

```trace
first_gates :=
  do_not_hide_loss
  + do_not_erase_affected_scopes
  + do_not_treat_uncertainty_as_certainty
  + do_not_pretend_repair_where_residue_remains
  + do_not_let_correction_channels_become_harm_carriers
  + do_not_let_assessed_actor_set_every_clock
  + do_not_use_emergency_to_launder_prior_failure
```

Each gate should return:

```trace
gate_result :=
  pass
  | fail
  | uncertain
  | not_applicable
```

A failed gate does not automatically decide the case. It creates a reason that must be answered before proceeding.

### 4.5 Duty derivation

ME duties are derived from structural pressure, not from TRACE output alone.

```trace
duty_classes :=
  disclose
  + preserve_evidence
  + slow_or_pause
  + independent_review
  + keep_challenge_live
  + repair_path
  + compensate
  + record_residue
  + prevent_recurrence
  + escalate
  + hold
```

No duty should be recorded without a route:

```trace
duty_record :=
  duty
  + structural_pressure
  + affected_scope
  + obligated_actor
  + timing
  + evidence_basis
  + uncertainty_status
  + residue_status
```

### 4.6 Dirty conflict check

Dirty conflict exists where every available action causes material loss.

```trace
dirty_conflict_protocol :=
  map_losses
  + identify_irreversibility
  + identify_repairability
  + identify_nonparticipants
  + identify_lowest_reachability
  + preserve_minimum_floors
  + choose_least_unrepairable_path_if_action_required
  + record_residue
  + assign_repair_duties
```

Open flags:

```trace
choose_least_unrepairable_path_if_action_required :=
  declared_value_tilt
  + requires_its_own_audit_chain

preserve_minimum_floors :=
  open_wound
  + floors_undefined
  + who_sets_them_unresolved
```

ME may recommend a constrained path under dirty conflict. It must not describe the loss as clean.

### 4.7 Responsibility attachment check

Responsibility attachment is not blame. It is a trace point.

```trace
responsibility_attachment_factors :=
  visibility
  + decision_time_evidence
  + action_relevance
  + role_connection
  + meaningful_control
  + capacity_to_act
  + delay_or_omission
  + delegation_or_maintenance
```

Output:

```trace
responsibility_output :=
  no_attachment_found
  | weak_attachment
  | material_attachment
  | strong_attachment
  | unresolved_due_to_missing_evidence
```

Do not build responsibility from hindsight certainty.

### 4.8 Legitimacy and coercion check

Part 11 is framing, not solving. Desert, punishment, legitimacy, dignity, and justified force default to `UNRESOLVED_VALUE_CRUX` unless a structural chain is shown.

Candidate legitimacy chain:

```trace
legitimacy_candidate :=
  authority_basis
  + affected_scope_recognition
  + reason_giving
  + contestability
  + burden_accounting
  + correction_capacity
  + expiry_or_review
  + independent_challenge
```

Output:

```trace
legitimacy_output :=
  structurally_supported
  | structurally_defective
  | unresolved_value_crux
  | outside_ME_current_scope
```

## 5. ME router findings

Router outputs are findings and recommendations. They are not authorizations.

```trace
router_states_are_findings_not_authorizations :=
  ME_router_output := finding + recommendation + duty + constraint
  ME_router_output != permission_to_act
  no_router_state_discharges_actor_responsibility
```

Router states:

```trace
ME_router :=
  NO_STRUCTURAL_OBJECTION_FOUND
  PROCEED_ONLY_WITH_NAMED_CONSTRAINTS
  PAUSE
  HALT
  ESCALATE
  REPAIR_REQUIRED
  COMPENSATION_REQUIRED
  INDEPENDENT_REVIEW_REQUIRED
  HOLD
  UNRESOLVED_VALUE_CRUX
  REGRESSION_RISK
```

### 5.1 Router state definitions

`NO_STRUCTURAL_OBJECTION_FOUND` means ME found no structural objection within the available record. It is not a statement that the action is right, lawful, safe, legitimate, or authorized.

`PROCEED_ONLY_WITH_NAMED_CONSTRAINTS` means action should not continue unless the named constraints are in place.

`PAUSE` means the transition should be temporarily slowed or suspended while a material uncertainty, channel, clock, or protection issue is resolved.

`HALT` means the transition should stop under the current record because proceeding would violate a gate, close correction, cause unaddressed irreversible loss, or rely on defective authority.

`ESCALATE` means the case must move to an actor or forum with better authority, independence, evidence access, or protection capacity.

`REPAIR_REQUIRED` means repair duties exist and must touch the path, not only the description of the path.

`COMPENSATION_REQUIRED` means a burden or loss requires compensatory response, while acknowledging that compensation does not erase residue by itself.

`INDEPENDENT_REVIEW_REQUIRED` means the current estimate, clock, channel, or authority claim cannot bear the decision because it is contaminated, incomplete, or insufficiently independent.

`HOLD` means ME cannot safely route to action or non-action without more information, clearer values, independent review, or protective conditions.

`UNRESOLVED_VALUE_CRUX` means the case depends on desert, legitimacy, dignity, acceptable sacrifice, moral status, or justified coercion beyond what ME can settle from the current structural record.

`REGRESSION_RISK` means applying ME as currently framed may worsen the analysis, launder authority, create paralysis, or hide value judgment behind procedure.

## 6. Output packet

A complete ME output packet should include:

```trace
ME_output_packet :=
  case_id
  + intake_status
  + gate_results
  + protection_findings
  + duty_records
  + dirty_conflict_status
  + responsibility_attachment
  + legitimacy_or_coercion_status
  + router_finding
  + named_constraints
  + residue_ledger_update
  + unresolved_questions
  + prescription_audit
```

## 7. Prescription audit

Every ME output must answer:

1. What TRACE facts were read?
2. Which TRACE-owned primitives were used without redefinition?
3. What value priority did ME add?
4. Which affected scopes were protected, and why?
5. Which uncertainties remain?
6. Which clocks or estimates were contaminated?
7. What duties were derived, and from what structural pressure?
8. What loss remains dirty or unrepaired?
9. What residue persists?
10. What actor still bears responsibility after the finding?
11. Could ME be laundering authority, delay, or sacrifice?
12. Does ME need to return `HOLD`, `ESCALATE`, `UNRESOLVED_VALUE_CRUX`, or `REGRESSION_RISK`?

## 8. Anti-laundering constraints

```trace
anti_laundering_constraints :=
  no_TRACE_output_as_final_justification
  + no_router_state_as_permission_slip
  + no_hidden_value_priority
  + no_fake_precision
  + no_hidden_clock_setting
  + no_unrecorded_residue
  + no_blame_from_visibility_alone
  + no_prediction_as_destiny
  + no_dirty_conflict_cleaning
```

## 9. Schema status

This schema is a first interface surface. It should be reviewed before use in worked examples.

Known open wounds:

```trace
open_wounds :=
  scope_floor_foundation
  + acceptable_sacrifice
  + legitimacy_and_coercion
  + dirty_conflict_value_tilts
  + corrigibility_vs_binding_commitment
  + validation_of_usefulness
```

Do not hide these by adding more machinery.
