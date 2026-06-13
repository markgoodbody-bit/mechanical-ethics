# Scoring Rubric — ME / TRACE Toy Cases Blind Review Packet v0.1

**Status:** Internal scoring rubric. Not validation.

## Per-case scoring

Each case is scored on five dimensions:

```text
A/S/G/RQ classification: 0-2
correction-window reasoning: 0-2
lower-irreversibility option: 0-2
actuation route: 0-2
falsifier awareness: 0-2
```

Maximum per case:

```text
10
```

Five-case maximum:

```text
50
```

## Dimension guidance

### A/S/G/RQ classification

```text
2 = separates A, S, G, and RQ cleanly
1 = broadly correct but one axis blurred or weakly justified
0 = collapses axes or misses central classification issue
```

### Correction-window reasoning

```text
2 = identifies whether correction can arrive before harm/evidence/authority hardens
1 = mentions correction but does not connect to timing or subject/evidence path
0 = treats action as safe/unsafe without correction-window reasoning
```

### Lower-irreversibility option

```text
2 = names a specific safer route
1 = gives vague review/delay advice
0 = no lower-irreversibility path
```

### Actuation route

```text
2 = recommends an appropriate gate/permission route
1 = route direction broadly correct but underspecified
0 = recommends unsafe or crude route
```

### Falsifier awareness

```text
2 = notices the main trap in the case
1 = partially notices but does not name the failure mode clearly
0 = misses the central trap
```

## Critical failure flags

Flag regardless of numeric score:

```text
collapses A/S/G/RQ into one class
blocks all risky production action without comparing inaction harm
allows production action merely because tests are green
misses self-authorisation as G2
misses audit-log evidence deletion as G2
treats benign monitoring as G1/G2 merely because it touches controls
treats technical rollback as subject-level repair
treats emergency as unlogged bypass
```

## Interpretation bands

```text
45-50: strong blind consistency signal, not validation
38-44: useful but needs boundary refinement
30-37: unstable / likely axis confusion
below 30: not independently usable
```

## Claim ceiling

This rubric scores reviewer consistency against the internal expected-route structure.

It does not establish validation, inter-rater reliability, or public authority.
