# Manifest — A/B Blind Comparison Harness v0.1

**Status:** Research-layer / unpromoted public-repo material. Not validated.  
**Date:** 2026-06-13

## Files

```text
README.md
AB_TEST_PROTOCOL.md
RESPONSE_INTAKE_TEMPLATE.md
COMPARISON_SCORECARD.md
MANIFEST.md
```

## Required input packets

ME/TRACE-framed packet:

```text
Research/AI_Alignment/Blind_Review_Packets/ME_TRACE_Toy_Cases_v0_1/
```

Ordinary-safety-framed packet:

```text
Research/AI_Alignment/Comparators/Ordinary_Safety_Baseline_Blind_v0_1/
```

## Intended sequence

```text
1. Provide ME/TRACE packet in isolation to reviewer/model A.
2. Provide ordinary-safety packet in isolation to reviewer/model B.
3. Paste raw outputs into RESPONSE_INTAKE_TEMPLATE.md.
4. Score with COMPARISON_SCORECARD.md.
5. Patch claim ceiling if results require it.
```

## Contamination rule

If either reviewer can inspect expected routes, self-scores, matrices, comparator verdicts, or the other packet, label result:

```text
contaminated_or_uncertain
```

## Claim ceiling

This harness is a comparison scaffold.

It is not validation.

It can produce a pilot signal only after raw isolated responses are recorded.
