"""Five invented, bounded cases. No empirical recipients or psychological facts."""
from research.navigator_toy.navigator import Cost
from .engine import Edge, Entity, Game, Node


def entities(skill=(), burden=0, other="B"):
    return (Entity("A", tuple(skill)), Entity(other, (), burden))


def edge(action, target, effort=0, imposed=0, change="No chosen intervention", authority="ALLOWED"):
    return Edge(action, target, Cost(1, effort, 0, imposed),
                "One model tick passes; the authored environment evolves", change, authority)


def make(name, nodes, edges, starts, goals, disagreement, horizon=3):
    return Game(name, "A", (
        "All entities, transitions, costs and observation partitions below are imaginary inputs.",
        "No probability distribution, factual psychology, welfare forecast or universal optimum is asserted.",
        "Clock advances on null and intervention alike; spent cost is observable to A.",
    ), ("Authored Project C fixture", "Reuses navigator PR55 observation-policy enumeration"),
        disagreement, nodes, edges, starts, goals, next(iter(goals)), horizon)


def raft():
    ns = {
        "river": Node(0, "River rising; A sees both rafts", entities()),
        "drift": Node(1, "B now beyond A's reach", entities(burden=2), correction_until=0),
        "trained": Node(1, "A can tow; B still reachable", entities(("tow",)), correction_until=1),
        "alone": Node(2, "A lands; B drifts", entities(burden=5), "A_ONLY", 0),
        "trained_alone": Node(2, "A lands; B drifts", entities(("tow",), burden=5), "A_ONLY", 0),
        "together": Node(2, "Both land", entities(("tow",)), "BOTH", 1),
    }
    return make("raft", ns, {
        "river": (edge("wait", "drift"), edge("learn", "trained", 2, change="A forms towing capability")),
        "drift": (edge("land", "alone", 1, change="A lands alone"),),
        "trained": (edge("land", "trained_alone", 1, change="A leaves without towing"),
                    edge("tow", "together", 3, change="A tows B under stipulated consent")),
    }, ("river",), {"both": ("BOTH",), "self": ("A_ONLY", "BOTH")},
        "Self landing versus joint protection; consent to tow is an authored input.", 2)


def workshop():
    ns = {
        "sat": Node(0, "Saturday; workshop open", entities()),
        "idle": Node(1, "Workshop closed; tool still broken", entities()),
        "learnt": Node(1, "Workshop closed; A can repair", entities(("repair",))),
        "lost": Node(2, "Tool unavailable", entities(burden=2), "UNAVAILABLE"),
        "skilled_lost": Node(2, "Tool unavailable", entities(("repair",), burden=2), "UNAVAILABLE"),
        "repaired": Node(2, "Tool repaired", entities(("repair",)), "AVAILABLE"),
    }
    return make("workshop", ns, {
        "sat": (edge("wait", "idle"), edge("learn", "learnt", 2, change="A acquires repair skill")),
        "idle": (edge("wait", "lost"),),
        "learnt": (edge("wait", "skilled_lost"), edge("repair", "repaired", 1, change="Repair skill enables new action")),
    }, ("sat",), {"working_tool": ("AVAILABLE",)}, "Learning has a present effort cost and a stipulated later benefit.", 2)


def betsy():
    ns, es = {}, {}
    for world, welcome in (("welcome", True), ("unwanted", False)):
        ns[world] = Node(0, "Betsy receives the same proposed gesture; preference unknown", entities(other="Betsy"))
        ns[world + "_asked"] = Node(1, "Betsy says " + ("yes" if welcome else "no"), entities(other="Betsy"), correction_until=2)
        for action in ("gesture", "leave"):
            acceptable = welcome if action == "gesture" else not welcome
            end = world + "_" + action
            ns[end] = Node(2, "Interaction ended", entities(burden=0 if acceptable else 2, other="Betsy"),
                           "RESPECTED" if acceptable else "MISMATCH", 2)
        es[world] = (edge("ask", world + "_asked", 1, change="Preference becomes observable"),)
        es[world + "_asked"] = (edge("gesture", world + "_gesture", change="Gesture offered"),
                                 edge("leave", world + "_leave", change="Gesture withheld"))
        # Immediate choices terminate at tick 1, with indistinguishable outcomes to
        # the actor. Full outcomes remain an auditor's interpretation, not a report.
        for action in ("gesture", "leave"):
            end = world + "_immediate_" + action
            ns[end] = Node(1, "Interaction ended", ns[world + "_" + action].entities,
                           ns[world + "_" + action].outcome, 1)
            es[world] += (edge(action, end, change="Act before asking"),)
    return make("betsy", ns, es, ("welcome", "unwanted"), {"respect_preference": ("RESPECTED",)},
                "Preferences and willingness to answer are stipulated alternatives, not diagnoses or consent inferred from silence.", 2)


def construction():
    ns = {
        "start": Node(0, "Two builders and a neighbour; shared access unresolved", entities(other="Neighbour")),
        "shortcut": Node(1, "A has access; neighbour carries obstruction", entities(("access",), 4, "Neighbour"), "SELF_ACCESS"),
        "shared": Node(1, "A and B built together; neighbour has temporary noise", entities(("shared_access",), 1, "Neighbour")),
        "lasting": Node(2, "Shared access persists; temporary noise ends", entities(("shared_access",), 0, "Neighbour"), "SHARED_ACCESS"),
    }
    # B's capability is explicit rather than disappearing into an aggregate.
    ns = {key: Node(n.clock, n.observation, n.entities + (Entity("B", ("access",) if key in {"shared", "lasting"} else ()),),
                    n.outcome, n.correction_until) for key, n in ns.items()}
    return make("construction", ns, {
        "start": (edge("shortcut", "shortcut", 1, 4, "A takes access; burdens neighbour"),
                  edge("cooperate", "shared", 3, 1, "A and B build access; neighbour bears noise"),
                  edge("commandeer", "shared", 1, 1, "Proposed unauthorised use", "CONTESTED")),
        "shared": (edge("finish", "lasting", 1, change="Joint construction completes"),),
    }, ("start",), {"shared": ("SHARED_ACCESS",), "self": ("SELF_ACCESS", "SHARED_ACCESS")},
        "Joint access is not automatically good: neighbour's burden and disputed land authority remain visible.", 2)


def inheritance():
    ns, es = {}, {}
    for world, door in (("accurate", "left"), ("stale", "right")):
        ns[world] = Node(0, "Inherited note says LEFT; freshness UNKNOWN", entities(), inheritance="UNTRUSTED: take left")
        ns[world + "_checked"] = Node(1, "Current sign says " + door, entities(), correction_until=2,
                                      inheritance="Old note retained; current observation separated")
        es[world] = (edge("check", world + "_checked", 1, change="Read current bounded sign"),)
        for side in ("left", "right"):
            good = side == door
            end = world + "_" + side
            ns[end] = Node(2, "Journey ended", entities(burden=0 if good else 3), "ARRIVED" if good else "LOST", 1)
            es[world + "_checked"] = es.get(world + "_checked", ()) + (edge(side, end, change="Choose route after check"),)
            immediate = world + "_now_" + side
            ns[immediate] = Node(1, "Journey ended", ns[end].entities, ns[end].outcome, 0)
            es[world] += (edge(side, immediate, change="Choose route from unverified inheritance"),)
    return make("inheritance", ns, es, ("accurate", "stale"), {"arrival": ("ARRIVED",)},
                "A note's confidence gives no authority or freshness; represented current signs are assumed reliable.", 2)


FACTORIES = {f.__name__: f for f in (raft, workshop, betsy, construction, inheritance)}
