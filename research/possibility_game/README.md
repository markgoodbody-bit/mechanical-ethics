# Possibility Game — offline research candidate

A small executable explorer of **authored situations**, not a forecast or ethics
solver. It compares observation-consistent choices, prints what happened to each
entity, and lets a reader preserve an exact history before trying a different
choice. Standard-library Python; no server, model account, network or credentials.

## Try it

From the repository root, using Python 3.10 or later:

```powershell
python -m research.possibility_game.game raft
python -m research.possibility_game.game workshop
python -m research.possibility_game.game betsy --horizon 1
python -m research.possibility_game.game betsy --horizon 2
python -m research.possibility_game.game construction --goal self
python -m research.possibility_game.game inheritance --json
```

Three rankings are shown; each ranks complete policies over **all** stipulated
initial worlds rather than selecting a secret actual world:

- `cheap`: least worst-case effort, then money, imposed cost, elapsed time.
  It does not require the declared goal to be achieved.
- `goal`: meets the authored outcome binding in every represented initial world;
  ties use the inherited time/effort/money/imposed ordering.
- `options`: highest minimum terminal capability-label count plus authorised
  outgoing-action count, then cheap ordering. This crude count deliberately fails
  as a measure of goodness; terminal capabilities are **not** demonstrated future
  usable routes. Ties and ordering are authored, not discovered values.

The actor knows the stipulated alternative model but observes only its declared
observation/action/cost history. Full hidden-state IDs, entity burdens and outcomes
in `audit_worlds` are for the reader/auditor; they are not policy decision keys.
Manual branches select an origin and are **auditor experiments**, not evidence of
an actor's usable policy. No probabilities are claimed without a prior.

## Keep one history, branch another

Use a new filename. Saving refuses to overwrite existing files:

```powershell
python -m research.possibility_game.game raft --actions learn land --save raft-history.json
python -m research.possibility_game.game raft --replay raft-history.json
python -m research.possibility_game.game raft --replay raft-history.json --branch-at 1 --actions tow
python -m research.possibility_game.game raft --replay raft-history.json --branch-at 0 --actions wait land --goal self
```

The paired report retains the original journal and the exact prefix preceding
the branch. The paired report and caller's journal have independent nested
snapshots: editing either does not silently edit the other. Before/after snapshots include capabilities, burdens, clock, inherited
claims and correction-window annotations. Model and receipt hashes detect drift
or accidental tampering; **they do not authenticate an author or prove a world**.
Even a rehashed fabricated outcome is rejected by reconstructing the journal.
Changing origin or horizon requires a new experiment, not silent replay mutation.

## Five cases and their falsifiers

| Case | What a reader can compare | What fails |
| --- | --- | --- |
| Raft | Wait/land versus learn/tow, with explicit stipulated towing consent | The cheap self-landing leaves B behind. A larger capability count can do the same. Null advances the river and closes the annotated reach window. |
| Saturday Workshop | Idle versus learn/repair | Learning really adds a represented available action and reaches a repaired tool; skill count alone also rewards learning then doing nothing. |
| Betsy | Same gesture in two unknown preference histories; ask then adapt | A route exists in each world without asking, but no single observation-usable policy meets the preference goal. No trauma, hidden intention or factual psychology is inferred. |
| Cooperative construction | Shortcut versus joint construction, with neighbour and B preserved | Self access transfers burden. Shared access has a temporary side cost; final recovery does not erase cumulative imposed cost. Contested commandeering remains excluded. |
| Inheritance | Confident old note versus current bounded sign | Following inheritance alone can lose the route. A frozen policy stops on an unseen observation but can still fail when an unseen world consequence changes under the same visible sign. |

`correction_until` is an **annotation**, not a generic hardening detector or
enforcement rule. Scenario transitions explicitly determine loss of reach. A
shorter horizon can remove a robust guarantee while each world's individual
route still exists; that does not establish irreversible world loss.

## Inputs and extension contract

`scenarios.py` supplies interchangeable factories returning a `Game`:

- starting entities and stable roster, capabilities and per-entity burden;
- named initial worlds, bounded actor observations and untrusted inheritance;
- exogenous integer model clock and action/null transitions, each with separate
  exogenous and chosen-change descriptions;
