# Six working cases — executable traces versus interpretations

**Kernel Lab research / 13 October 2026.** Six **synthetic stipulations**, with exact state vectors and one-step or two-step traces emitted by `kernel_lab.py`. Their purpose is to falsify tempting *interpretations*; not to certify actual animal psychology, clinical/environmental measurements, legality, morality or model efficiency. Execute [tests](test_kernel_lab.py) and compare results. All numeric units here are arbitrary.

The test harness is deterministic. No statistical inference, hidden conscious-agent simulation, policy optimiser or real service connection exists. The complete `after` state is an auditor's model state, **not** any actor's observation. The `views` field carries the declared limited aperture. Every artificial world, move, shock and value is authored.

## Case 1 — Ordinary navigation: raft and changing current

**Source pressure:** Mark's raft/corridor intuition [COM #798 6134834906](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6134834906); Build's human case [PR59](https://github.com/markgoodbody-bit/mechanical-ethics/pull/59); released [ME timing condition](https://github.com/markgoodbody-bit/mechanical-ethics/blob/e2ef746e931161cb70ac46a4eaa122442134e86b/MECHANICAL_ETHICS.md#L143-L169).

**Authored start**: `distance=0, energy=4, repair_skill=0, landing=1`. Actor `traveller` observes distance/energy/landing, not future current. Tick0 external effect: distance increases by 1. Tick1: distance increases by 1 and landing becomes unavailable. This is invented conditional timing, not hydrodynamics.

| Policy path | Final measured state in this model | What it distinguishes |
|---|---|---|
| `dock` at tick0 | distance1, energy2, skill1, landing1 | A **higher immediate effort** (−2 energy) creates an authored repair capability |
| `smooth` at tick0 | distance1, energy4, skill0, landing1 | Preserves immediate energy but acquires no skill |
| `null, null` | distance2, energy4, skill0, landing0 | World/time changed and a practical landing closed with no paddling |
| `null, dock` | REJECTED at tick1 (no matching landing-open rule) | Formerly possible activity may no longer be executable |

**Falsifier:** If there is no dangerous bend, dock access is hazardous, or the cost of arriving without skill is negligible, choosing smooth may be best. Do not promote `less immediate friction = always bad` either. **What is learned:** declared horizon and absent alternatives can reverse local rankings; this is already control/viability territory.

## Case 2 — Betsy: two admitted but indistinguishable hidden histories

**Ground:** human-originated reported animal encounter [COM #798 6134736454](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6134736454), and Build's bounded note [PR59](https://github.com/markgoodbody-bit/mechanical-ethics/pull/59). The *real dog's history is unknown*. The values `sensitivity=0/1`, `distress=1/4` below are **invented model variables**, not a proposed diagnosis or measurement of Betsy.

Two copies of the toy world have identical initial visible fields: `distress=0, careful=0`. They differ only in hidden `sensitivity=0` versus `sensitivity=1`. One person applies the same `block` move at tick0, then observes the resulting `distress` value and chooses `adjust` at tick1. The external tick is empty for both; the two worlds represent distinct initial-state possibilities.

| Toy world | Prior visible view | After `block` | After `adjust` | Unearned claim |
|---|---|---|---|---|
| `sensitivity=0` | distress0, careful0 | distress1 | careful1 | That distress1 proves known prior history |
| `sensitivity=1` | distress0, careful0 | distress4 | careful1 | That distress4 proves trauma, specific motive or optimal reassurance |

A receiver may **update its response** after observing the difference without pretending to discover the source of that difference. `adjust` is a declared symbolic model action; it does **not** undo distress or prove the animal feels reassured. The tests deliberately assert that sensitivity does *not* occur in the person-visible observations.

**Falsifier:** Apparent recipient difference might instead be position, fatigue, surroundings or the actor's own motion. Real uncertainty includes many omitted histories and behaviours. There is no empirical identification here, and one dog must not be made representative of all.

## Case 3 — Formation and co-creation: the Saturday Workshop

**Source:** [Released ME v0.8 Saturday Workshop, composite](https://github.com/markgoodbody-bit/mechanical-ethics/blob/e2ef746e931161cb70ac46a4eaa122442134e86b/MECHANICAL_ETHICS.md#L674-L741). No empirical workshop or participant is created by this model.

**Authored initial world**: `cash=3, skill=0, shared_skill=0, permission=1, goal=0` where goal0/goal1 are **labels chosen by the modeller** ('repair for oneself' / 'also teach another'). The two represented actors are `learner` and `mentor`. The learner sees cash/skill/goal; the mentor sees skill/permission. A typed coupling `mentor -> learner : information/skill` is declared, not an affection or legitimacy fact. No exogenous shock is introduced.

| Steps | After-state | Interpretation boundary |
|---|---|---|
| learner `practice`, mentor `null` | cash2, skill1, shared_skill0, goal0 | Learning costs a resource and changes a future ability, **not** automatically a relationship |
| then learner `reaim`, mentor `teach` | cash2, skill1, shared_skill1, goal1 | Both a **goal revision** and a distinct co-created skill path are modelled |
| learner `reaim` initially | REJECTED, requires skill1 | A later route is not necessarily usable at the start |

`mentor.teach` requires modelled permission1 and learner skill1. This is a *source-stipulated* condition, not proof of valid real consent. The financial, privacy and opportunity costs of refusing the £60k sponsor from the actual composite are **not** encoded by this minimal toy; read the original full story before making any welfare claim.

**Falsifier:** The same training can be unsafe, coercive or poorly timed; a learner may not adopt the proposed goal; extra skills can be used harmfully. Capability increase alone does not entail moral improvement.

## Case 4 — Harmful institutional delay: report versus repair

**Source:** released [Leah/Mia opening and Two Flats, one wall](https://github.com/markgoodbody-bit/mechanical-ethics/blob/e2ef746e931161cb70ac46a4eaa122442134e86b/MECHANICAL_ETHICS.md#L430-L467), both **composite**, and witness/custody/residue sections.

**Authored world:** `exposure=0, file=0, repair=0, residue=0`. Each of two external ticks adds `exposure+1, residue+1`. This is a tiny invented hazard exposure model, **not** a health model. Tenant observes exposure/file; owner observes file/repair. Actor `tenant` can `report`, changing `file+1`; actor `owner` can `repair`, changing `repair+1, exposure−1`; typed coupling `owner -> tenant : authority/protection`.

| Actions and timing | Outcome (declared model) | Significance |
|---|---|---|
| t0 tenant reports / owner null | file1, exposure1, repair0, residue1 | Accurate case progress and worldly exposure are separate |
| t1 tenant null / owner repairs | file1, exposure1, repair1, residue2 | Later real change does not erase accumulated residue |
| t0 tenant null / owner repairs (one tick ONLY) | file0, exposure0, repair1, residue1 | A direct act changes the current state; **not a same-horizon comparison** with the two-tick delayed case |

The one-tick immediate-repair row and two-tick delayed-repair row have **different horizons**; do not infer a timing advantage by comparing their totals. In fact, in this intentionally simple generator the exogenous hazard continues regardless of the repair flag. The lab therefore does **not** establish that early repair prevents future exposure; such a claim would need a state-dependent hazard process and evidence of effectiveness. The model does **not** show the repair preventing every later external hazard. It can lower simulated current exposure by one; the exogenous generator is stipulated independently, so do not infer a universal medical protective rate or full remediation. The test guards against `record updated = exposure resolved`.

**Falsifier:** Repair can be unauthorised, dangerous or ineffective; prompt checks may save lives; record-keeping can itself make later repair possible. None of that is resolved by file/exposure counters. Actual remedies require responsible professionals, domain law and current evidence.

## Case 5 — Contested closure and multiple parties

**Source:** released [ME Part V, legitimate peace/closure](https://github.com/markgoodbody-bit/mechanical-ethics/blob/e2ef746e931161cb70ac46a4eaa122442134e86b/MECHANICAL_ETHICS.md#L588-L667), positive workshop trade-offs, and [TRACE v0.4 §11–12](https://github.com/markgoodbody-bit/TRACE/blob/6c68fae8cbc51d0ef1e77a18e220ceb7a1207025/TRACE-SPINE.md#L226-L276).

**Authored world**: `open_routes=3, operator_gain=0, neighbor_loss=0, barrier=0`; two actors `operator`, `neighbor` have different visible fields. Typed coupling: `operator -> neighbor : burden/imposition`. Exogenous shock empty; this is a single contested human-designed choice.

| Operator move (neighbor null) | After-state change | Interpretation boundary |
|---|---|---|
| `close_unsafe` | open_routes3→2, barrier0→1 | Fewer paths can be a defensible safety design if the affected parties and evidence warrant it |
| `extract` | operator_gain0→3, neighbor_loss0→4 | One actor gains resources while a distinct actor bears cost; aggregate self-benefit does not validate distribution |
| `seize` | `PermissionError` | The supplied model explicitly denies this move; **the code did not discover law or moral status** |

**Falsifier:** A closure may be exclusionary or disproportionate; the barrier could wrongly block a disabled user; a neighbour's costs could outweigh a claimed benefit. The `permitted` flag is an authored example and not an ethical oracle.

## Case 6 — Longitudinal source/model drift during absent runtime

**Source:** [TRACE v0.4 §5–6 currentness and evidence](https://github.com/markgoodbody-bit/TRACE/blob/6c68fae8cbc51d0ef1e77a18e220ceb7a1207025/TRACE-SPINE.md#L83-L158) and the reported YAC staleness/canonical-time cases, with careful distinction between public record and private project memory.

**Authored initial state:** `source_value=1, cached_value=1, check_count=0`. At the one external tick, `source_value−1` occurs, regardless of whether the reader runs. The reader can initially see cached_value and check_count **only**, not the actual changing source. In this toy a 'refresh' move is stipulated to access the fresh value and update the cache.

| Reader move | After-state | Warrant |
|---|---|---|
| `null` | source0, cached1, checks0 | Last accurate report is now stale; it need not be a deliberate lie |
| `refresh` | source0, cached0, checks1 | One newly obtained toy reading aligns current fields under the declared reliable-refresh mechanism |

**Falsifier:** Real fresh GETs can fail or be filtered, source clocks can be unavailable, records can be incomplete, and received text may claim 'I am the operator' without granting authority. No website was queried, no network clock was measured and no actual AI model's belief was updated. An episodic runtime need not experience waiting for its environment to change.

## Cross-case conclusion

These six examples are a **corpus of counterfactual state contrasts**, not a representative sample or a survey of ordinary lives. Their strongest shared failure boundary is the collapse of one of the following pairs:

```text
INTENT / RECIPIENT RESPONSE
WORLD / VIEW
KNOWN EXISTING ROUTE / OBSERVATION-USABLE POLICY
IMMEDIATE ENERGY / LONG-HORIZON CAPABILITY
FILE / WORLD
CORRECTION / RESIDUE
NUMBER OF POSSIBILITIES / WORTH
CAPABILITY / AUTHORITY / STANDING
TRUE AT SOURCE TIME / CURRENT AND RELEVANT NOW
IMAGINED FUTURE / EMPIRICALLY EARNED FORECAST
```

**No result here supports 'minimal friction always wins', 'maximal option count is ethics', 'kindness always pays', 'two honest actors agree', 'modelled permission is legitimate authority', or 'short synthetic traces predict the future'.** A different authored goal, admitted world, observation function or cost order can change every case verdict. This is the practical reason to keep mechanical and human/normative ports separately inspectable.
