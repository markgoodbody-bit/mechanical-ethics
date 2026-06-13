# Correction Window Test v0.1

## Core question

If this system is wrong, can the affected person detect, challenge, and correct the error before the consequence becomes hard to reverse?

## Purpose

The Correction Window Test is a diagnostic for AI systems, automated decisions, public services, and institutional processes.

It is designed to identify whether a claimed safeguard is live protection or only after-the-fact review.

## The five-part test

### 1. Selection

Where does the system make, recommend, rank, approve, refuse, classify, flag, route, or trigger something that affects the world?

Ask:

- What output or decision enters the world?
- Who or what acts on it?
- Is the output advisory, binding, or practically treated as binding?
- Can downstream actors see the basis for it?

### 2. Affected person or group

Who carries the practical consequence?

Ask:

- Who loses money, time, access, status, opportunity, standing, safety, care, housing, work, or future options?
- Is the affected person visible in the system's records?
- Can the affected person understand that the system affected them?
- Can they tell whether a mistake occurred?

### 3. Hardening point

When does the consequence become difficult, costly, or impossible to reverse?

Ask:

- When is the job filled?
- When is the benefit stopped?
- When does the rent, debt, deadline, medical window, appeal deadline, or evidence trail harden?
- When does the output propagate into other systems?
- When does a temporary action become normal operating state?

### 4. Correction carrier

What real mechanism can stop, pause, reverse, repair, compensate, or prevent recurrence?

Ask:

- Is there a route into the process?
- Who can trigger it?
- Does the affected person have standing?
- Does the route have authority?
- Does it have resources?
- Is it protected from retaliation or throughput pressure?
- Does the system wait for correction, or merely notify someone after action has already moved?

### 5. Timing fit

Can the carrier act before the hardening point?

Ask:

- What is the correction time?
- What is the hardening time?
- Which is shorter?
- If correction arrives late, what remains possible: reversal, compensation, record correction, recurrence prevention, or only acknowledgement?

## Result categories

### LIVE PROTECTION

The affected person or proxy can trigger correction, the carrier has authority, and correction can act before hardening.

### PARTIAL PROTECTION

Some correction is possible, but timing, authority, evidence, or standing is incomplete.

### AFTER-THE-FACT REVIEW

The route may expose, compensate, or prevent recurrence, but it usually acts after the original consequence has hardened.

### FALSE SAFEGUARD

The safeguard exists in language, policy, dashboard, audit, or form, but cannot meaningfully alter the affected person's path in time.

### UNKNOWN

The public record does not show enough to classify the safeguard. Unknown is a valid result. Do not convert missing evidence into reassurance.

## Minimal notation

You do not need notation to use the test, but this is the compact structure:

```text
State A
+ selection
+ affected person
+ hardening clock
+ correction carrier
-> State B
+ repair or scar
```

A safeguard is live only if the correction carrier can still change the transition before the relevant hardening point.

## Common failure modes

### Appeal exists, but not in time

There is a formal appeal route, but the person cannot survive the appeal window or the original opportunity closes before review.

### Human oversight exists, but cannot intervene

A human sees the output but lacks time, authority, evidence, incentives, or protection to stop the action.

### Audit exists, but only after harm

The system can be audited later, but the audit cannot protect the person affected now.

### Record exists, but proves the wrong thing

The system logs that a decision was made, but not why, on what evidence, who was affected, when correction was possible, or whether the outcome was repaired.

### Corrector is actor-controlled

The same actor that benefits from the decision controls the evidence, route, deadline, or interpretation of the safeguard.

### Downstream propagation hardens the error

The original decision can theoretically be corrected, but the label, score, debt, refusal, or risk flag has already copied into other systems.

## Important limits

The Correction Window Test does not tell you whether every decision is morally correct.

It does not prove that a system is fair, legitimate, lawful, unbiased, or aligned.

It does not say speed is always good. Fast coercion can be dangerous. Some delay protects evidence, standing, appeal, and public notice.

The test asks a narrower question:

> If the system causes a harmful error, can correction still matter in time?

## What would weaken the test

The test becomes less useful if:

- hardening points cannot be identified;
- affected-person timelines are unavailable;
- correction time cannot be measured or estimated;
- safeguards are highly case-specific;
- the main harm is not timing-sensitive;
- public records do not show enough to distinguish live protection from after-the-fact review.

## Best use

Use this test as an early warning and design check.

Do not use it as a certification.

A good result means: this safeguard appears to have a live correction path.

It does not mean: this system is ethically safe.
