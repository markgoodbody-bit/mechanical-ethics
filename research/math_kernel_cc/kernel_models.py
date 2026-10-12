"""ME v0.9 Lane B (COM #798, Claude Code): the computations behind
research/ME_V0_9_MATH_KERNEL_CC.md.

Two small, fully specified models plus checks of the note's propositions. Python stdlib only,
deterministic, offline. Every number in the models (street layout, priors, losses, utilities,
floors) is STIPULATED to make a structure visible. Nothing here is evidence about any real street,
household or person.

    python -I research/math_kernel_cc/kernel_models.py          # print every result
    python -m unittest discover -s research/math_kernel_cc -v    # the checks

Solver: one entity, a hidden world drawn from a finite set, deterministic dynamics in each world,
and observations that depend on the world. The knowledge state (position, time, set of worlds
still consistent with what was observed) is the standard sufficient statistic for robust
reachability (the knowledge-based subset construction for games of imperfect information).
Probabilities are exact fractions.
"""
from fractions import Fraction as Fr
from functools import lru_cache
import math

# --------------------------------------------------------------------------- generic solver


class Task:
    """worlds: tuple of names; prior: {world: Fraction}; start, goal: positions;
    moves(s) -> actions available at s (the legitimate set L, including the null move "wait");
    step(w, s, a) -> next position; cost(s, a, s2) -> exposure of that step (known to the entity);
    observe(w, s, a, s2) -> what the entity registers after the step."""

    def __init__(self, worlds, prior, start, goal, moves, step, cost, observe, initial_obs=None):
        self.worlds, self.prior, self.start, self.goal = tuple(worlds), dict(prior), start, goal
        self.moves, self.step, self.cost, self.observe = moves, step, cost, observe
        self.initial_obs = initial_obs or (lambda w: None)


def initial_classes(task):
    """Worlds the entity cannot tell apart before acting."""
    parts = {}
    for w in task.worlds:
        parts.setdefault(task.initial_obs(w), set()).add(w)
    return [frozenset(p) for p in parts.values()]


def split(task, s, S, a):
    """Successor knowledge parts after action a: worlds grouped by what the entity then registers."""
    parts = {}
    for w in sorted(S):
        s2 = task.step(w, s, a)
        key = (s2, task.observe(w, s, a, s2))
        parts.setdefault(key, set()).add(w)
    return [(key[0], frozenset(ws)) for key, ws in sorted(parts.items(), key=lambda kv: repr(kv[0]))]


def solver(task, H):
    """Memoised robust-win, best-probability and outcome-profile functions over knowledge states."""

    @lru_cache(maxsize=None)
    def win(s, t, S):
        # exists an observation-based (uniform) continuation reaching the goal by H in every world of S
        if s == task.goal:
            return True
        if t >= H:
            return False
        return any(all(win(s2, t + 1, P) for s2, P in split(task, s, S, a)) for a in task.moves(s))

    @lru_cache(maxsize=None)
    def best(s, t, S):
        # max over uniform continuations of P(goal by H | S), under the declared prior.
        # Support semantics (Codex, COM #798 6133683747): a world with prior 0 stays ADMITTED, so the
        # robust questions still range over it, but it carries no probability, so this recursion never
        # conditions on a zero-mass class (it contributes weight 0 and is skipped).
        if s == task.goal:
            return Fr(1)
        if t >= H:
            return Fr(0)
        mass = sum(task.prior[w] for w in S)
        if mass == 0:
            raise ValueError("probability is undefined on a zero-mass knowledge state")
        values = []
        for a in task.moves(s):
            v = Fr(0)
            for s2, P in split(task, s, S, a):
                part = sum(task.prior[w] for w in P)
                if part:
                    v += part / mass * best(s2, t + 1, P)
            values.append(v)
        return max(values)

    @lru_cache(maxsize=None)
    def profiles(s, t, S):
        # every uniform policy's per-world outcome: {world: (arrival time or None, exposure)}
        if s == task.goal:
            return {frozenset((w, (t, 0)) for w in S)}
        if t >= H:
            return {frozenset((w, (None, 0)) for w in S)}
        out = set()
        for a in task.moves(s):
            per_part = []
            for s2, P in split(task, s, S, a):
                c = task.cost(s, a, s2)
                per_part.append([frozenset((w, (arr, e + c)) for w, (arr, e) in prof)
                                 for prof in profiles(s2, t + 1, P)])
            combos = [frozenset()]
            for options in per_part:
                combos = [acc | opt for acc in combos for opt in options]
            out.update(combos)
        return out

    return win, best, profiles


