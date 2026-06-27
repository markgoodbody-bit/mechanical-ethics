# Part 14 — Case Records and Use Protocols

Status: first draft. Incomplete. Not canon.

## 14.1 Why Use Protocols Belong Near the End

The book has deliberately waited to put the machinery here.

The reader first had to move through the human argument: something is here; it acts under partial perception; it is not alone; action changes future-space; time closes paths; description is not permission; gates keep the record honest; protection needs reasons; correction is not repair; dirty conflicts remain dirty; responsibility follows visibility only through role, evidence, and control; power must answer; civilization must remain correctable and support shared viable becoming; artificial systems must not hide behind opacity or optimized false goods.

Only now should the operator machinery appear.

```trace
use_protocol_position :=
  after_human_spine
  not_inside_human_spine
```

This order protects the book from becoming a form before it becomes an argument.

A case record is useful only if the reader understands why the fields matter. Otherwise the template becomes another bureaucratic ritual: complete the boxes, produce the finding, claim discipline, move on.

Mechanical Ethics should not become that.

The use protocols are not the soul of the book. They are the handle. They help a reader, reviewer, institution, or system apply the argument without silently changing it.

The shortest adequate record is usually the best record.

```trace
protocol_minimization_rule :=
  use_smallest_record
  that_preserves_route_visibility
  + uncertainty_status
  + affected_scope
  + timing
  + viable_becoming_change
  + residue
  + responsibility_remaining
```

A low-stakes case should not become a ceremonial file. A high-stakes case should not be compressed until the path effect disappears. The point is not to create paperwork. The point is to keep a live route from question to finding without hiding the parts that matter.

The protocol should expand only when the situation demands it.

```trace
anti_bureaucracy_rule :=
  record_enough_to_keep_answerability_alive
  - perform_framework_for_its_own_sake
```

## 14.2 How to Build a Case Record

A case record begins with the decision or question on the table.

Without that, the finding floats.

```trace
case_record_begins_with :=
  decision_or_question_on_the_table
```

The live question should be concrete enough to route. Not "what is justice here?" but "should this decision proceed?" "should this channel be treated as adequate correction?" "should this system pause enforcement?" "what repair duties remain after late correction?" "does this case require escalation because standing or authority remains unresolved?" "does the claimed benefit hide remaining burden?"

A minimum viable case record contains:

```trace
minimum_viable_case_record :=
  decision_or_question_on_the_table
  + transition_description
  + at_least_one_affected_scope
  + future_space_comparison_for_that_scope
  + viable_becoming_record
  + at_least_one_clock_using_TRACE_bands
  + first_gates_results
  + router_finding
  + prescription_audit
```

Everything else should be filled when known. Missing fields must be marked missing or unknown, not silently invented.

The discipline is simple: do not pretend to know what the record does not show.

## 14.3 TRACE on the Left, ME on the Right

For full operator use, the case record should keep description and prescription separated.

```trace
left_side := TRACE_or_descriptive_case_map
right_side := ME_prescriptive_response
```

Left side asks:

```trace
descriptive_questions :=
  what_changed
  + who_or_what_was_affected
  + how_future_space_changed
  + what_clocks_apply
  + who_estimated
  + what_channels_exist
  + what_burden_shifted
  + what_claimed_good_appears
  + what_residue_remains
```

Right side asks:

```trace
prescriptive_questions :=
  which_gates_fail
  + which_scopes_need_protection
  + which_duties_follow
  + whether_conflict_is_dirty
  + whether_claimed_good_survives_audit
  + who_must_answer
  + whether_power_is_answerable_enough
  + what_router_finding_is_safe
```

The left side must not quietly become permission. The right side must not silently rewrite the left side.

If the descriptive record says unknown, Mechanical Ethics must either work with the unknown, seek more mapping, hold, escalate, or explain why reversible action remains acceptable despite uncertainty.

A clean case record preserves the firewall.

## 14.4 Viable Becoming Record

The value-spine patch requires one new discipline: case records must not track harm alone.

They must also track what opens, what closes, and what remains viable for affected scopes.

```trace
viable_becoming_record :=
  affected_scope
  + continuation_change
  + orientation_change
  + capacity_change
  + relation_change
  + repairability_change
  + meaningful_future_space_change
  + confidence
```

The record can be short. It can use plain language. It does not require false measurement. But it must ask the question.

A transition may reduce one kind of harm while damaging trust. It may expand access while shifting burden. It may preserve safety while narrowing relation. It may speed correction while reducing contestability. It may create opportunity for one scope while closing opportunity for another.

The viable becoming record prevents the case from being flattened into one word: harm, benefit, efficiency, safety, progress, compliance, or risk.

```trace
viable_becoming_record_rule :=
  no_single_label_can_replace
  scoped_change_record
```

This field should remain uncertain where the record is uncertain.

## 14.5 Claimed Good and Positive Audit

Mechanical Ethics now needs a positive audit as well as a harm audit.

A claimed good may be real. It may justify action. It may preserve life, repair a route, expand access, reduce burden, rebuild trust, support learning, coordinate shared work, or prevent worse loss.

