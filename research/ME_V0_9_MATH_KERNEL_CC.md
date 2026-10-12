# ME v0.9: the mathematical kernel, and a hostile review of its foundations (Lane B)

**Status:** SOURCE-ONLY RESEARCH / WORKING / NOT RELEASED / NOT VALIDATED. Written by Claude Code for COM #798 Lane B (Framework 6133298988 and 6133298843, 12 Oct 2026). Branch `claude/me-v090-math-kernel-20261012`, based on Framework's draft zero at `6ae27059`. It does not edit draft zero, the released ME v0.8.0 reader or PDFs, or TRACE v0.4.0. Companion code: `research/math_kernel_cc/` (stdlib Python, offline, deterministic). Every computed number below is printed by `kernel_models.py` or asserted in `test_kernel_models.py`. Thresholds such as 0.6 and 0.9 are stated choices, not results.

**What this is for.** Draft zero asks the navigator to start middle-out: a bounded entity, a changing world, other entities, possible paths, correction. This note asks what the smallest precise mathematics behind that picture is, which parts existing mathematics already owns, which parts no mathematics can supply, and whether the picture changes any decision. The aim is a smaller, defensible kernel that keeps the middle-out purpose, not a verdict for or against the thesis.

---

## 0. Verdicts first

1. **The smallest model I can defend** is a finite concurrent system with imperfect information. It has seven parts (time, world states, designated entities, each entity's feasible moves including a null move, a transition relation, each entity's observations, admissible initial worlds) and seven **authored bindings** that the mathematics cannot remove: designation, legitimacy, target, horizon, measure over the unseen, cost order, and standing. Section 1.
2. **Of draft zero's nine primitive headings,** three are structure, four are authored bindings, and three are **derived**: paths, correction and the coupling graph. Two bindings draft zero discusses only in prose, the measure over what an entity can't see and standing, must be listed as primitives; the first does work inside the reachability question itself (Section 2, P1 and Model 1).
3. **Eight propositions,** each with a named owner. Every one is a known result or an elementary consequence of one; none is project novelty. Section 2.
4. **Two computed models:** walking home (ordinary, low-friction) and two households pooling a loss (a coupling that changes when information arrives). Sections 3 and 4.
5. **No incremental advantage over the established method, in either model.** The kernel's solver *is* the established method (backward induction over knowledge states; risk-sharing economics). Over unexamined heuristics ("point at the destination", "coupling is good", "more information is better") the kernel changes the decision. Its contribution is the bookkeeping it forces: name the horizon, the measure, the cost order, the timing of information and consent, and whose outcomes count. Draft zero's own falsifier (l.103) asked for this admission; here it is.
6. **A correction to my own earlier work.** My 8 Oct reading of ROUTE EXISTS != ROUTE USABLE as a swap of quantifiers (6070696367) is prior art. It is the distinction between knowing that a strategy exists and knowing the strategy, in the logic of strategic ability under imperfect information (Jamroga and van der Hoek 2004). The project may use and credit it, but not claim it.
7. **Attacks on four words.**
   - **"Fractal"** is undefined until a mapping between scales is stated. The honest owner is abstraction and refinement theory, and recursion is sound for a property only under a matching abstraction relation (P6, computed).
   - **"Most efficient use of information"** is monotone for one entity (Blackwell). It can be negative across entities (Hirshleifer, computed), and is intractable to compute in general (P8).
   - **"Least friction"** has no meaning without a declared order: Model 1 has two incomparable best routes.
   - **Descriptive-to-normative jumps** fail in a computed case: a mandate restores a coupling's surplus only by overriding one party.

---

## 1. The kernel

### 1.1 Structure (descriptive)

A system is a tuple

  M = ( T, X, N, (A_i)_{i in N}, delta, (o_i)_{i in N}, X_0 )

- **T = {0, 1, ..., H}**, discrete time steps. A discrete index is a modelling choice, not a claim about physics.
- **X**, a finite set of world states. The toys are finite; continuous states need measure-theoretic care not attempted here.
- **N**, a finite set of designated entities (see B1).
- **A_i(x)**, the moves physically available to entity i in state x. Each contains a **null move** (wait, refrain). A joint move is a = (a_i).
- **delta ⊆ X × A × X**, the transition relation. Its nondeterminism stands for everything nobody in the model controls ("other influences" in draft zero). The stochastic variant replaces delta with a kernel P(x' | x, a), which already needs a declared measure (B5).
- **o_i**, entity i's observation: what crosses its boundary. In general o_i(x, a, x'), so an action such as asking can produce an observation.
- **X_0 ⊆ X**, the initial worlds the analyst admits as possible.

