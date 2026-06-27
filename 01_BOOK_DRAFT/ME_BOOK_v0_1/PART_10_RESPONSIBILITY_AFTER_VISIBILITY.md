# Part 10 — Responsibility After Visibility

Status: first draft. Incomplete. Not canon.

## 10.1 Visibility Is Not Blame

Seeing a harm path does not automatically make someone guilty.

This matters.

Mechanical Ethics is built to make hidden paths visible. That creates a risk. If every visible path becomes blame, people and institutions will learn not to see. They will avoid records, suppress warnings, narrow review, and punish those who bring bad news.

So the first rule of responsibility is restraint:

```trace
visibility != blame
```

Visibility is a condition for some forms of responsibility. It is not the whole of responsibility.

A person may see a risk without causing it. A worker may see a failure without having authority to alter it. A witness may see harm after meaningful correction has already become impossible. An institution may have a record somewhere but no functioning route for the relevant actor to know and act in time.

Blame requires more.

Mechanical Ethics therefore distinguishes seeing, warning, control, duty, omission, and fault. They are connected, but they are not identical.

The purpose is not to protect powerful actors from answerability. It is to keep answerability accurate enough to matter.

### 10.1.1 Visibility Includes Openings as Well as Closures

Visibility is not only visibility of harm.

An actor may also see that a path can be kept open, that an opportunity can still be preserved, that a route can be made reachable, that a warning can be made usable, that repair can still arrive in time, or that trust can be protected before it collapses.

Responsibility therefore attaches not only to seen closures, but sometimes to seen openings.

```trace
visible_transition_field :=
  seen_closure
  + seen_opening
  + seen_uncertainty
  + seen_clock
  + seen_affected_scope
```

This matters for the value spine. If Mechanical Ethics tracks viable becoming, then answerability concerns both what an actor damages and what an actor could reasonably preserve or reopen.

```trace
answerability_for_viable_becoming :=
  could_see_opening_or_closure
  + had_meaningful_control
  + had_time_or_route_to_act
  -> duty_to_answer_for_response
```

This does not turn every missed good into blame. That would be dishonest and paralysing. It says only that some positive routes become responsibility-relevant once they are visible, reachable, and within role-shaped control.

## 10.2 Foresight Is Not Omniscience

No actor sees the whole future.

Responsibility cannot require omniscience. It can require attention to what was visible enough at the time.

```trace
foresight_standard :=
  decision_time_evidence
  + reasonable_visibility_for_role
  + known_or_knowable_path
```

A regulator is not responsible for every possible failure no one could have detected. But it may be responsible for ignoring repeated warnings. A designer is not responsible for every unforeseen use. But it may be responsible for foreseeable failure modes in the system it releases. A minister is not responsible for every local error. But they may be responsible for a policy that routes correction too slowly by design.

Foresight is role-shaped.

A doctor, engineer, parent, judge, platform operator, prison governor, teacher, model deployer, or public authority does not have the same visibility duty as a passer-by. Role creates expected attention. Power creates expected attention. Prior warning creates expected attention. Control over the path creates expected attention.

But foresight must remain tied to what could be known at the time.

Mechanical Ethics should not use later knowledge to pretend the actor knew more than they did.

That is hindsight blame.

The same limit applies to positive futures. An actor is not blameworthy merely because a better future can be imagined later. The question is whether the opening was reasonably visible under the actor's role, evidence, time, and capacity.

```trace
positive_foresight_limit :=
  better_future_visible_later
  != better_future_reasonably_actionable_then
```

## 10.3 Prediction Is Not Destiny

Prediction changes responsibility, but it does not create destiny.

A risk model may predict harm. A doctor may predict deterioration. A regulator may predict market failure. A teacher may predict exclusion. A parent may predict danger. An institution may predict delay. A system may predict fraud, violence, default, relapse, or failure.

Prediction can help action become earlier and more careful.

But prediction is not proof that the predicted thing must happen. Nor is it permission to treat a person as if they have already done what the model predicts.

