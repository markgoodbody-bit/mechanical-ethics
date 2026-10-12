"""Finite, deterministic observation-policy enumeration; no network or inference.

Hidden-state names are available to the auditor, NEVER policy decision keys.
All goals, resource limits and permission labels are fixture-authored inputs.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from itertools import product
from typing import Mapping


@dataclass(frozen=True)
class Cost:
    time: int = 0
    effort: int = 0
    money: int = 0
    imposed: int = 0

    def __post_init__(self):
        if any(type(v) is not int or v < 0 for v in self.vector()):
            raise ValueError("Costs must be nonnegative integers")

    def vector(self):
        return (self.time, self.effort, self.money, self.imposed)

    def plus(self, other: Cost) -> Cost:
        return Cost(*(a + b for a, b in zip(self.vector(), other.vector())))


@dataclass(frozen=True)
class State:
    observation: str
    outcome: str | None = None
    correction_until: int | None = None


@dataclass(frozen=True)
class Move:
    action: str
    target: str
    cost: Cost
    authorised: bool = True


@dataclass(frozen=True)
class Binding:
    """An authored acceptability rule, not a computed moral judgement.

Rank only acceptable policies by worst-case (time, effort, money, imposed).
This ordering is intentionally explicit and replaceable, NOT ethical utility.
"""
    acceptable_outcomes: frozenset[str]
    mode: str = "robust"
    threshold: Fraction = Fraction(1)
    rank_order: tuple[str, ...] = ("time", "effort", "money", "imposed")

    def __post_init__(self):
        if self.mode not in ("robust", "probability"):
            raise ValueError("Unknown acceptability mode")
        if not 0 <= self.threshold <= 1:
            raise ValueError("Threshold outside [0,1]")
        if set(self.rank_order) != {"time", "effort", "money", "imposed"} or len(self.rank_order) != 4:
            raise ValueError("Declare each cost dimension exactly once")


@dataclass(frozen=True)
class Scenario:
    name: str
    assumptions: tuple[str, ...]
    states: Mapping[str, State]
    moves: Mapping[str, tuple[Move, ...]]
    starts: tuple[str, ...]
    horizon: int
    budget: Cost
    binding: Binding | None
    prior: Mapping[str, Fraction] | None = None

    def __post_init__(self):
        if type(self.horizon) is not int or not 0 <= self.horizon <= 8:
            raise ValueError("Toy horizon must be 0..8")
        if not self.starts or len(set(self.starts)) != len(self.starts):
            raise ValueError("Unique initial represented worlds required")
        if any(s not in self.states for s in self.starts):
            raise ValueError("Unknown initial state")
        for source, moves in self.moves.items():
            if source not in self.states or self.states[source].outcome is not None:
                raise ValueError("Only nonterminal states have moves")
            if len({m.action for m in moves}) != len(moves):
                raise ValueError("One deterministic transition per action/state")
            for move in moves:
                if move.target not in self.states or move.cost.time <= 0:
                    raise ValueError("Targets must exist and moves advance time")
        terminal_by_observation = {}
        for state in self.states.values():
            terminal = state.outcome is not None
            if state.observation in terminal_by_observation and terminal_by_observation[state.observation] != terminal:
                raise ValueError("Terminal visibility cannot differ under one observation")
            terminal_by_observation[state.observation] = terminal
        if self.prior is not None:
            if set(self.prior) != set(self.starts) or any(v < 0 for v in self.prior.values()) or sum(self.prior.values()) != 1:
                raise ValueError("Prior must cover represented initial worlds and sum to 1")


@dataclass(frozen=True)
class Frame:
    origin: str
    state: str
    cost: Cost = Cost()
    history: tuple[str, ...] = ()
    path: tuple[str, ...] = ()
    stopped: str | None = None


@dataclass(frozen=True)
class Policy:
    # Keys are observation/action histories, never hidden-state IDs.
    decisions: tuple[tuple[tuple[str, ...], str], ...] = ()
    ends: tuple[Frame, ...] = ()


@dataclass
class Report:
    status: str
    scenario: Scenario
    policies: list[Policy] = field(default_factory=list)
    accepted: list[Policy] = field(default_factory=list)
    selected: Policy | None = None
    rejected_moves: set[str] = field(default_factory=set)


def observation_key(scenario: Scenario, frame: Frame) -> tuple[str, ...]:
    # Spent resources and elapsed time are assumed observable in these fixtures.
    return frame.history + (scenario.states[frame.state].observation,
                            "spent=" + str(frame.cost.vector()))


def permitted(scenario: Scenario, frame: Frame, move: Move) -> str | None:
    if not move.authorised:
        return "AUTHORITY_WITHHELD"
    cost = frame.cost.plus(move.cost)
    if cost.time > scenario.horizon:
        return "HORIZON_EXCEEDED"
    if any(v > limit for v, limit in zip(cost.vector()[1:], scenario.budget.vector()[1:])):
        return "RESOURCE_EXCEEDED"
    return None


def enumerate_policies(scenario: Scenario, rejected: set[str]) -> list[Policy]:
    def solve(frames: tuple[Frame, ...]) -> list[Policy]:
        terminal = tuple(f for f in frames if scenario.states[f.state].outcome is not None)
        active = tuple(f for f in frames if scenario.states[f.state].outcome is None)
        if not active:
            return [Policy(ends=terminal)]
        groups: dict[tuple[str, ...], list[Frame]] = {}
        for frame in active:
            groups.setdefault(observation_key(scenario, frame), []).append(frame)
        choices = []
        for key, group in sorted(groups.items()):
            available = []
            for frame in group:
                usable = {}
                for move in scenario.moves.get(frame.state, ()):
                    reason = permitted(scenario, frame, move)
                    if reason:
                        rejected.add(f"{frame.state}/{move.action}: {reason}")
                    else:
                        usable[move.action] = move
                available.append(usable)
            # A policy cannot condition on a hidden permission/world fact.
            common = set(available[0]).intersection(*(set(a) for a in available[1:]))
            alternatives = []
            for action in sorted(common):
                advanced = tuple(Frame(f.origin, a[action].target,
                                       f.cost.plus(a[action].cost), key + (action,),
                                       f.path + (action,)) for f, a in zip(group, available))
                for continuation in solve(advanced):
                    alternatives.append(Policy(((key, action),) + continuation.decisions,
                                               continuation.ends))
            if not alternatives:
                alternatives = [Policy(((key, "STOP"),), tuple(
                    Frame(f.origin, f.state, f.cost, f.history, f.path,
                          "NO_COMMON_AUTHORISED_RESOURCE_FEASIBLE_MOVE") for f in group))]
            choices.append(alternatives)
        combined = []
        for combination in product(*choices):
            combined.append(Policy(tuple(d for p in combination for d in p.decisions),
                                   terminal + tuple(f for p in combination for f in p.ends)))
        return combined
    return solve(tuple(Frame(s, s) for s in scenario.starts))


def success(scenario: Scenario, frame: Frame) -> bool:
    return frame.stopped is None and scenario.states[frame.state].outcome in scenario.binding.acceptable_outcomes


def probability(scenario: Scenario, policy: Policy) -> Fraction:
    if scenario.prior is None:
        raise ValueError("A probability statement requires an authored prior")
    return sum((scenario.prior[f.origin] for f in policy.ends if success(scenario, f)), Fraction(0))


def analyse(scenario: Scenario) -> Report:
    report = Report("UNKNOWN_VALUE_BINDING", scenario)
    if scenario.binding is None:
        return report  # Do not quietly substitute the author's preferred goal.
    if scenario.binding.mode == "probability" and scenario.prior is None:
        report.status = "UNKNOWN_PRIOR"
        return report
    report.policies = enumerate_policies(scenario, report.rejected_moves)
    for policy in report.policies:
        accepted = (all(success(scenario, f) for f in policy.ends)
                    if scenario.binding.mode == "robust"
                    else probability(scenario, policy) >= scenario.binding.threshold)
        if accepted:
            report.accepted.append(policy)
    if report.accepted:
        def rank(policy):
            vector = tuple(max(getattr(f.cost, dimension) for f in policy.ends)
                           for dimension in scenario.binding.rank_order)
            return vector, policy.decisions
        report.selected = min(report.accepted, key=rank)
        report.status = "REPRESENTED_POLICY_FOUND"
    else:
        report.status = "STOP_NO_POLICY_MEETS_BINDING"
    return report


def route_exists_per_world(scenario: Scenario) -> bool | None:
    """Auditor's forall-world exists-route, explicitly NOT a usable policy."""
    if scenario.binding is None:
        return None
    return all(any(success(scenario, f) for p in enumerate_policies(
        Scenario(scenario.name, scenario.assumptions, scenario.states, scenario.moves,
                 (start,), scenario.horizon, scenario.budget, scenario.binding), set())
                   for f in p.ends) for start in scenario.starts)


