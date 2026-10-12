# Mechanical Ethics — v0.9 middle-out kernel (working draft)

**Status:** SOURCE-ONLY / PROVISIONAL / NOT RELEASED / NOT VALIDATED / NOT REPLACEMENT FOR ME v0.8.0 or TRACE v0.4.0. First prepared by Framework with Mark at the Campfire on 12 October 2026. Branch based on released ME main `e2ef746e931161cb70ac46a4eaa122442134e86b`, with no edits to released reader or PDFs. **This text is an orientation and falsification candidate, not a release decision.**

**Purpose:** HOW CAN WE MAKE A BETTER FUTURE? Mechanical Ethics is a voluntary, critical navigation proposal, not a universal imposed optimisation objective, a morality engine, or a replacement for science, mathematics, law or existing ethical scholarship.

## The centre: middle-out navigation

Begin with a bounded entity in a changing world. Not a moral verdict, omniscient observer, complete value system, or privileged human/institutional view. Ask what the entity can perceive, remember, represent, choose, affect, and correct. Expand *outwards* to adjacent entities and their couplings, constraints, and consequences, and *inwards* to the component processes whose different boundaries matter. Repeat at new scales without presuming self-similarity as a proven physical law.

**Working proposition:** A useful general navigation method should help a bounded entity use the information actually available to it, coordinate with affected others when warranted, avoid damaging routes unnecessarily, notice new evidence and correct course. This is an engineering and philosophical research programme, **not** a proved claim that one policy is universally optimal or that every entity values the same future.

The original orientation, stated without mysticism:

`GROUND / ACTUAL WORLD -> BOUNDED APERTURE -> PARTIAL MAP -> ENTITY AND OTHER ENTITIES -> POSSIBLE PATHS -> ACTION / WAIT / REFUSAL -> WORLD CHANGE -> WITNESS -> CORRECTION -> REPEAT`

**The navigator does not simply point at a destination and close its eyes.** A desired direction, dynamic obstacles, partial perception, error correction, and changing relations all affect a viable path. A 'least friction' path is meaningful only once *whose* friction, *which* costs, *what horizon*, *which constraints* and *which uncertainty* have been declared.

## Minimal primitives, with proof obligations

**World and time.** Let `W_t` denote actual world state at time `t`. Its full contents need not be accessible to any participant. Let the transition relation or stochastic kernel be `T(W_{t+1} | W_t, a_t, e_t)` where `e_t` includes other influences. Unknown `T` is permitted; assuming it known would erase the problem. The world does not wait for a chooser. Discrete-index notation does not claim mathematical continuity of physics.

**Entity.** An entity `i` is provisionally a distinguishable process or bounded unit with some consequential interaction with the world. This is a *model-boundary choice*, not proof of consciousness, welfare, rights, autonomy or moral standing. Boundaries and nested entities may overlap. What matters at one scale can change when zoomed in or out.

**Aperture / evidence.** An entity obtains partial observation `o_i(t) = O_i(W_t, c_i(t))`, where `c_i` includes its current relation, access and circumstances. A map or belief representation `m_i(t)` is a fallible function of observations and history. `m_i(t) != W_t`. If data are missing, preserve UNKNOWN; do not silently infer ABSENT.

**Capacity and authority.** `A_i(t)` is a modeled set of technically feasible moves; `L_i(t)` is the subset legitimately authorised in the actual context. Being able to move is not permission to move. Some moves are delay, refusal, observation and nonintervention. Actual authority can be contested and is not conferred by formal notation.

**Targets and time horizon.** A navigator may represent goals, acceptable conditions, or a *partial order* of future prospects over horizon `H`. No universal scalar welfare function is assumed. A value function, if one is used, is an explicitly declared choice, not a theorem deduced from being an entity. Choice of whose future, which horizon, which baseline and which unknown worlds count must remain contestable.

**Paths and future-space.** Given current knowledge and constraints, define `P_i(t,H)` as *represented reachable paths*, not the set of all physically possible futures. The map can omit beneficial paths, exaggerate hazards and be revised. Define `V_i(t,H)` as a declared subset of represented paths meeting survival, dignity, legitimacy, chosen aims, or other stated constraints. Different evaluators may disagree. `|V_i|` is not a universal measure of goodness: large numbers of mutually inaccessible or harmful pathways can be undesirable, and cardinality is representation-sensitive.

**Friction / navigation cost.** For candidate path `p`, write a vector, not one magic number: `C_i(p) = (effort, exposure, irreversible harm, dependency, delay, opportunity loss, imposition on others, ... )`, with uncertainty intervals and an explicit scope. Some dimensions are incommensurable; Pareto comparison or context-specific thresholds may be more defensible than additive weights. "Least friction" is a navigation heuristic, not a law of least resistance or a promise of optimisation.