```trace
prediction != destiny
```

This is especially important for artificial systems.

A predictive model may narrow a person's future-space before any human has understood the basis of the prediction. A risk score may become a sentence. A classification may become a route. A probability may become a wall.

Mechanical Ethics asks what the prediction does.

Does it preserve options? Does it trigger support? Does it invite human attention? Does it open contestability? Or does it close access, impose stigma, shift burden, and harden before correction?

```trace
prediction_audit :=
  predicted_risk
  + action_taken_because_of_prediction
  + contestability
  + reversibility
  + affected_scope_future_space
```

Prediction can create duty to watch, support, warn, slow, or review.

It does not erase the difference between possibility and fact.

Prediction can also reveal a chance to protect viable becoming. If a system predicts failure and uses that signal to offer support, keep a route open, slow a harmful path, or preserve repairability, the prediction may expand future-space rather than close it.

```trace
prediction_as_support_signal :=
  predicted_risk
  + non_punitive_response
  + support_or_review_route
  + contestability_preserved
  -> possible_viable_future_expansion
```

This is the difference between a warning that helps an entity continue and a label that traps it.

## 10.4 Decision-Time Evidence

Responsibility attaches to evidence available at the time of decision.

Not evidence invented later. Not evidence hidden from the actor. Not evidence that became obvious only after the loss. Not evidence that no one in the role could reasonably access.

```trace
decision_time_evidence :=
  evidence_available_or_reasonably_available
  before_or_during_relevant_action_window
```

This protects against hindsight blame, but it also prevents convenient ignorance.

An actor cannot avoid responsibility by designing a system that keeps evidence away. An institution cannot say decision-makers did not know if the institution's own structure prevented warnings from reaching them. A model deployer cannot say the harms were invisible if it refused to monitor affected-scope outcomes. A public authority cannot rely on ignorance produced by underfunded challenge routes.

So the evidence question has two sides.

First: what did the actor actually know or have reason to know?

Second: did the actor have a duty to build a route by which relevant evidence could reach them?

```trace
evidence_route_duty :=
  role_power
  + foreseeable_harm
  + capacity_to_monitor
  -> duty_to_make_warning_reachable
```

Decision-time evidence includes warnings, complaints, anomalies, repeated patterns, near misses, known failure modes, and credible affected-scope accounts.

It does not include omniscience.

For value-spine purposes, the evidence route must carry positive signals too. A system that records only failures and never records lost opportunities, blocked repair, trust collapse, capacity damage, or reachable support will misread viable becoming.

```trace
evidence_route_value_scope :=
  warnings
  + complaints
  + anomalies
  + opportunity_signals
  + repairability_signals
  + trust_and_reachability_signals
```

## 10.5 Meaningful Control

Responsibility requires control.

Not total control. Not perfect control. Meaningful control.

```trace
meaningful_control :=
  ability_to_change
  or slow
  or pause
  or escalate
  or warn
  or preserve_evidence
  or reduce_harm
```

A person with no ability to alter a path should not be treated as if they controlled it. A low-level worker may see a problem but lack authority. A child may cause harm without mature control. An actor under severe pressure may choose from a collapsed option set. A traumatised actor may have impaired control. A local official may operate inside a system designed elsewhere.

Control is graded.

But control is also often hidden.

Senior actors may claim they were too far from the operational path. Designers may claim users misused the system. Operators may claim policy required it. Vendors may claim clients deployed it. Committees may claim no single member decided. Automated systems may be treated as if they acted by themselves.

Mechanical Ethics asks where control actually sat.

Who could change the rule? Who could pause enforcement? Who could preserve evidence? Who could fund correction? Who could open a challenge route? Who could alter the incentive? Who could decide not to deploy? Who could monitor recurrence?

Responsibility follows meaningful control, not formal distance.

The value-spine question is: who could preserve or reopen viable becoming?

