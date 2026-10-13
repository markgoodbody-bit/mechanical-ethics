"""Fictional fixtures, not case evidence. Outcomes/permissions are stipulations."""
from dataclasses import replace
from fractions import Fraction
from navigator import Binding, Cost, Move, Scenario, State


def office(early_notice=False, mode="robust", threshold=Fraction(1)):
    states, moves = {}, {}
    for world in "AB":
        states[world] = State("office unknown", correction_until=2)
        states[world + "notice"] = State("office=" + world, correction_until=2)
        states[world + "late"] = State("receipt available after last filing opportunity", correction_until=2)
        states[world + "ok"] = State("filed", "filed", 2)
        states[world + "miss"] = State("wrong filing; no second attempt", "missed", 2)
        sends = tuple(Move("send" + destination, world + ("ok" if destination == world else "miss"), Cost(1, 1)) for destination in "AB")
        moves[world] = sends + (Move("inquire", world + ("notice" if early_notice else "late"), Cost(1 if early_notice else 2, 1)),
                               Move("delay", world + "late", Cost(2)),
                               Move("refuse", world + "miss", Cost(1)))
        moves[world + "notice"] = sends
        moves[world + "late"] = sends  # Visible information cannot buy elapsed time back.
    return Scenario("office/" + ("early" if early_notice else "late") + "/" + mode,
                    ("one filing attempt; A/B hidden", "deadline2; no appeal after wrong filing",
                     "notice costs time; delay/refusal are transitions", "prior P(A)=9/10 is STIPULATED"),
                    states, moves, ("A", "B"), 2, Cost(0, 3),
                    Binding(frozenset({"filed"}), mode, threshold), {"A": Fraction(9, 10), "B": Fraction(1, 10)})


def disputed(protection_authorised=True):
    return Scenario("disputed shared leak",
                    ("repair ownership contested", "temporary protection independently permitted, unless variant withholds it",
                     "protective deadline1; repair enquiry takes2", "temporary protection does NOT settle repair entitlement"),
                    {"start": State("leak; repair responsibility disputed", correction_until=1),
                     "protected": State("temporarily protected", "protected", 1),
                     "lost": State("protective deadline missed", "unprotected", 1)},
                    {"start": (Move("repair", "protected", Cost(1, 1), False),
                               Move("temporary_protection", "protected", Cost(1, 1), protection_authorised),
                               Move("inquire", "lost", Cost(2, 1)), Move("delay", "lost", Cost(1)),
                               Move("refuse_disputed_repair", "lost", Cost(1)))},
                    ("start",), 1, Cost(0, 1), Binding(frozenset({"protected"})))


def separation(binding="self"):
    goals = {"self": frozenset({"safe_separate"}), "capacity": frozenset({"joint_capacity"})}
    return Scenario("changing coupling/" + str(binding),
                    ("shared service now imposes unwanted control", "leave costs effort3; stay effort1",
                     "joint capacity preserved by staying; personal autonomy by leaving",
                     "no preferences inferred from coupling or capacity"),
                    {"start": State("coupling terms changed", correction_until=1),
                     "stay": State("capacity maintained under unwanted control", "joint_capacity", 0),
                     "leave": State("separate and safe", "safe_separate", 2),
                     "wait": State("control now locked in", "locked", 0)},
                    {"start": (Move("stay", "stay", Cost(1, 1, imposed=4)),
                               Move("separate", "leave", Cost(1, 3)),
                               Move("delay", "wait", Cost(1)), Move("refuse", "leave", Cost(1, 3)))},
                    ("start",), 2, Cost(0, 5, imposed=5),
                    Binding(goals[binding]) if binding is not None else None)


def low_reserve(enough=False, known_protection=True):
    states = {"start": State("problem; safe interim action known", correction_until=1),
              "mapped": State("alternatives mapped", correction_until=1),
              "safe": State("interim harm prevented", "protected", 1),
              "lost": State("protection too late", "unprotected", 1)}
    # Even ample money cannot restore an elapsed protective window.
    first = [Move("inquire", "mapped", Cost(2, 3)), Move("delay", "lost", Cost(1)),
             Move("refuse", "lost", Cost(1))]
    if known_protection:
        first.append(Move("known_interim_protection", "safe", Cost(1, 1)))
    return Scenario("low reserves/" + str((enough, known_protection)),
                    ("protective deadline1; mapping costs2 time/3 effort", "person has effort1 unless ample variant",
                     "ordinary comparator: take already-known interim protection", "no measured advantage over comparator"),
                    states, {"start": tuple(first), "mapped": (Move("protect_after_mapping", "lost", Cost(1, 1)),)},
                    ("start",), 3 if enough else 1, Cost(0, 4 if enough else 1), Binding(frozenset({"protected"})))


def friends(consent=True, shared_error=False):
    states, moves = {}, {}
    for world in "AB":
        states[world] = State("route unknown", correction_until=2)
        answer = ("B" if world == "A" else "A") if shared_error else world
        states[world + "hint"] = State("voluntary hint=" + answer, correction_until=2)
        states[world + "solo"] = State("own map=" + world, correction_until=2)
        states[world + "ok"] = State("arrived before closing", "arrived", 2)
        states[world + "miss"] = State("late or wrong route", "missed", 0)
        moves[world] = (Move("ask_friend", world + "hint", Cost(1, 1, imposed=1), consent),
                        Move("check_own_map", world + "solo", Cost(2, 2)),
                        Move("delay", world + "miss", Cost(1)), Move("refuse", world + "miss", Cost(1)))
        # The hint is fallible data, not an instruction or oracle.
        for suffix in ("hint", "solo"):
            moves[world + suffix] = tuple(Move("take" + destination, world + ("ok" if destination == world else "miss"), Cost(1, 1)) for destination in "AB")
    return Scenario("fictional two friends/" + str((consent, shared_error)),
                    ("both friends voluntarily permit one brief question, only in consent variant",
                     "friend knows route in base fixture; participant cost1 explicitly counted",
                     "own lookup2 then travel1 misses horizon2", "no welfare or identity inferred"),
                    states, moves, ("A", "B"), 2, Cost(0, 3, imposed=1), Binding(frozenset({"arrived"})))


def suite():
    return (office(), office(True), office(False, "probability", Fraction(85, 100)),
            office(False, "probability", Fraction(95, 100)), disputed(), disputed(False),
            separation(), separation("capacity"), separation(None), low_reserve(),
            low_reserve(True), low_reserve(False, False), friends(), friends(False))


if __name__ == "__main__":
    from navigator import analyse, trace
    print("SOURCE-ONLY FIXTURES: not field efficacy, a moral oracle, or new mathematics.\n")
    for case in suite():
        print(trace(analyse(case)) + "\n")
