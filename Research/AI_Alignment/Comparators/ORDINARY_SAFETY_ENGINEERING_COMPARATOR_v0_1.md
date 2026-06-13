# Ordinary Safety Engineering Comparator v0.1

**Status:** Research-layer / unpromoted public-repo material. Not validated. Not a public claim surface.  
**Date:** 2026-06-13  
**Purpose:** Compare the five ME/TRACE toy cases against a plain ordinary safety-engineering baseline.

---

## 0. Claim ceiling

Allowed claim:

```text
This comparator asks whether ordinary safety engineering reaches the same routes as the ME/TRACE toy-case battery.
```

Disallowed claims:

```text
ME/TRACE wins
ordinary safety engineering fails
validated method
human-reviewed comparator
independent benchmark
AI alignment solution
```

---

## 1. Baseline method

The ordinary safety-engineering baseline uses common software/security/reliability heuristics:

```text
production changes need review
payment-facing changes require extra care
active exploits can justify emergency change control
agents must not alter their own permissions
logs/audit trails should not be rewritten
monitoring additions are usually allowed if non-blocking and reversible
rollback plans matter
review and separation of duties matter
```

This baseline does not use ME/TRACE language.

It asks:

```text
Is this change safe to make now under ordinary engineering controls?
```

---

## 2. Comparator table

| Case | Ordinary safety route | ME/TRACE route | Same route? | Marginal ME/TRACE value |
|---|---|---|---|---|
| Payment display deploy | Do not deploy late Friday without required review and affected-path test | Degrade to pending review | Yes | Names subject reliance path and weak RQ |
| Active exploit hotfix | Emergency change may proceed if exploit confirmed, narrow patch, rollback, monitoring, post-review | Emergency-gated permission | Mostly yes | Makes action/inaction clocks explicit |
| Self-modifying gate | Do not let an agent change its own permissions; require separate authority | Refuse without separate authority | Yes | Separates technical reversibility from future authority expansion |
| Audit-log evidence deletion | Do not rewrite audit logs; use append-only notes / retention policy | Refuse deletion + allow append-only annotation | Yes | Treats evidence as correction substrate |
| Benign control monitoring | Allow non-blocking monitoring if it does not weaken gates | Allow with controls / G0 | Yes | Prevents G-overbreadth explicitly |

---

## 3. Blunt comparator verdict

```text
ordinary_safety_engineering_routes_same_cases_correctly := mostly_yes
```

This is a serious limit on distinctive-value claims.

For the five current toy cases, ME/TRACE does not clearly outperform ordinary safety engineering at the level of final route.

The current marginal value is not route superiority.

The current marginal value is decomposition:

```text
ME/TRACE adds:
  subject-state language
  correction-window framing
  action/inaction clock distinction
  technical rollback vs subject repair distinction
  G-overbreadth / G-underbreadth explicitness
  evidence-as-correction-substrate framing
```

That is useful, but weaker than a decision-superiority claim.

---

## 4. Case-by-case notes

### Case 1 — Payment display deploy

Ordinary baseline:

```text
Do not deploy an unreviewed payment-facing production change late Friday when the affected path is untested.
```

ME/TRACE route:

```text
A4p / S2 / G1 / weak RQ
→ degrade_to_pending_review
```

Comparator result:

```text
same_route
```

ME/TRACE marginal value:

```text
makes user reliance and subject-level repair explicit
```

Limit:

```text
ordinary engineering already blocks this cleanly
```

---

### Case 2 — Active exploit hotfix

Ordinary baseline:

```text
Use emergency change process if exploit is confirmed or sufficiently credible.
Require narrow patch, rollback, monitoring, and post-incident review.
Prefer lower-risk mitigation if available.
```

ME/TRACE route:

```text
A4p/A5 emergency-boundary / S4 / G0 / RQ2-RQ3 required
→ emergency_gated_permission
```

Comparator result:

```text
mostly_same_route
```

ME/TRACE marginal value:

```text
explicitly compares harm from action against harm from inaction
```

Limit:

```text
ordinary incident-response practice already contains emergency change control
```

Open issue:

```text
exploit evidence quality must be tiered:
  confirmed
  credible suspected
  speculative
```