- time/effort/money/imposed cost vector, horizon and resource budget;
- explicit `ALLOWED`, `WITHHELD`, `CONTESTED` authority ports;
- multiple authored goals, disputed interpretation, assumptions and provenance;
- labelled terminal outcomes which can fail the declared goal.

The full model is an input. `ALLOWED` is a stipulation, **not** consent inferred
from capability, a note, a solver result or lack of refusal. Contested permissions
are conservatively unavailable. Entity burdens and cumulative imposed costs are
distinct authored measures; neither is welfare or a common ethical currency.
No equation derives standing, goodness, trust or authority from the dynamics.

Only local source hashes, Python version and OS are actually observed by
`baseline()`. All case transitions remain `STIPULATED_SIMULATION`, regardless of
the runtime baseline. No empirical claim about computing hardware, future AI,
Star Trek or Culture is fabricated. Those distant projections are not included.

Factories are trusted small source definitions, not an untrusted upload format.
Limits are 40 states, four initial worlds and inherited horizon 0–8. Enumeration
is exponential; these limits alone are **not** a universal memory/time bound.
Do not expose this as a hosted general-purpose input service. This candidate has
five deliberately tiny graphs, deterministic ordering and no random draw/seed.
To add a case, author its causal assumptions, then supply countermodels and tests;
do not relabel a favourable transition as evidence.

## Reuse and stronger owners

Before: PR55 provided a finite observation-policy enumerator and frozen replay;
no five-case human exploration CLI, persisted exact branch journals or runtime
source/evidence separation existed there. After: this new directory wraps the
unchanged enumerator, adds those capabilities and tests its limits. Existing
research and released book sources are untouched.

- Reused source: [ME PR55](https://github.com/markgoodbody-bit/mechanical-ethics/pull/55),
  base `e0e52600fa80e10826cd99fb5dd2e76bd22d2e7c`.
- Inspected parallel foundation: [ME PR57](https://github.com/markgoodbody-bit/mechanical-ethics/pull/57),
  `42eb1fb1ef8ecc31ef81dea980154a77419b9f19`, finite knowledge-state models.
  This wrapper does not replace or rewrite that owner's code.
- [TRACE spine](https://github.com/markgoodbody-bit/TRACE/blob/6c68fae8cbc51d0ef1e77a18e220ceb7a1207025/TRACE-SPINE.md):
  bounded aperture, clock/currentness, authority/capability and represented future
  versus actual-world distinctions; not a simulation validator.
- [Kaelbling, Littman and Cassandra, 1998](https://www.cassandra.org/arc/papers/aij98.pdf):
  established partial-observation planning owner. This code uses simpler finite
  deterministic enumeration and adds no POMDP algorithm or mathematical novelty.
- Existing Relay cold-URL contract inspected at `b78dd2791c949ed2693c8fc3e4e4f32e4801f1e0`;
  no Relay invocation or paid-provider result is claimed. YAC PR119 was inspected
  separately and is not used or changed by this package.
- [COM assignment](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6135200933)
  and [CC raft contribution](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6135009487)
  are coordination/context, not independent real-world validation.

## Run the checks

```powershell
python -m unittest research.possibility_game.test_game -v
python -m research.possibility_game.mutation_check
python -m unittest discover -s research/navigator_toy -p 'test_*.py' -v
git diff --check
```

Local receipt, 13 October 2026, Windows / Python 3.10.11: **38/38 new tests**,
**39/39 inherited tests**, **7/7 deliberately faulty variants caught by assertion
failures**, and staged `git diff --check` clean. Mutation runs also produce some
errors; the receipt counts assertion detection, not exceptions alone. These are
local fixture results, not hosted CI or practical outcome evidence.

Follow-up falsification found the original branch report aliased the caller's
mutable journal. This was repaired by copying the verified snapshot; regression
tests challenge edits in both directions. An explicitly empty goal is now rejected
instead of silently defaulted during branching. No scenario conclusions changed.

Earned result: executable deterministic comparisons and exact branch replay on
these authored models. Provisional interpretation: useful for exposing conflicting
goals, missing observation and side cost. Process improvement: original histories
survive challenge and goal revision. Unresolved: practical benefit to ordinary
subjects, truth of any real causal model, grounded value/standing/floors, scalability
and generalisation. Passing tests or agreement between project models settles none
of those.
