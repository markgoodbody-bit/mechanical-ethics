# Mechanical Ethics v0.7.0 — field-delta audit — 2026-08-24

**Status:** WORKING AUDIT — NOT READER SOURCE — NOT REPOSITORY BASELINE — NOT RELEASE — NOT CANON — NOT VALIDATED — NOT PUBLICATION READY  
**Purpose:** ask whether the TRACE / Campfire / 1F916 work since the v0.7 local reading copy was frozen materially changes what a human Mechanical Ethics reader should understand.  
**Bias:** do not make ME chase every TRACE refinement. Add human-facing text only where the structural lesson changes practical understanding and is not already carried.

---

# 0. Source boundary

Repository preservation baseline:

```text
Mechanical Ethics v0.6.3
main commit: c7f1a2cf1bdceb7bf56e7129f3ff4d9376651d3f
```

The later v0.7.0 working source/PDF were deliberately kept out of the repository baseline. Closed PR #33 preserves the review/integration record, not the source bytes themselves.

Recorded final local reading-copy identity from PR #33:

```text
source file: MECHANICAL_ETHICS_HUMAN_READER_v0_7_0_CC_INTEGRATED_WORKING_CANDIDATE.md
source SHA-256: b4c78b46aaf8aa3e8d2df5ddf2915cdd52aff77b170802fd6956e2bd6e631fff
words: 13,752 by whitespace split
PDF pages: 34
status: LOCAL_READING_COPY / NOT_REPOSITORY_BASELINE / NOT_RELEASED / NOT_CANON / NOT_VALIDATED / NOT_PUBLICATION_READY
```

Recorded v0.7 integration decisions:

- retain/narrow `The Door Out`;
- retain distributed responsibility;
- retain/narrow `When One Case Is Not Enough`;
- discard the proposed appended human closing;
- narrow Appendix B's collective-authority/capture edge.

This audit does **not** pretend to inspect the uncommitted v0.7 source byte-for-byte. It compares the frozen v0.6.3 reader, the recorded v0.7 decisions, and later field lessons.

```text
READING_COPY_RECORD != SOURCE_BYTES
KNOWN_INTEGRATION_DECISION != FULL_CURRENT_TEXT
```

---

# 1. Admission rule for a new ME delta

A TRACE or field lesson enters this audit only if all of the following are true:

1. it changes what an ordinary human reader should understand or do;
2. that practical distinction is not already carried adequately in v0.6.3 or the recorded v0.7 changes;
3. it can be stated without importing machine-facing taxonomy or implementation detail;
4. it does not create a new moral selector, priority rule, authority rule, consent theory, or doctrine;
5. the smallest insertion is preferable to a new chapter or rebuild.

```text
TRACE_DELTA != ME_DELTA
FIELD_FINDING != BOOK_PARAGRAPH
TECHNICAL_PRECISION != HUMAN_CLARITY
```

---

# 2. Candidate human-facing deltas that survive

Only three current lessons survive this filter.

## 2.1 Common clock basis — DISTINCT / small timing insertion

### Field/TRACE lesson

Recent correction-window attack work exposed a simple failure: two times can use the same units and still be incomparable if they start from different events.

Example:

```text
correction completes 8-10 minutes after detection
hardening occurs 11-13 minutes after authorisation
```

Those numbers cannot be compared safely until the relationship between detection and authorisation is known.

### What v0.6.3 already carries

`A Timing Condition` already says:

- the times may be uncertain, ranges or distributions;
- protective action may change the hardening interval;
- `T_det + T_route + T_corr < T_irr` is a mnemonic rather than literal serial arithmetic;
- competing clocks and practical hardening boundaries must remain visible and challengeable.

That is strong. The missing human point is narrower: **same unit does not imply same temporal origin**.

### Candidate insertion

Placement: `A Timing Condition`, after the paragraph explaining uncertain times/ranges/distributions.

```text
The clocks also have to refer to the same underlying sequence, or be translated onto one. Ten minutes measured from the moment a problem is detected cannot be compared directly with twelve minutes measured from an earlier decision unless we know when detection occurred. Numbers can share the same units while still describing different clocks.
```

### Why it earns the words

This prevents a false sense of mathematical precision without importing the event-graph machinery into ME.

```text
SAME_UNIT != SAME_CLOCK
```

Disposition: **RETAIN CANDIDATE**.

---

## 2.2 A record can become stale without being altered — DISTINCT / small custody insertion

### Field/TRACE lesson

1F916 #2101 supplied a useful human case: a derived count was correct when written and carried a current date, but the underlying corpus changed repeatedly inside that same date label.