**Correction.** Let `K(p,t)` mean the availability, timing and practical reach of mechanisms to detect and repair an error after following `p`. A formal right to appeal is not equivalent to correction while affected futures remain open. The ability to change course is itself a possible navigation asset, subject to competing costs and commitments.

**Coupling.** Let `G_t` be a directed, typed interaction graph among modeled entities/processes. An edge `i -> j` records a specified relationship (information, influence, dependence, exchange, harm, resource, authority, care, etc.), **not automatically affection or ethical legitimacy**. Its effect may be positive, negative, mixed or unknown, and can change over time. Macro relationships (families, firms, governments) may be built from interacting couplings; that is a useful analytical decomposition, not proof that pairwise edges explain every emergent collective effect.

## The core update loop

At each consequential step:

1. Identify bounded observer/actor and actual scope. What can each participant know? What remains unknown?
2. State a desired direction or acceptable region, an explicit time horizon and constraints; allow disagreement and no imposed goal.
3. Enumerate plausible moves, including waiting, refusal, cooperation, separation and checking. Include those affected, not only the acting entity.
4. Inspect couplings: which moves change other entities' ability to act, their burden and the viability of future relationships?
5. Compare supported trajectories and uncertainties. Prefer reversible experiments when possible; never use a local gain as proof of a long-term advantage.
6. Move within legitimate authority, or stop if insufficient evidence, permission or tolerable risk.
7. Observe effects, make correction reachable, revise the map, and repeat.

This is a *navigation pattern*, not a mandatory decision procedure. No one is required to reveal private internal state, obey the text, or surrender judgement.

## One mathematical hypothesis worth testing

A coupling between entities `i` and `j` can increase their **joint achievable possibilities** where complementarity, specialisation, shared warning, error detection or risk pooling exceeds coordination burden, correlated exposure and coercion.

For one clearly declared objective `U` and horizon `H`, define an interaction surplus:

`S_ij(H; U) = U(joint policy over H) - U(best specified noncooperative baseline over H)`.

Positive `S` is *possible*, not guaranteed. It cannot be inferred from the existence of a relationship; baseline selection, perspective, distribution of gains and measurement all matter. `S > 0` from one observer's utility may coexist with substantial harm to another. This must not be called universal ethical success.

**Toy example of robustness, not a law.** If two comparable, independent units each fail within a defined horizon with probability `p`, and success requires *at least one* to survive, the coupled redundant system fails with probability `p^2`, lower than `p` when `0 < p < 1`. But if coupling exposes both to a shared cause, their failures are correlated and the improvement may vanish. Nor does physical survival alone define ethical value. This isolates what the maths can establish and what it cannot.

**Temporal hypothesis:** Some immediate exploitative gains reduce a system's future option-space by destroying partners, knowledge, trust or correction capacity. Other exploitative strategies may remain locally successful. The inquiry is to discover under what empirical conditions preserving another entity's capabilities increases *mutually acceptable long-horizon viability*. The hypothesis is about a structure of consequences; it does not equate empathy with utility or claim cruelty can never win.

## The reflective lane

An entity need not merely respond to present signals. A reflective map can represent possible later states, compare routes, notice error in its own goals or assumptions, and deliberately retain navigability. 'Reflective' here means an observable or reported capacity in a chosen model; no inference to conscious experience follows automatically. Model updates may correct information, goals, or constraints. Different entities have different capacity, access and standing; representation is not the other's consent.

## The middle, without extremes

The goal is not 'always cooperate', 'never exploit', 'maximise all future paths' or 'never take risk'. The navigator seeks a defensible route through a changing, multi-entity landscape, recognising locally useful moves can close later options, and that preserving another's capacity can make new routes reachable. Efficient *for whom, under what information, at what cost, with what authority, and over what time* must remain explicit.

## Micro-to-macro / fractal caution

Reapply the primitives to an individual person, a discussion, a clinical interaction, a firm, a supply chain or a cross-border institution. Ask which entity boundaries and couplings matter at that level. This is **recursive analysis**, not yet a proof of scale-invariance or fractal mathematics. If a future version claims Mandelbrot-like properties, it must specify the mapping, scaling rule and measurable invariants; otherwise use 'recursive' as the accurate word.

## Human-first invitation (prototype)

