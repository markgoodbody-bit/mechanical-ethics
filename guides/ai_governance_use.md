# Guide: Using the Correction Window Test in AI Governance

## Purpose

This guide shows how to use the Correction Window Test when reviewing an AI system.

It does not claim to solve AI alignment. It focuses on one narrower issue:

> Can correction act before an AI-shaped consequence hardens?

## Why this matters for AI

AI systems can compress the time between selection and consequence.

They may rank, classify, recommend, generate, approve, refuse, flag, route, summarise, prioritise, or execute.

Even when they are officially advisory, their outputs may become practically binding if people, workflows, or other systems normally follow them.

The faster and more automated the route, the more important the correction window becomes.

## Apply the test before deployment

### 1. Identify the AI selection

Ask:

- What output does the AI produce?
- Who or what acts on it?
- Does it affect access, ranking, timing, payment, risk, opportunity, care, enforcement, or status?
- Is it advisory, binding, or practically treated as binding?

### 2. Identify affected people

Ask:

- Who can be harmed by a false positive?
- Who can be harmed by a false negative?
- Who may never know the AI affected them?
- Who has the least ability to challenge?

### 3. Identify hardening points

Ask:

- When does the recommendation become action?
- When does the action become difficult to reverse?
- Does the output copy into other systems?
- Does a temporary label become permanent record?
- Does an opportunity close before review?

### 4. Identify correction carriers

Ask:

- Can the affected person trigger review?
- Can a human pause the route?
- Can the system rollback or restore?
- Are reasons, inputs, and outputs logged?
- Is there a deadline for the corrector?
- Is override protected from throughput pressure?

### 5. Compare clocks

Ask:

- How long before harm hardens?
- How long does review take?
- Which is shorter?
- What remains possible if review arrives late?

## Common AI governance failures

### Human-in-the-loop theatre

A human is present but lacks time, authority, evidence, incentives, or permission to intervene.

### Audit-after-harm

The system can be audited later, but the audit cannot protect the person affected now.

### Model-card substitution

Documentation describes the model, but does not give the affected person a live correction route.

### Dashboard without brake

The system monitors risk but the warning does not reach a mechanism that can pause or reverse the action.

### Advisory output treated as binding

The system is officially advisory, but downstream actors follow it as default.

### Propagation before challenge

The output enters other systems before the affected person can contest it.

### Operator-controlled safeguard

The actor benefiting from the system controls the evidence, review route, and deadline.

## Minimum deployment questions

Before consequential deployment, answer:

1. What is the fastest route by which the AI output can affect a person?
2. What is the earliest point at which the affected person can know?
3. Can they trigger review?
4. Can the review pause the action?
5. Can the route restore the original path?
6. What happens while review is pending?
7. What records prove the selection, reason, timing, and outcome?
8. Who is responsible if correction arrives late?

## Design pattern: staged action

The safest pattern is often not "AI cannot act."

It is:

1. AI drafts or recommends;
2. action enters a reversible stage;
3. affected person or reviewer can detect and challenge;
4. release to irreversible effect requires a carrier with authority;
5. logs preserve selection, reason, time, and repair outcome.

## Design pattern: pause-on-credible-challenge

Where harm can harden quickly, a credible challenge should pause the pathway unless there is a stronger countervailing risk.

If the system cannot pause, it should not describe the review route as live protection.

## Design pattern: correction deadline for the corrector

Many systems impose deadlines on affected people but not on the correction authority.

A live safeguard needs a deadline for the corrector that fits inside the hardening window.

## Design pattern: false-negative review

Systems often audit visible positives: people flagged, blocked, rejected, or selected.

For many AI systems, false negatives also matter: people wrongly ignored, deprioritised, excluded, or not escalated.

Correction design should account for both.

## Claim limit

A system passing this test is not automatically safe or aligned.

It only means that one necessary condition appears stronger: the correction route may still matter in time.
