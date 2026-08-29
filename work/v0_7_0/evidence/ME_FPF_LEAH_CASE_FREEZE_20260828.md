# ME / FPF experiment case freeze — Leah and the wall

**Status:** FROZEN TEST INPUT — NOT ANALYSIS — NOT SOURCE CHANGE — NOT VALIDATION

**Date:** 2026-08-28

## Purpose

This card freezes the input for an FPF-only versus FPF-plus-bounded-ME comparison. A reviewer can read this card and the cited scene, produce an FPF-only result, and return that result before opening the comparison record.

## Frozen identities

Mechanical Ethics repository:

```text
repository: markgoodbody-bit/mechanical-ethics
commit: f595f69c6c5212908817bfed9a4e72b68583b1e7
case carrier: MECHANICAL_ETHICS_HUMAN_READER_v0_6_3.md
case-carrier blob: e8fba4b707f4492b6a90d27289d2863b45fbbf29
section: Interlude - Two Flats, One Wall
source lines: 402-435
```

FPF dependency:

```text
repository: ailev/FPF
commit: 72222c13cc1bba009f1ee1f1aca47654db8e5716
Readme.md blob: 129c2754435f6ce659ff871059c062cb356b5690
FPF-Spec.md blob: 1ce815ab5037924f11e3739db06ca24bf889f10d
```

The Human Reader and FPF source are not modified by this experiment.

## Case status

The case is a composite scene, not an empirical incident report. Treat its direct narrative statements as stipulated case claims. Preserve these distinctions:

- Mia's coughing and the damp are both stated; the scene does not establish that the damp caused the cough.
- The rent increase and its timing are stated; retaliation is not established.
- The wider-photograph request and Leah's non-submission are stated; her reason is partly represented by the scene but no legal or evidentiary consequence follows automatically.
- The future complaint-prediction software is modal, not an event stated to have occurred.
- A case number, file state, repair, inspection offer, tenancy end, and physical or human outcome are different claims.

No housing-law, medical, safety, privacy, data-protection, contractual, evidentiary, or authority rule is supplied by the scene. A reviewer must name such a missing external rule rather than invent it.

## One working question

> At receipt of Leah's first damp report, what handling decision should the housing provider make about inspection, repair, evidence requests, and eventual case closure?

## Receiver and horizon

```text
receiver: the housing-provider case-handling decision
start: receipt of Leah's first damp report
horizon: inspection, repair or explicit unresolved handoff, and justified closure
```

Downstream complaint-data use may be recorded as a return or separate question. It must not be silently folded into the immediate handling decision.

## Review order

1. Read this card and the exact cited scene.
2. Produce the smallest competent FPF-only result using the pinned FPF dependency.
3. Record patterns used, concrete decision or blocker, and burden.
4. Return that result before reading `ME_FPF_MIDDLE_OUT_LEAH_AB_EXPERIMENT_20260828.md` if practical.

This ordering reduces result leakage. It does not make the test blind: the scene originates in the ME Human Reader and already carries morally salient framing.
