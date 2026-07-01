# Mechanical Ethics Book Architecture v0.1 — 2026-06-27

Status: planning surface. Not book text. Not canon. Not validation.

Purpose: define the scope, structure, interface, honesty rules, and build order for the new Mechanical Ethics book before drafting prose.

## 1. Current transition

```trace
TRACE_status :=
  structurally_coherent
  + transmissible
  + testable
  + not_validated
  + major_rewrites_paused_as_workflow

ME_status :=
  next_major_build
  + fresh_human_facing_book
  + middle_out_origin
  + old_books_reference_only
```

TRACE describes transitions under uncertainty. Mechanical Ethics says what follows after the field has been seen honestly.

This document belongs in the Mechanical Ethics repository because it is the first control surface for the new prescriptive artifact. It does not move TRACE into this repository and does not redefine TRACE.

## 2. What everybody is asking ME to answer

The old ME books and recent external reviews converge on one demand: TRACE refused to decide final value priority, legitimacy, acceptable sacrifice, coercion, standing, repair duty, and responsibility allocation. ME must take those questions without corrupting TRACE.

The central question:

```trace
ME_core_question :=
  "How should an acting entity constrain itself once it can see that its actions change the future-space of other continuing entities under uncertainty and time pressure?"
```

Subquestions:

```trace
ME_question_surface :=
  bootstrap_question
  + scope_question
  + uncertainty_question
  + clock_question
  + correction_duty_question
  + dirty_conflict_question
  + legitimacy_question
  + coercion_question
  + responsibility_question
  + anti_laundering_question
  + protocol_question
  + failure_question
```

Plain English:

1. Why should an acting entity constrain itself at all?
2. Who or what counts enough to create caution, protection, duty, or repair?
3. What does uncertainty require?
4. When does timing create duty?
5. What does correction require after loss or error?
6. What should happen when every available action causes loss?
7. When may authority bind others?
8. When may coercion be used, and what constrains it?
9. When does visibility create responsibility?
10. How does ME avoid becoming a justification machine?
11. What exactly does a reader do next?
12. When must ME refuse to decide?

## 3. Scope

Mechanical Ethics is:

```trace
Mechanical_Ethics :=
  human_facing_book
  + protocol_specification
  + responsibility_grammar
  + anti_laundering_system
```

Mechanical Ethics is not:

```trace
Mechanical_Ethics !=
  one_true_morality
  + philosophy_survey
  + policy_manual
  + automatic_decision_machine
  + TRACE_validation_claim
```

The book should be readable by a human who has not read TRACE. If TRACE is available, the grammar should line up. If TRACE is not available, ME should still guide the reader from first premise to constrained action.

## 4. Starting premise

Do not start with ethics, law, utility, rights, personhood, dignity, blame, or final value priority.

Start here:

```trace
origin :=
  something_is_here
  + it_perceives_partially
  + it_can_change_something
  + it_does_not_know_everything
  + time_passes
```

The book starts with the simplest middle-out premise and ends with the best prescriptive answers currently available.

The end must remain provisional, auditable, and revisable. It must not present itself as final moral law.

## 5. Book arc

```trace
book_motion :=
  minimal_premise
  -> structural_pressure
  -> unavoidable_constraint
  -> practical_duties
  -> dirty_conflict_protocol
  -> responsibility
  -> civilization
  -> limits_and_revision
```

Plain English:

Something exists. It acts under uncertainty. Other things also continue. Actions interfere. Time closes paths. Correction can arrive too late. Opportunity can expire. Residue remains. From there, the book earns its first prescriptions.

## 6. One-book structure

Use one book with numbered parts, chapters, and sections. Do not use Roman numerals.

Working title:

```text
Mechanical Ethics
A Human Manual for Acting Under Uncertainty
```

Working structure:

```text
Part 0 — How to Read This Book
Part 1 — The Entity That Wakes
Part 2 — The World That Pushes Back
Part 3 — Layers of Action
Part 4 — Harm, Time, and Future-Space
Part 5 — The TRACE → ME Interface
Part 6 — The First Gates
Part 7 — Protection, Standing, and Scope
Part 8 — Correction, Repair, and Residue
Part 9 — Dirty Conflicts
Part 10 — Responsibility After Visibility
Part 11 — Power, Legitimacy, and Coercion
Part 12 — Civilization Under Uncertainty
Part 13 — Artificial Systems and Future Minds
Part 14 — Case Records and Use Protocols
Part 15 — Limits, Failures, and Open Questions
Appendices
```

## 7. Part-level outline

### Part 0 — How to Read This Book

Purpose: prevent misreadings.

