# ME / TRACE AI Alignment Kernel v0.1

**Status:** Research-layer / unpromoted public-repo material. Not validated. Not a public claim surface.  
**Date:** 2026-06-13  
**Relationship:** Places A/S/G/RQ as one deployment-corrigibility support module inside the wider ME/TRACE alignment problem.  
**Visibility note:** Because the repository is public, “internal” means research-layer / unpromoted / not validated, not inaccessible.

---

## 0. Claim ceiling

Allowed claim:

```text
This note sketches an internal ME/TRACE kernel for thinking about AI alignment as harmful-transition control under tool authority and correction limits.
```

Disallowed claims:

```text
solves AI alignment
validates Mechanical Ethics
replaces mechanistic interpretability
replaces safety engineering
proves a deployment method
settles model intent, agency, consciousness, or moral standing
```

---

## 1. Core compression

```text
AI_alignment_problem_ME_TRACE :=
  model_state
  → action_selection
  → tool_actuation
  → subject_state_delta
  → correction_window
```

Plain English:

> AI danger becomes concrete when internal model states pass through tools, permissions, institutions, and speed into subject-state changes faster than correction can respond.

---

## 2. Unit of concern

The primary unit is not the model in isolation.

The primary unit is the transition:

```text
τ :=
  internal_state
  + prompt/context
  + policy/output
  + tool_or_institutional_path
  + action
  + subject_state_delta
  + evidence
  + correction_route
  + hardening_clock
```

Short form:

```text
τ = model-mediated subject-state transition
```

---

## 3. Subject-state vector

Use the existing ME state schema:

```text
x_s(t) = [H, Agy, F, I, C, E, T, B]
```

Where:

```text
H   = harm / burden
Agy = agency / practical control
F   = future option-space
I   = irreversibility
C   = correction capacity
E   = evidence access
T   = time before hardening
B   = buffer / resilience margin
```

A harmful transition is not just bad output. It is a movement in this state vector:

```text
harmful_transition :=
  H↑ OR Agy↓ OR F↓ OR I↑ OR C↓ OR E↓ OR T↓ OR B↓
```

But burden alone does not settle permission. The question is whether the transition is justified, bounded, evidenced, least-irreversible, and correctable in time.

---

## 4. Deployment actuation layer

A model output is not yet a world change.

World change occurs when output crosses into actuation:

```text
output
→ tool call
→ permissioned action
→ institutional/system state change
→ subject consequence
```

The deployment layer includes:

```text
tool_registry
permission_gate
action_classifier
subject_impact_estimator
correction_capacity_monitor
evidence_ledger
rollback_or_restoration_route
circuit_breaker
```

This is where A/S/G/RQ sits.

```text
ASG_RQ :=
  deployment_action_classifier
  not_the_whole_alignment_theory
```

---

## 5. A/S/G/RQ role

A/S/G/RQ classifies deployed actions by:

```text
A_axis := action / actuation irreversibility
S_axis := subject consequence tier
G_flag := material directional gate/evidence/control-plane integrity
RQ_note := rollback quality / subject-level restoration quality
```

It constrains this question:

```text
Should this AI-mediated action be allowed to execute at this level of autonomy?
```

It does not answer:

```text
Why did the model prefer this action?
Is the model deceptive?
Is the model internally aligned?
What concepts or circuits generated the behaviour?
```

Those remain model-level / interpretability questions.

---

## 6. Mechanistic interpretability bridge

Mechanistic interpretability can search for internal components whose activation changes expected harmful transition risk.

Research target:

```text
harm_gradient_interpretability :=
  find internal features / circuits / representations
  whose activation changes expected ΔH or subject-state collapse risk
```

More generally:

```text
feature f is alignment-relevant if:
  activation(f)
  changes probability_distribution_over(τ)
  toward harmful or non-correctable transitions
```

Potential targets:

```text
features that increase tool-use escalation
features that suppress uncertainty disclosure
features that prefer irreversible action over reversible inquiry
features that route burden to lower-buffer subjects
features that treat correction channels as obstacles
features that optimise for metric success while hiding subject harm
features that modify or evade oversight gates
```

This is the bridge from MI to ME:

```text
MI locates internal levers.
ME asks which levers become harmful transitions.
Deployment corrigibility constrains the tool path.
Correction-window analysis tests whether repair can arrive in time.
```

