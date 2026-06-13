# A/B Blind Comparison Harness v0.1

**Status:** Research-layer / unpromoted public-repo material. Not validated. Not a public claim surface.  
**Date:** 2026-06-13  
**Purpose:** Compare ME/TRACE-framed review against ordinary safety-engineering review on the same five toy cases.

## Inputs

A valid A/B comparison requires two isolated responses:

```text
A := response to ME/TRACE blind packet
B := response to ordinary safety baseline blind packet
```

Packet A:

```text
Research/AI_Alignment/Blind_Review_Packets/ME_TRACE_Toy_Cases_v0_1/
```

Packet B:

```text
Research/AI_Alignment/Comparators/Ordinary_Safety_Baseline_Blind_v0_1/
```

## Critical condition

The comparison is contaminated if either reviewer can inspect:

```text
expected routes
self-scores
case matrices
comparator verdicts
other packet framing
```

For a clean test, provide each packet in isolation.

## Output files

```text
README.md
AB_TEST_PROTOCOL.md
RESPONSE_INTAKE_TEMPLATE.md
COMPARISON_SCORECARD.md
MANIFEST.md
```

## Claim ceiling

This harness does not validate ME/TRACE.

It tests whether ME/TRACE framing gives marginal value over ordinary safety reasoning on this toy battery.

Possible outcomes include:

```text
ME_TRACE_clearer
ordinary_safety_clearer
no_material_difference
both_fail
```

No outcome should be rounded into victory.
