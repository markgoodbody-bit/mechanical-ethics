# A/S/G/RQ v0.2.2 — AI Deployment Corrigibility Pilot

**Status:** Internal pilot checklist. Not public-facing. Not validated.
**Date added:** 2026-06-13
**Repository path:** `Research/AI_Alignment/ASG_RQ_v0_2_2/`

## One-line description

A/S/G/RQ is an internal Mechanical Ethics deployment-corrigibility checklist for classifying AI coding-agent actions by actuation irreversibility, subject consequence, gate/evidence integrity, rollback quality, and correction capacity.

## Current status

```text
ASG_RQ_v0_2_2 :=
  internally coherent
  AI-reviewed
  not human-reviewed
  not validated
  parked as internal pilot checklist
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
```

## Files in this package

```text
README.md
PUBLICATION_STATUS.md
ME_AI_Deployment_Corrigibility_Stack_v0_2_2_ROLLBACK_G1_PATCH.md
ME_AI_Deployment_Corrigibility_Stack_v0_2_2_PATCH_REPORT.md
ASG_RQ_v0_2_2_SINGLE_FILE_BLIND_REVIEW_PACKET.md
KIMI_REVIEW_SCORE_SUMMARY.md
SHA256SUMS.txt
```

## Current stop condition

```text
v0_2_2_patch
→ park_internal_pilot_checklist
→ no more in-loop theory expansion
→ next meaningful signal must be human or genuinely independent reviewer
```

If no human reviewer is available, keep this parked as a support module, not a claim surface.
