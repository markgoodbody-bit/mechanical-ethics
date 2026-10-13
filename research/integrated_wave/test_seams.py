"""Integration challenges; matching claims does not make models equivalent."""
from dataclasses import replace
import importlib.util
from pathlib import Path
import unittest

import sys
from research.navigator_toy import navigator
# The retained Lane C cases use a script-local import. Alias the exact owner
# module instead of modifying that source or loading a second implementation.
sys.modules["navigator"] = navigator
from research.navigator_toy import cases
from research.possibility_game import engine, scenarios
from research.kernel_lab import kernel_lab as lab
from .check_wave import check_paths


def load_math():
    path = Path(__file__).resolve().parents[1] / "math_kernel_cc/kernel_models.py"
    spec = importlib.util.spec_from_file_location("wave_math", path)
    module = importlib.util.module_from_spec(spec)
    # dataclass resolves annotations through sys.modules.
    import sys
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


km = load_math()


class IntegrationSeams(unittest.TestCase):
    def test_custody_rejects_changed_deleted_and_missing_bytes(self):
        for actual in ({"a": "changed"}, {}, {"b": "same"}):
            with self.assertRaises(ValueError):
                check_paths({"a": "same"}, actual, ("a",))
        self.assertEqual(check_paths({"a": "same"}, {"a": "same"}, ("a",)), 1)

    def test_information_loss_is_not_world_hardening(self):
        task = km.walking_home()
        window = km.correction_window(task, 2, km.optimistic_replanner, "w1")
        self.assertEqual([entry[2] for entry in window], [False, True, True])
        self.assertIsNone(km.hardening_time(task, 2, km.optimistic_replanner, "w1"))
        # The annotation in the navigator is a different object, not this predicate.
        self.assertIsNotNone(cases.office().states[cases.office().starts[0]].correction_until)

    def test_null_progresses_two_different_authored_clocks(self):
        game = engine.run(scenarios.raft(), "river", ["wait"])
        self.assertEqual(game["steps"][0]["after"]["clock"], 1)
        joint = lab.trace(lab.case("raft"), ({"traveller": "null"},))[0]
        self.assertEqual(joint["after"]["distance"], 1)
        # Shared names do not equate distance with a clock or equate the rafts.
        self.assertNotIn("clock", joint["after"])

    def test_learning_and_joint_capability_are_distinct(self):
        scene = lab.case("workshop")
        first = lab.trace(scene, ({"learner": "practice", "mentor": "null"},))[0]
        self.assertEqual((first["after"]["skill"], first["after"]["shared_skill"]), (1, 0))
        with self.assertRaises(ValueError):
            lab.trace(scene, ({"learner": "practice", "mentor": "teach"},))
        later = lab.trace(scene, ({"learner": "practice", "mentor": "null"},
                                 {"learner": "null", "mentor": "teach"}))[-1]
        self.assertEqual(later["after"]["shared_skill"], 1)

    def test_permission_not_inferred_from_positive_effect(self):
        scene = lab.case("closure")
        with self.assertRaises(PermissionError):
            lab.trace(scene, ({"operator": "seize", "neighbor": "null"},))
        denied = navigator.analyse(cases.friends(consent=False))
        self.assertEqual(denied.status, "STOP_NO_POLICY_MEETS_BINDING")

    def test_record_effect_does_not_erase_exposure_or_residue(self):
        after = lab.trace(lab.case("remedy"), ({"tenant": "report", "owner": "null"},))[0]["after"]
        self.assertEqual((after["file"], after["exposure"], after["residue"]), (1, 1, 1))

    def test_mandatory_learning_loses_urgent_opportunity(self):
        scene = cases.low_reserve()
        result = navigator.analyse(scene)
        self.assertTrue(result.accepted)
        self.assertTrue(any("known_interim_protection" in str(p) for p in result.accepted))
        first = scene.moves[scene.starts[0]]
        mapping_only = replace(scene, moves=dict(scene.moves, **{
            scene.starts[0]: tuple(m for m in first if m.action != "known_interim_protection")}))
        self.assertFalse(navigator.analyse(mapping_only).accepted)


if __name__ == "__main__":
    unittest.main()