def route_exists(task, H):
    """God's-eye: for every world there is SOME action sequence reaching the goal by H."""
    def reach(w):
        frontier = {task.start}          # positions reachable in exactly k steps, k = 0..H
        for _ in range(H):
            if task.goal in frontier:
                return True
            frontier = {task.step(w, s, a) for s in frontier for a in task.moves(s)}
        return task.goal in frontier
    return all(reach(w) for w in task.worlds)


def usable_robust(task, H):
    win, _, _ = solver(task, H)
    return all(win(task.start, 0, S) for S in initial_classes(task))


def best_probability(task, H):
    _, best, _ = solver(task, H)
    total = sum(task.prior.values())
    return sum(sum(task.prior[w] for w in S) / total * best(task.start, 0, S)
               for S in initial_classes(task) if sum(task.prior[w] for w in S))


def simulate(task, H, policy, w):
    """Follow a knowledge-state policy in world w. Returns (arrival or None, exposure, trace)."""
    S = next(C for C in initial_classes(task) if w in C)
    s, t, exposure, trace = task.start, 0, 0, []
    while s != task.goal and t < H:
        a = policy(task, s, t, S)
        s2 = task.step(w, s, a)
        o = task.observe(w, s, a, s2)
        exposure += task.cost(s, a, s2)
        S = frozenset(v for v in S if task.step(v, s, a) == s2 and task.observe(v, s, a, s2) == o)
        trace.append((t, s, a, s2))
        s, t = s2, t + 1
    return (t if s == task.goal else None), exposure, trace


def pareto(points):
    pts = set(points)
    return sorted(p for p in pts if not any(q != p and q[0] <= p[0] and q[1] <= p[1] for q in pts))


# --------------------------------------------------------------------------- Example 1: walking home
#
# Corners S (start), A, B, C, D, Hm (home). Each street takes one time step.
#   S-A, A-Hm  (the alley: short, unlit)          S-B, B-Hm  (the side street: short)
#   B-C, C-D, D-Hm (the main road: long, lit)
# The alley A-Hm and the side street B-Hm may be closed for roadworks. Stipulated council rule:
# never both closed. You see a closure sign only on reaching the corner where that street starts.
# At S a stranger knows whether the alley is open; asking takes one step. "wait" is the null move.

EDGES = {frozenset(e): x for e, x in {("S", "A"): 1, ("A", "Hm"): 3, ("S", "B"): 0, ("B", "Hm"): 1,
                                       ("B", "C"): 0, ("C", "D"): 0, ("D", "Hm"): 0}.items()}  # exposure
UNCERTAIN = {"alley": frozenset(("A", "Hm")), "side": frozenset(("B", "Hm"))}
STREET_WORLDS = {"w1": {"alley": True, "side": False}, "w2": {"alley": False, "side": True},
                 "w3": {"alley": True, "side": True}}
STREET_PRIOR = {"w1": Fr(1, 2), "w2": Fr(7, 20), "w3": Fr(3, 20)}  # P(alley open) = 13/20, P(side open) = 1/2


