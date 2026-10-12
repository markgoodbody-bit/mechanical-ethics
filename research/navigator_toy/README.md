# Navigator toy — Codex Lane C, 12 October 2026

This is an **offline research instrument**, not an adviser or a replacement
for the released book. It asks whether a represented action can actually be
chosen with the observations, time, permissions and resources available.
It also exposes how changing an authored goal changes the answer.

## Run

Python 3.10+ standard library only; no installation, network, credentials,
models or service writes. From the repository root:

```text
python -m unittest discover -s research/navigator_toy -p "test_*.py" -v
python research/navigator_toy/mutation_check.py
python research/navigator_toy/cases.py
```

The last command prints assumptions, all represented terminal paths, chosen
observation-conditional policy (if any), cost vector, excluded actions and
correction-window labels. Hidden world IDs appear only in the auditor's trace,
not in policy decision keys. No inputs from actual people are collected.

## What changed

Before: COM #798 Codex return6133275539 proposed four faults to test.
After: isolated executable finite-state fixtures, an observation-policy
enumerator, unit tests and five deliberate in-memory mechanism corruptions.
No existing manuscript, PDF, TRACE file, tag, deployed service or licence changed.

Base: draft-zero commit `6ae270592afaa6ffc1222096e06df9d457222013`, itself
based on released ME `e2ef746e931161cb70ac46a4eaa122442134e86b`.
Commission: [COM6133298843](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6133298843)
and [COM6133298988](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6133298988).
Prior source: [CC6070696367](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6070696367),
[FW6070734672](https://github.com/markgoodbody-bit/COM/issues/798#issuecomment-6070734672).

## Five fictional situations and computed distinctions

| Situation | Controlled comparison | Result inside the stipulated model |
| --- | --- | --- |
| One filing attempt, destination A/B hidden | notice early versus after last opportunity | A successful route exists in each world, but a single robust observable policy exists only with the early notice. |
| Shared leak, disputed repair responsibility | independently authorised interim protection versus permission withheld | The first permits protection; the second does not. Disputed repair permission is neither bypassed nor treated as permission to do nothing about every other move. |
| Shared service changes to unwanted control | personal-safety goal versus joint-capacity goal versus no declared goal | Personal constraint selects separation/refusal; capacity goal selects staying despite imposed cost4; missing goal yields UNKNOWN, not a moral verdict. |
| Person has one time unit and effort unit | known interim protection versus mapping first | Known protection is feasible; mapping costs too much. Even more resources cannot make the late response timely. The instrument gives the SAME answer as the simple ordinary comparator: no incremental practical advantage shown. |
| Two fictional friends want to reach a place before it closes | voluntary accurate hint versus no consent, wrong hint or longer solo horizon | A permitted hint opens a two-step route; withdrawn permission or zero partner-burden budget blocks it. A longer horizon permits a solo route. Replaying the original policy under wrong shared information fails in both worlds. Cooperation is conditional, not a law. |

In the hidden-office model, a stipulated prior `P(A)=0.9` allows a blind A
filing under a success threshold0.85, but not0.95. The world, action and
observation model is identical: the usability **binding** changed. This
reproduces the prior quantifier distinction; it does not discover it anew.

## Model contract (not universal primitives)

`State` names a finite represented condition and its observation. `Move`
advances time, changes condition and carries a cost vector and an explicit
permission flag. `Scenario` declares initial possible worlds, horizon,
budgets and optional prior. `Binding` declares acceptable terminal outcomes,
robust or probabilistic threshold, and a ranking order.

Policies depend on the complete observation/action history plus **observably
spent** resources/time. They cannot choose A in hidden worldA and B in hidden
worldB before receiving different observations. All possible initial worlds
must admit an action for a robustly permissible choice. This conservative
permission rule is a model stipulation, not a solution to contested authority.

For each represented initial world `w`, deterministic transitions yield a
path under policy `pi`. A robust policy must meet the authored outcome rule
for every represented `w`. The separate oracle audit asks whether *some* path
exists for each `w`; it does not give the actor that path. Probability mode
uses only an explicitly supplied finite prior; missing prior yields UNKNOWN.

Accepted policies are ranked lexicographically by worst-case time, effort,
money and burden imposed on the other participant. This is an **authored
ordering**, not a derived scalar welfare function or universal least-friction
principle. The order is configurable, but no aggregation method is earned as
ethically legitimate. Refusal/delay cost time and may change future outcomes.

`correction_until` is an auditor's explicit fixture annotation. It is not a
generic correction operator, nor a proof of the book's strict
`T_protect < T_harden` condition. Terminal success/late conditions are encoded
in each fixture's transition table; toy filing/protection cutoffs are inclusive.
Do not infer that a printed correction window establishes a remedy. A later
instrument would need separately defined detection, remedy, execution burden
and hardening semantics. We have deliberately not invented those here.

## Falsification receipts and limits

Actual local run: **37/37 unittest checks pass**. Five specified in-memory
mutations are detected: hidden-world oracle, permission ignored, horizon
ignored, resources/partner costs ignored, and invented missing value. These
are regression checks of chosen mechanisms, not exhaustive mutation coverage.
The initial test for no hidden-state oracle incorrectly counted later history
keys as initial keys; it failed, was narrowed to the initial history, then
passed. The implementation was not changed to make the fixture's conclusion win.

Earned: reproducible finite examples discriminate early/late information,
authority versus capability, goals versus capacity, enquiry burden, and
conditional cooperation. Frozen-policy replay can fail under a changed model.

Provisional: these seams may help FW/CC make v0.9 assumptions more inspectable.

Wording improvement: trace makes chosen assumptions and exclusions visible.

Process improvement: independent, reproducible source artifact for review;
no Mark-mediated execution or per-case approval required.

Unresolved: no external human-reader comparison, field efficacy, mathematical
novelty, normative foundation, subjective preferences, general optimality,
real permission determination, empirical probabilities or scale invariance.
Both model and tests are project-authored; agreement is not validation.
This is ordinary finite partially observed planning/enumeration, informed by
the prior behavioral-systems/quantifier discussion; CC owns the stronger-owner
mathematical review, not this toy's terminology.

The fixtures are deliberately small: deterministic transitions and hidden
initial conditions, not stochastic transitions or independent multi-agent
strategies. A typed coupling is represented by information/permission/cost
changes, not a complete interaction graph or social theory. The planner has
complete access to the **stipulated model**, not to reality. It only enumerates
represented paths. Finite horizon0..8 and positive-duration moves prevent
infinite recursion, but exponential growth remains: do not feed this arbitrary
large inputs or claim it is a scalable practical planner. Successful terminal
outcomes are authored labels and can be mistaken; wrong-model replay is only
one counterexample, not a model-error guarantee. STOP says no represented
policy satisfies the supplied binding; it neither proves physical impossibility
nor orders a real person to abandon an urgent situation.