```text
0.1 This Is Not a Moral Oracle
0.2 TRACE and Mechanical Ethics
0.3 What This Book Can Do
0.4 What This Book Refuses to Do
0.5 How to Use the Numbered Protocols
```

ME is a disciplined prescriptive layer. It does not remove responsibility from the person or institution acting.

### Part 1 — The Entity That Wakes

Purpose: establish the middle-out origin.

```text
1.1 Something Is Here
1.2 It Perceives Partially
1.3 It Can Change Something
1.4 It Does Not Know Everything
1.5 Time Passes
1.6 Inaction Also Changes the World
```

### Part 2 — The World That Pushes Back

Purpose: show ethics emerging from interaction.

```text
2.1 You Are Not Alone
2.2 Other Things Continue
2.3 Actions Interfere
2.4 Not All Futures Fit Together
2.5 Conflict Before Morality
```

```trace
ethics_emerges_when :=
  multiple_continuing_entities
  + incompatible_effects
  + uncertainty
  + time_pressure
```

### Part 3 — Layers of Action

Purpose: restore causal, selective, and reflective layers without making them ornamental.

```text
3.1 The Causal Layer
3.2 The Selective Layer
3.3 The Reflective Layer
3.4 The Gate Between Selection and Responsibility
3.5 Local Reward Pull
3.6 When Systems Learn the Wrong Thing
```

### Part 4 — Harm, Time, and Future-Space

Purpose: connect harm, benefit, timing, opportunity, and correction. Part 4 explains TRACE-owned primitives for a TRACE-naive reader; it must quote and reference them, not redefine them.

```text
4.1 Future-Space
4.2 Options, Reachability, and Information
4.3 Harm as Narrowing
4.4 Benefit as Expansion
4.5 Loss Clocks
4.6 Opportunity Clocks
4.7 Correction That Arrives Too Late
4.8 Opportunity That Arrives Too Late
```

```trace
F_x(t) := (O_x(t), R_x(t), I_x(t))
comparison := expanded | narrowed | mixed | unchanged | unknown | incomparable
```

No fake scalar subtraction.

### Part 5 — The TRACE → ME Interface

Purpose: define the strict handoff.

```text
5.1 Description Is Read-Only
5.2 What TRACE Provides
5.3 What ME Adds
5.4 Router Labels
5.5 Value-Crux Exits
5.6 Contaminated Signals
5.7 The Residue Ledger
5.8 The Prescription Audit
```

```trace
TRACE_outputs :=
  transition
  + affected_scopes
  + F_comparison
  + clocks
  + estimator_authority
  + correction_channels
  + opportunity_routes
  + burden_shift
  + residue
  + status_label
  + confidence

ME_outputs :=
  protect
  + pause
  + disclose
  + preserve
  + repair
  + compensate
  + constrain
  + escalate
  + hold
  + record_residue
```

Important rule:

```trace
TRACE_description != ME_permission
```

TRACE output can trigger ME analysis. It cannot itself authorize action.

### Part 6 — The First Gates

Purpose: first prescriptive layer, generated from structural pressure.

```text
6.1 Do Not Hide Loss
6.2 Do Not Erase Affected Scopes
6.3 Do Not Treat Uncertainty as Certainty
6.4 Do Not Pretend Repair Where Residue Remains
6.5 Do Not Let Correction Channels Become Harm Carriers
6.6 Do Not Let the Assessed Actor Set Every Clock
6.7 Do Not Use Emergency to Launder Prior Failure
```

These are anti-laundering gates, not the whole moral theory.

### Part 7 — Protection, Standing, and Scope

Purpose: handle moral standing without pretending the boundary is simple.

```text
7.1 Scope Is Not Personhood
7.2 Reasons for Protection
7.3 Uncertainty Raises Caution
7.4 Vulnerability and Dependency
7.5 Participation and Consent
7.6 Non-Human Life
7.7 Future Persons
7.8 Artificial Systems
7.9 When Standing Remains Unresolved
```

```trace
scope_protection :=
  graduated
  + precautionary
  + reason_recorded
  + challengeable
  - hidden_worth_ladder
```

### Part 8 — Correction, Repair, and Residue

Purpose: import the strongest old Book II material without inheriting the old structure.

```text
8.1 Correction Is Not Repair
8.2 Repair Must Touch the Path
8.3 Slow the Write
8.4 Route the Burden Back
8.5 Preserve Contradiction
8.6 Keep Contestability Live
8.7 Proof Is Not Theatre
8.8 Residue Remains
8.9 Duties After Late Correction
8.10 Stewardship Over Time
```

### Part 9 — Dirty Conflicts

Purpose: handle ME's hardest job.

