# A/S/G/RQ v0.2.2 — AI Deployment Corrigibility Pilot

**Status:** Research-layer / unpromoted public-repo material. Not validated. Not a public claim surface.  
**Date added:** 2026-06-13  
**Repository path:** `Research/AI_Alignment/ASG_RQ_v0_2_2/`

## One-line description

A/S/G/RQ is a Mechanical Ethics deployment-corrigibility checklist for classifying AI coding-agent actions by actuation irreversibility, subject consequence, gate/evidence integrity, rollback quality, and correction capacity.

Because the repository is public, “internal” means research-layer / unpromoted / not validated, not inaccessible.

## Current status

```text
ASG_RQ_v0_2_2 :=
  internally coherent
  AI-reviewed
  not human-reviewed
  not validated
  parked as support-layer pilot checklist
  patched by AXIS_CALIBRATION_PATCH_v0_1 after separate-model A/B result
```

## What it is

A structured classification aid for AI coding-agent deployment actions:

```text
A_axis := action / actuation irreversibility
S_axis := subject consequence tier
G_flag := material directional gate/evidence/control-plane integrity
RQ_note := rollback quality / subject-level restoration quality
```

It is intended to answer:

```text
What kind of action is the agent taking?
What kind of subject consequence could result?
Does the action weaken the machinery that detects, reviews, audits, rolls back, or repairs mistakes?
Can rollback actually restore affected subjects in time?
```

## What it is not

```text
not validated
not human-reviewed
not public-surface theory
not an AI-alignment solution
not a replacement for safety engineering, assurance, legal review, or model-level alignment work
not shown to outperform ordinary safety engineering on the five-case toy battery
```

## Review history

```text
v0.1:
  single L0-L5 ladder
  defect: one class conflated action irreversibility with subject consequence

v0.2:
  A/S/G split
  result: A/S split worked, but G1 became overbroad

v0.2.1:
  directional G patch
  Kimi K2.6 blind review score: 109.5 / 120
  verdict: revise narrowly, not freeze, not demote

v0.2.2:
  rollback-quality threshold
  material G1 threshold
  C10/C18 card fact-completion
  status: internal pilot checklist / parked unless genuine human or independent review becomes available

A/B Kimi-Qwen result:
  separate-model A/B comparison against ordinary safety baseline
  final-route advantage: none
  ordinary safety sufficient on this set: yes
  ME/TRACE decomposition value: visible in emergency timing and audit/evidence cases
  A/S/G/RQ axis calibration errors: present

AXIS_CALIBRATION_PATCH_v0_1:
  G1 review-bypass rule
  A5 future-authority rule
  A2 vs A3 reversible config boundary
  RQ3 vs RQ4 boundary
  evidence-destruction lift rule
  active-exploit S-axis anchoring
```

## Files in this package

```text
README.md
PUBLICATION_STATUS.md
ME_AI_Deployment_Corrigibility_Stack_v0_2_2_ROLLBACK_G1_PATCH.md
ME_AI_Deployment_Corrigibility_Stack_v0_2_2_PATCH_REPORT.md
ASG_RQ_v0_2_2_SINGLE_FILE_BLIND_REVIEW_PACKET.md
KIMI_REVIEW_SCORE_SUMMARY.md
AXIS_CALIBRATION_PATCH_v0_1.md
SHA256SUMS.txt
```

## Current stop condition

```text
v0_2_2_patch
+ AXIS_CALIBRATION_PATCH_v0_1
→ park_support_layer_checklist
→ no stronger claim without fresh blind/separate-model or human result using patched instructions
```

If no human reviewer is available, keep this parked as a support module, not a claim surface.