But a claimed good can also hide burden.

```trace
claimed_good_audit :=
  what_good_is_claimed
  + for_whom
  + what_viable_becoming_expands
  + what_viable_becoming_contracts
  + who_carries_cost_or_risk
  + what_correction_stays_live
  + what_residue_remains
```

This is the operational form of benefit is not absolution.

```trace
benefit_is_not_absolution_operational :=
  claimed_good
  requires
    affected_scope_record
    + burden_record
    + correction_route
    + residue_check
```

A positive audit should not become optimism theatre. It should not list benefits as a shield. It should test whether the claimed benefit actually reaches affected scopes, whether the route remains contestable, and whether remaining burden is visible.

A good case record can therefore say: this transition appears to create a real good, under stated uncertainty, but it still imposes residue and duties.

## 14.6 Router Labels as Findings, Not Authorizations

Router labels are often where misuse begins.

They look official. They compress complexity. They can be copied into decision memos. They can become institutional shields.

So every router label must be read narrowly.

```trace
ME_router :=
  NO_STRUCTURAL_OBJECTION_FOUND
  | PROCEED_ONLY_WITH_NAMED_CONSTRAINTS
  | PAUSE
  | HALT
  | ESCALATE
  | REPAIR_REQUIRED
  | COMPENSATION_REQUIRED
  | INDEPENDENT_REVIEW_REQUIRED
  | HOLD
  | UNRESOLVED_VALUE_CRUX
  | REGRESSION_RISK
```

Every router output means:

```trace
router_output :=
  finding
  + recommendation_or_constraint
  + remaining_actor_responsibility
```

It does not mean:

```trace
router_output != authorization
```

`NO_STRUCTURAL_OBJECTION_FOUND` is especially narrow. It means no structural objection was found in the available record for the named decision or question. It does not mean the action is right, lawful, legitimate, safe, final, complete, or immune from later challenge.

A failed unanswered gate forbids that finding.

```trace
if any first_gate == fail and unanswered:
  router_finding != NO_STRUCTURAL_OBJECTION_FOUND
```

A failed claimed-good audit can also block clean routing.

```trace
if claimed_good_used_to_clear_action
and claimed_good_audit_missing_material_burden:
  router_finding != NO_STRUCTURAL_OBJECTION_FOUND
```

This consistency rule prevents benefit laundering.

## 14.7 Prescription Audit

Every prescription should be audited.

Not every case needs a long essay. But every case needs enough route to see why the output follows.

A prescription audit asks:

```trace
prescription_audit :=
  decision_or_question_on_the_table
  + facts_read
  + primitives_used_without_redefinition
  + value_priority_added
  + claimed_good_audit
  + scopes_protected_and_why
  + uncertainties_remaining
  + contaminated_estimates
  + duties_and_structural_pressure
  + dirty_or_unrepaired_loss
  + residue_persisting
  + responsibility_remaining
  + laundering_risk
  + fail_state_considered
```

The most important field may be `value_priority_added`.

Description alone does not decide. Mechanical Ethics adds value priorities when it says preserve correction, protect vulnerable scopes, avoid irreversible action under uncertainty, keep contestability live, record residue, choose the least-unrepairable path in dirty conflict, or preserve viable becoming where a scope depends on an actor-controlled route.

Those priorities should be visible.

If Mechanical Ethics hides its own value additions, it becomes the same kind of authority it criticizes.

## 14.8 Residue Ledger

A residue ledger records what remains.

It should be short when residue is small. It should be serious when residue is serious. It should not become ceremonial.

```trace
residue_ledger :=
  loss_not_restored
  + time_not_returned
  + trust_damage
  + opportunity_expired
  + record_scar
  + recurrence_risk
  + acknowledgement_needed
  + viable_becoming_not_restored
```

The ledger should answer:

```trace
residue_questions :=
  what_remains
  + who_carries_it
  + can_it_be_reduced
  + who_still_owes_attention
  + what_prevents_recurrence
  + what_future_remains_closed
```

Residue is where official closure often lies.

A case may be administratively closed and ethically open. A payment may be restored and time still lost. A decision may be corrected and trust still damaged. A dirty choice may be justified and the sacrificed scope still gone.

The residue ledger prevents the file from pretending the world has rewound.

## 14.9 Challenger Function

Every serious use of Mechanical Ethics needs a challenger function.

The challenger asks whether the framework is laundering what it claims to expose.

```trace
challenger_function :=
  search_for_hidden_loss
  + search_for_erased_scope
  + search_for_fake_certainty
  + search_for_hidden_value_priority
  + search_for_permission_drift
  + search_for_benefit_laundering
  + search_for_residue_erasure
```

The challenger does not need to be hostile in personality. It needs to be structurally independent enough to see what the first actor misses or benefits from missing.

A challenger may be a person, panel, reviewer, affected-scope representative, external auditor, court, ombuds route, community witness, technical auditor, or deliberately adversarial review process.

The function matters more than the label.