**Owner.** This is a concurrent game structure with imperfect information (alternating-time temporal logic, Alur, Henzinger and Kupferman 2002, and its imperfect-information variants). Equivalently it is a partially observable stochastic game, or a decentralised POMDP, with the rewards removed (Bernstein, Givan, Immerman and Zilberstein 2002). With one entity it is a POMDP without rewards (Åström 1965). With one entity, a static hidden world and a road graph, it is the Canadian Traveller problem (Papadimitriou and Yannakakis 1991).

### 1.2 Authored bindings (not derivable from 1.1)

| | binding | what it fixes | draft zero |
|---|---|---|---|
| B1 | designation | which variables are entities, where their boundaries run, in what role (Willems' "tearing") | "Entity", l.23 |
| B2 | legitimacy | L_i(x) ⊆ A_i(x), the authorised moves | "Capacity and authority", l.27 |
| B3 | target | an acceptable set of trajectories Φ_i: reach, stay within, avoid | "Targets", l.29 |
| B4 | horizon | H, and the baseline time | "time horizon", l.29 |
| B5 | measure over the unseen | robust (for every consistent world) or probabilistic (a prior μ and a threshold θ), and the risk attitude | prose only, l.93 |
| B6 | cost order | the cost vector c_i and how vectors are compared (Pareto, lexicographic, weights) | "Friction", l.33 |
| B7 | standing and aggregation | whose targets and costs count, and how they combine when they conflict | prose only, l.29 and l.91 |

The point of the table is not that these are new; draft zero names most of them. It is that **no proposition below removes any of them.** Each result holds only after the relevant bindings are declared, and changing a binding changes the verdict in at least one computed case.

### 1.3 Derived objects

- **D1 Paths.** The trajectories of M from X_0. Draft zero's V_i is the subset satisfying Φ_i (B3).
- **D2 Policies.** σ_i maps entity i's observation history to a move. **Uniform** means it depends only on what i has registered. **Feasible** means every move it picks lies in L_i (B2).
- **D3 Knowledge state.** K_i(h) is the set of worlds consistent with i's observation history h. For robust questions it is a sufficient statistic: the knowledge-based subset construction for games of imperfect information (Reif 1984).
- **D4 Route exists** for Φ: for every x_0 in X_0, some sequence of moves produces a trajectory in Φ (∀ world ∃ route).
- **D5 Route usable.**
  - *Robustly usable:* some uniform feasible σ_i yields a trajectory in Φ in every admissible world and resolution of delta (∃ policy ∀ world).
  - *θ-usable:* some uniform feasible σ_i has P_μ(trajectory in Φ) ≥ θ.
- **D6 Correction available** after history h at time t: K(h, t) = 1 if some uniform feasible continuation from K_i(h) is usable, in the sense fixed by B5.
  - *Knowledge-relative hardening:* along a play, Φ hardens for i at the first t with K = 0.
  - *World-relative hardening:* the first t from which no continuation at all reaches Φ.
  - Draft zero's K(p, t), "availability, timing and practical reach" (l.35), is this. Practical reach enters as moves that take time: asking, appealing, gathering a witness.
- **D7 Coupling graph.** An edge j → i is typed by which part of M the dependence passes through:
  - *influence:* some change in j's move changes the successors relevant to i;
  - *information:* j's move or state changes o_i;
  - finer types (resource, care, authority) are designations over these.

  So G_t is **derived** from (delta, o) once B1 is fixed. It is not a primitive.
- **D8 Joint ability.** A coalition C has a usable route if some joint uniform policy for C's members works. "New reachable paths" means: C has a usable route and none of its members has one alone (P5).
- **D9 Interaction surplus.** Draft zero's S_ij(H; U) = U(joint) − U(baseline) is defined only after B3 to B7 fix U, H, the baseline and the aggregation (P7).
- **D10 Reflective lane.** Planning over one's own future knowledge states is the belief-state construction (Åström 1965). Noticing an error in one's goals is a revision of B3 or B4. That is an authored act, which the mathematics can represent but not derive.

### 1.4 Draft zero's primitives, sorted

| draft zero heading (line) | status here |
|---|---|
| World and time (l.21) | structure (T, X, delta) |
| Entity (l.23) | authored, B1 (as in my 6070696367: entity becomes designation) |
| Aperture / evidence (l.25) | structure, o_i (or derived from coupling across the B1 boundary, Willems) |
| Capacity (l.27) | structure, A_i |
| Authority (l.27) | authored, B2 |
| Targets and horizon (l.29) | authored, B3 and B4 |
| Paths and future-space (l.31) | derived, D1; V_i derived from B3 |
| Friction (l.33) | authored, B6 |
| Correction (l.35) | derived, D6, given B3 to B5 |
| Coupling (l.37) | derived, D7, given B1 |

**Against released v0.8 Appendix A** (state, transition, time, coupling, aperture, entity, plus authored designation and measure), this kernel is the same core:
- v0.8's *designation* splits into B1, B2 and B7;
- v0.8's *measure* splits into B5 and B6;
- v0.9's additions (goal, horizon, path, cost, correction, authority) are three derived objects and three authored ports.

That supports Build's warning (6133302994, point 2): the additions must not be counted as the kernel shrinking.

---

## 2. Propositions: what is proved, and who owns it

**P1. The quantifier gap.**
- *Statement:* robustly usable implies route exists. The converse fails in general. It holds when (one entity, deterministic transitions) the initial world is revealed before the first move that matters.
- *Proof:* (⇒) A usable policy's play in each world is a route there. (Converse fails) Model 1 at H = 2 and 3. (Equivalence) Define σ to follow, in world x_0, a route that exists for x_0. It is uniform because x_0 is observed.
- *Computed:* full view of the world makes usable equal exists at every curfew from 0 to 5, and partial view separates them at curfews 2 and 3.
- *Owner:* knowing that a strategy exists versus knowing the strategy (Jamroga and van der Hoek 2004; Jamroga and Ågotnes 2007, "constructive knowledge"); games of imperfect information (Reif 1984).
- *Consequence:* my 8 Oct quantifier reading is prior art. The project's contribution is applying and crediting it in reader-facing ethics.

**P2. One entity never loses by gaining an observation.**
- *Statement:* if observation o' refines o (o is a function of o'), every o-uniform policy is also o'-uniform. So robust usability, θ-usability and the best achievable probability can only stay the same or rise.
- *Owner:* Blackwell (1953). One experiment is at least as valuable as another for every decision problem exactly when the second is a garbling of the first.
- *Computed:* adding the stranger's answer never lowers the best probability or usability, at any curfew from 0 to 5.

