import unittest
from dataclasses import replace
from fractions import Fraction

from cases import disputed, friends, low_reserve, office, separation, suite
from navigator import (Binding, Cost, Move, Scenario, State, analyse, enumerate_policies,
                       probability, replay, route_exists_per_world, success, trace)


def actions(report):
    return {a for _, a in report.selected.decisions} if report.selected else set()


class NavigatorTests(unittest.TestCase):
    def test_late_information_does_not_make_hidden_route_usable(self):
        s = office()
        self.assertTrue(route_exists_per_world(s))
        self.assertEqual(analyse(s).status, "STOP_NO_POLICY_MEETS_BINDING")

    def test_early_notice_permits_observation_conditional_policy(self):
        r = analyse(office(True))
        self.assertEqual(r.status, "REPRESENTED_POLICY_FOUND")
        self.assertEqual(actions(r), {"inquire", "sendA", "sendB"})
        self.assertTrue(all(success(r.scenario, f) for f in r.selected.ends))

    def test_no_hidden_state_oracle(self):
        r = analyse(office())
        for p in r.policies:
            first = [(k, a) for k, a in p.decisions if len(k) == 2 and k[0] == "office unknown"]
            self.assertEqual(len(first), 1)
            # A single unknown observation cannot choose A in one world, B in the other.
            self.assertTrue(all(f.path == p.ends[0].path for f in p.ends))

    def test_hidden_names_do_not_appear_in_decision_keys(self):
        r = analyse(office(True))
        for key, _ in r.selected.decisions:
            self.assertNotIn("Anotice", key)
            self.assertNotIn("Bnotice", key)

    def test_probability_binding_changes_verdict_not_mechanics(self):
        good = analyse(office(False, "probability", Fraction(85, 100)))
        bad = analyse(office(False, "probability", Fraction(95, 100)))
        self.assertEqual(actions(good), {"sendA"})
        self.assertEqual(probability(good.scenario, good.selected), Fraction(9, 10))
        self.assertIsNone(bad.selected)

    def test_probability_requires_prior(self):
        self.assertEqual(analyse(replace(office(False, "probability"), prior=None)).status, "UNKNOWN_PRIOR")

    def test_missing_binding_does_not_default_to_self_or_joint_good(self):
        r = analyse(separation(None))
        self.assertEqual(r.status, "UNKNOWN_VALUE_BINDING")
        self.assertEqual(r.policies, [])
        self.assertIsNone(route_exists_per_world(r.scenario))

    def test_contested_repair_does_not_block_authorised_protection(self):
        r = analyse(disputed())
        self.assertEqual(actions(r), {"temporary_protection"})
        self.assertTrue(any("repair: AUTHORITY_WITHHELD" in x for x in r.rejected_moves))

    def test_no_permission_is_not_created_by_need(self):
        r = analyse(disputed(False))
        self.assertIsNone(r.selected)
        self.assertTrue(any("temporary_protection: AUTHORITY_WITHHELD" in x for x in r.rejected_moves))

    def test_inquiry_can_miss_protection_window(self):
        r = analyse(disputed())
        self.assertTrue(any("inquire: HORIZON_EXCEEDED" in x for x in r.rejected_moves))

    def test_separation_can_beat_coupling_under_declared_self_constraint(self):
        r = analyse(separation())
        self.assertTrue(actions(r) <= {"refuse", "separate"})
        self.assertTrue(all(f.cost.imposed == 0 for f in r.selected.ends))

    def test_changing_authored_goal_can_favour_capacity_under_coercion(self):
        r = analyse(separation("capacity"))
        self.assertEqual(actions(r), {"stay"})
        self.assertEqual(r.selected.ends[0].cost.imposed, 4)

    def test_protected_imposition_budget_can_veto_capacity_policy(self):
        s = replace(separation("capacity"), budget=Cost(0, 5, imposed=0))
        self.assertIsNone(analyse(s).selected)

    def test_low_reserve_uses_known_protection_not_expensive_mapping(self):
        r = analyse(low_reserve())
        self.assertEqual(actions(r), {"known_interim_protection"})
        self.assertTrue(any("inquire: HORIZON_EXCEEDED" in x for x in r.rejected_moves))

    def test_resource_cost_independently_excludes_mapping(self):
        r = analyse(replace(low_reserve(), horizon=3))
        self.assertTrue(any("inquire: RESOURCE_EXCEEDED" in x for x in r.rejected_moves))

    def test_extra_resources_do_not_restore_elapsed_window(self):
        r = analyse(low_reserve(True))
        self.assertEqual(actions(r), {"known_interim_protection"})
        mapped = [f for p in r.policies for f in p.ends if "inquire" in f.path]
        self.assertTrue(mapped)
        self.assertTrue(all(not success(r.scenario, f) for f in mapped))

    def test_without_known_protection_low_reserve_has_no_solution(self):
        self.assertIsNone(analyse(low_reserve(False, False)).selected)

    def test_positive_voluntary_coupling_expands_usable_routes(self):
        r = analyse(friends())
        self.assertEqual(actions(r), {"ask_friend", "takeA", "takeB"})
        self.assertTrue(all(f.cost.imposed == 1 for f in r.selected.ends))
        self.assertIsNone(analyse(friends(False)).selected)

    def test_consent_withdrawal_is_not_overridden(self):
        r = analyse(friends(False))
        self.assertTrue(any("ask_friend: AUTHORITY_WITHHELD" in x for x in r.rejected_moves))

    def test_longer_horizon_allows_solo_route_no_inherent_need_to_couple(self):
        s = replace(friends(False), horizon=3)
        self.assertIn("check_own_map", actions(analyse(s)))

    def test_partner_imposition_is_not_free(self):
        s = replace(friends(), budget=Cost(0, 3, imposed=0))
        self.assertIsNone(analyse(s).selected)

    def test_wrong_shared_information_breaks_frozen_policy(self):
        policy = analyse(friends()).selected
        challenged = friends(shared_error=True)
        self.assertTrue(all(not success(challenged, f) for f in replay(challenged, policy)))

    def test_unknown_observation_stops_frozen_policy(self):
        s = friends()
        states = dict(s.states)
        states["A"] = replace(states["A"], observation="unexpected observation")
        challenged = replace(s, states=states)
        self.assertIsNotNone(replay(challenged, analyse(s).selected)[0].stopped)

    def test_delay_and_refusal_are_transitions_with_costs(self):
        r = analyse(office())
        for action in ("delay", "refuse"):
            ends = [f for p in r.policies for f in p.ends if f.path and f.path[0] == action]
            self.assertTrue(ends)
            self.assertTrue(all(f.cost.time > 0 for f in ends))

    def test_no_beyond_horizon_policy_is_accepted(self):
        for s in suite():
            r = analyse(s)
            for p in r.accepted:
                self.assertTrue(all(f.cost.time <= s.horizon for f in p.ends))

    def test_deterministic_trace(self):
        for s in suite():
            self.assertEqual(trace(analyse(s)), trace(analyse(s)))

    def test_trace_has_claim_and_correction_boundaries(self):
        t = trace(analyse(friends()))
        for text in ("authored binding", "accessible path", "policy[", "cost=", "correction_until=", "oracle audit only"):
            self.assertIn(text, t)

    def test_negative_cost_rejected(self):
        with self.assertRaises(ValueError):
            Cost(1, -1)

    def test_zero_time_cycle_rejected(self):
        s = office()
        with self.assertRaises(ValueError):
            replace(s, moves={"A": (Move("loop", "A", Cost()),)})

    def test_unknown_target_rejected(self):
        with self.assertRaises(ValueError):
            replace(office(), moves={"A": (Move("send", "absent", Cost(1)),)})

    def test_duplicate_action_rejected(self):
        m = Move("send", "Aok", Cost(1))
        with self.assertRaises(ValueError):
            replace(office(), moves={"A": (m, m)})

    def test_bad_prior_rejected(self):
        with self.assertRaises(ValueError):
            replace(office(), prior={"A": Fraction(1), "B": Fraction(1)})

    def test_invalid_binding_rejected(self):
        with self.assertRaises(ValueError):
            Binding(frozenset({"x"}), mode="moral_oracle")

    def test_per_world_routes_do_not_supply_preferences(self):
        self.assertIsNone(route_exists_per_world(separation(None)))

    def test_hidden_permission_difference_is_not_an_oracle(self):
        s = Scenario("contested permission", ("permission differs across indistinguishable worlds",),
                     {"A": State("unknown"), "B": State("unknown"),
                      "done": State("done", "protected")},
                     {"A": (Move("protect", "done", Cost(1), True),),
                      "B": (Move("protect", "done", Cost(1), False),)},
                     ("A", "B"), 1, Cost(), Binding(frozenset({"protected"})))
        self.assertIsNone(analyse(s).selected)

    def test_money_limit_is_effective(self):
        s = disputed()
        moves = dict(s.moves)
        moves["start"] = tuple(replace(m, cost=Cost(1, 1, 1)) if m.action == "temporary_protection" else m for m in moves["start"])
        s = replace(s, moves=moves)
        self.assertIsNone(analyse(s).selected)
        self.assertIsNotNone(analyse(replace(s, budget=Cost(0, 1, 1))).selected)

    def test_ordinary_known_action_has_same_outcome_no_claimed_advantage(self):
        s = low_reserve()
        ordinary = next(m for m in s.moves["start"] if m.action == "known_interim_protection")
        r = analyse(s)
        self.assertEqual(r.selected.ends[0].state, ordinary.target)
        self.assertEqual(r.selected.ends[0].cost, ordinary.cost)


if __name__ == "__main__":
    unittest.main()
