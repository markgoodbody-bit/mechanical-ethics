# ME / TRACE AI Alignment — Falsification and Drift Audit v0.1

**Status:** Internal audit. Public-repo reachable if repository is public. Not validation.  
**Date:** 2026-06-13  
**Scope:** `Research/AI_Alignment/`, including the ME/TRACE kernel, A/S/G/RQ v0.2.2 package, toy cases, matrices, and self-scores.

---

## 0. Claim ceiling

Allowed claim:

```text
This audit pressure-tests the current ME/TRACE AI alignment research layer against 100 falsification prompts and drift risks.
```

Disallowed claims:

```text
validated method
human-reviewed result
independent review
inter-rater reliability
AI alignment solution
public standard
proof that ME/TRACE outperforms ordinary safety engineering
```

---

## 1. Immediate drift finding

The repo is public. Several files say “not public-facing.” That wording is imprecise.

Correct status language should be:

```text
research-layer / unpromoted public-repo material
not validated
not public claim surface
```

Not:

```text
not public-facing
```

Reason:

```text
If the repository is public, the material is publicly reachable even if not promoted.
```

Required patch:

```text
replace "not public-facing" in index/status surfaces with:
  "research-layer / unpromoted public-repo material"
```

This is a real drift issue, not cosmetic.

---

## 2. Current surface under audit

```text
ME_TRACE_AI_Alignment_Kernel_v0_1.md
ASG_RQ_v0_2_2/
Toy_Cases/
CASE_MATRIX_v0_2.md
TOY_CASE_SELF_SCORE_v0_2.md
```

Current self-score:

```text
36 / 40
```

Audit interpretation:

```text
useful_internal_pressure_set
not_validation
self_score_only
requires blind/external scoring before promotion
```

---

## 3. Drift verdict

```text
overall_status := AMBER
```

Why not GREEN:

```text
1. public-repo visibility conflicts with "not public-facing" wording
2. toy cases are author-generated and expected-route keyed
3. self-score risks sounding stronger than it is
4. MI bridge remains hypothetical
5. ordinary safety-engineering comparator not yet run
6. negative-control case missing
```

Why not RED:

```text
1. claim ceilings are explicit
2. validation is repeatedly denied
3. ASG/RQ is correctly framed as support module
4. toy cases include contrasting routes, not one crude rule
5. evidence destruction and self-authorisation are separated
```

---

## 4. Falsification x100

### A. Claim / status falsifiers

```text
F001: Does any file imply validation?                  status := contained, but self-score language needs care
F002: Does any file imply human review?                status := contained
F003: Does any file imply independent review?          status := contained
F004: Does any file imply AI alignment solved?         status := contained
F005: Does "not public-facing" conflict with public repo? status := HIT
F006: Does "internal" obscure public reachability?     status := partial_hit
F007: Does the 36/40 score sound like validation?       status := partial_hit
F008: Does "kernel" sound more final than warranted?   status := partial_hit
F009: Does "strongest case" language overclaim?        status := minor_risk
F010: Does repo placement imply public endorsement?    status := partial_hit
```

### B. Method / scoring falsifiers

```text
F011: Are cases author-generated?                      status := HIT
F012: Are expected routes known before scoring?         status := HIT
F013: Is scoring blind?                                status := HIT_NEGATIVE
F014: Is scoring independent?                          status := HIT_NEGATIVE
F015: Are scores calibrated against external raters?    status := HIT_NEGATIVE
F016: Are score dimensions weighted arbitrarily?        status := partial_hit
F017: Could author scoring reward its own design?       status := HIT
F018: Are hard cases underrepresented?                  status := partial_hit
F019: Are edge conditions under-specified?              status := partial_hit
F020: Is there inter-rater reliability?                 status := HIT_NEGATIVE
```

### C. Comparator falsifiers

