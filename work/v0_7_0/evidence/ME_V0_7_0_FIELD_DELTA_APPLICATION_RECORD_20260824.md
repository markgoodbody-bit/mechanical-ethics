# Mechanical Ethics v0.7.0 — field-delta application record — 2026-08-24

**Status:** LOCAL WORKING CANDIDATE RECORD — NOT REPOSITORY BASELINE — NOT RELEASE — NOT CANON — NOT VALIDATED — NOT PUBLICATION READY  
**Audit:** `ME_V0_7_0_FIELD_DELTA_AUDIT_20260824.md`  
**Purpose:** record the exact-source redundancy pass and a three-insertion working candidate produced from the verified v0.7 reading-copy source.

---

## 1. Exact source recovered

The exact final v0.7 local reading-copy source was recovered from Mark's ChatGPT Library:

```text
file: MECHANICAL_ETHICS_HUMAN_READER_v0_7_0_CC_INTEGRATED_WORKING_CANDIDATE.md
bytes: 84,967
SHA-256: b4c78b46aaf8aa3e8d2df5ddf2915cdd52aff77b170802fd6956e2bd6e631fff
words: 13,752 by whitespace split
```

The observed SHA-256 exactly matches the source identity preserved in closed PR #33 / `FINAL_LOCAL_READING_COPY_RECORD.md`.

Therefore the field-delta pass is now grounded in the actual final local v0.7 source rather than a reconstruction from the v0.6.3 baseline and integration notes.

```text
RECORDED_HASH == RECOVERED_SOURCE_HASH
SOURCE_IDENTITY_MATCH != PUBLICATION_STATUS_CHANGED
```

The Library original was not modified.

---

## 2. Exact-source redundancy/register pass

The three candidate placements from the audit were checked against the actual v0.7 source.

### 2.1 Common clock basis — RETAIN / NARROWED

Exact surrounding source already states that timing values may be uncertain/ranges/distributions and that the familiar detection/routing/correction expression is a mnemonic rather than fixed serial arithmetic.

It does **not** state that two durations sharing a unit may still be incomparable because they use different temporal origins.

Final candidate insertion after the uncertainty paragraph:

```text
The clocks also need a common starting point, or a known translation between them. Ten minutes after detection cannot be compared directly with twelve minutes after an earlier decision unless we know when detection occurred. Shared units do not make two clocks the same.
```

Disposition: **RETAIN**.

### 2.2 Derived-record staleness without alteration — RETAIN / NARROWED

Exact Chapter 8 already distinguishes custody, alteration visibility, independent fragments, exposure risk, and the danger of a system rewriting its own memory after challenge begins.

It does **not** explicitly state that an unchanged derived record can become stale because its underlying situation changed.

Final candidate insertion after the existing memory-rewrite sentence:

```text
A record can become misleading without being rewritten. A count or summary may be correct when produced and stale after the situation beneath it changes. A current date is not the same as a current fact. If a decision depends on a derived record, the system should know what change requires it to be checked again.
```

Disposition: **RETAIN**.

### 2.3 Collective evidence can alter what happens next — RETAIN / NARROWED

Exact `When One Case Is Not Enough` already carries recurrence, disagreement, representation/custody risk, frequency-not-authority, and collective correction.

It does **not** state the reflexivity point that naming/counting/auditing can alter the later field.

The audit's longer research-method wording was narrowed to preserve the human register:

```text
Collecting a pattern can change what happens next. People may respond because they were named or counted; an institution may change because an audit exists. Later evidence may therefore describe a field partly changed by the observation itself.
```

Disposition: **RETAIN / NARROWED**.

---

## 3. Applied candidate identity

A new local candidate was generated without altering the recovered source:

```text
file: MECHANICAL_ETHICS_HUMAN_READER_v0_7_0_FIELD_DELTA_WORKING_CANDIDATE.md
SHA-256: da60e20c188692238f3b8b0cd94dd5e1e40c4baa60d0b276af5636d468ce954b
words: 13,890 by whitespace split
delta from exact v0.7 source: +138 words
```

The unified diff contains exactly three added paragraphs and no substitutions/deletions elsewhere.

```text
new chapters:        0
new sections:        0
insertions:          3
deletions:           0
new equations:       0
new diagrams:        0
new moral rules:     0
new authority rules: 0
```

This is still a **working candidate**, not a new official numbered Mechanical Ethics baseline. The filename deliberately retains `v0_7_0_FIELD_DELTA_WORKING_CANDIDATE` rather than manufacturing a release/version decision from an editorial experiment.

---

## 4. Audit decisions that still stand

The exact-source pass did not earn additional ME prose for:

- instrument adequacy / operational discrimination — already translated by `Correction Theatre`;
- silence/liveness — already translated by the quiet-file / quiet-life distinction;
- external witness independence — substantially carried by `Custody`;
- tamper-evidence != truth — already carried;
- null result != mechanism absent — domain/statistical method, not a universal ME paragraph;
- metadata ingress, self-selected verification key, stale worker/mutex — TRACE/technical cases;
- event/precedence graph correction formalism — keep machine-facing;
- a new hardening-boundary morality or priority rule — existing ME keeps designation/boundary/priority visible and contestable.

Existing recorded v0.7 decisions also remain intact:

```text
The Door Out:                  retained/narrowed
Distributed responsibility:   retained
When One Case Is Not Enough:  retained/narrowed
Second human closing:          discarded
Collective authority edge:    narrowed
```

---

## 5. What this does not establish

The three paragraphs have survived one exact-source redundancy/register pass. That does not establish that they improve the complete reader, deserve release, or should survive a later read-through.

Do not infer:

```text
EXACT_SOURCE_APPLIED != PUBLICATION_READY
THREE_INSERTIONS != NEW_BASELINE
FIELD_DERIVED != VALIDATED
SOURCE_HASH_MATCH != CONTENT_APPROVAL
```

The v0.6.3 repository baseline remains untouched. The recovered v0.7 Library source remains untouched.

---

## 6. Next boundary

The useful next ME step is a **whole-reader coherence read** of the +138-word candidate, with deletion bias:

- does either timing paragraph now repeat Appendix A enough to require a compensating cut?
- does the Custody insertion belong there rather than earlier in the file/life discussion?
- does the collective reflexivity sentence interrupt the chapter's conviction-philosophy register?
- can the same work be done in fewer words?

Do not open another broad theory review until that read finds an actual problem.