```trace
control_over_viable_becoming :=
  ability_to_preserve_opportunity
  or keep_route_reachable
  or restore_information
  or support_capacity
  or maintain_relation
  or reopen_repair_path
  or prevent_false_finality
```

If an actor had this kind of control and the relevant opening or closure was visible enough, responsibility may attach even where no direct personal malice exists.

## 10.6 Role Duty

Roles carry duties.

A role is not merely a title. It is a position in a path.

```trace
role_duty :=
  position_in_path
  + expected_attention
  + capacity_or_authority
  + affected_scope_dependency
```

Some roles exist because affected scopes cannot protect themselves alone. A judge, doctor, teacher, engineer, prison officer, social worker, regulator, auditor, designer, maintainer, parent, minister, platform operator, or data controller may hold power over another's future-space.

That power creates role duty.

Role duty does not mean every bad outcome becomes personal guilt. It means the role carries expected attention to certain kinds of harm, correction, and burden.

A maintainer may have a duty to monitor recurrence. A designer may have a duty to test foreseeable failure modes. A regulator may have a duty to preserve independent signal. A public authority may have a duty to keep contestability live. A platform may have a duty to provide meaningful appeal before account loss hardens. A parent may have a duty to protect a child's future-space before the child can protect it.

Roles are how systems act through people.

If the role has power but no duty, the system has built unanswerable authority.

Role duty also includes positive preservation where dependency exists. A role that controls another scope's route may owe more than non-injury. It may owe usable information, timely support, preserved opportunity, or a real return path.

```trace
role_positive_duty :=
  role_controls_route
  + affected_scope_depends_on_route
  + viable_becoming_at_stake
  -> duty_to_preserve_conditions_where_reasonably_possible
```

## 10.7 Delegation Is Not Erasure

Delegation moves work.

It does not erase responsibility.

```trace
delegation != erasure
```

A public body may delegate administration to a contractor. A hospital may use a triage tool. A court may rely on expert evidence. A school may use a behaviour platform. A company may outsource moderation. A state may rely on automated detection. A manager may assign review to a junior team.

Delegation may be legitimate. Complex systems need distributed work.

But if delegation creates opacity, delay, contaminated incentives, unreachable appeal, or responsibility gaps, then delegation becomes part of the harm mechanism.

Mechanical Ethics asks:

```trace
delegation_audit :=
  what_was_delegated
  + who_retained_power
  + who_can_correct
  + affected_scope_route
  + monitoring_duty
  + failure_responsibility
```

The delegating actor should not be able to say, "the contractor decided," if the actor designed the contract, controlled the incentive, ignored warnings, or kept the benefit.

The operator should not be able to say, "the model decided," if the operator chose to use the model, trusted it beyond its evidence, or failed to preserve challenge.

Delegation can distribute responsibility.

It cannot dissolve it.

The value-spine audit adds: who retained responsibility for viable becoming after delegation?

```trace
delegated_viable_becoming_audit :=
  who_preserves_notice
  + who_preserves_contestability
  + who_preserves_repairability
  + who_tracks_residue
  + who_can_reopen_path
```

A delegated path that expands efficiency while destroying reachability is not an innocent improvement. It is a value trade that must be named.

## 10.8 Automation Is Not Absolution

Automation changes the mechanism.

It does not absolve the humans and institutions that design, deploy, maintain, benefit from, or refuse to monitor it.

```trace
automation != absolution
```

Automated systems are powerful because they act quickly, consistently, and at scale. Those strengths can also make harm faster, less visible, and harder to contest.

A human decision can sometimes be interrupted by human doubt. An automated path may harden before anyone sees the individual case. A model can convert partial data into confident classification. A queue can turn delay into default. A dashboard can make a person's future appear as a metric.

Mechanical Ethics asks whether automation preserves correction.

```trace
automation_constraint :=
  preserve_notice
  + preserve_contestability
  + preserve_human_answerability
  + monitor_outcomes
  + prevent_irreversible_action_from_unchecked_estimates
```

