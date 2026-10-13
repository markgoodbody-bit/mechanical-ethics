"""ME v0.9 kernel lab: deterministic, deliberately tiny trace witness.
No ethical optimizer, empirical prediction, or simulated consciousness.
All states, actions, observations, permission ports and exogenous changes are authored.
"""
from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class Rule:
    actor: str
    move: str
    requires: tuple[tuple[str, int], ...] = ()
    delta: tuple[tuple[str, int], ...] = ()
    permitted: bool = True


@dataclass(frozen=True)
class Scenario:
    name: str
    actors: tuple[str, ...]
    initial: tuple[tuple[str, int], ...]
    visible: tuple[tuple[str, tuple[str, ...]], ...]
    rules: tuple[Rule, ...]
    shocks: tuple[tuple[tuple[str, int], ...], ...]
    claims: tuple[str, ...] = ()


def _change(values: dict[str, int], deltas: tuple[tuple[str, int], ...]) -> None:
    for key, amount in deltas:
        if key not in values:
            raise KeyError(f"unknown variable: {key}")
        values[key] += amount


def view(scene: Scenario, world: Mapping[str, int], actor: str) -> dict[str, int]:
    if actor not in scene.actors:
        raise ValueError("unidentified actor")
    keys = dict(scene.visible)[actor]
    return {key: world[key] for key in keys}


def tick(scene: Scenario, world: Mapping[str, int], t: int,
         actions: Mapping[str, str]) -> dict:
    """External tick occurs even when everybody selects null; then resolved joint moves.

    Pre-action views are the only facts for observation-bound policy choice.
    Rules can test hidden facts as part of the *modelled world mechanism*; actors
    are not thereby entitled to see them. This is an execution engine, not a solver.
    """
    if t < 0 or t >= len(scene.shocks):
        raise IndexError("outside authored horizon")
    if set(actions) != set(scene.actors):
        raise ValueError("one move per actor required, including null")
    if not set(world) == dict(scene.initial).keys():
        raise ValueError("world schema differs from initial contract")
    seen = {actor: view(scene, world, actor) for actor in scene.actors}
    after = dict(world)
    _change(after, scene.shocks[t])
    impacts = []
    for actor in scene.actors:
        move = actions[actor]
        if move == "null":
            impacts.append((actor, move, "NO_DIRECT_ACT;_WORLD_STILL_CHANGED"))
            continue
        matches = [r for r in scene.rules if r.actor == actor and r.move == move
                   and all(after[k] == v for k, v in r.requires)]
        if len(matches) != 1:
            raise ValueError(f"move has {len(matches)} matching rules: {actor}/{move}")
        if not matches[0].permitted:
            raise PermissionError(f"modelled permission denied: {actor}/{move}")
        _change(after, matches[0].delta)
        impacts.append((actor, move, "MODELLED_EFFECT_ONLY"))
    return {"case": scene.name, "t": t, "before": dict(world), "views": seen,
            "external": dict(scene.shocks[t]), "actions": dict(actions),
            "impacts": impacts, "after": after}


def trace(scene: Scenario, moves: tuple[Mapping[str, str], ...]) -> list[dict]:
    state = dict(scene.initial)
    if len(moves) > len(scene.shocks):
        raise ValueError("more moves than authored exogenous clocks")
    result = []
    for t, chosen in enumerate(moves):
        event = tick(scene, state, t, chosen)
        result.append(event)
        state = event["after"]
    return result


# A named set of *synthetic* worlds. Numerical values are stipulations, not measurements.
def case(name: str, variant: int = 0) -> Scenario:
    if name == "raft":
        return Scenario(name, ("traveller",),
            (("distance", 0), ("energy", 4), ("repair_skill", 0), ("landing", 1)),
            (("traveller", ("distance", "energy", "landing")),),
            (Rule("traveller", "dock", (("landing", 1),), (("energy", -2), ("repair_skill", 1))),
             Rule("traveller", "smooth", (), (("energy", 0),))),
            ((("distance", 1),), (("distance", 1), ("landing", -1))),
            ("Immediate effort is not long-horizon value",))
    if name == "betsy":
        if variant not in (0, 1):
            raise ValueError("two synthetic possible recipient histories only")
        return Scenario(name, ("person",),
            (("sensitivity", variant), ("distress", 0), ("careful", 0)),
            (("person", ("distress", "careful")),),
            (Rule("person", "block", (("sensitivity", 0),), (("distress", 1),)),
             Rule("person", "block", (("sensitivity", 1),), (("distress", 4),)),
             Rule("person", "adjust", (), (("careful", 1),))),
            ((), ()), ("Unseen history is not a diagnosis",))
    if name == "workshop":
        return Scenario(name, ("learner", "mentor"),
            (("cash", 3), ("skill", 0), ("shared_skill", 0), ("permission", 1)),
            (("learner", ("cash", "skill")), ("mentor", ("skill", "permission"))),
            (Rule("learner", "practice", (), (("cash", -1), ("skill", 1))),
             Rule("mentor", "teach", (("skill", 1), ("permission", 1)), (("shared_skill", 1),))),
            ((), ()), ("Ability acquired is not proof of cooperation's goodness",))
    if name == "remedy":
        return Scenario(name, ("tenant", "owner"),
            (("exposure", 0), ("file", 0), ("repair", 0), ("residue", 0)),
            (("tenant", ("exposure", "file")), ("owner", ("file", "repair"))),
            (Rule("tenant", "report", (), (("file", 1),)),
             Rule("owner", "repair", (), (("repair", 1),))),
            ((("exposure", 1), ("residue", 1)), (("exposure", 1), ("residue", 1))),
            ("Record movement cannot undo accumulated damage",))
    if name == "closure":
        return Scenario(name, ("operator", "neighbor"),
            (("open_routes", 3), ("operator_gain", 0), ("neighbor_loss", 0), ("barrier", 0)),
            (("operator", ("open_routes", "operator_gain")), ("neighbor", ("open_routes", "neighbor_loss"))),
            (Rule("operator", "close_unsafe", (), (("open_routes", -1), ("barrier", 1))),
             Rule("operator", "extract", (), (("operator_gain", 3), ("neighbor_loss", 4))),
             Rule("operator", "seize", (), (("operator_gain", 5),), False)),
            ((),), ("More routes/wealth for one actor is not an ethical ranking",))
    if name == "stale":
        return Scenario(name, ("reader",),
            (("source_value", 1), ("cached_value", 1), ("check_count", 0)),
            (("reader", ("cached_value", "check_count")),),
            (Rule("reader", "refresh", (("source_value", 0),), (("cached_value", -1), ("check_count", 1))),
             Rule("reader", "refresh", (("source_value", 1),), (("check_count", 1),))),
            ((("source_value", -1),),),
            ("Source valid at t0 may be false at t1; observation time matters",))
    raise KeyError(name)


CASES = ("raft", "betsy", "workshop", "remedy", "closure", "stale")