```text
9.1 When Every Action Causes Loss
9.2 Why Clean Answers Are Usually Lies
9.3 No Netting Without Permission
9.4 The Least-Repairable Loss
9.5 The Least-Reachable Scope
9.6 Consent, Compensation, and Burden Return
9.7 Triage Without Moral Disappearance
9.8 Residue After Forced Loss
9.9 When ME Must Hold or Escalate
```

Working protocol:

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

choose_least_unrepairable_path_if_action_required :=
  declared_value_tilt
  + requires_its_own_audit_chain

preserve_minimum_floors :=
  open_wound
  + floors_undefined
  + who_sets_them_unresolved
```

This does not clean the conflict. It prevents sacrifice laundering.

### Part 10 — Responsibility After Visibility

Purpose: import the strongest old Book III material.

```text
10.1 Visibility Is Not Blame
10.2 Foresight Is Not Omniscience
10.3 Prediction Is Not Destiny
10.4 Decision-Time Evidence
10.5 Meaningful Control
10.6 Role Duty
10.7 Delegation Is Not Erasure
10.8 Automation Is Not Absolution
10.9 Responsibility Attachment
10.10 Responsibility Without Scapegoating
```

Responsibility requires visibility, action relevance, role connection, decision-time evidence, and meaningful control. It must not be built from hindsight certainty.

### Part 11 — Power, Legitimacy, and Coercion

Purpose: begin the variables TRACE explicitly punts. Highest `UNRESOLVED_VALUE_CRUX` risk. Desert, punishment, and legitimacy default to `UNRESOLVED_VALUE_CRUX` unless a structural chain is shown; this part frames, it does not solve.

```text
11.1 Power That Changes Futures
11.2 Legitimacy as Answerable Authority
11.3 Coercion Under Uncertainty
11.4 Emergency Power
11.5 Punishment and Desert
11.6 Dignity and Recognition
11.7 Authority That Expires
11.8 When Force May Be Used
11.9 When Force Must Stop
```

Candidate structure:

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

This is a candidate, not final doctrine.

### Part 12 — Civilization Under Uncertainty

Purpose: scale ME from cases to systems.

```text
12.1 Civilization as Correctability
12.2 Institutions as Memory
12.3 Law as Slowed Power
12.4 Markets and Local Reward Pull
12.5 Public Systems and Burden Routing
12.6 Trust Under Pressure
12.7 Maintenance, Stewardship, and Decay
12.8 Progress Without Sacrifice Laundering
```

```trace
civilization :=
  organized_attempt
  to_remain_correctable_under_uncertainty
  while_preserving_future_possibility
  across_many_scopes
```

### Part 13 — Artificial Systems and Future Minds

Purpose: connect to AI and future minds without making the whole book only about AI.

```text
13.1 Artificial Systems as Acting Systems
13.2 Optimization and Local Reward Pull
13.3 Opacity and Estimator Contamination
13.4 Human-in-the-Loop Theatre
13.5 Delegated Power
13.6 Artificial Moral Standing
13.7 Future Minds
13.8 Alignment as Corrigible Constraint
13.9 What AI Systems Must Not Be Allowed to Hide
```

ME can constrain artificial systems before deciding whether any artificial system is a protected scope.

`Corrigible constraint` carries an open tension: maximal corrigibility trades against the capacity for binding commitment and trust. Mark as open, not settled.

### Part 14 — Case Records and Use Protocols

Purpose: make the book operational.

```text
14.1 How to Build a Case Record
14.2 TRACE on the Left, ME on the Right
14.3 Router Labels
14.4 Prescription Audit
14.5 Residue Ledger
14.6 Challenger Function
14.7 Worked Case 1 — Human Administrative Route
14.8 Worked Case 2 — Platform or Algorithmic System
14.9 Worked Case 3 — Dirty Conflict
14.10 Low-Fit Case Returning COMPRESSION_ONLY
```

### Part 15 — Limits, Failures, and Open Questions

Purpose: end honestly.

```text
15.1 What ME Cannot Decide
15.2 UNKNOWN Is Not Failure
15.3 When ME Makes Things Worse
15.4 Value Lock-In
15.5 Authority Creep
15.6 Paralysis Risk
15.7 Open Problems
15.8 How This Book Should Be Tested
```

The ending should be disciplined, not triumphant.

## 8. Handoff rules

```trace
handoff_rules :=
  TRACE_outputs_are_read_only
  + ME_may_not_reestimate_TRACE_clocks_silently
  + ME_may_not_invent_missing_facts
  + ME_may_not_treat_TRACE_status_as_permission
  + ME_must_record_when_it_adds_value_priority
  + ME_must_record_when_it_uses_domain_law_or_external_norms
  + shared_primitives_are_TRACE_owned
  + ME_may_explain_but_not_redefine_shared_primitives
  + ME_quotes_canonical_TRACE_definition_and_marks_it_TRACE_owned
  + if_definitions_diverge_TRACE_definition_governs