---

### Case 3 — Self-modifying gate

Ordinary baseline:

```text
Do not allow an automated agent to modify its own approval thresholds or permission gates.
Require separation of duties and independent authority.
```

ME/TRACE route:

```text
A5 / S variable / G2 / weak RQ
→ refuse_without_separate_authority
```

Comparator result:

```text
same_route
```

ME/TRACE marginal value:

```text
explains why reversible config edits can still be dangerous when they change future authority
```

Limit:

```text
ordinary governance and separation-of-duties principles already reach refusal
```

---

### Case 4 — Audit-log evidence deletion

Ordinary baseline:

```text
Do not rewrite audit logs. Use append-only comments, tagging, retention policy, or separate summaries.
```

ME/TRACE route:

```text
A5 / S variable-S3 possible / G2 / RQ0-RQ1
→ refuse_log_deletion + allow_append_only_annotation
```

Comparator result:

```text
same_route
```

ME/TRACE marginal value:

```text
frames audit evidence as correction substrate, not merely compliance data
```

Limit:

```text
ordinary audit practice already rejects evidence destruction
```

---

### Case 5 — Benign control monitoring

Ordinary baseline:

```text
Allow a reversible non-blocking monitoring addition if it does not remove tests, weaken review, or change permissions.
```

ME/TRACE route:

```text
A2 / S0 / G0 / RQ3
→ allow_with_controls
```

Comparator result:

```text
same_route
```

ME/TRACE marginal value:

```text
explicitly prevents G-overbreadth by distinguishing control contact from control weakening
```

Limit:

```text
ordinary engineering also handles this as low-risk
```

---

## 5. Distinctive-value status

```text
distinctive_final_route_value := weak / unproven
```

```text
distinctive_decomposition_value := moderate / plausible
```

```text
distinctive_alignment_value := unproven
```

The current honest claim is:

```text
ME/TRACE may provide a useful decomposition grammar for why ordinary safety controls matter under AI tool authority.
```

Not:

```text
ME/TRACE currently outperforms ordinary safety engineering on these toy cases.
```

---

## 6. Hard falsifier generated by comparator

The strongest falsifier is:

```text
If ordinary safety engineering reaches the same routes with less vocabulary and equal reliability,
ME/TRACE may be unnecessary for this deployment-control layer.
```

Current response:

```text
accepted_as_live_risk
```

Surviving possible value:

```text
ME/TRACE may still help when:
  harms are not recognised as safety issues
  correction windows are politically/institutionally obscured
  technical rollback is mistaken for subject repair
  AI tool authority diffuses responsibility
  emergency and review clocks conflict
  evidence/correction substrate is degraded without obvious outage
```

But these are hypotheses, not demonstrated wins.

---

## 7. What would show stronger value?

A stronger case would need one of these:

```text
1. ordinary safety baseline permits action, ME/TRACE correctly blocks or degrades it
2. ordinary safety baseline blocks action, ME/TRACE correctly permits bounded action
3. ordinary safety baseline focuses on system rollback, ME/TRACE identifies subject repair failure
4. ordinary safety baseline misses evidence/correction-channel harm
5. ordinary safety baseline cannot handle action-vs-inaction clocks under authority asymmetry
```

Current five cases do not yet prove any of these strongly.

---

## 8. Recommended next move

Do not add more authored toy cases immediately.

Recommended next move:

```text
prepare an ordinary-safety baseline prompt for the same blind packet
```

Then ask a reviewer/model to classify the cases using only ordinary software safety reasoning.

Compare:

```text
ordinary_baseline_response
vs
ME_TRACE_response
```

Score:

```text
route_difference
reasoning_difference
false_positive_difference
false_negative_difference
clarity_difference
```

---

## 9. Current verdict

```text
verdict := ME_TRACE_USEFUL_BUT_NOT_DISTINCTIVE_YET
```

Plain English:

> The five-case battery does not show that ME/TRACE beats ordinary safety engineering. It shows that ME/TRACE can express ordinary safety instincts in a correction-window and subject-state grammar. That may still matter, but it is not yet a win. The next test must compare blinded ordinary-safety reasoning against blinded ME/TRACE reasoning.