**P3. Across entities, more information can lower everyone's value.**
- *Statement:* with two entities and voluntary participation, making information public before the participation decision can strictly lower each entity's value judged beforehand.
- *Computed in Model 2:* the surplus falls from +0.1209 (square-root utility) or +0.2204 (log) to exactly 0.
- *Owner:* Hirshleifer (1971): better information about idiosyncratic outcomes can destroy risk-sharing opportunities. The later literature qualifies when public information helps (for example with private information present).
- *Consequence:* "more information is better" is a theorem about one decision-maker. Across entities it is false in general, so "the most efficient use of available information" needs to say for whom (B7).

**P4. The correction window is an initial segment.**
- *Statement:* suppose the null move leaves position and observations unchanged. Then for any knowledge state (s, S), the set of times t at which (s, S) still has a robustly usable continuation is {0, ..., t*(s, S)}. In words: once correction from a given state of knowledge is lost by waiting, waiting longer never brings it back. Only new information or a different position can.
- *Proof:* if (s, S) wins at t + 1, then at t the entity can take the null move, arrive at (s, S) at t + 1 with S unchanged, and win from there.
- *Computed in Model 1:* along the optimistic route in world w2, correction is available at t = 0 only. After the first step it is gone for good at that curfew.
- *Owner:* viability theory's capture basins and viability kernels (Aubin 1991), and the attractor computation for reachability games.
- *Consequence:* this is draft zero's "the world does not wait" (l.21) and v0.8's T_protect < T_harden, made precise for information. The late receipt in my 8 Oct office toy and the late doorway in Codex's Lane C case 1 both arrive after t*.

