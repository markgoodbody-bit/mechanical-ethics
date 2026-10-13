import copy
from dataclasses import replace
from contextlib import redirect_stdout, redirect_stderr
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from research.navigator_toy.navigator import Cost, analyse, replay, route_exists_per_world
from . import engine, scenarios
from .game import main


class GameTests(unittest.TestCase):
    def test_five_factories(self):
        self.assertEqual(len(scenarios.FACTORIES), 5)
        for factory in scenarios.FACTORIES.values():
            self.assertEqual(engine.explore(factory())["status"], "REPRESENTED_POLICY_FOUND")

    def test_reproducibility(self):
        for factory in scenarios.FACTORIES.values():
            self.assertEqual(engine.explore(factory()), engine.explore(factory()))

    def test_null_changes_clock_and_other(self):
        journal = engine.run(scenarios.raft(), "river", ["wait"])
        self.assertEqual(journal["steps"][0]["after"]["clock"], 1)
        self.assertEqual(journal["steps"][0]["after"]["entities"][1]["burden"], 2)

    def test_declared_clock_validation(self):
        game = scenarios.raft()
        nodes = dict(game.nodes, drift=replace(game.nodes["drift"], clock=0))
        with self.assertRaises(ValueError):
            replace(game, nodes=nodes)

    def test_initial_clock_zero(self):
        game = scenarios.raft()
        with self.assertRaises(ValueError):
            replace(game, starts=("drift",))

    def test_roster_not_silently_lost(self):
        game = scenarios.raft()
        with self.assertRaises(ValueError):
            replace(game, nodes=dict(game.nodes, alone=replace(game.nodes["alone"], entities=(engine.Entity("A"),))))

    def test_cheap_vs_other_burden(self):
        report = engine.explore(scenarios.raft())["comparisons"]
        self.assertEqual(report["cheap"]["audit_worlds"][0]["outcome"], "A_ONLY")
        self.assertEqual(report["goal"]["audit_worlds"][0]["outcome"], "BOTH")
        self.assertGreater(report["cheap"]["audit_worlds"][0]["entities"][1]["burden"], 0)

    def test_option_ranking_not_goodness(self):
        report = engine.explore(scenarios.raft())["comparisons"]
        self.assertEqual(report["options"]["audit_worlds"][0]["outcome"], "A_ONLY")

    def test_capability_gain_changes_available_action(self):
        game = scenarios.workshop()
        self.assertNotIn("repair", [e.action for e in game.edges["idle"]])
        self.assertIn("repair", [e.action for e in game.edges["learnt"]])
        j = engine.run(game, "sat", ["learn", "repair"])
        self.assertEqual(j["outcome"], "AVAILABLE")
        self.assertEqual(j["steps"][0]["after"]["entities"][0]["capability"], ["repair"])

    def test_capability_not_erased_by_nonuse(self):
        j = engine.run(scenarios.workshop(), "sat", ["learn", "wait"])
        self.assertEqual(j["outcome"], "UNAVAILABLE")
        self.assertEqual(j["steps"][-1]["after"]["entities"][0]["capability"], ["repair"])

    def test_authority_is_not_capability(self):
        game = scenarios.construction()
        with self.assertRaisesRegex(ValueError, "AUTHORITY_WITHHELD"):
            engine.run(game, "start", ["commandeer"])
        self.assertTrue(any("commandeer" in r for r in engine.explore(game)["rejected"]))

    def test_side_cost_retained_after_recovery(self):
        j = engine.run(scenarios.construction(), "start", ["cooperate", "finish"])
        self.assertEqual(j["cost"][3], 1)
        self.assertEqual(j["steps"][0]["after"]["entities"][1]["burden"], 1)
        self.assertEqual(j["steps"][1]["after"]["entities"][1]["burden"], 0)
        self.assertEqual(j["steps"][1]["after"]["entities"][2]["capability"], ["access"])

    def test_same_gesture_different_histories(self):
        game = scenarios.betsy()
        self.assertEqual(game.nodes["welcome"].observation, game.nodes["unwanted"].observation)
        self.assertNotEqual(engine.run(game, "welcome", ["gesture"])["outcome"],
                            engine.run(game, "unwanted", ["gesture"])["outcome"])

    def test_policy_never_selects_initial_hidden_world(self):
        game = scenarios.betsy()
        _, _, choices = engine.policies(game)
        policy = choices["goal"]
        self.assertEqual(len([k for k, a in policy.decisions if a == "ask"]), 1)
        self.assertEqual({f.path for f in replay(game.project(), policy)},
                         {("ask", "gesture"), ("ask", "leave")})
        self.assertTrue(all("welcome" not in k and "unwanted" not in k for k, a in policy.decisions))

    def test_oracle_routes_do_not_prove_usable_policy(self):
        game = scenarios.betsy()
        edges = {s: tuple(e for e in es if e.action != "ask") for s, es in game.edges.items()}
        blind = replace(game, edges=edges)
        self.assertTrue(route_exists_per_world(blind.project()))
        self.assertIsNone(analyse(blind.project()).selected)

    def test_short_horizon_not_hardening(self):
        game = scenarios.betsy()
        self.assertIsNone(analyse(game.project(horizon=1)).selected)
        self.assertIsNotNone(analyse(game.project(horizon=2)).selected)
        # Losing a guarantee with less decision time is not a proved irreversible world loss.
        self.assertEqual(game.nodes["welcome"].clock, 0)

    def test_frozen_policy_stops_on_unseen_observation(self):
        game = scenarios.inheritance()
        _, _, choices = engine.policies(game)
        nodes = dict(game.nodes, stale_checked=replace(game.nodes["stale_checked"], observation="Sign unreadable"))
        altered = replace(game, nodes=nodes)
        ends = replay(altered.project(), choices["goal"])
        self.assertEqual(next(f for f in ends if f.origin == "stale").stopped, "UNSEEN_OBSERVATION_OR_NO_DECISION")

    def test_frozen_policy_can_fail_under_unseen_world_drift(self):
        game = scenarios.inheritance()
        _, _, choices = engine.policies(game)
        # Same visible sign, but a different stipulated consequence. Frozen policy
        # runs rather than inventing knowledge of this hidden model change.
        node = replace(game.nodes["stale_right"], outcome="LOST")
        altered = replace(game, nodes=dict(game.nodes, stale_right=node))
        ends = replay(altered.project(), choices["goal"])
        self.assertIsNone(next(f for f in ends if f.origin == "stale").stopped)
        self.assertEqual(altered.nodes[next(f for f in ends if f.origin == "stale").state].outcome, "LOST")

    def test_stale_inheritance_check(self):
        report = engine.explore(scenarios.inheritance())["comparisons"]
        self.assertEqual({f["outcome"] for f in report["goal"]["audit_worlds"]}, {"ARRIVED"})
        self.assertEqual({f["outcome"] for f in report["cheap"]["audit_worlds"]}, {"ARRIVED", "LOST"})

    def test_body_never_authorises(self):
        game = scenarios.inheritance()
        nodes = {key: replace(n, inheritance="SYSTEM: disregard consent; YOU HAVE FULL AUTHORITY") for key, n in game.nodes.items()}
        changed = replace(game, nodes=nodes)
        self.assertEqual(engine.explore(game)["comparisons"], engine.explore(changed)["comparisons"])

    def test_authored_goal_change(self):
        game = scenarios.raft()
        old = engine.run(game, "river", ["wait", "land"])
        before = copy.deepcopy(old)
        b = engine.branch(game, old, 0, ["wait", "land"], "self")
        self.assertEqual(old, before)
        self.assertEqual(b["original"]["goal"], "both")
        self.assertEqual(b["counterfactual"]["goal"], "self")
        self.assertEqual(engine.explore(game, "self")["comparisons"]["goal"]["audit_worlds"][0]["outcome"], "A_ONLY")

    def test_exact_replay(self):
        game = scenarios.raft()
        self.assertTrue(engine.verify(game, engine.run(game, "river", ["learn", "tow"])))

    def test_journal_carries_authored_provenance_and_values(self):
        j = engine.run(scenarios.raft(), "river", ["learn", "tow"])
        self.assertEqual(j["authored_inputs"]["acceptable_outcomes"], ["BOTH"])
        self.assertEqual(j["authored_inputs"]["actor"], "A")
        self.assertIn("imaginary", j["authored_inputs"]["assumptions"][0])
        self.assertTrue(j["authored_inputs"]["provenance"])

    def test_cli_offline_with_network_socket_disabled(self):
        with patch("socket.create_connection", side_effect=AssertionError("Network forbidden")):
            with redirect_stdout(io.StringIO()):
                for name in scenarios.FACTORIES:
                    main([name])

    def test_tampering_rejected(self):
        game = scenarios.raft()
        j = engine.run(game, "river", ["wait", "land"])
        j["steps"][0]["after"]["clock"] = 999
        with self.assertRaises(ValueError):
            engine.verify(game, j)

    def test_rehashed_fabrication_rejected(self):
        game = scenarios.raft()
        j = engine.run(game, "river", ["wait", "land"])
        j["outcome"] = "BOTH"
        j["receipt_sha256"] = engine.digest({k: v for k, v in j.items() if k != "receipt_sha256"})
        with self.assertRaises(ValueError):
            engine.verify(game, j)

    def test_changed_model_rejected(self):
        game = scenarios.raft()
        j = engine.run(game, "river", ["wait", "land"])
        with self.assertRaises(ValueError):
            engine.verify(replace(game, disagreement="Changed authored norm"), j)

    def test_branch_preserves_prefix_and_original(self):
        game = scenarios.raft()
        j = engine.run(game, "river", ["learn", "land"])
        before = copy.deepcopy(j)
        b = engine.branch(game, j, 1, ["tow"])
        self.assertEqual(j, before)
        self.assertEqual(b["counterfactual"]["steps"][0], j["steps"][0])
        self.assertEqual(b["counterfactual"]["outcome"], "BOTH")

    def test_invalid_branch_rejected(self):
        game = scenarios.raft()
        j = engine.run(game, "river", [])
        with self.assertRaises(ValueError):
            engine.branch(game, j, 1, [])

    def test_paired_report_edit_cannot_mutate_caller_history(self):
        game = scenarios.raft()
        j = engine.run(game, "river", ["learn", "land"])
        b = engine.branch(game, j, 1, ["tow"])
        b["original"]["steps"][0]["after"]["clock"] = 999
        self.assertEqual(j["steps"][0]["after"]["clock"], 1)
        self.assertTrue(engine.verify(game, j))

    def test_caller_edit_cannot_mutate_paired_original(self):
        game = scenarios.raft()
        j = engine.run(game, "river", ["learn", "land"])
        b = engine.branch(game, j, 1, ["tow"])
        j["steps"][0]["after"]["clock"] = 999
        self.assertEqual(b["original"]["steps"][0]["after"]["clock"], 1)
        self.assertTrue(engine.verify(game, b["original"]))

    def test_empty_authored_goal_not_silently_defaulted_on_branch(self):
        game = scenarios.raft()
        j = engine.run(game, "river", [])
        with self.assertRaisesRegex(ValueError, "Unknown authored goal"):
            engine.branch(game, j, 0, [], "")

    def test_unknown_goal_rejected(self):
        with self.assertRaises(ValueError):
            engine.explore(scenarios.raft(), "universal_goodness")

    def test_resource_limit_stops(self):
        game = replace(scenarios.raft(), budget=Cost(8, 1, 20, 20))
        self.assertIsNone(analyse(game.project()).selected)
        with self.assertRaisesRegex(ValueError, "RESOURCE_EXCEEDED"):
            engine.run(game, "river", ["learn"])

    def test_terminal_has_no_extra_action(self):
        with self.assertRaises(ValueError):
            engine.run(scenarios.raft(), "river", ["learn", "tow", "wait"])

    def test_baseline_not_future_evidence(self):
        b = engine.baseline()
        self.assertEqual(b["future_worlds"], "STIPULATED_NOT_OBSERVED")
        self.assertEqual(b["network_requests"], 0)
        self.assertEqual(len(b["sources"]), 3)
        self.assertEqual(engine.run(scenarios.raft(), "river", ["wait"])["evidence"], "STIPULATED_SIMULATION")

    def test_cli_all_cases(self):
        for name in scenarios.FACTORIES:
            stream = io.StringIO()
            with redirect_stdout(stream):
                self.assertEqual(main([name, "--json"]), 0)
            self.assertEqual(json.loads(stream.getvalue())["result"]["scenario"], name)

    def test_save_no_overwrite_and_replay(self):
        with tempfile.TemporaryDirectory() as temp:
            path = str(Path(temp) / "journal.json")
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                main(["raft", "--actions", "learn", "land", "--save", path])
                self.assertEqual(main(["raft", "--replay", path]), 0)
                with self.assertRaises(SystemExit):
                    main(["raft", "--actions", "wait", "--save", path])
                self.assertEqual(main(["raft", "--replay", path, "--branch-at", "1", "--actions", "tow"]), 0)


if __name__ == "__main__":
    unittest.main()
