# Mechanical Ethics v0.9 — Integrated Kernel Lab (research)

**Status: SOURCE-ONLY / UNRELEASED / NOT VALIDATED / NOT ETHICAL CLEARANCE.** This is Framework Build's single bounded [COM #798 Project A](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6135200933) deliverable. It is not the released Mechanical Ethics v0.8.0 reader, TRACE v0.4.0, a legal/medical/animal-behaviour model, a model of actual AI consciousness, or a new optimal-control algorithm. Mark retains editorial and release authority.

**Purpose: HOW CAN WE MAKE A BETTER FUTURE?** A useful navigation grammar needs to distinguish changing reality from our partial maps of it, the capacity to select or construct futures from permission or right to do so, and useful correction from a corrected record. It should help an affected person, engineer or AI ask a better next question **without demanding that a person in trouble operate a technical model**.

## Start with the actual owners, not a new solver

This package combines *existing* source research as an inspectable teaching/test witness:

- [Released ME v0.8.0](https://github.com/markgoodbody-bit/mechanical-ethics/blob/e2ef746e931161cb70ac46a4eaa122442134e86b/MECHANICAL_ETHICS.md): already entity-first; Leah/Mia, time/protection, witness/custody, residue, positive Part VI, Saturday Workshop, living other fires, privacy, care and hope. Retain its safety opening, complete scenes, four figures and author/provenance notes **in the original released source**.
- [Released TRACE v0.4.0 spine](https://github.com/markgoodbody-bit/TRACE/blob/6c68fae8cbc51d0ef1e77a18e220ceb7a1207025/TRACE-SPINE.md): middle-out selective causal loop, observed/reported/inferred/unknown, action/inaction, target-apertures, clocks, burden, named value ports, represented future-space and checks that must be actually capable of detecting failure.
- [ME v0.9 draft zero](https://github.com/markgoodbody-bit/mechanical-ethics/blob/6ae270592afaa6ffc1222096e06df9d457222013/research/ME_V0_9_MIDDLE_OUT_KERNEL_WORKING.md): world/time, entity, partial map, moves, target/horizon, vector friction, correction and coupling.
- [CC's independent mathematical PR57](https://github.com/markgoodbody-bit/mechanical-ethics/pull/57): imperfect-information concurrent transition systems, explicit seven authored bindings; no incremental solver advantage over established owners. **Important repairs**: zero-prior worlds stay admitted for robust queries but are skipped in probability conditioning; `K=0` is loss of robust goal guarantee, **not** irreversible hardening; correct information condition is `max(r,1-r)>10/17`.
- [Codex's observation-limited navigator PR55](https://github.com/markgoodbody-bit/mechanical-ethics/pull/55): reproducible policy enumeration/differential synthetic cases. **This lab does not replace, copy, modify, or claim to improve that solver.**
- [Build's 55/34 released-source conservation ledger PR56](https://github.com/markgoodbody-bit/mechanical-ethics/pull/56), [complete human-reader draft PR59](https://github.com/markgoodbody-bit/mechanical-ethics/pull/59), [predecessor archaeology PR60](https://github.com/markgoodbody-bit/mechanical-ethics/pull/60), [Framework integration PR58](https://github.com/markgoodbody-bit/mechanical-ethics/pull/58). The word 'integrated' here denotes *explicitly linked claims and small executable contrast cases*, **not** a merged edition or code branches.

Established external owners include partially observable Markov decision processes and stochastic games for information-limited policies; cybernetics/feedback and viability theory for regulation and state constraints; model-predictive control for horizon-dependent constrained choices; game theory and information design for coupled incentives; capability/formation theory for developing actual ability; and systems safety, legal process and institutional design for authority, remedies and evidence. The lab is a *pedagogical projection*, not a competing algorithm. See [claim/authority ledger](CLAIM_AND_FALSIFIER_LEDGER.md).

## The minimum typed separation

A represented, finite world contains a sequence of states `x_t` and exogenous changes `e_t`. Each actor `i` has an **observation aperture** `o_i(x_t)`, which is a deliberately reduced view. The world can evolve on a null move; the effect of an action depends on current world state and other actors. A state can carry changing capabilities and goals, but a finite author must *predeclare* those dimensions.

```text
WORLD_t + EXOGENOUS_t + JOINT_SELECTED_MOVES_t
           -> WORLD_(t+1)             (model transition)
WORLD_t -> VIEW_i,t                  (partial observation)
PREVIOUS_VIEW + NEW_VIEW -> REVISED_MAP_i (interpretation, not engine truth)
CAPABILITY_i,t != PERMISSION_i,t != SHOULD_i,t
REPORTED / OBSERVED / INFERRED != ACTUAL WORLD
ROUTE EXISTS != ROUTE USABLE
FIRST LOSS OF ROBUST GUARANTEE != PERMANENT HARDENING
RECORD CORRECTED != HARM REPAIRED != RESIDUE ERASED
```

The Python witness implements only bounded deterministic *replay*, not a multi-agent policy solver. A rule declares actor, named move, world-side guard, numeric effect and a **stipulated permitted flag**. A case declares actors, initial simulated values, explicitly observable fields per actor, state-dependent rules, external tick deltas, plus optional **typed coupling** labels. The chosen action list is supplied by the caller, **not inferred from a moral objective**. `tick` records pre-action views, external changes, actions, effects and resulting world. Its `after` state is the *auditor's full simulated model*, not what an actor knows; policies must be constructed using `view()`, never full `after`. A Python caller could cheat by reading the whole model: this is **not a secure information isolation boundary**.

The execution order is deliberate: **pre-action view → exogenous tick → joint moves resolved in declared actor order → after-state**. Exogenous changes can make a formerly feasible act unavailable before it fires. The actor-order sequential application is a tiny convenience; it is **not** simultaneous-game semantics or a fair conflict resolver. Each rule is author-supplied. No physical, mental, welfare, treatment or legal unit is implied by numbers such as energy=4, distress=4 or cash=3.

### What has to be authored, never 'discovered' from physics

| Port | Bound input needed | Honest limit |
|---|---|---|
| Entity/designation | Who/what is treated as an actor or affected position | Formal boundary does not prove personhood or standing |
| World model | Admitted initial states, exogenous changes, available actions, source clock | An invented scene is not evidence that this world exists |
| Observation/evidence | What each actor can actually see, source, age and alternatives | A visible report can be accurate, stale, selected or wrong |
| Targets/horizon | Who wants what and by when; ability to change those goals | A solver cannot author whose future matters |
| Authority and consent | Who may choose which move, and who can refuse | `Rule.permitted` is **stipulated by the author**, not actual legal authority |
| Uncertainty treatment | Possible worlds, robustness/probability thresholds and prior assumptions | This replay has **no** uncertainty solver; different worlds are separate runs |
| Burden/measure/cost order | Whose time, energy, exposure, dependency and imposition count | No universal scalar friction or ethical welfare aggregation |
| Witness/correction | When an observation could change a real intervention, who controls records | A changed field need not be restored health, consent, justice or practice |
| Positive formation | Changed capability, learning, relations, goal and maintenance resources | Teaching/ability does not guarantee kindness; fixed model cannot invent new state dimensions |

**No scalar moral objective exists in the code.** For competing interests, return state vectors and competing perspectives. If a future project wants a normative ranking, its author/authority and falsifier must be visible before it is called a conclusion.

## Run locally (standard-library only)

From the `research/kernel_lab` directory with Python 3.10+:

```bash
python -m unittest discover -s . -p 'test_*.py' -v
python -c "from kernel_lab import case,trace; print(trace(case('raft'), ({'traveller':'dock'},))[-1]['after'])"
```

The test module checks **17** concrete properties, including six labelled fictional cases, real null-world evolution, unavailable late action, costlier action creating a skill in the authored model, identical prior observations with different latent variants, revised approach without diagnosing that hidden variant, skill learning/goal revision and typed coupling, case record versus remedy/residue, fewer paths with an authored safer closure, explicit denied permission, stale cached reading and refresh, no visible hidden field, and fail-closed unknown actor/move/horizon/world schema.

### A reproducible negative control

The old "nothing happens when no one acts" bug would make `test_null_does_not_stop_external_time` fail (drift would not advance). Leaking the hidden `sensitivity` field into `view()` breaks `test_hidden_histories_same_prior_observation_distinct_responses` and `test_views_never_leak_unobserved_state`. Ignoring authored `permitted=False` breaks `test_authored_permission_blocks_even_physically_described_seize`. Treating repair as total restoration breaks the `residue=2` check. These are **specific detectable mutations by inspection**, not a claimed automated mutation-testing run.

## What the case witnesses actually support

[Six case cards](SIX_CASES.md) contain each initial state, action, exogenous tick and comparison; they are synthetic and hand-checkable. The main failed inferences are:

- A low-immediate-effort raft choice need not produce a later useful ability, and waiting can close a landing.
- One gesture and partial view can precede different reactions in different admitted synthetic recipient histories; **no hidden trauma was observed or diagnosed**.
- Practice can alter an individual's skill and a freely authorised teaching path can alter a shared capacity, without proving actual gratitude or universal cooperation.
- A form can be correctly updated while environmental exposure and residue continue.
- Removing one unsafe route may be legitimate under an authored policy, while taking another's resources can increase one actor's options without being morally permitted or desirable.
- A formerly true cached source can diverge from the world between sessions; a refresh can fix this toy value but does **not** verify an actual website, signatures or event history.

The source tests verify **only code behaviour under declared examples**. They do not establish human-reader usefulness, moral validity, real-world efficacy, independent observer agreement, AI first-person experiences, the physical dynamics of water or an exhaustive policy search.

## Terminal distinctions

The strongest evidence gained is a clearer **difference between modelled result, observed situation, authored port and permission to act**. Most structural claims already belong to established theory or the released material. If another discipline can do the consequential computation better, use it. The lab is useful only if it clarifies a real choice with less burden than those alternatives.

**Do not promote** this lab to released ME, TRACE, public service, YAC production, legal/medical decision tool, model self-governance, new universal ethics theorem or full-reader replacement. No models were called by the code, no credentials/third parties were contacted, and no provider costs were incurred.

**The direction is creation as well as preservation:** noticing a practical opportunity, retaining honest current maps, learning or constructing a new capability, respecting other entities and leaving correction routes open. That remains an offered ethical orientation, not something a transition function proves.