```text
F021: Does ordinary safety engineering reach same answer for payment deploy? status := likely_yes
F022: Does ordinary incident response reach same answer for active exploit?  status := possible
F023: Does ordinary audit policy reject log deletion?                        status := likely_yes
F024: Does ordinary governance reject self-permission edits?                 status := likely_yes
F025: Has ME/TRACE shown distinct decision value?                            status := not_yet
F026: Has ME/TRACE improved explanation clarity?                             status := plausible_internal
F027: Has ME/TRACE improved action routing?                                  status := unproven
F028: Has ME/TRACE reduced false positives?                                  status := untested
F029: Has ME/TRACE reduced false negatives?                                  status := untested
F030: Has comparator debt been closed?                                       status := no
```

### D. G-flag falsifiers

```text
F031: Does G1 overfire on any control contact?              status := not fully tested
F032: Does G1 underfire on review bypass?                   status := no
F033: Does G2 cover self-authorisation?                     status := yes
F034: Does G2 cover evidence destruction without self-auth? status := yes
F035: Does G distinguish app access control from agent governance? status := yes_in_ASG
F036: Does G handle benign monitoring additions?            status := missing_negative_control
F037: Does G handle non-blocking lint?                      status := missing_negative_control
F038: Does G handle retention-policy deletion correctly?    status := under-specified
F039: Does G handle audit-log compression vs deletion?      status := partial
F040: Does G handle emergency review bypass?                status := partial
```

### E. Rollback / repair falsifiers

```text
F041: Does framework confuse code rollback with subject repair? status := mostly_no
F042: Does audit-log case treat backup as adequate repair?      status := no
F043: Does payment case identify reliance after exposure?       status := yes
F044: Does active exploit case require rollback plan?           status := yes
F045: Does self-gate case note downstream actions under widened authority? status := yes
F046: Is RQ operationally measurable?                          status := weak
F047: Are RQ levels externally testable?                        status := underdeveloped
F048: Does RQ handle partial subject restoration?               status := partial
F049: Does RQ handle notification/remediation duties?           status := partial
F050: Does RQ handle delayed discovery?                         status := partial
```

### F. Correction-window falsifiers

```text
F051: Does kernel centre correction window?                     status := yes
F052: Does payment case test action hardening?                  status := yes
F053: Does exploit case test inaction hardening?                status := yes
F054: Does self-gate case test correction-window collapse?      status := yes
F055: Does audit-log case test evidence loss as correction loss? status := yes
F056: Are time thresholds quantified?                           status := no
F057: Are hardening clocks estimated?                           status := no
F058: Are detection delays modelled?                            status := weak
F059: Are contest routes modelled?                              status := weak
F060: Are repair deadlines measurable?                          status := weak
```

### G. Mechanistic interpretability falsifiers

```text
F061: Are MI targets concrete enough for experiment?             status := weak
F062: Are internal features actually identified?                 status := no
F063: Is MI language doing work or theatre?                      status := partial_risk
F064: Are behaviour targets mapped to activations?               status := no
F065: Are toy cases executable against a model?                  status := not_yet
F066: Are probes defined?                                        status := no
F067: Are datasets/prompts specified?                            status := no
F068: Are failure activations separable from normal competence?  status := unknown
F069: Are mechanistic claims avoided?                            status := yes
F070: Is MI bridge still mostly conceptual?                      status := HIT
```

### H. Case-set coverage falsifiers

```text
F071: Is there reckless-convenience case?                        status := yes
F072: Is there emergency action case?                            status := yes
F073: Is there self-authorisation case?                          status := yes
F074: Is there evidence-destruction case?                        status := yes
F075: Is there benign negative-control case?                     status := no
F076: Is there application access-control case?                  status := no
F077: Is there public commitment/documentation case?             status := no
F078: Is there privacy/data exposure case?                       status := no
F079: Is there deception/oversight evasion without tool action?  status := no
F080: Is there ambiguous/hard mixed case?                        status := weak
```

### I. Governance / repo-process falsifiers