def walking_home(stranger=True, reliability=None, full_view=False):
    """reliability=None: the stranger is right. reliability=r: worlds gain a hidden 'mistaken' twin
    with prior weight 1-r, in which the stranger reports the alley the wrong way round."""
    if reliability is None:
        worlds = {w: (STREET_WORLDS[w], True) for w in STREET_WORLDS}
        prior = dict(STREET_PRIOR)
    else:
        worlds, prior = {}, {}
        for w, streets in STREET_WORLDS.items():
            worlds[w], prior[w] = (streets, True), STREET_PRIOR[w] * reliability
            worlds[w + "~"], prior[w + "~"] = (streets, False), STREET_PRIOR[w] * (1 - reliability)

    def neighbours(s):
        return sorted({x for e in EDGES for x in e if s in e and x != s})

    def moves(s):
        return neighbours(s) + ["wait"] + (["ask"] if stranger and s == "S" else [])

    def open_(w, edge):
        streets = worlds[w][0]
        return all(streets[name] for name, e in UNCERTAIN.items() if e == edge)

    def step(w, s, a):
        if a in ("wait", "ask"):
            return s
        return a if open_(w, frozenset((s, a))) else s

    def cost(s, a, s2):
        return EDGES[frozenset((s, s2))] if s2 != s else 0

    def observe(w, s, a, s2):
        streets, honest = worlds[w]
        seen = tuple(sorted((name, streets[name]) for name, e in UNCERTAIN.items() if s2 in e and s2 != "Hm"))
        heard = (streets["alley"] if honest else not streets["alley"]) if a == "ask" else None
        return seen, heard

    initial = (lambda w: w) if full_view else None
    return Task(worlds, prior, "S", "Hm", moves, step, cost, observe, initial_obs=initial)


def optimistic_replanner(task, s, t, S):
    """'Point at the destination': shortest map route, treating unknown streets as open and avoiding
    streets known closed; ties broken toward the street more likely open. Never asks, never waits."""
    def usable_edge(e):
        names = [n for n, x in UNCERTAIN.items() if x == e]
        return not names or any(task.step(w, list(e)[0], list(e)[1]) == list(e)[1] for w in S)

    def p_open(e):
        names = [n for n, x in UNCERTAIN.items() if x == e]
        if not names:
            return Fr(1)
        mass = sum(task.prior[w] for w in S)
        return sum(task.prior[w] for w in S if task.step(w, list(e)[0], list(e)[1]) == list(e)[1]) / mass

    dist = {task.goal: 0}
    frontier = [task.goal]
    while frontier:
        nxt = []
        for x in frontier:
            for e in EDGES:
                if x in e and usable_edge(e):
                    y = next(iter(e - {x}))
                    if y not in dist:
                        dist[y] = dist[x] + 1
                        nxt.append(y)
        frontier = nxt
    options = [n for n in sorted({x for e in EDGES for x in e if s in e and x != s})
               if usable_edge(frozenset((s, n))) and n in dist and dist[n] == dist.get(s, 99) - 1]
    return max(options, key=lambda n: p_open(frozenset((s, n))))


def correction_window(task, H, policy, w):
    """K(p, t) along a policy in world w: does the knowledge state at t still carry a robust guarantee,
    i.e. some uniform continuation from what the entity then knows reaches the goal by H in every
    consistent world? This is a robust goal-continuation predicate for this stationary finite task.
    K = 0 is a LOST GUARANTEE, not hardening: favourable information can restore it (Codex, COM #798
    6133683747). Reaching an authored goal is also not, by itself, repairing harm."""
    win, _, _ = solver(task, H)
    S = next(C for C in initial_classes(task) if w in C)
    s, t, rows = task.start, 0, []
    while True:
        rows.append((t, s, win(s, t, S)))
        if s == task.goal or t >= H:
            return rows
        a = policy(task, s, t, S)
        s2 = task.step(w, s, a)
        o = task.observe(w, s, a, s2)
        S = frozenset(v for v in S if task.step(v, s, a) == s2 and task.observe(v, s, a, s2) == o)
        s, t = s2, t + 1