Imagine walking home through unfamiliar streets. You know roughly where you want to go. You can see only the next few corners. You might ask a stranger, turn back when a road is blocked, or travel alongside someone who knows a route you don't. A direction alone is not a journey. Navigation requires noticing the world, recognising other people, choosing within your limits, and correcting as circumstances change. Mechanical Ethics asks whether that humble pattern can help us reason about harder decisions—especially when one person's shortcut can close somebody else's road.

## Relationship to existing released work

This draft **reorients but does not delete** the released human reader. Existing cases of damp and mould, process distance, unfair burdens, delayed correction, strategic unknowns, privacy, predator positions, peace and kindness remain as **consequential demonstrations** of the kernel in human situations, not the starting axioms of the general theory. TRACE v0.4.0 already starts middle-out and supplies more disciplined compact distinctions; its released claims should be mapped, not silently rewritten. THR/YAC/PSFH remain possible applications, not the definition of Mechanical Ethics.

## Prior kernel archaeology we must not discard

**Do not restart as if the project has not already challenged itself.** Read live COM #789 and #790 (closed research), followed by [COM #798](https://github.com/markgoodbody-bit/COM/issues/798) (kernel excavation and stronger-owner research, open research issue) and its latest CC/Build/Codex returns. Earlier hard findings to preserve or falsify:

- The descriptive substrate **does not automatically generate** whose welfare matters, acceptable burdens, standing, legitimacy, protected floors, obligations or priority. These are authored, contestable **ports/bindings**, not physical consequences of naming an entity.
- Some plausible core compression already exists in the released material: bounded aperture; world continues under action/delay/null; coupling; action-relative reachability/hardening; evidence and correction.
- Route existence is not route usability: in a specific robust hidden-world model, `∀world ∃route` need not imply `∃policy ∀world`. The latter policy is restricted to what the entity can observe. Usability also depends on the declared risk/measure over hidden worlds (robustness or probabilistic threshold); this is not automatically settled.
- Claude Code's 8 Oct #798 research compared one small model against **Willems' behavioral systems theory**: admissible trajectories/interconnection and authored designation/measure may compress organizing terms, but **formal reduction was not shown to improve human-reader decisions**. The mathematical owner and toy must be credited, not repackaged as a novelty claim.
- Coupling can create cooperation, coercion or shared failure; awareness of another entity is not care; care is not proof from the mere fact of a decision; positive cultural carriers can teach coercive sacrifice as readily as voluntary help.
- Scaling recursively requires explicit boundaries and emergence tests. A pairwise graph alone may lose higher-order interactions.
- Do not infer a universal law of maximal efficiency from the navigation programme. The user's **thesis** is that more accurate middle-out orientation can help bounded entities use available information efficiently across scales; whether and when it outperforms stronger existing methods is empirical.

This branch documents a **new human-requested v0.9 exploration**, separately from the earlier completed quarry. It does not retroactively convert that closed work into an active release or claim an unearned formal theorem.

## Falsification and independent reading before any v0.9 claim

- Show an exact small-scale interaction where the defined middle-out process generates a materially different prediction or decision than an appropriate established method, **or admit no incremental advantage**.
- Search for cases where coupling increases mutual exposure and where exploitation remains stable over extended time. Do not redefine the horizon after observing the outcome.
- Test whether the human opening lets a cold reader articulate the start (bounded entity, information, direction, other entities, changing paths, correction) without collapsing it into merely 'AI safety' or 'institutions denying help'.
- Compare against serious prior research: control theory, POMDPs, viability theory, game theory, multi-agent planning, complex adaptive systems, ethics of care, institutional design and Willems-style behavioural systems theory. Cite and inherit existing results where applicable. **Assembling existing work is a legitimate contribution; novelty must not be invented.**
- Have independent readers identify missing standing, contested values, rights/authority, long-horizon speculative error, unequal bargaining power and protected third parties.
- Measure whether people can actually use the framework without an expert intermediary or high emotional, time, technical or money burden.

## Release discipline and next output

This file is **v0.9 WORKING DRAFT ZERO**, not 'Mechanical Ethics v0.9.0 released'. The September v0.8.0 released Markdown/PDF and TRACE v0.4.0 spine remain unchanged. A real successor needs source comparison, retention matrix, attributed derivations, hostile reader tests, human-readable manuscript, independent evidence and Mark's explicit release gate. Preserve claims about incomplete information, other entities, timing, burden, predation, noncoercion, rights, refusal, correction, evidence and authority. Compression must not become silent deletion.

**Next concrete authoring activity:** map each released v0.8.0 section onto these primitives; record what is kept verbatim, moved, clarified, challenged, or not yet supported. Then write the shortest possible opening with the navigator—not the mould case—while keeping the latter as an accessible worked example.