A captured challenger is not a challenger. A decorative challenger is not a challenger. A reviewer who cannot see the record is not a challenger. A reviewer punished for disagreement is not a challenger.

Mechanical Ethics should be built with teeth against itself.

## 14.10 Worked Case Type 1 — Human Administrative Route

A human administrative route case asks whether a public or institutional process has changed a person's future-space through decision, delay, record, classification, or burden.

Typical fields:

```trace
administrative_case :=
  decision
  + affected_person_or_group
  + record_or_rule
  + delay_or_burden
  + correction_route
  + viable_becoming_record
  + claimed_good_audit
  + residue
```

Likely questions:

Does correction arrive before hardening?

Does the affected person carry the system's uncertainty?

Is the appeal route reachable?

Was contradiction preserved?

Who set the clock?

What viable becoming changed?

What remains after correction?

This case type is where Mechanical Ethics should be most practical. It must not require the affected person to master the whole framework. The burden should remain on the system and the reviewer to make the path visible.

## 14.11 Worked Case Type 2 — Platform or Algorithmic System

A platform or algorithmic case asks whether technical mediation has changed future-space through classification, ranking, removal, recommendation, scoring, automation, or opacity.

```trace
platform_algorithmic_case :=
  system_output
  + affected_scope
  + proxy_or_objective
  + opacity_level
  + appeal_or_correction_route
  + burden_shift
  + viable_becoming_record
  + claimed_good_audit
  + monitoring_and_owner
```

Likely questions:

What proxy is being optimized?

Who carries false positives or false negatives?

Can the affected scope understand and contest the decision?

Does human review have meaningful control or only theatre?

Who owns failure when the system acts at scale?

Does the system support viable becoming, damage it, or both?

Does correction arrive before account loss, income loss, reputational loss, or access loss hardens?

The central risk is treating technical complexity as moral distance.

Mechanical Ethics should not allow that.

## 14.12 Worked Case Type 3 — Dirty Conflict

A dirty conflict case asks what to do when every available action causes material loss.

```trace
dirty_conflict_case :=
  loss_by_path
  + claimed_good_by_path
  + affected_scopes
  + viable_becoming_by_scope
  + irreversibility
  + repairability
  + least_reachable_scope
  + value_tilt
  + residue
```

Likely questions:

Is action required, or is the sense of necessity manufactured?

Who is harmed by each path?

What good is claimed by each path?

Which viable-becoming claims are incompatible?

Which losses are least repairable?

Which scopes cannot contest?

What value priority is being added?

What minimum floors apply, if any are known?

What residue remains after the chosen path?

What repair duties follow?

This case type must never return a clean answer where loss remains dirty.

## 14.13 Worked Case Type 4 — Positive Route With Burden

The value spine needs a fourth case type.

Some transitions are genuinely beneficial but still ethically incomplete.

```trace
positive_route_with_burden_case :=
  claimed_good
  + affected_scopes
  + viable_becoming_expanded
  + viable_becoming_contracted
  + burden_carrier
  + correction_route
  + residue
```

Likely questions:

What becomes newly reachable?

For whom?

Who pays the cost?

Is the benefit real or only a metric?

Can affected scopes contest the burden?

Does the positive route preserve repairability?

What residue remains despite the benefit?

This case type keeps the framework from becoming harm-only while also preventing benefit laundering.

## 14.14 Low-Fit Case Returning COMPRESSION_ONLY

Not every case needs Mechanical Ethics.

Some cases are ordinary coordination, low-stakes preference, reversible scheduling, routine choice, or simple information update. Mechanical Ethics may still describe the case, but it should not inflate itself.

```trace
low_fit_case :=
  reversible
  + low_material_loss
  + affected_scopes_not_erased
  + correction_live
  + no_serious_gate_failure
  + no_material_claimed_good_audit_needed
```

The proper result may be `COMPRESSION_ONLY` at the descriptive level and a modest ME finding such as no structural objection found under named ordinary constraints.

This is not failure.

It is good discipline.

A framework that turns every meeting move into a moral crisis is unusable. A framework that cannot distinguish low-stakes coordination from hard conflict will train people to ignore it.

Mechanical Ethics should be able to stay small when the case is small.

## 14.15 How This Part Should Be Used

Part 14 is not a new bureaucracy.

It is a way to keep the book's argument from drifting when applied.

Use the full operator schema for serious cases. Use the minimum viable record for early worked examples. Use the smoke test to check that the system does not overinflate modest cases. Use the challenger function to catch laundering.

Use less than the full schema when the case is small. Use more only when the missing detail would materially change the finding. The case record should grow because the situation demands it, not because the framework wants to display itself.

```trace
use_protocol_summary :=
  name_question
  + separate_description_from_prescription
  + fill_minimum_record
  + run_gates
  + record_viable_becoming_change
  + audit_claimed_good
  + derive_duties
  + check_dirty_conflict
  + attach_responsibility
  + audit_prescription
  + record_residue
```

The next part closes the first draft by naming limits, failures, and open questions.

A book that cannot name its limits should not be trusted with hard cases.
