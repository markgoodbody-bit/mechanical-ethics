# Worked Example: Medical Prioritisation Tool

## Scenario

A healthcare provider uses a triage, prioritisation, or risk-scoring tool to help decide how quickly a patient should receive assessment, diagnosis, or treatment.

The tool is described as advisory. Staff can override it.

## 1. Selection

The system selects a risk category, priority level, waiting-list position, or recommended pathway.

## 2. Affected person

The patient carries the consequence.

Possible effects:

- delayed diagnosis;
- missed treatment window;
- worsening condition;
- stress and uncertainty;
- reduced ability to seek alternative care;
- false reassurance;
- escalation only after deterioration.

## 3. Hardening point

Hardening depends on the condition.

Examples:

- diagnostic window closes;
- symptoms worsen;
- condition becomes less treatable;
- patient loses trust and disengages;
- evidence changes or disappears;
- clinical pathway locks in.

## 4. Correction carrier

Possible carriers:

- clinician override;
- patient escalation route;
- rapid second review;
- safety-netting instructions;
- time-limited reassessment;
- automatic flag if symptoms persist or worsen;
- audit of missed escalations;
- authority to move patient up before deterioration.

A human in the loop is not enough if the human lacks time, evidence, authority, or practical ability to override the tool.

## 5. Timing fit

The relevant question is whether review can occur inside the clinical window.

A correction route that works after deterioration is not live protection for the original diagnostic opportunity.

## 6. Classification

Likely result where override exists but is pressured or slow:

**PARTIAL PROTECTION**

Reason: clinical review may exist, but its protective value depends on whether patients and clinicians can trigger timely reassessment before the relevant medical window hardens.

## 7. Minimum repair

A stronger route would include:

- visible escalation instructions;
- patient-facing explanation of what to do if symptoms change;
- clinician override protected from throughput penalties;
- rapid review clock tied to condition risk;
- audit of false negatives, not only throughput;
- record of whether reassessment happened before deterioration.

## One-sentence result

A medical prioritisation tool is only protected by human oversight if the human can actually see, challenge, and change the pathway before the patient's clinical window closes.
