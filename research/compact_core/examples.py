"""Thin, fixed-case adapter to PR65 instruments; no new planner/input service."""
from dataclasses import replace
import json
import sys

from research.navigator_toy import navigator
sys.modules["navigator"] = navigator  # retained script-local Lane C import
from research.navigator_toy import cases
from research.kernel_lab import kernel_lab as lab
from research.possibility_game import engine, scenarios


def bounded(name, computation):
    return {"case": name, "evidence": "STIPULATED_MODEL_EXECUTED_LOCALLY",
            "real_protection": "UNKNOWN", "legitimate_authority": "NOT_ESTABLISHED_BY_MODEL",
            "practical_advantage": "NOT_MEASURED", "model_result": computation}


def protection():
    timely = navigator.analyse(cases.low_reserve())
    unavailable = navigator.analyse(cases.low_reserve(known_protection=False))
    denied = navigator.analyse(cases.disputed(False))
    recorded = lab.trace(lab.case("remedy"), ({"tenant": "report", "owner": "null"},))[0]["after"]
    return bounded("Leah/Mia contrast — fictional models, not the scene's measurements", {
        "known_timely_action": timely.status,
        "no_known_timely_action": unavailable.status,
        "permission_withheld": denied.status,
        "file_exposure_residue_after_report": [recorded[k] for k in ("file", "exposure", "residue")],
        "real_deadline": "UNKNOWN",
        "simpler_owner": "ordinary known authorised protection; relevant responsible domain service",
    })


def workshop():
    scene = lab.case("workshop")
    steps = ({"learner": "practice", "mentor": "null"},
             {"learner": "null", "mentor": "teach"})
    events = lab.trace(scene, steps)
    denied = replace(scene, initial=tuple((k, 0 if k == "permission" else v) for k, v in scene.initial))
    try:
        lab.trace(denied, steps)
    except PermissionError:
        blocked = True
    except ValueError as exc:
        # This owner's Workshop encodes permission as a guard, whereas other
        # cases use Rule.permitted. Do not hide unrelated model errors.
        if str(exc) != "move has 0 matching rules: mentor/teach":
            raise
        blocked = True
    else:
        blocked = False
    return bounded("Saturday Workshop contrast", {
        "after_learning_skill_shared": [events[0]["after"][k] for k in ("skill", "shared_skill")],
        "after_later_teaching_skill_shared": [events[1]["after"][k] for k in ("skill", "shared_skill")],
        "teaching_blocked_when_permission_withheld": blocked,
        "human_learning_or_consent": "NOT_OBSERVED",
        "simpler_owner": "existing capability/learning disciplines and full v0.8 composite",
    })


def collision():
    capacity = cases.separation("capacity")
    constrained = replace(capacity, budget=replace(capacity.budget, imposed=0))
    return bounded("Conflicting actors and authored burden limit", {
        "personal_target": navigator.analyse(cases.separation("self")).status,
        "capacity_target": navigator.analyse(capacity).status,
        "capacity_target_with_zero_imposition": navigator.analyse(constrained).status,
        "no_target": navigator.analyse(cases.separation(None)).status,
        "floor_grounding": "UNRESOLVED; ZERO LIMIT IS AUTHORED",
        "simpler_owner": "explicit ordinary comparison and legitimate domain conflict process",
    })


def institutional():
    late, early = cases.office(), cases.office(True)
    return bounded("Institution/person scale — office analogy only", {
        "late_per_world_route_exists": navigator.route_exists_per_world(late),
        "late_observation_usable_policy": navigator.analyse(late).status,
        "early_observation_usable_policy": navigator.analyse(early).status,
        "real_institution_or_scale_transfer": "NOT_TESTED",
        "simpler_owner": "established imperfect-information planning; accountable domain handoff",
    })


def stale():
    game = scenarios.inheritance()
    old = engine.run(game, "stale", ["left"])
    checked = engine.run(game, "stale", ["check", "right"])
    return bounded("Stale inherited evidence", {
        "old_note_outcome": old["outcome"], "checked_outcome": checked["outcome"],
        "checked_journal_reconstructs": engine.verify(game, checked),
        "real_witness_independence": "NOT_ESTABLISHED",
        "simpler_owner": "bounded current-source check and existing provenance methods",
    })


EXAMPLES = (protection, workshop, collision, institutional, stale)


def main():
    print(json.dumps([example() for example in EXAMPLES], indent=2))


if __name__ == "__main__":
    main()