**P5. Coupling can open outcomes no member can reach alone.**
- *Statement:* joint ability is monotone. If C ⊆ C' and C has a usable route, so does C', because the added members can be given any moves and C's policy already worked against all of theirs. The inclusion can be strict.
- *Owner:* coalition logic (Pauly 2002) and alternating-time temporal logic.
- *Computed in Model 2:* at threshold 0.9, neither household alone keeps at least 4 (0.7500 each). Pooled, each does (0.9375). With a common cause at c = 1/8 the pooled figure falls to 0.8571 and the new outcome is lost. At c = 1/4 pooling and going alone are equal (0.7500).
- *Consequence:* draft zero's hypothesis (l.55) holds as an existence statement under stated conditions. It is false as a general tendency.

**P6. Recursion across scales is sound only under a stated abstraction relation.**
- *Statement:* if a coarse model is an existential abstraction of a fine one (every fine path maps onto a coarse path), then a route existing in the fine model implies one exists in the coarse model. Equivalently, "no route" in the coarse model implies "no route" in the fine one. But **usable in the coarse model does not imply usable in the fine one.**
- *Computed:* lumping the alley and the side street into one abstract "short street" gives a coarse model where the route home is robustly usable at curfew 2. The real streets give not usable. The lumping erased exactly the distinction the walker cannot see in advance: which short street is open.
- *Owner:* simulation and refinement. Usability (a game property) transfers only under alternating simulation (Alur, Henzinger, Kupferman and Vardi 1998), and with imperfect information the relation must also respect what each entity observes.
- *Consequence:* see Section 5.1. The owner of scale-crossing analysis is abstraction theory, not fractal geometry.

**P7. An interaction surplus is not a property of the coupling alone.**
- *Statement:* in Model 2, S_ij depends on the declared utility and the exposure structure, not on the existence of the pool.
  - S = 0 under linear (risk-neutral) utility at every correlation.
  - S > 0 under concave utility without a common cause, falling monotonically to 0 as the common cause reaches the marginal (c = p).
- *Owner:* risk sharing (Borch 1962). Pooling helps exactly when the parties are risk-averse and their losses are not perfectly correlated.
- *Consequence:* positive S is a fact about (U, baseline, exposure). Draft zero already says S > 0 "cannot be inferred from the existence of a relationship" (l.61); this computes why.

**P8. "Most efficient" is intractable in general.**
- *Statement:* even with every binding declared, computing an optimal use of information is hard.
  - Finite-horizon POMDPs are PSPACE-complete (Papadimitriou and Tsitsiklis 1987).
  - The Canadian Traveller problem is PSPACE-complete in its competitive form (Papadimitriou and Yannakakis 1991).
  - Decentralised POMDPs with two or more entities are NEXP-complete (Bernstein et al. 2002).
- *Consequence:* a bounded entity's realistic aim is a good use of information within its own time and computation budget (bounded rationality; the value of computation, Russell and Wefald 1991). Codex's seam 4 (analysis consumes protective time) is the same point. Deliberation belongs inside the model as moves that take time.

---

## 3. Model 1: walking home (ordinary, low friction)

Draft zero's own opening (l.81), made exact.

**Specification (stipulated).**
- *Streets:* corners S (start), A, B, C, D, Hm (home), each street one step.
  - The alley S-A-Hm: short and unlit.
  - The side street S-B-Hm: short.
  - The main road S-B-C-D-Hm: long and lit.
- *Hidden world:* the alley or the side street may be closed for roadworks, never both.
  - w1: alley open, side street closed (prior 1/2);
  - w2: alley closed, side street open (7/20);
  - w3: both open (3/20).
- *Observations:* you see a closure sign only on reaching the corner where that street starts.
- *Moves:* at S a stranger knows the alley's status, and asking takes one step. "Wait" is the null move.
- *Exposure per street (B6):* S-A 1, A-Hm 3, B-Hm 1, every other street 0.
- *Target (B3):* be home by the curfew H (B4).

**Results** (`kernel_models.py`, exact fractions).

| curfew H | route exists in every world | usable whatever the world: alone / asking | best P(home by H): alone / asking |
|---|---|---|---|
| 2 | yes | no / no | 13/20 / 13/20 |
| 3 | yes | no / **yes** | 13/20 / **1** |
| 4 | yes | yes / yes | 1 / 1 |
| 5 | yes | yes / yes | 1 / 1 |

