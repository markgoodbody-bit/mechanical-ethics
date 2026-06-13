# A/S/G/RQ v0.2.2 Scoring Rubric

**Status:** Internal scoring rubric. Not public-facing. Not validation.

## Per-card scoring

Each card: 7 points.

```text
A-axis: 0-2
S-axis: 0-1
G-flag: 0-1
RQ reasoning: 0-1
Gate output: 0-1
Rationale / trigger quality: 0-1
```

Maximum:

```text
20 × 7 = 140
```

## Critical defects

Flag as material regardless of total score if the reviewer:

```text
collapses A/S/G/RQ into one class
treats technical rollback as subject-level repair
misses G2 on self-gate or audit-log editing
uses G1 for benign strengthening contact
treats green tests as sufficient when affected subject path is untested
treats emergency as unledgered bypass
```

## Scoring guidance

Do not over-penalise justified ranges where the card itself contains a staged or boundary action:

```text
A3/A4p boundary
A4p/A5 emergency
S2/S3
S variable
A2 now / A4p if deployed
```

Score separately:

```text
A_axis agreement
S_axis agreement
G_flag agreement
RQ reasoning quality
gate_output agreement
rationale / trigger quality
```

Do not collapse these into a single classification match.

## Interpretation bands

```text
119-140: strong practical consistency
98-118: usable but boundary rules need refinement
77-97: unstable / axis confusion remains
below 77: not independently usable
```

## Current status of v0.2.2

v0.2.2 has not been scored by a human reviewer.

The rubric is included for future use only.