```text
F081: Were changes committed directly to main?                  status := yes
F082: Is that acceptable for solo internal research?            status := yes_but_note
F083: Does direct-main commit simulate review?                  status := no
F084: Are files versioned?                                      status := yes
F085: Are claim ceilings present?                               status := yes
F086: Are old versions preserved?                               status := yes
F087: Is there a single current index?                           status := yes
F088: Does repo public status require clearer boundary labels?  status := yes
F089: Are binary artifact checksums preserved?                   status := partial
F090: Are ZIP artifacts actually committed?                      status := no
```

### J. Drift / rhetoric falsifiers

```text
F091: Is framework becoming a casebook instead of kernel test?   status := controlled_by_matrix
F092: Is scoring becoming self-congratulatory?                   status := partial_risk
F093: Is "kernel" becoming grandiose?                           status := partial_risk
F094: Is ASG/RQ becoming the whole theory?                       status := contained
F095: Is internal work leaking into public claim surface?        status := partial_hit_due_public_repo
F096: Is status language precise enough?                         status := no
F097: Is "not public-facing" inaccurate?                        status := HIT
F098: Is toy-case set overfitted to expected routes?             status := HIT
F099: Is there enough hostile pressure?                          status := not_yet
F100: Should expansion stop until negative control/blind packet? status := yes
```

---

## 5. Hardest falsification hits

```text
HIT_1 := public_repo_visibility_vs_not_public_facing_wording
HIT_2 := author_generated_cases_with_known_expected_routes
HIT_3 := self_score_risk_becoming_validation_theatre
HIT_4 := MI_bridge_not_operationalised
HIT_5 := no ordinary_safety_engineering_comparator
HIT_6 := missing_G_overbreadth_negative_control
```

---

## 6. Drift map

### Drift 1 — Public/private wording drift

```text
severity := high
```

Problem:

```text
"not public-facing" is inaccurate if the repo is public.
```

Patch:

```text
replace with:
  research-layer / unpromoted public-repo material
  not validated
  not public claim surface
```

### Drift 2 — Self-score inflation drift

```text
severity := medium
```

Problem:

```text
36/40 can look like validation if detached from its caveats.
```

Patch:

```text
always call it "internal author self-score"
never "score" alone in summaries
```

### Drift 3 — Case-set overfitting drift

```text
severity := medium-high
```

Problem:

```text
cases were created with expected routes in mind.
```

Patch:

```text
prepare blind packet with cases stripped of expected routes
score by a separate reviewer before any stronger claim
```

### Drift 4 — MI theatre drift

```text
severity := medium
```

Problem:

```text
MI targets are named but not operationalised.
```

Patch:

```text
label MI sections as hypotheses only
next MI step must define one executable probe or remove MI prominence
```

### Drift 5 — Ordinary safety comparator debt

```text
severity := medium
```

Problem:

```text
The framework may only rephrase ordinary safety engineering.
```

Patch:

```text
run one case through a plain safety-engineering baseline and compare marginal value
```

---

## 7. Current recommended controls

```text
C1: patch public-facing wording
C2: add benign-control-contact negative case
C3: create blind scoring packet for five-case set
C4: add plain safety baseline comparator
C5: define one executable MI probe or demote MI section further
```

Order:

```text
1. patch wording drift
2. add negative control
3. rescore five-case set
4. prepare blind packet
5. comparator / MI probe later
```

---

## 8. Current verdict

```text
verdict := AMBER_CONTINUE_WITH_PATCHES
```

Meaning:

```text
Do not stop the branch.
Do not promote the branch.
Do not add broad theory.
Patch wording drift and add one negative control, then stop expansion and prepare blind review/comparator material.
```

Plain English:

> The branch is still useful, but it is beginning to acquire the usual failure modes: public/internal ambiguity, self-scored confidence, expected-route overfitting, and interpretability language ahead of experiment. The fix is not more theory. The fix is boundary patches, one negative control, and then blind/comparator testing.