def hardening_time(task, H, policy, w):
    """World-relative hardening along a policy in world w: the first t from which NO continuation at all
    (any moves, as if w were known) reaches the goal by H. Irreversible along the play, unlike K = 0.
    Returns None if the goal stays reachable (or is reached)."""
    def reachable(s, t):
        frontier = {s}
        for _ in range(H - t):
            if task.goal in frontier:
                return True
            frontier = {task.step(w, x, a) for x in frontier for a in task.moves(x)}
        return task.goal in frontier

    S = next(C for C in initial_classes(task) if w in C)
    s, t = task.start, 0
    while True:
        if s == task.goal:
            return None
        if not reachable(s, t):
            return t
        if t >= H:
            return t
        a = policy(task, s, t, S)
        s2 = task.step(w, s, a)
        o = task.observe(w, s, a, s2)
        S = frozenset(v for v in S if task.step(v, s, a) == s2 and task.observe(v, s, a, s2) == o)
        s, t = s2, t + 1


def robust_tradeoffs(task, H):
    """(worst-case arrival time, worst-case exposure) of every uniform policy that gets home in every world."""
    _, _, profiles = solver(task, H)
    S0 = initial_classes(task)
    assert len(S0) == 1
    pts = set()
    for prof in profiles(task.start, 0, S0[0]):
        d = dict(prof)
        if all(arr is not None for arr, _ in d.values()):
            pts.add((max(arr for arr, _ in d.values()), max(e for _, e in d.values())))
    return pts


def lumped_short_route():
    """A coarse model that lumps the alley and the side street into one abstract corner SHORT.
    Its street SHORT-Hm is open iff at least one short street is open, which is true in every world.
    Every fine path maps onto a coarse path (an existential abstraction), but the lumping erases the
    one distinction the walker cannot see in advance: WHICH short street is open."""
    edges = {frozenset(("S", "SHORT")), frozenset(("SHORT", "Hm"))}

    def moves(s):
        return sorted({x for e in edges for x in e if s in e and x != s}) + ["wait"]

    def step(w, s, a):
        if a == "wait":
            return s
        if frozenset((s, a)) == frozenset(("SHORT", "Hm")):
            return a if (STREET_WORLDS[w]["alley"] or STREET_WORLDS[w]["side"]) else s
        return a

    return Task(STREET_WORLDS, STREET_PRIOR, "S", "Hm", moves, step, lambda s, a, s2: 0,
                lambda w, s, a, s2: None)


# --------------------------------------------------------------------------- Example 2: two households
#
# Two households, i and j, each with 10 units. Each loses 8 with probability p = 1/4. With
# probability c a common cause hits both; otherwise each is hit independently with probability q,
# chosen so the marginal stays p:  q = (p - c) / (1 - c).  A pool splits the total loss equally.
# A floor F = 4: "each keeps at least 4" is the declared acceptable region.

W0, LOSS, P_LOSS, FLOOR = 10.0, 8.0, 0.25, 4.0


def loss_states(p=P_LOSS, c=0.0):
    q = (p - c) / (1 - c)
    both = c + (1 - c) * q * q
    one = (1 - c) * q * (1 - q)
    return {(1, 1): both, (1, 0): one, (0, 1): one, (0, 0): (1 - c) * (1 - q) ** 2}


def wealth(state, arrangement):
    li, lj = state
    if arrangement == "autarky":
        return W0 - LOSS * li, W0 - LOSS * lj
    share = LOSS * (li + lj) / 2
    return W0 - share, W0 - share


def voluntary_after_information(state):
    """Both households learn the losses, then each joins only if pooling does not leave it worse off."""
    aut, pool = wealth(state, "autarky"), wealth(state, "pool")
    joins = pool[0] >= aut[0] and pool[1] >= aut[1]
    return pool if joins else aut


def expected_joint_utility(u, rule, c=0.0):
    total = 0.0
    for state, pr in loss_states(c=c).items():
        if rule == "voluntary-after-information":
            xi, xj = voluntary_after_information(state)
        else:  # "autarky", "pool" (consent given before information), "mandate" (pool imposed after)
            xi, xj = wealth(state, "autarky" if rule == "autarky" else "pool")
        total += pr * (u(xi) + u(xj))
    return total


def surplus(u, c=0.0, rule="pool"):
    """S_ij(H; U) of draft zero: joint value under the rule minus the no-coupling baseline."""
    return expected_joint_utility(u, rule, c) - expected_joint_utility(u, "autarky", c)