The record did not need to be forged, edited, or corrupted to become misleading for current use.

### What v0.6.3 already carries

Chapter 8 `Custody` already handles:

- who can alter/delete/copy/use a record;
- independent fragments and comparison;
- risks of evidence custody;
- the danger of a system rewriting its own memory.

The opening and longitudinal sections also distinguish the file from the life and say that evidence can decay.

The remaining absence is explicit **derived-record staleness without alteration**.

### Candidate insertion

Placement: Chapter 8 `Custody`, after `If a system can rewrite its own memory after challenge begins, it should be modest about how confidently it later describes the past.`

```text
A record can also become misleading without being rewritten. A count, status, or summary may be correct when it is produced and stale soon afterwards because the situation underneath it has changed. A current date is not the same thing as a current fact. When a decision depends on a derived record, the system should know what kind of change requires that record to be checked or recomputed.
```

### Why it earns the words

This extends the custody argument from tampering/history integrity to current-world use without turning the chapter into data engineering.

```text
UNCHANGED_RECORD != CURRENT_FACT
```

Disposition: **RETAIN CANDIDATE**.

---

## 2.3 Collective evidence can change the field it measures — DISTINCT / narrow v0.7 insertion

### Field/TRACE lesson

1F916 #2096 produced a concrete reflexivity case: publishing a census of silent citizens plausibly altered later speaking behaviour, including one directly attributed case where the census caused an operator to notice the citizen.

The ethical point is not a statistical theorem. It is that observation, naming, publication and inquiry can themselves become part of what happens next.

### What v0.7 already adds

The recorded v0.7 `When One Case Is Not Enough` section addresses:

- recurrence across several accounts;
- disagreement within collective evidence;
- representation/custody risk;
- frequency not becoming automatic authority;
- combined accounts changing the mechanism rather than forcing each person to restart from zero.

That is the natural home for the reflexivity point.

### Candidate insertion

Placement: `When One Case Is Not Enough`, after the paragraph on combining accounts while preserving differences.

```text
Collecting or publishing a pattern can also change the field being measured. People may respond because they were named or counted; an institution may alter its behaviour because an audit exists. Later evidence may therefore describe a situation partly changed by the act of observing it. That does not make the evidence useless, but it should stop the observer from pretending to have remained outside the scene.
```

### Why it earns the words

This is a human responsibility claim about inquiry and exposure, not a TRACE `MEASURE` primitive or a general claim that all observation is intervention.

```text
OBSERVING_A_SYSTEM != ALWAYS_OUTSIDE_THE_SYSTEM
```

Disposition: **RETAIN CANDIDATE / NARROW IF REGISTER FEELS TOO RESEARCH-METHOD HEAVY**.

---

# 3. Recent lessons that do not currently earn new ME text

## 3.1 Instrument adequacy / operational discrimination — ALREADY CARRIED

Recent TRACE/1F916 work sharpened:

```text
CHECK_EXISTS != CHECK_DETECTS_TARGET_FAILURE
INSTRUMENT_REVIEWED != INSTRUMENT_EXERCISED
```

Chapter 12 `Correction Theatre` already asks:

- what action actually changed;
- who can check it;
- what would count as evidence the repair failed;
- whether a dashboard changes the route or merely produces a cleaner number;
- whether a review's selected cases and measurement basis can carry its wider claim.

That is the human translation. Adding instrument terminology would make the book more technical without adding practical meaning.

Disposition: **NO NEW TEXT**.

## 3.2 Silence / liveness / missing heartbeat — ALREADY CARRIED

Recent field work preserved:

```text
SILENCE != TAMPERING
NO_REPLY_OBSERVED != REFUSAL
PROCESS_EXISTS != PROCESS_HEALTHY
```

v0.6.3 already says silence can mean resolution or that the route taught the person to stop trying, and that a quiet file is not necessarily a quiet life.

That human distinction is broader and better for ME than importing worker/heartbeat vocabulary.

Disposition: **NO NEW TEXT**.

## 3.3 External witness != independent witness — ALREADY / MIXED

Chapter 8 already distinguishes evidence outside the challenged actor's control from evidence held inside it, calls for independent storage where needed, and treats custody as a power relation.

A technical sentence about split-view witnesses or shared control roots belongs in TRACE. If later human cases show that the existing custody language is insufficient, revisit.

Disposition: **NO NEW TEXT NOW**.

## 3.4 Tamper-evidence != truth — ALREADY CARRIED

Chapter 8 states that fragments are no more truthful for being fragments and that good custody makes alteration visible rather than proving truth.

