# Mechanical Ethics Architecture Alignment Note — 2026-06-27

Status: alignment note. Not book text. Not canon. Not validation.

Purpose: prevent stale-surface drift after the later skeleton and interface schema repairs.

## 1. Why this note exists

The original `ME_BOOK_ARCHITECTURE_v0_1_2026_06_27.md` correctly established the broad ME rebuild: one human-facing book, numbered parts/chapters/sections, middle-out origin, old material as quarry only, TRACE outputs read-only, and ME router outputs as findings rather than authorizations.

Later review caught one placement defect: the artifact-to-artifact TRACE→ME interface should not sit inside the human argument spine. That correction was made in the later skeleton and interface schema surfaces. This note records that correction without rewriting the entire architecture file.

## 2. Current precedence rule

```trace
surface_precedence :=
  architecture_v0_1_sets_scope
  + skeleton_v0_1_sets_human_book_spine
  + interface_schema_v0_1_sets_operator_schema
```

If these surfaces appear to conflict:

```trace
if conflict_about_Part_5_or_interface_placement:
  skeleton_v0_1_and_interface_schema_v0_1_govern
```

## 3. Corrected Part 5 placement

The human book spine should use:

```text
Part 5 — Description Is Not Permission
```

Not:

```text
Part 5 — The TRACE → ME Interface
```

The human principle retained in the book spine is:

```trace
description_is_not_permission :=
  seeing_a_transition
  != authorizing_that_transition
```

The artifact-to-artifact interface belongs in:

```trace
interface_plumbing_location :=
  Part_14_Case_Records_and_Use_Protocols
  + appendices
  + ME_INTERFACE_SCHEMA_v0_1
```

## 4. Operator schema location

Use `00_CURRENT_SURFACE/ME_INTERFACE_SCHEMA_v0_1/TRACE_ME_INTERFACE_SCHEMA_v0_1_2026_06_27.md` for:

```trace
operator_schema_content :=
  TRACE_input_packet
  + minimum_viable_case_record
  + ME_interpretation_layers
  + router_findings
  + residue_ledger
  + prescription_audit
  + gate_router_consistency_rule
```

Do not reinsert this machinery into the human argument spine.

## 5. Current drift check

```trace
drift_status :=
  architecture_scope_clean
  + skeleton_spine_clean
  + interface_schema_clean
  + stale_Part_5_label_recorded_and_neutralized
```

This note is enough for now. Do not spend further build time rewriting old surfaces unless they actively mislead a reader or block the next test case.