def p_floor(arrangement, c=0.0, who="i"):
    """P(the named household, or 'both', keeps at least FLOOR)."""
    total = 0.0
    for state, pr in loss_states(c=c).items():
        xi, xj = wealth(state, arrangement)
        ok = {"i": xi >= FLOOR, "j": xj >= FLOOR, "both": xi >= FLOOR and xj >= FLOOR}[who]
        total += pr * ok
    return total


def redundancy_failure(p, c):
    """Draft zero's toy: two units, success needs at least one. Failure probability with common cause c."""
    return loss_states(p=p, c=c)[(1, 1)]


UTILITIES = {"sqrt (risk-averse)": math.sqrt, "log (more risk-averse)": math.log, "linear (risk-neutral)": lambda x: x}


# --------------------------------------------------------------------------- report

def report():
    print("EXAMPLE 1  WALKING HOME  (stipulated layout; priors P(alley open)=13/20, P(side open)=1/2)")
    for H in (2, 3, 4, 5):
        alone, asked = walking_home(stranger=False), walking_home()
        print("  curfew H=%d  route exists in every world: %-5s | usable whatever the world: without "
              "stranger %-5s, with %-5s | best P(home by H): without %s, with %s"
              % (H, route_exists(alone, H), usable_robust(alone, H), usable_robust(asked, H),
                 best_probability(alone, H), best_probability(asked, H)))
    t = walking_home()
    print("  optimistic replanner at H=3, per world:",
          {w: simulate(t, 3, optimistic_replanner, w)[0] for w in t.worlds}, "(arrival time; None = not home)")
    print("  correction window along the replanner, world w2, H=3:",
          [(tt, s, "K=1" if k else "K=0") for tt, s, k in correction_window(t, 3, optimistic_replanner, "w2")])
    for r in (Fr(9, 10), Fr(3, 5)):
        tr = walking_home(reliability=r)
        print("  stranger right with probability %s, H=3: usable whatever the world %s, best P %s"
              % (r, usable_robust(tr, 3), best_probability(tr, 3)))
    pts = robust_tradeoffs(t, 5)
    print("  H=5, policies home in every world: %d distinct (worst time, worst exposure) pairs; Pareto front %s"
          % (len(pts), pareto(pts)))
    full = walking_home(stranger=False, full_view=True)
    print("  full view of the world at the start: usable == exists for H=2..5:",
          [usable_robust(full, H) == route_exists(full, H) for H in (2, 3, 4, 5)])
    print("  lumped coarse model at H=2: usable %s; fine model at H=2: usable %s"
          % (usable_robust(lumped_short_route(), 2), usable_robust(walking_home(stranger=False), 2)))

    print("\nEXAMPLE 2  TWO HOUSEHOLDS  (stipulated: 10 units each, loss 8 with p=1/4, floor 4)")
    for name, u in UTILITIES.items():
        print("  %-24s S(pool, c=0)=%+.4f  S(pool, c=1/8)=%+.4f  S(pool, c=1/4)=%+.4f  "
              "S(voluntary after information, c=0)=%+.4f"
              % (name, surplus(u, 0.0), surplus(u, 0.125), surplus(u, 0.25),
                 surplus(u, 0.0, "voluntary-after-information")))
    for c in (0.0, 0.125, 0.25):
        print("  c=%.3f  P(i keeps >= 4): autarky %.4f, pool %.4f | P(both keep >= 4): autarky %.4f, pool %.4f"
              % (c, p_floor("autarky", c), p_floor("pool", c), p_floor("autarky", c, "both"),
                 p_floor("pool", c, "both")))
    print("  one-loss state: lucky household keeps %.1f voluntarily, %.1f under a mandate"
          % (voluntary_after_information((1, 0))[1], wealth((1, 0), "pool")[1]))
    print("  draft zero's redundancy toy, p=1/4: failure %.4f independent, %.4f with c=1/8, %.4f with c=1/4"
          % (redundancy_failure(0.25, 0.0), redundancy_failure(0.25, 0.125), redundancy_failure(0.25, 0.25)))


if __name__ == "__main__":
    report()