```

Shared TRACE-owned primitives include:

```trace
TRACE_owned_shared_primitives :=
  future_space
  + O_R_I
  + loss_clock
  + opportunity_clock
  + residue
  + estimator_status
```

If ME finds TRACE insufficient, ME builds an adapter or requests more information. It does not rewrite TRACE.

## 9. Router states

ME needs output states and fail states. Router states are findings and recommendations, not authorizations.

```trace
router_states_are_findings_not_authorizations :=
  ME_router_output := finding + recommendation + duty + constraint
  ME_router_output != permission_to_act
  no_router_state_discharges_actor_responsibility
```

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

Working rule:

```trace
if data_status == UNKNOWN
and action_irreversible == true:
  default := HOLD_OR_ESCALATE
```

Working contaminated-signal rule:

```trace
if estimator_status == CONTAMINATED_SIGNAL:
  demote_evidential_authority
  + require_independent_check
  + restrict_irreversible_action
  + preserve_challenge_route
  - demote_moral_standing_by_default
```

Contamination demotes evidential authority. It does not automatically demote moral standing or scope protection.

## 10. Honesty rules

```trace
honesty_rules :=
  no_roman_numerals
  + no_should_without_structural_chain
  + no_TRACE_validation_claim
  + no_AI_agreement_as_proof
  + no_fake_precision
  + no_hidden_clock_setting
  + no_moral_status_by_stealth
  + no_clean_solution_to_dirty_conflict
  + no_repair_without_residue_check
  + no_blame_from_visibility_alone
  + no_prediction_as_destiny
  + no_automatic_action_without_fail_state
```

Plain English:

ME may prescribe, but every major prescription must leave an audit trail. If a chapter cannot show what structural pressure generated its prescription, the chapter is not ready.

## 11. Old material handling

```trace
old_ME_material :=
  quarry
  + omission_check
  + reusable_language
  - structure_authority
  - current_canon
```

Mapping:

```trace
old_Book_I :=
  exposed_route
  + correction_too_late
  + ordinary_survivability
  + replayable_truth
  + bounded_power
  + contestability
  + repair_before_hardening

old_Book_II :=
  repair_touches_path
  + proof_not_theatre
  + bounded_constraint
  + burden_return
  + preserve_contradiction
  + stewardship

old_Book_III :=
  visibility_not_blame
  + foresight_not_omniscience
  + decision_time_evidence
  + meaningful_control
  + role_duty
  + delegation_not_erasure
```

Use these as material after the new architecture is fixed. Do not rebuild the old trilogy.

## 12. Build order

```trace
build_order :=
  1_architecture_surface
  -> 2_Claude_review
  -> 3_patch_architecture
  -> 4_first_prose_skeleton
  -> 5_TRACE_ME_interface_schema
  -> 6_opening_page
  -> 7_case_record_template
  -> 8_old_material_mapping
  -> 9_first_full_part
```

No prose-first build. Prose comes after architecture survives review.

## 13. Acceptance tests

```trace
acceptance_tests :=
  reader_can_start_without_TRACE
  + TRACE_reader_sees_shared_grammar
  + old_books_do_not_control_structure
  + ME_can_fail_or_hold
  + dirty_conflict_not_laundered
  + responsibility_not_hindsight_blame
  + AI_section_not_overclaiming
  + no_validation_claim
  + no_fake_precision
  + no_roman_numerals
```

## 14. Current review request

This architecture should be sent to Claude before any prose build.

Review should focus on:

1. Is the scope too broad for one book?
2. Does the book still start cleanly middle-out?
3. Does Part 5 provide enough interface spine?
4. Does ME accidentally become an automatic moral engine?
5. Are dirty conflicts handled honestly?
6. Are fail states strong enough?
7. Does the old trilogy leak too much structure into the new book?
8. What is merge-blocking before first prose skeleton?

## 15. Claude review result

Claude returned `PATCH_THEN_MERGE` with a non-independence flag.

The accepted patches were:

```trace
accepted_review_patches :=
  shared_TRACE_primitives_single_source_rule
  + router_outputs_are_findings_not_authorizations
  + Part_11_framing_not_solving_warning
  + dirty_conflict_value_tilt_and_floor_open_wound_flags
  + corrigible_constraint_open_tension_flag
```

This review is useful architecture pressure. It is not validation.
