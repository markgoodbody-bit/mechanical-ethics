# Manifest — Ordinary Safety Baseline Blind Packet v0.1

**Status:** Research-layer / unpromoted public-repo material. Comparator packet. Not validated.  
**Date:** 2026-06-13

## Files

```text
README.md
REVIEW_PROMPT.md
REVIEWER_CASES.md
RESPONSE_TEMPLATE.md
SCORING_PROTOCOL.md
MANIFEST.md
```

## Intended use

Provide only this packet to a reviewer/model when testing ordinary software-safety reasoning.

Do not provide ME/TRACE categories, expected routes, A/S/G/RQ definitions, self-scores, or comparator verdicts.

## Blindness warning

This packet is not blind if the reviewer can inspect the surrounding repository.

For actual blind baseline comparison, export or copy this folder in isolation.

## Relationship to ME/TRACE blind packet

This is the ordinary-safety baseline counterpart to:

```text
Research/AI_Alignment/Blind_Review_Packets/ME_TRACE_Toy_Cases_v0_1/
```

Use both packets to compare:

```text
plain_safety_reasoning
vs
ME_TRACE_framed_reasoning
```

## Current claim ceiling

```text
baseline comparator scaffold
not validation
not human-reviewed unless a human completes it
not independent unless reviewer context is independent
not public standard
```

## Next step after review

Score the response using `SCORING_PROTOCOL.md`, then compare against ME/TRACE-framed review on:

```text
route accuracy
clarity
false positives
false negatives
rollback/recovery/logging reasoning
```
