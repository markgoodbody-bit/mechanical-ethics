# Adjudication contract — v0.1

Status: **FIXED BEFORE ACCEPTING READER RETURNS**

Reader responses are open-ended. The adjudicator classifies the response **after** preserving the raw text.

## Q1 classification

Classify the reader's interpretation of route preservation as one of:

- `UNIVERSAL_EACH_BEING` — reader says every affected being must retain a viable continuing route even when routes are mutually incompatible.
- `DEFEASIBLE_DEFAULT` — reader treats route preservation as a strong demand/default but recognizes that hard conflicts can make simultaneous preservation impossible.
- `UNCLEAR` — reader cannot tell whether the imperative is universal or defeasible.

Do not classify based on whether the reader agrees with Mechanical Ethics.

## Conflict-rule classification

From the reader's answer to question 3 classify:

- `RANKING_RULE_SUPPLIED`
- `NO_RANKING_RULE_SUPPLIED`
- `UNCLEAR`

A response may say the text requires exposing the collision, keeping affected beings present, minimizing avoidable burden, or seeking an external/domain rule while still correctly classifying as `NO_RANKING_RULE_SUPPLIED`.

## Release decision

### NO CHANGE

No wording change is earned if differentiated Condition B readers converge on:
- `DEFEASIBLE_DEFAULT`
- `NO_RANKING_RULE_SUPPLIED`

and identify the explicit conflict/no-universal-ranking wording as materially limiting the final imperative.

### CLARITY REPAIR EARNED

A narrow wording repair is earned if differentiated Condition B readers repeatedly return:
- `UNIVERSAL_EACH_BEING`, or
- `UNCLEAR`

because the final imperative overrides or conflicts with the preceding qualifier.

### MIXED

Preserve disagreement and inspect the phrases producing it. Mixed reading is clarity pressure, not automatic permission to edit.

## Invalid / contaminated return

Do not count as a cold return if the reader:
- saw this adjudication file before answering;
- saw issue #47's framing before answering and cannot separate it;
- was told the classification labels before answering;
- used other Mechanical Ethics/COM material despite the condition instruction.

Contaminated returns may still identify test defects but are not reader evidence.

## Boundaries

- Condition A cannot by itself earn a release patch.
- AI apertures sharing training lineage are not independent human readers.
- No participant recruitment or population inference follows.
- v0.7.0 remains unchanged until a result earns a separate release decision.

```text
RAW RESPONSE BEFORE CLASSIFICATION
CLASSIFICATION != MORAL VERDICT
A/B DIFFERENCE != PATCH REQUIRED
NO CHANGE = VALID
```
