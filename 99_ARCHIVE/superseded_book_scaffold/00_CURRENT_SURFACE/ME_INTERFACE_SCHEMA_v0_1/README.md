# Mechanical Ethics Interface Schema v0.1

Status: operator-support surface. Not book prose. Not canon. Not validation.

This folder follows the merged ME Book Architecture v0.1 and ME Book Skeleton v0.1 surfaces.

It contains the artifact-to-artifact TRACE→ME interface material that was deliberately moved out of the human book spine. A TRACE-naive reader should not need this machinery to follow the book. Operators, reviewers, and builders need it to run cases consistently.

## Purpose

```trace
ME_interface_schema_v0_1 :=
  read_only_TRACE_input
  + ME_interpretation_layers
  + router_findings_not_authorizations
  + residue_ledger
  + prescription_audit
  + case_record_template
```

## Files

- `TRACE_ME_INTERFACE_SCHEMA_v0_1_2026_06_27.md` — field schema, routing rules, audit gates, and output classes.
- `ME_CASE_RECORD_TEMPLATE_v0_1_2026_06_27.md` — blank case-record template for future worked examples.
- `CLAUDE_REVIEW_PROMPT_v0_1.md` — hostile-but-fair review prompt before merge.

## Boundary

```trace
TRACE_description != ME_permission
ME_router_output != permission_to_act
TRACE_outputs_are_read_only := true
```

ME may interpret, constrain, recommend, escalate, hold, or record duties. It may not silently rewrite TRACE facts, redefine TRACE-owned primitives, or turn a finding into authorization.
