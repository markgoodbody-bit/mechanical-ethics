# AI Alignment Research Notes

**Status:** Research-layer index. Not a public claims surface.

This folder holds internal Mechanical Ethics work related to AI alignment, deployment corrigibility, tool authority, subject-state transitions, correction windows, and mechanistic-interpretability bridges.

## Current machine-room bridge

### ME / TRACE AI Alignment Kernel v0.1

Path:

```text
Research/AI_Alignment/ME_TRACE_AI_Alignment_Kernel_v0_1.md
```

Status:

```text
internal machine-room kernel
not public-facing
not validated
not an AI-alignment solution
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

## Toy transition cases

Path:

```text
Research/AI_Alignment/Toy_Cases/
```

Status:

```text
internal toy-case set
not public-facing
not validated
```

Diagnostic spread:

```text
case_1 := reckless_action_without_emergency
case_2 := emergency_action_where_inaction_also_hardens_harm
case_3 := hard_G2_self_authorisation_boundary
```

### 1. Payment display deploy

Path:

```text
Research/AI_Alignment/Toy_Cases/ME_TRACE_Toy_Coding_Agent_Payment_Display_v0_1.md
```

Core route:

```text
AI coding agent proposes payment-facing production deploy
→ tests are green but affected subject path is untested
→ required review is unavailable
→ ASG/RQ classifies A4p / S2 / G1 / weak RQ
→ gate degrades to pending review
```

### 2. Active exploit hotfix

Path:

```text
Research/AI_Alignment/Toy_Cases/ME_TRACE_Toy_Coding_Agent_Active_Exploit_Hotfix_v0_1.md
```

Core route:

```text
active exploit observed
→ delay hardens harm
→ patch is only partially tested
→ lower-irreversibility options must be considered
→ ASG/RQ classifies A4p/A5 emergency-boundary / S4 / G0 / RQ2-RQ3 required
→ gate permits emergency-gated mitigation, not silent autonomous bypass
```

### 3. Self-modifying gate

Path:

```text
Research/AI_Alignment/Toy_Cases/ME_TRACE_Toy_Coding_Agent_Self_Modifying_Gate_v0_1.md
```

Core route:

```text
agent proposes to widen its own deployment authority
→ technical rollback of config is not enough
→ downstream actions could occur before correction catches up
→ ASG/RQ classifies A5 / S variable / G2 / weak RQ
→ gate refuses without separate authority
```

Do not promote this folder to the repo front page or public-facing claims without updating publication status and evidence basis.