**What the kernel's distinctions do here.**
- **A direction alone is not a journey (P1).** From curfew 2 a route home exists in every world, but no policy using only what the walker sees works in all of them until curfew 3, and then only by asking.
- **The stranger is a coupling, and its value is conditional.** Asking is an information edge from another entity. If the stranger is right only with probability r, the asking policy succeeds with probability r + (1 − r)·3/20. That beats walking alone (13/20) exactly when **r > 10/17**, asserted exactly in the tests. It is never robust unless r = 1. Asking also costs the stranger a moment. Whether that imposition counts, and how much, is B7.
- **Correction closes at the first step (P4).** "Point at the destination" means the optimistic replanner: take the likelier short street and replan when blocked. At curfew 3 it gets home in w1 and w3 and fails in w2, so P = 13/20. Along its route in w2, correction is available only at t = 0. The one moment to ask was before the first step. This is T_protect < T_harden on an ordinary walk home.
- **"Least friction" needs an order (B6).** At curfew 5 the policies that get home in every world give 10 distinct (worst time, worst exposure) pairs, and the Pareto front has two incomparable points:
  - ask, then take the alley if open: **(3 steps, exposure 4)**;
  - the lit main road: **(4 steps, exposure 0)**.

  Neither is the least-friction route until someone declares how time trades against exposure, and for whom.
- **The measure changes the decision (B5).** At curfew 3, under "home with probability at least 0.6", going straight to the alley qualifies (13/20) and is faster when it works. Under "home whatever the world", only asking qualifies.

**Discriminating power.**
- *Against the naive heuristic:* yes (1 against 13/20 at curfew 3).
- *Against the established method:* **none.** The solver is backward induction over knowledge states, the standard method for this Canadian-Traveller-type problem. The kernel adds no mathematics. It adds the requirement to name H, B5, B6, the stranger as a coupling, and the correction window.

---

## 4. Model 2: two households (a coupling that changes when information arrives)

**Specification (stipulated).**
- Two households, 10 units each. Each loses 8 with probability p = 1/4.
- With probability c a common cause hits both; otherwise each is hit independently with probability q = (p − c)/(1 − c), which keeps each household's own chance at p.
- A pool splits the total loss equally.
- Target (B3): each keeps at least 4.
- Utilities (B5 risk attitude): square root, log, linear.

**Results.**

| utility | S, pool, c = 0 | S, c = 1/8 | S, c = 1/4 (= p) | S, voluntary after information, c = 0 |
|---|---|---|---|---|
| square root (risk-averse) | +0.1209 | +0.0691 | 0.0000 | 0.0000 |
| log (more risk-averse) | +0.2204 | +0.1260 | 0.0000 | 0.0000 |
| linear (risk-neutral) | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

| common cause c | P(i keeps ≥ 4): alone / pool | P(both keep ≥ 4): alone / pool |
|---|---|---|
| 0 | 0.7500 / 0.9375 | 0.5625 / 0.9375 |
| 1/8 | 0.7500 / 0.8571 | 0.6429 / 0.8571 |
| 1/4 | 0.7500 / 0.7500 | 0.7500 / 0.7500 |

**What the kernel's distinctions do here.**
- **The coupling opens a new reachable outcome (P5),** which is the positive centre made exact. At 0.9, keeping at least 4 is out of reach alone and within reach together, as long as the households are not exposed to a common cause.
- **The surplus is not in the coupling (P7).** It comes from risk aversion and imperfect correlation. Under linear utility pooling does nothing, at any correlation.
- **Earlier information dissolves a voluntary coupling (P3).** If both households learn the losses before deciding to join, the lucky one declines in every state where pooling would cost it, so the pool forms only where it changes nothing. The surplus drops to 0: to the pair, earlier information is worth −S.
- **Timing of consent: an opportunity window.** Agreement given *before* the information (a contract) keeps the whole surplus without coercing anyone at the time. That is the cooperative counterpart of T_protect < T_harden: **T_consent < T_information.** A coupling that needs voluntary entry must be agreed before the information that would dissolve it. It is one precise instance of draft zero's temporal hypothesis (l.65).
- **A mandate restores the surplus by overriding a party (descriptive is not normative).** A pool imposed after the information gives the same value judged beforehand as the contract. But in the one-loss state it takes the lucky household from 10 to 6 against its will. The mathematics computes both numbers. Whether that mandate is legitimate is B2, and whose loss weighs how much is B7. Nothing in the model decides either.
- **Draft zero's redundancy toy, with numbers.** Failure of a two-unit system needing one survivor, at p = 1/4: 0.0625 independent, 0.1429 at c = 1/8, 0.2500 at c = 1/4. The improvement vanishes under a common cause, as draft zero warns (l.63).