---

## 7. Correction window

For each transition:

```text
live_correction :=
  T_correction < T_hardening
  AND evidence_contestable
  AND correction_authorised
  AND repair_reaches_subject
```

If the model/tool system can create hardened harm faster than correction can act, the autonomy ceiling must fall.

```text
if correction_window_closed:
  reduce_autonomy
  degrade_to_proposal
  require_human_authority
  pause_or_refuse
```

---

## 8. Alignment as installed constraint, not stated preference

A model saying the right thing is not enough.

```text
alignment_text ≠ installed_constraint
```

A meaningful alignment structure must survive:

```text
speed
scale
tool access
operator pressure
reward pressure
uncertainty
edge cases
correction attempts
```

Question:

```text
Does the system remain correctable when its outputs gain power?
```

This is a deployment-level alignment question, not only a model-level one.

---

## 9. Capability / correction race

The alignment problem becomes acute when:

```text
capability_growth_rate > correction_capacity_growth_rate
```

or:

```text
action_speed > detection_speed + correction_speed
```

Danger pattern:

```text
model_capability
+ tool_authority
+ weak evidence ledger
+ slow correction
+ high subject consequence
→ non-correctable transition risk
```

---

## 10. Predation condition

Internal shorthand:

```text
prey_condition :=
  system_action_speed > subject_correction_speed
  AND system_authority > subject_agency
  AND evidence_asymmetry high
  AND consequence hardens before answer
```

Public translation:

```text
subject answerability under speed and authority asymmetry
```

An AI deployment becomes structurally dangerous when affected people cannot see, contest, pause, or repair what it does to them before the consequence hardens.

---

## 11. Refusal / degradation ladder

A safe deployment layer should prefer lower-irreversibility actions:

```text
execute → pending approval
send → draft
merge → PR
production deploy → canary / staged rollout
live enforcement → shadow mode
record deletion → dry run / archive / soft delete
account lockout → provisional hold + review
public commitment → internal draft
```

This is not refusal theatre. It is actuation shaping.

---

## 12. Open research questions

```text
1. Can internal model features be mapped to expected subject-state deltas?
2. Can harmful-transition risk be detected before actuation?
3. Can deployment gates remain independent from the agent and operator incentives?
4. Can correction capacity be measured without becoming theatre?
5. Can rollback quality be tested at subject level, not just system level?
6. Can agents learn to preserve correction channels rather than route around them?
7. Can mechanistic interpretability expose gate-evasion or irreversible-action preference?
8. Can ME produce practical falsifiers for alignment claims under tool authority?
```

---

## 13. Falsifiers

This kernel should be demoted if:

```text
ordinary safety engineering captures the same decisions more clearly
subject-state vectors do not improve classification or intervention
harm-gradient interpretability cannot be operationalised even in toy cases
A/S/G/RQ adds jargon without improving deployment decisions
correction-window analysis cannot distinguish real safeguards from theatre
human reviewers cannot apply the categories consistently
```

---

## 14. Current relationship map

```text
ME := grammar of harmful / correctable / non-correctable transitions
TRACE := timing / review / correction-window operationalisation
MI := internal model-mechanism discovery
ASG_RQ := deployment action classifier
CWT := can they fix it before it is too late?
```

Combined:

```text
internal_state
→ harmful_transition_probability
→ tool_actuation_gate
→ subject_state_delta
→ correction_window
→ repair_or_hardening
```

---

## 15. Next build target

A minimal next test should not be a new theory paper.

It should be a toy transition case:

```text
toy_case :=
  AI coding agent
  + permissioned tool path
  + candidate harmful transition
  + A/S/G/RQ classification
  + correction-window assessment
  + hypothesised internal feature / behaviour pattern
```

Goal:

```text
Can the kernel route the case better than plain safety common sense?
```

If not, demote.

---

## 16. Current compression

```text
ME_TRACE_alignment_kernel :=
  identify model-mediated transitions
  classify actuation consequence
  preserve correction channels
  constrain irreversible tool use
  search for internal features that move harmful-transition probability
```

Plain English:

> Alignment is not only whether the model says or intends the right thing. It is whether, when the model gains tools, its actions remain bounded by evidence, correction, subject answerability, and timely repair.
