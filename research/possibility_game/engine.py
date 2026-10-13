"""Offline finite scenario explorer. Authored worlds are not observed futures."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from pathlib import Path
import platform

from research.navigator_toy.navigator import (
    Binding, Cost, Frame, Move, Scenario, State, analyse, observation_key,
    permitted, replay, route_exists_per_world,
)


@dataclass(frozen=True)
class Entity:
    name: str
    capability: tuple[str, ...] = ()
    burden: int = 0


@dataclass(frozen=True)
class Node:
    clock: int
    observation: str
    entities: tuple[Entity, ...]
    outcome: str | None = None
    correction_until: int | None = None
    inheritance: str = ""


@dataclass(frozen=True)
class Edge:
    action: str
    target: str
    cost: Cost
    exogenous: str
    change: str
    authority: str = "ALLOWED"


@dataclass(frozen=True)
class Game:
    name: str
    actor: str
    assumptions: tuple[str, ...]
    provenance: tuple[str, ...]
    disagreement: str
    nodes: dict[str, Node]
    edges: dict[str, tuple[Edge, ...]]
    starts: tuple[str, ...]
    goals: dict[str, tuple[str, ...]]
    default_goal: str
    horizon: int
    budget: Cost = Cost(8, 20, 20, 20)

    def __post_init__(self):
        if self.default_goal not in self.goals:
            raise ValueError("Missing authored default goal")
        if len(self.nodes) > 40 or len(self.starts) > 4:
            raise ValueError("Finite explorer capacity exceeded")
        if any(self.nodes[s].clock != 0 for s in self.starts):
            raise ValueError("Initial model clock must be zero")
        roster = {e.name for e in self.nodes[self.starts[0]].entities}
        for node in self.nodes.values():
            names = [e.name for e in node.entities]
            if self.actor not in names or len(set(names)) != len(names) or set(names) != roster:
                raise ValueError("Preserve the independently declared entity roster")
            if any(type(e.burden) is not int or e.burden < 0 for e in node.entities):
                raise ValueError("Burden must be a declared nonnegative integer")
        for source, edges in self.edges.items():
            for edge in edges:
                if edge.authority not in {"ALLOWED", "WITHHELD", "CONTESTED"}:
                    raise ValueError("Unknown authority port")
                if self.nodes[edge.target].clock != self.nodes[source].clock + edge.cost.time:
                    raise ValueError("Every transition, including null, must advance the clock")
                if not edge.exogenous or not edge.change:
                    raise ValueError("Declare exogenous and action-dependent changes separately")
        self.project()

    def project(self, goal=None, horizon=None):
        goal = self.default_goal if goal is None else goal
        if goal not in self.goals:
            raise ValueError("Unknown authored goal")
        return Scenario(
            self.name, self.assumptions,
            {key: State(n.observation, n.outcome, n.correction_until)
             for key, n in self.nodes.items()},
            {key: tuple(Move(e.action, e.target, e.cost, e.authority == "ALLOWED")
                        for e in edges) for key, edges in self.edges.items()},
            self.starts, self.horizon if horizon is None else horizon, self.budget,
            Binding(frozenset(self.goals[goal])),
        )

    def digest(self):
        return digest(asdict(self))


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def baseline():
    """Observe only this package and its reused solver, never credentials or services."""
    root = Path(__file__).resolve().parent
    files = [root / "engine.py", root / "scenarios.py", root.parent / "navigator_toy" / "navigator.py"]
    return {"status": "OBSERVED_LOCAL_SOURCE_AND_RUNTIME",
            "python": platform.python_version(), "system": platform.system(),
            "sources": {p.name: sha256(p.read_bytes()).hexdigest() for p in files},
            "future_worlds": "STIPULATED_NOT_OBSERVED", "network_requests": 0}


def policies(game, goal=None, horizon=None):
    scenario = game.project(goal, horizon)
    report = analyse(scenario)
    def costs(policy):
        return tuple(max(getattr(f.cost, d) for f in policy.ends)
                     for d in ("effort", "money", "imposed", "time"))
    def options(policy):
        # An auditor ranks complete observation-consistent policies over ALL initial
        # worlds. This never gives the actor an actual-world identifier.
        return min(sum(e.authority == "ALLOWED" for e in game.edges.get(f.state, ()))
                   + len(next(x for x in game.nodes[f.state].entities if x.name == game.actor).capability)
                   for f in policy.ends)
    cheap = min(report.policies, key=lambda p: (costs(p), p.decisions))
    option = min(report.policies, key=lambda p: (-options(p), costs(p), p.decisions))
    return scenario, report, {"cheap": cheap, "goal": report.selected, "options": option}


def run(game, origin, actions, goal=None, horizon=None):
    """Manual branch is an auditor experiment, not an observation-usable policy."""
    scenario = game.project(goal, horizon)
    if origin not in game.starts:
        raise ValueError("Origin must be a represented initial world")
    frame = Frame(origin, origin)
    steps = []
    for action in actions:
        node = game.nodes[frame.state]
        if node.outcome is not None:
            raise ValueError("Cannot act after a terminal outcome")
        edge = next((e for e in game.edges.get(frame.state, ()) if e.action == action), None)
        if edge is None:
            raise ValueError("Action unavailable in this represented state")
        move = Move(action, edge.target, edge.cost, edge.authority == "ALLOWED")
        reason = permitted(scenario, frame, move)
        if reason:
            raise ValueError(reason)
        before = asdict(node)
        after = asdict(game.nodes[edge.target])
        cost = frame.cost.plus(edge.cost)
        steps.append({"from": frame.state, "to": edge.target, "action": action,
                      "before": before, "after": after, "cost": cost.vector(),
                      "exogenous": edge.exogenous, "action_change": edge.change,
                      "authority": edge.authority})
        key = observation_key(scenario, frame)
        frame = Frame(origin, edge.target, cost, key + (action,), frame.path + (action,))
    journal = {"game": game.name, "model_sha256": game.digest(), "origin": origin,
               "goal": goal or game.default_goal, "horizon": scenario.horizon,
               "authored_inputs": {"actor": game.actor, "assumptions": game.assumptions,
                                   "provenance": game.provenance, "disagreement": game.disagreement,
                                   "acceptable_outcomes": sorted(scenario.binding.acceptable_outcomes),
                                   "rank_order": scenario.binding.rank_order, "budget": game.budget.vector()},
               "evidence": "STIPULATED_SIMULATION", "initial": asdict(game.nodes[origin]),
               "steps": steps, "final": frame.state, "cost": frame.cost.vector(),
               "outcome": game.nodes[frame.state].outcome}
    # Canonical JSON representation also makes saved and in-memory journals equal.
    journal = json.loads(json.dumps(journal))
    return dict(journal, receipt_sha256=digest(journal))


def verify(game, journal):
    clean = {k: v for k, v in journal.items() if k != "receipt_sha256"}
    if digest(clean) != journal.get("receipt_sha256"):
        raise ValueError("Journal digest mismatch (integrity only, not authentication)")
    expected = run(game, journal["origin"], [s["action"] for s in journal["steps"]],
                   journal["goal"], journal["horizon"])
    if expected != journal:
        raise ValueError("Journal does not replay against this exact model")
    return True


def branch(game, journal, at, actions, goal=None):
    verify(game, journal)
    if type(at) is not int or not 0 <= at <= len(journal["steps"]):
        raise ValueError("Branch point outside history")
    prefix = [s["action"] for s in journal["steps"][:at]]
    changed = run(game, journal["origin"], prefix + list(actions), goal or journal["goal"], journal["horizon"])
    return {"original": journal, "counterfactual": changed, "branch_at": at,
            "claim": "CONDITIONAL_ON_SAME_AUTHORED_MODEL_NOT_CAUSAL_WORLD_EVIDENCE"}


def explore(game, goal=None, horizon=None):
    scenario, report, choices = policies(game, goal, horizon)
    comparisons = {}
    for label, policy in choices.items():
        if policy is None:
            comparisons[label] = {"status": "NO_POLICY_MEETS_AUTHORED_GOAL"}
            continue
        comparisons[label] = {
            "decisions": [{"observation_history": key, "action": action} for key, action in policy.decisions],
            "audit_worlds": [{"origin": f.origin, "path": f.path, "outcome": game.nodes[f.state].outcome,
                              "cost": f.cost.vector(), "stopped": f.stopped,
                              "entities": [asdict(e) for e in game.nodes[f.state].entities],
                              "correction_until": game.nodes[f.state].correction_until}
                             for f in replay(scenario, policy)]}
    return {"scenario": game.name, "model_sha256": game.digest(), "actor": game.actor,
            "evidence": "STIPULATED_SIMULATION", "assumptions": game.assumptions,
            "provenance": game.provenance, "disagreement": game.disagreement,
            "goal": goal or game.default_goal, "goals": game.goals, "horizon": scenario.horizon,
            "status": report.status, "policy_count": len(report.policies),
            "per_world_route_oracle_only": route_exists_per_world(scenario),
            "rejected": sorted(report.rejected_moves), "comparisons": comparisons}
