import unittest
from kernel_lab import case, tick, trace, view, CASES


class KernelLabTests(unittest.TestCase):
    def test_six_named_scenarios(self):
        self.assertEqual(len(CASES), 6)
        self.assertEqual(len(set(CASES)), 6)
        for name in CASES:
            self.assertTrue(case(name).claims)

    def test_null_does_not_stop_external_time(self):
        x = trace(case("raft"), ({"traveller": "null"},))
        self.assertEqual(x[0]["after"]["distance"], 1)
        self.assertEqual(x[0]["after"]["landing"], 1)
        later = trace(case("raft"), ({"traveller": "null"}, {"traveller": "null"}))[-1]
        self.assertEqual(later["after"]["landing"], 0)
        self.assertIn("NO_DIRECT_ACT", x[0]["impacts"][0][2])

    def test_raft_immediate_cost_builds_capacity_when_landing_still_open(self):
        # A different authored timing contract: landing remains available for one step.
        from dataclasses import replace
        s = case("raft")
        s = replace(s, shocks=((('distance', 1),),))
        dock = trace(s, ({"traveller": "dock"},))[0]["after"]
        glide = trace(s, ({"traveller": "smooth"},))[0]["after"]
        self.assertEqual((dock["energy"], dock["repair_skill"]), (2, 1))
        self.assertEqual((glide["energy"], glide["repair_skill"]), (4, 0))

    def test_raft_late_dock_not_supported(self):
        with self.assertRaises(ValueError):
            trace(case("raft"), ({"traveller": "null"}, {"traveller": "dock"}))

    def test_hidden_histories_same_prior_observation_distinct_responses(self):
        a, b = case("betsy", 0), case("betsy", 1)
        self.assertEqual(view(a, dict(a.initial), "person"), view(b, dict(b.initial), "person"))
        x = trace(a, ({"person": "block"},))[0]
        y = trace(b, ({"person": "block"},))[0]
        self.assertEqual((x["after"]["distress"], y["after"]["distress"]), (1, 4))
        self.assertNotIn("sensitivity", x["views"]["person"])
        self.assertNotIn("sensitivity", y["views"]["person"])

    def test_betsy_adaptation_without_hidden_history_diagnosis(self):
        z = trace(case("betsy", 1), ({"person": "block"}, {"person": "adjust"}))
        self.assertEqual(z[1]["views"]["person"]["distress"], 4)
        self.assertEqual(z[1]["after"]["careful"], 1)
        self.assertEqual(z[1]["after"]["sensitivity"], 1)

    def test_workshop_learning_and_voluntary_transfer_not_automatic(self):
        s = case("workshop")
        a = trace(s, ({"learner": "practice", "mentor": "null"},))[-1]["after"]
        self.assertEqual((a["cash"], a["skill"], a["shared_skill"]), (2, 1, 0))
        b = trace(s, ({"learner": "practice", "mentor": "null"},
                       {"learner": "null", "mentor": "teach"}))[-1]["after"]
        self.assertEqual(b["shared_skill"], 1)

    def test_report_changes_file_not_exposure(self):
        first = trace(case("remedy"), ({"tenant": "report", "owner": "null"},))[0]["after"]
        self.assertEqual((first["file"], first["repair"], first["exposure"]), (1, 0, 1))

    def test_later_repair_keeps_residue(self):
        last = trace(case("remedy"), ({"tenant": "report", "owner": "null"},
                                     {"tenant": "null", "owner": "repair"}))[-1]["after"]
        self.assertEqual((last["file"], last["repair"], last["residue"]), (1, 1, 2))

    def test_closure_fewer_routes_without_moral_scoring(self):
        shut = trace(case("closure"), ({"operator": "close_unsafe", "neighbor": "null"},))[0]
        self.assertEqual((shut["after"]["open_routes"], shut["after"]["barrier"]), (2, 1))
        extract = trace(case("closure"), ({"operator": "extract", "neighbor": "null"},))[0]
        self.assertEqual((extract["after"]["operator_gain"], extract["after"]["neighbor_loss"]), (3, 4))

    def test_authored_permission_blocks_even_physically_described_seize(self):
        with self.assertRaises(PermissionError):
            trace(case("closure"), ({"operator": "seize", "neighbor": "null"},))

    def test_stale_currentness_false_if_null(self):
        e = trace(case("stale"), ({"reader": "null"},))[0]
        self.assertEqual(e["views"]["reader"]["cached_value"], 1)
        self.assertEqual((e["after"]["cached_value"], e["after"]["source_value"]), (1, 0))

    def test_refresh_reduces_mismatch_but_is_not_true_provenance(self):
        e = trace(case("stale"), ({"reader": "refresh"},))[0]
        self.assertEqual((e["after"]["cached_value"], e["after"]["source_value"]), (0, 0))
        self.assertEqual(e["after"]["check_count"], 1)

    def test_views_never_leak_unobserved_state(self):
        for name in CASES:
            s = case(name)
            for actor in s.actors:
                self.assertEqual(set(view(s, dict(s.initial), actor)), set(dict(s.visible)[actor]))

    def test_unknown_actor_and_move_fail_closed(self):
        s = case("workshop")
        with self.assertRaises(ValueError):
            view(s, dict(s.initial), "unlisted")
        with self.assertRaises(ValueError):
            trace(s, ({"learner": "invent", "mentor": "null"},))
        with self.assertRaises(ValueError):
            trace(s, ({"learner": "null"},))

    def test_horizon_and_world_schema_fail_closed(self):
        with self.assertRaises(ValueError):
            trace(case("closure"), ({"operator":"null", "neighbor":"null"},)*2)
        with self.assertRaises(ValueError):
            tick(case("closure"), {"not_world":1}, 0, {"operator":"null", "neighbor":"null"})


if __name__ == "__main__":
    unittest.main()
