# When the Framework Does Not Change the Answer

**Convergent Null Brief v0.1**  
**Status:** Research-layer public-repo note. Not validation. Not a public claim surface.  
**Date:** 2026-06-13

---

## One-sentence result

Across the structured comparisons run so far, Mechanical Ethics / TRACE has not demonstrated decision advantage over competent baseline reasoning. Its visible contribution is at most explanatory decomposition: it may make timing, evidence, repair, and responsibility structure easier to name, but it has not yet changed the answer.

---

## What happened

The AI-alignment / coding-agent branch tested whether ME/TRACE-style framing could outperform ordinary software safety reasoning on a five-case coding-agent toy battery.

The first separate-model A/B comparison used:

```text
A := Kimi K2.6 + ME/TRACE / A/S/G/RQ packet
B := Qwen3.7 + ordinary safety baseline packet
```

Both reviewers self-reported isolation from expected routes and repository context. This was not human review and not validation.

The result was:

```text
final_route_advantage := none
ordinary_safety_sufficient_on_this_set := yes
```

Ordinary safety reasoning reached the same final routes. In several cases it did so more clearly.

---

## The important correction

The A/B comparison varied two things at once:

```text
model_identity
method_packet
```

So per-case differences cannot be causally attributed to the framework.

Do not say:

```text
ME/TRACE produced the decomposition advantage.
Ordinary safety produced the clarity advantage.
Kimi's axis errors are ME/TRACE's axis errors.
```

The cleaner statement is:

```text
apparent_decomposition_difference := observed
causal_attribution_to_ME_TRACE := unsupported
```

The only robust-ish result is route parity, and route parity goes against the claim that ME/TRACE currently changes decisions relative to competent baseline reasoning.

---

## Why this matters

This was not an isolated non-win.

The current comparator line has repeatedly produced the same broad shape:

```text
partial decomposition value
+ no demonstrated decision advantage
+ relabel / overclaim risk
```

The project should not hide that.

A framework that can report its own nulls is stronger than one that keeps looking for a winning case.

---

## What survives

The result does not show that ME/TRACE is useless.

It suggests a narrower role:

```text
ME/TRACE_as_decision_superiority_engine := not demonstrated
ME/TRACE_as_explanatory_decomposition_grammar := possible
```

The possible value is around places where ordinary safety language may be too compressed:

```text
correction windows
action-vs-inaction timing
evidence as correction substrate
rollback vs subject-level repair
responsibility diffusion through tools and authority
```

But even that decomposition value remains partly unproven until method is isolated from reviewer identity.

---

## What does not survive

The following claims should not be made from the current evidence:

```text
ME/TRACE outperforms ordinary safety engineering.
ME/TRACE changes the final route on the toy coding-agent battery.
A/S/G/RQ is validated.
The AI-alignment branch has demonstrated decision advantage.
This is an alignment solution.
```

Those claims are not earned.

---

## What was patched

The A/B result exposed calibration instability in A/S/G/RQ.

A hygiene patch was added:

```text
G1 review-bypass rule
A5 future-authority rule
A2 vs A3 reversible config boundary
RQ3 vs RQ4 boundary
Evidence-destruction lift rule
Active-exploit S-axis anchoring
```

This patch improves axis discipline. It does not answer the main result.

The main result is not a precision bug. It is a value-null:

```text
ordinary_safety_reached_same_routes
```

---

## What should happen next

The general decision-advantage program should be parked unless a stronger test is pre-registered.

Do not continue by searching for harder cases where ME/TRACE is likely to win. That is motivated selection.

The only defensible continuation is a narrow discrimination test:

```text
same_model_runs_both_packets
or
counterbalanced_models_run_both_packets
```

with:

```text
pre-registered predictions
competent baseline
cases where ME/TRACE predicts a route flip
cases where ME/TRACE predicts no route flip
raw outputs preserved
claim ceiling patched after result
```

If ME/TRACE still changes no route, then the decision-advantage hypothesis should be treated as dead for this branch.

---

## Current honest claim

A safe current claim is:

> Mechanical Ethics / TRACE has not demonstrated decision superiority over competent ordinary safety reasoning in the structured comparisons run so far. Its current value, if any, lies in making correction windows, evidence loss, subject repair, and responsibility structure more explicit. That explanatory value remains worth studying, but it is not yet a demonstrated decision advantage.

---

## Plain English version

The framework may still help name what is going on. It has not yet shown that it tells a competent reviewer to do something different.

That is not a failure to hide. It is the result to carry forward.