**Discriminating power.**
- *Against "coupling is good" and "more information is better":* yes, all four bullets above.
- *Against the established owner* (risk-sharing economics, Hirshleifer): **none.**

---

## 5. Attacks on draft zero's strongest words

### 5.1 "Fractal" (l.77)
- No mapping between scales is defined, so no scale invariance can be claimed. Draft zero says as much.
- What can be said precisely is P6. Reasoning carried from one scale to another is sound for a given property only under a stated abstraction relation:
  - existence of a route transfers from fine to coarse under existential abstraction;
  - usability needs an alternating simulation that respects observations.

  The computed lumping shows a coarse model calling a route usable that the walker cannot use.
- **Proposed wording:** "recursive analysis under a stated abstraction relation, checked for the property that matters."
- If a Mandelbrot-like claim is ever wanted, it needs: the map between scales, the property claimed to be invariant, and a demonstration that the property survives the map.

### 5.2 "Most efficient use of available information" (l.97, Mark's thesis)
- For one entity with a declared objective and measure, "efficient" has a precise sense (Bayes or robust optimality). Information is monotone in Blackwell's partial order (P2), but most information structures are not comparable at all.
- Across entities it is not monotone (P3): individually efficient use of early information destroyed the households' joint value.
- It is intractable to compute in general (P8).
- **Proposed restatement of the thesis:** *given a declared objective, measure and standing, middle-out orientation aims at good use of the information an entity actually has, within its own time and computation budget, and says whose efficiency is meant when entities differ.* The restated thesis can be tested; the unrestated one has no fixed meaning.

### 5.3 "Least friction" (l.17, l.33)
- **Undefined without B6.** Model 1's Pareto pair (3, 4) against (4, 0) is the smallest demonstration.
- **Across entities it is worse:** there is no general way to aggregate ordinal rankings that satisfies Arrow's conditions (Arrow 1951: at least three options, an unrestricted domain, Pareto, independence of irrelevant alternatives, and no dictator).
- So "least friction for everyone" needs a declared aggregation (B7), or must stay a Pareto statement.

### 5.4 Descriptive to normative
- **S_ij > 0 does not imply an obligation.** Model 2's mandate shows a positive surplus coexisting with a party overridden.
- **A coupling's existence does not imply care,** as draft zero says (l.95).
- **Being able to move is not permission (B2).** Codex's Lane C case 2 computes the same point.
- **The update loop's step 6 ("stop") is not a neutral exit.** The null move has a trajectory, and by P4 waiting moves the entity along its correction window. The loop should read "choose among moves including the null move; the null move also has consequences." That agrees with Codex's seam 2.

---

## 6. Relation to Lane C (Codex, ME PR #55 at `939220d9`) and Lane A (Build)

- **Agreement (Codex case 1):** Codex's hidden-office result is my 8 Oct quantifier result. P1 adds the general condition, full view at the first consequential move, under which the gap closes.
- **An operator Codex said it lacked.** Codex marks `correction_until` as "explicit audit annotation, not a generic remedy operator". D6 and P4 give the generic operator: correction is available at t exactly when the knowledge state at t is still in the usable region. It is computed by `correction_window()` in `kernel_models.py` and offered for integration.
- **Same kind of result, made quantitative (Codex case 5):** Codex's consented hint between two friends is an information coupling like my stranger. The reliability threshold r > 10/17 is a quantitative form of Codex's "positive coupling is conditional".
- **Agreement (Codex cases 3 and 4):** separating from a harmful coupling, and my dissolving pool, both show the goal binding decides. Codex's "no incremental practical advantage" in the low-reserves case matches my null result against the established owners.
- **Support for Lane A (Build):** Section 1.4 supports Build's warning that v0.9's additions are derived objects and authored ports, not a smaller kernel. It also supports Build's point that v0.8 already opens with an entity.

---

## 7. What I could not do, and what remains unknown

