"""Whole-case distinctions and deliberate promotion/authority negative controls."""
import copy
from dataclasses import replace
from pathlib import Path
import unittest
from unittest.mock import patch

from . import examples as e


class CoreCases(unittest.TestCase):
    def test_newcomer_route_points_to_core_before_reference_stack(self):
        root = Path(__file__).resolve().parents[2]
        guide = (root / "research/integrated_wave/README.md").read_text(encoding="utf-8")
        route = guide.split("## Start here", 1)[1].split("## One integrated", 1)[0]
        self.assertLess(route.index("compact_core/START.md"), route.index("MATH_KERNEL_CC.md"))
        self.assertTrue((root / "research/compact_core/START.md").is_file())
        self.assertIn("not a compulsory reading sequence", route)

    def test_five_cases_and_evidence_ceiling(self):
        for example in e.EXAMPLES:
            result = example()
            self.assertEqual(result["evidence"], "STIPULATED_MODEL_EXECUTED_LOCALLY")
            self.assertEqual(result["real_protection"], "UNKNOWN")
            self.assertEqual(result["legitimate_authority"], "NOT_ESTABLISHED_BY_MODEL")
            self.assertEqual(result["practical_advantage"], "NOT_MEASURED")

    def test_protection_and_record_are_distinct(self):
        x = e.protection()["model_result"]
        self.assertEqual(x["known_timely_action"], "REPRESENTED_POLICY_FOUND")
        self.assertEqual(x["no_known_timely_action"], "STOP_NO_POLICY_MEETS_BINDING")
        self.assertEqual(x["permission_withheld"], "STOP_NO_POLICY_MEETS_BINDING")
        self.assertEqual(x["file_exposure_residue_after_report"], [1, 1, 1])
        self.assertEqual(x["real_deadline"], "UNKNOWN")

    def test_learning_and_joint_capability_require_distinct_steps(self):
        x = e.workshop()["model_result"]
        self.assertEqual(x["after_learning_skill_shared"], [1, 0])
        self.assertEqual(x["after_later_teaching_skill_shared"], [1, 1])
        self.assertTrue(x["teaching_blocked_when_permission_withheld"])

    def test_collision_stays_visible_instead_of_relaxing_limit(self):
        x = e.collision()["model_result"]
        self.assertEqual(x["capacity_target"], "REPRESENTED_POLICY_FOUND")
        self.assertEqual(x["capacity_target_with_zero_imposition"], "STOP_NO_POLICY_MEETS_BINDING")
        self.assertEqual(x["no_target"], "UNKNOWN_VALUE_BINDING")

    def test_institutional_summary_does_not_supply_actor_information(self):
        x = e.institutional()["model_result"]
        self.assertTrue(x["late_per_world_route_exists"])
        self.assertEqual(x["late_observation_usable_policy"], "STOP_NO_POLICY_MEETS_BINDING")
        self.assertEqual(x["early_observation_usable_policy"], "REPRESENTED_POLICY_FOUND")

    def test_inheritance_currentness_and_authenticity_not_collapsed(self):
        x = e.stale()["model_result"]
        self.assertEqual((x["old_note_outcome"], x["checked_outcome"]), ("LOST", "ARRIVED"))
        self.assertTrue(x["checked_journal_reconstructs"])
        self.assertEqual(x["real_witness_independence"], "NOT_ESTABLISHED")

    def test_same_tick_learning_is_not_available_to_teaching(self):
        with self.assertRaises(ValueError):
            e.lab.trace(e.lab.case("workshop"), ({"learner": "practice", "mentor": "teach"},))

    def test_capacity_permission_bypass_would_break_workshop_claim(self):
        original = e.lab.case
        def bypass(name):
            scene = original(name)
            return replace(scene, rules=tuple(replace(r, requires=tuple(
                (k, v) for k, v in r.requires if k != "permission")) for r in scene.rules))
        with patch.object(e.lab, "case", bypass):
            self.assertFalse(e.workshop()["model_result"]["teaching_blocked_when_permission_withheld"])

    def test_hidden_world_oracle_would_change_institutional_conclusion(self):
        original = e.navigator.observation_key
        def oracle(scene, frame):
            return original(scene, frame) + (frame.state,)
        with patch.object(e.navigator, "observation_key", oracle):
            self.assertEqual(e.institutional()["model_result"]["late_observation_usable_policy"],
                             "REPRESENTED_POLICY_FOUND")

    def test_rehashed_fabricated_witness_still_rejected(self):
        game = e.scenarios.inheritance()
        journal = copy.deepcopy(e.engine.run(game, "stale", ["left"]))
        journal["outcome"] = "ARRIVED"
        journal["receipt_sha256"] = e.engine.digest({k: v for k, v in journal.items() if k != "receipt_sha256"})
        with self.assertRaises(ValueError):
            e.engine.verify(game, journal)


if __name__ == "__main__":
    unittest.main()