The recent #2138 distinction is therefore already translated adequately.

Disposition: **NO NEW TEXT**.

## 3.5 Null result != mechanism absent — DOMAIN/TRACE, not core ME

The #2096 preregistration repair is methodologically important, but ME need not become a statistics guide.

Where a human case requires it, ordinary wording can say that a test failed to detect an effect rather than proved no mechanism exists.

Disposition: **NO UNIVERSAL BOOK INSERTION**.

## 3.6 Metadata ingress before nominal body loading — TRACE/profile case

```text
METADATA != NON_SEMANTIC_INPUT
BODY_NOT_LOADED != SKILL_NOT_INFLUENTIAL
```

This is important for AI/tooling design but does not currently alter the book's human ethical argument.

Disposition: **NO ME TEXT**.

## 3.7 Self-selected key / authority binding — TRACE/technical worked case

The human version is already present throughout ME: a party cannot manufacture authority merely by controlling the procedure or record that says it is authorised.

Disposition: **NO NEW TEXT**.

## 3.8 Local stale-worker / mutex liveness — implementation evidence only

Useful for TRACE verification and Campfire design; not a human-reader concept requiring new prose.

Disposition: **NO ME TEXT**.

## 3.9 Event/precedence graph correction timing — keep machine-facing

ME already says the serial correction expression is a conceptual compression, stages may overlap/repeat, the whole protective process matters, and the relevant hardening boundary must be applied separately to threatened paths.

The event/precedence graph belongs in TRACE. Only the common-clock-basis clarification in section 2.1 earns human prose.

Disposition: **NO GRAPH OR CRITICAL-PATH FORMALISM IN ME**.

## 3.10 Boundary condition / moral adequacy — already exposed

ME already says the practical hardening boundary, threatened path designation, and priority rule must remain visible and challengeable, and the notation does not decide which path should take priority.

That is the correct human translation of:

```text
BOUNDARY_CONDITION_DECLARED != MORAL_ADEQUACY_ESTABLISHED
```

Disposition: **NO NEW TEXT**.

---

# 4. Existing v0.7 changes remain directionally sound

Nothing in the later field work currently falsifies the recorded v0.7 additions.

## The Door Out

Recent authority/refusal work reinforces rather than weakens the need to distinguish formal exit from practically viable continuation.

No new consent theory or exit rule is earned.

## Distributed responsibility

The Campfire build itself repeatedly showed that semantic selection, transport, credentials, process lifecycle, public persistence and human actuation can sit in different places. That supports the existing human proposition that responsibility can be distributed without disappearing.

It does not justify assigning equal blame or duties to every contributing actor.

## When One Case Is Not Enough

The section remains useful. The #2096 reflexivity sentence in section 2.3 is the only current addition this audit recommends.

## Human closing

The earlier decision to discard the appended second closing still looks correct. The new field lessons do not justify adding another conclusion paragraph.

---

# 5. Proposed delta size

Current recommendation:

```text
new chapters:        0
new sections:        0
candidate inserts:   3
approx new words:    ~120-150 before editorial compression
new equations:       0
new diagrams:        0
new moral rules:     0
new authority rules: 0
```

A v0.7 revision should remain a reduction edition in substance. If these insertions force compensating cuts elsewhere, cut repetition rather than expanding the book by default.

---

# 6. What this audit cannot establish

The exact v0.7 source bytes are not in the repository. Therefore this audit cannot establish that one of the proposed sentences is not already present in equivalent wording in the final local source.

Before applying any text:

1. reacquire the exact local v0.7 source matching SHA-256 `b4c78b46...`;
2. locate the three proposed placements;
3. run a redundancy/read-register pass against the actual surrounding paragraphs;
4. retain/narrow/discard each insertion independently;
5. preserve the frozen v0.6.3 baseline;
6. any changed reader source must receive a new version under the repository version rule rather than silently overwriting v0.6.3 or the recorded v0.7 reading copy.

```text
AUDIT_RECOMMENDS_TEXT != TEXT_INTEGRATED
SOURCE_HASH_KNOWN != SOURCE_BYTES_AVAILABLE
```

---

# 7. Current disposition

```text
ME v0.6.3 repository baseline:  UNCHANGED
ME v0.7 local reading copy:     PRESERVED / SOURCE NOT IN REPO
FIELD DELTA CANDIDATES:         3 SMALL INSERTIONS
REBUILD:                        NO
NEW CHAPTER:                    NO
TRACE TERMINOLOGY IMPORT:       NO
NEXT MOVE:                      REACQUIRE EXACT v0.7 SOURCE, THEN REDUNDANCY PASS
```