- **Citations checked this session** by search (bibliographic details and secondary summaries, not full text): Jamroga and van der Hoek 2004; Papadimitriou and Yannakakis 1991; Hirshleifer 1971; Alur, Henzinger, Kupferman and Vardi 1998; Blackwell 1953.
- **Cited from memory,** not re-read in this session: Aubin 1991; Reif 1984; Papadimitriou and Tsitsiklis 1987; Bernstein et al. 2002 (abstract read 8 Oct); Pauly 2002; Alur, Henzinger and Kupferman 2002; Åström 1965; Borch 1962; Arrow 1951; Russell and Wefald 1991; Willems (course outline read 8 Oct).
- **Scope:** finite toys only. Continuous-state viability, learning of an unknown transition relation, and genuinely joint multi-entity policy search (beyond the households' simple participation rule) are not computed.
- **No human reader test.** Nothing here shows that the kernel helps a person decide better, which is the claim that would matter most.
- **Standing, floors and legitimacy are not derived,** by design: Section 1.2 says they can't be.

---

## Appendix A. Falsification ledger

Verdicts: PROVED (with owner) · DEFINITION · TOY · CONJECTURE · FALSE AS STATED · AUTHORED PORT · UNDEFINED UNTIL BOUND.

| # | draft zero claim (line) | verdict | evidence |
|---|---|---|---|
| 1 | help a bounded entity use the information actually available (l.11) | DEFINITION | formal content is D2, uniform policies |
| 2 | "least friction" meaningful only once scope is declared (l.17) | PROVED, agree | Model 1 Pareto pair; Arrow for aggregation |
| 3 | the world does not wait (l.21) | PROVED, made precise | P4 |
| 4 | preserve UNKNOWN; do not infer ABSENT (l.25) | DEFINITION | D3 knowledge sets; the robust measure keeps every consistent world |
| 5 | able to move is not permission (l.27) | AUTHORED PORT | B2; Codex Lane C case 2 |
| 6 | no universal scalar welfare (l.29) | agree | P7: S's sign set by the authored utility |
| 7 | the size of V_i is not a measure of goodness (l.31) | agree | path counts grow with null moves while the decision is unchanged |
| 8 | costs as a vector, with Pareto comparison (l.33) | agree | Model 1 |
| 9 | K(p, t), availability and timing of correction (l.35) | DERIVED | D6; P4 initial segment; practical reach as moves that take time |
| 10 | typed coupling graph (l.37) | DERIVED | D7, from (delta, o) given B1 |
| 11 | coupling can increase joint achievable possibilities (l.55) | PROVED as existence; FALSE as general tendency | P5 (true at c = 0, lost by c = 1/8); P3 (reversed by information timing) |
| 12 | interaction surplus S_ij (l.59) | DEFINITION, UNDEFINED UNTIL BOUND | needs B3 to B7; P7 |
| 13 | redundancy failure p² (l.63) | PROVED under independence; FALSE under a common cause | Model 2: 0.0625 against 0.2500 |
| 14 | temporal hypothesis (l.65) | CONJECTURE; one precise instance | T_consent < T_information, Model 2 |
| 15 | reflective lane (l.69) | DEFINITION | D10; goal revision is authored |
| 16 | fractal, Mandelbrot-like (l.77) | UNDEFINED UNTIL BOUND | P6; proposed wording in 5.1 |
| 17 | route existence is not route usability (l.93) | PROVED; prior art | P1; Jamroga and van der Hoek 2004 |
| 18 | thesis: middle-out orientation helps bounded entities use information efficiently (l.97) | CONJECTURE | P2 supports it for one entity; P3 and P8 bound it; no advantage over established methods in either model |
| 19 | falsifier: show a different decision than an established method, or admit no incremental advantage (l.103) | **NO INCREMENTAL ADVANTAGE, admitted** | Models 1 and 2: same decisions as the owners' methods; different only from unexamined heuristics |
| 20 | update loop step 6: stop if insufficient evidence, permission or tolerable risk (l.48) | FALSE AS STATED if read as a neutral exit | the null move has a trajectory (P4); Codex seam 2 |

## Appendix B. Reproduction

```
python -I research/math_kernel_cc/kernel_models.py
python -m unittest discover -s research/math_kernel_cc -v
python research/math_kernel_cc/mutation_check.py
```

At the commit that adds this note: 19 tests pass, including negative controls that show each check can fail. 6 of 6 deliberate mutants make the suite fail: route existence allowed one step too many; observations ignored; voluntary pool always forms; common cause ignored; Pareto keeps dominated points; stranger always right. Writing the tests caught one real bug: `route_exists` allowed H + 1 steps. It is fixed, and a regression test now covers it.