Automation may reduce bias, error, delay, or arbitrary discretion in some cases. It may expand future-space. It may help detect harm early. It is not automatically bad.

But automation must not be allowed to hide uncertainty inside technical authority or move harm faster than answerability can follow.

If the system acts faster than correction, it needs stronger brakes.

Automation can be part of a good path only if its gains do not erase answerability.

```trace
automation_positive_condition :=
  improves_reachability_or_support_or_detection
  + preserves_uncertainty_visibility
  + preserves_contestability
  + preserves_human_answerability
  + records_remaining_burden
```

Local efficiency is not enough. The question is whether automation helps affected scopes navigate, correct, repair, and continue.

## 10.9 Responsibility Attachment

Responsibility attachment is the point where the record says: this actor must answer for this path in this way.

It is not always blame. It may be duty to disclose, duty to repair, duty to monitor, duty to compensate, duty to escalate, duty to preserve evidence, duty to prevent recurrence, or duty to explain why action continued.

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

Attachment should be specific.

Not: someone should have done something.

Instead: this actor, in this role, with this evidence, had this control, during this time window, and owed this response.

Specificity prevents scapegoating. It also prevents evasion.

A junior clerk should not absorb the guilt of a system designed above them. A minister should not hide behind frontline staff when policy created the path. A developer should not absorb every deployment choice made by a client. A client should not hide behind a vendor when it chose the system and benefited from it. A committee should not hide behind collective fog if roles and records show who could act.

Responsibility attachment is how Mechanical Ethics keeps answerability from becoming either witch hunt or mist.

The value-spine version of responsibility attachment asks what the actor could see and affect in relation to viable becoming.

```trace
responsibility_for_viable_becoming :=
  actor
  + role
  + decision_time_evidence
  + meaningful_control
  + visible_opening_or_closure
  + duty_response
```

The response may be to stop a closure, preserve an opening, reopen a route, disclose uncertainty, return burden, repair residue, or explain why none of those were possible.

## 10.10 Responsibility Without Scapegoating

Scapegoating is false repair.

A system finds one person to blame, sanctions them, and leaves the machinery intact. The public receives a story. The institution receives closure. The path remains.

```trace
scapegoating :=
  individual_blame
  + unchanged_harm_mechanism
  + institutional_closure
```

Mechanical Ethics rejects scapegoating for the same reason it rejects correction without repair. It does not touch the path.

This does not mean individuals are never responsible. They are. Some people misuse power, ignore warnings, falsify records, hide evidence, punish dissent, or choose serious wrongdoing. Individual blame may be warranted.

But individual blame should not be used to erase systemic responsibility where the system selected, rewarded, permitted, or protected the harmful path.

The better record asks:

```trace
responsibility_map :=
  individual_actions
  + role_duties
  + system_design
  + incentives
  + warnings
  + correction_failures
  + residue
```

Responsibility without scapegoating is harder than blame and harder than excuse.

It says: do not blame from visibility alone, but do not let complexity become weather. Do not sanction one visible actor while preserving the hidden machine. Do not call a system innocent because no single hand contains the whole path.

It must also avoid positive scapegoating: giving credit to one visible reform while leaving the path unrepaired. A system can celebrate a helpful actor, new tool, new policy, or new programme while the deeper route remains unreachable.

```trace
positive_scapegoating_risk :=
  visible_good_actor_or_reform
  + unchanged_path
  + institution_claims_moral_closure
```

Do not use blame to hide the machine. Do not use praise to hide the machine either.

Part 10 ends with the responsibility spine:

```trace
responsibility_spine :=
  visibility_is_not_blame
  + foresight_is_not_omniscience
  + prediction_is_not_destiny
  + decision_time_evidence
  + meaningful_control
  + role_duty
  + delegation_not_erasure
  + automation_not_absolution
  + responsibility_for_seen_openings_and_closures
  + anti_scapegoating
```

The next part moves into the most dangerous territory: power, legitimacy, authority, desert, dignity, and severe constraint.

That part must frame more than it solves.
