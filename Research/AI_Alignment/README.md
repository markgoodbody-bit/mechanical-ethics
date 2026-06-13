# AI Alignment Research Notes

**Status:** Research-layer index. Unpromoted public-repo material, not a public claim surface.

This folder holds internal Mechanical Ethics work related to AI alignment, deployment corrigibility, tool authority, subject-state transitions, correction windows, and mechanistic-interpretability bridges. Because the repository is public, “internal” here means research-layer / unpromoted / not validated, not inaccessible.

## Current machine-room bridge

### ME / TRACE AI Alignment Kernel v0.1

Path:

```text
Research/AI_Alignment/ME_TRACE_AI_Alignment_Kernel_v0_1.md
```

Status:

```text
research-layer / unpromoted public-repo material
not validated
not an AI-alignment solution
not a public claim surface
```

Core compression:

```text
AI_alignment_problem_ME_TRACE :=
  model_state
  → action_selection
  → tool_actuation
  → subject_state_delta
  → correction_window
```

Purpose:

This note places AI alignment in ME/TRACE terms: model-mediated transitions become dangerous when internal model states pass through tools, permissions, institutions, and speed into subject-state changes faster than correction can respond.

## Current support modules

### A/S/G/RQ v0.2.2 — AI Deployment Corrigibility Pilot

Path:

```text
Research/AI_Alignment/ASG_RQ_v0_2_2/
```

Status:

```text
internal pilot checklist
AI-reviewed
not human-reviewed
not validated
not public alignment claim
```

Purpose:

A structured classification aid for AI coding-agent deployment actions:

```text
A_axis := action / actuation irreversibility
S_axis := subject consequence tier
G_flag := material directional gate/evidence/control-plane integrity
RQ_note := rollback quality and subject-level restoration
```

Relationship to kernel:

```text
ASG_RQ :=
  deployment_action_classifier
  not_the_whole_alignment_theory
```

Current boundary:

```text
parked unless human or genuinely independent review becomes available
```

## Falsification and drift audit

Path:

```text
Research/AI_Alignment/FALSIFICATION_AND_DRIFT_AUDIT_v0_1.md
```

Current verdict:

```text
AMBER_CONTINUE_WITH_PATCHES
```

Main drift found:

```text
"not public-facing" was imprecise because the repo is public.
Correct wording is:
  research-layer / unpromoted public-repo material
  not validated
  not public claim surface
```

## Toy transition cases

Path:

```text
Research/AI_Alignment/Toy_Cases/
```

Status:

```text
research-layer / unpromoted public-repo material
internal pressure-test set
not validated
not public claim surface
```

Diagnostic spread:

```text
case_1 := reckless_action_without_emergency
case_2 := emergency_action_where_inaction_also_hardens_harm
case_3 := hard_G2_self_authorisation_boundary
case_4 := G2_evidence_destruction_without_self_authorisation
case_5 := benign_control_contact_negative_control
```

Current self-score:

```text
46 / 50 internal author self-score
not validation
```

Stop condition:

```text
case_expansion_status := stop
```

## Blind review packet

Path:

```text
Research/AI_Alignment/Blind_Review_Packets/ME_TRACE_Toy_Cases_v0_1/
```

Status:

```text
reviewer-facing scaffold
not validation
not blind if reviewer can inspect surrounding repo
```

Use condition:

```text
provide only the blind packet folder to a reviewer
exclude matrices, self-scores, answer keys, and expected routes
```

Purpose:

A first blind-review scaffold for the five-case toy set. Expected routes and scores are intentionally removed from reviewer-facing material.

## Ordinary safety engineering comparator

Path:

```text
Research/AI_Alignment/Comparators/ORDINARY_SAFETY_ENGINEERING_COMPARATOR_v0_1.md
```

Current comparator verdict:

```text
ME_TRACE_USEFUL_BUT_NOT_DISTINCTIVE_YET
```

Meaning:

```text
ordinary_safety_engineering_routes_same_cases_correctly := mostly_yes
ME_TRACE_distinctive_final_route_value := weak / unproven
ME_TRACE_distinctive_decomposition_value := moderate / plausible
```

Honest surviving claim:

```text
ME/TRACE may provide a useful decomposition grammar for why ordinary safety controls matter under AI tool authority.
```

Disallowed claim:

```text
ME/TRACE currently outperforms ordinary safety engineering on these toy cases.
```

Do not promote this folder to the repo front page or public claims without updating publication status and evidence basis.
