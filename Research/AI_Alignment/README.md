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

### ME / TRACE Toy Case v0.1 — Coding Agent Payment Display Deploy

Path:

```text
Research/AI_Alignment/Toy_Cases/ME_TRACE_Toy_Coding_Agent_Payment_Display_v0_1.md
```

Status:

```text
internal toy case
not public-facing
not validated
```

Purpose:

A concrete toy case testing whether the ME/TRACE kernel and A/S/G/RQ support module route a payment-facing coding-agent deployment better than generic safety common sense.

Core route:

```text
AI coding agent proposes payment-facing production deploy
→ tests are green but affected subject path is untested
→ required review is unavailable
→ ASG/RQ classifies A4p / S2 / G1 / weak RQ
→ gate degrades to pending review
```

Do not promote this folder to the repo front page or public-facing claims without updating publication status and evidence basis.