def replay(scenario: Scenario, policy: Policy) -> tuple[Frame, ...]:
    """Apply a FROZEN policy to a second model; do not re-plan using its secrets.

An unseen observation gives STOP/UNKNOWN. Useful for counter-model challenge,
not a real-world test or claim that all possible model errors are represented.
"""
    decisions = dict(policy.decisions)
    ends = []
    for origin in scenario.starts:
        frame = Frame(origin, origin)
        while scenario.states[frame.state].outcome is None:
            key = observation_key(scenario, frame)
            action = decisions.get(key)
            options = {m.action: m for m in scenario.moves.get(frame.state, ())}
            if action not in options:
                frame = Frame(origin, frame.state, frame.cost, frame.history, frame.path,
                              "UNSEEN_OBSERVATION_OR_NO_DECISION")
                break
            move = options[action]
            reason = permitted(scenario, frame, move)
            if reason:
                frame = Frame(origin, frame.state, frame.cost, frame.history, frame.path, reason)
                break
            frame = Frame(origin, move.target, frame.cost.plus(move.cost),
                          key + (action,), frame.path + (action,))
        ends.append(frame)
    return tuple(ends)


def trace(report: Report) -> str:
    s = report.scenario
    lines = [s.name, "  status: " + report.status,
             "  assumptions: " + " | ".join(s.assumptions),
             f"  horizon={s.horizon}; effort/money/imposition limits={s.budget.vector()[1:]}",
             "  authored binding: " + repr(s.binding),
             "  represented worlds: " + ", ".join(s.starts),
             f"  policies enumerated={len(report.policies)}; acceptable={len(report.accepted)}",
             "  per-world route exists (oracle audit only): " + str(route_exists_per_world(s))]
    # Show all represented accessible terminal paths, not only the chosen route.
    paths = sorted({(f.origin, f.path, s.states[f.state].outcome, f.cost.vector(), f.stopped)
                    for p in report.policies for f in p.ends}, key=repr)
    for path in paths:
        lines.append("  accessible path: " + repr(path))
    if report.selected:
        for key, action in report.selected.decisions:
            lines.append(f"  policy[{key!r}] -> {action}")
        for f in report.selected.ends:
            state = s.states[f.state]
            lines.append(f"  audit world={f.origin}: {f.path} -> {state.outcome}; cost={f.cost.vector()}; "
                         f"correction_until={state.correction_until}; reached_at={f.cost.time}")
        if s.prior is not None:
            lines.append("  stipulated success probability=" + str(probability(s, report.selected)))
    for reason in sorted(report.rejected_moves):
        lines.append("  excluded: " + reason)
    return "\n".join(lines)
