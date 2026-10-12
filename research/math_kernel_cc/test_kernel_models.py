"""Checks for kernel_models.py. Each proposition in ME_V0_9_MATH_KERNEL_CC.md that the toys
exhibit is asserted here in both directions: where it holds, and where its condition fails.

    python -m unittest discover -s research/math_kernel_cc -v
"""
import math
import os
import sys
import unittest
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kernel_models as km  # noqa: E402


class QuantifierGap(unittest.TestCase):
    """P1: usable (exists policy, for all worlds) implies exists (for all worlds, exists route);
    the converse fails under partial observation and holds under full view."""

    def test_route_exists_but_is_not_usable_without_information(self):
        alone = km.walking_home(stranger=False)
        for H in (2, 3):
            self.assertTrue(km.route_exists(alone, H))
            self.assertFalse(km.usable_robust(alone, H))

    def test_full_view_closes_the_gap(self):
        full = km.walking_home(stranger=False, full_view=True)
        for H in (0, 1, 2, 3, 4, 5):
            self.assertEqual(km.usable_robust(full, H), km.route_exists(full, H), H)
        self.assertTrue(km.usable_robust(full, 2))  # the same streets, seen in advance

    def test_no_route_exists_before_two_steps(self):
        # regression: route_exists once allowed H+1 steps and claimed a one-step route home
        for H in (0, 1):
            self.assertFalse(km.route_exists(km.walking_home(stranger=False), H), H)
        self.assertTrue(km.route_exists(km.walking_home(stranger=False), 2))

    def test_usable_always_implies_exists(self):
        for task in (km.walking_home(), km.walking_home(stranger=False), km.walking_home(reliability=Fr(3, 4))):
            for H in range(0, 6):
                if km.usable_robust(task, H):
                    self.assertTrue(km.route_exists(task, H))


class InformationAndCoupling(unittest.TestCase):
    def test_a_single_entity_never_loses_by_gaining_an_observation(self):
        # P2 (Blackwell-type): adding the stranger's answer never lowers usability or best probability
        for H in range(0, 6):
            alone, asked = km.walking_home(stranger=False), km.walking_home()
            self.assertGreaterEqual(km.best_probability(asked, H), km.best_probability(alone, H))
            self.assertTrue(km.usable_robust(asked, H) or not km.usable_robust(alone, H))

    def test_the_stranger_makes_the_route_usable_only_at_curfew_three(self):
        self.assertFalse(km.usable_robust(km.walking_home(), 2))   # asking costs the only spare step
        self.assertTrue(km.usable_robust(km.walking_home(), 3))
        self.assertFalse(km.usable_robust(km.walking_home(stranger=False), 3))
        self.assertTrue(km.usable_robust(km.walking_home(stranger=False), 4))  # the main road suffices

    def test_an_information_coupling_is_worth_it_only_above_a_reliability_threshold(self):
        # asking succeeds with r + (1 - r) * P(both open) = r + 3/20 (1 - r); break-even with 13/20 at r = 10/17
        self.assertEqual(km.best_probability(km.walking_home(reliability=Fr(10, 17)), 3), Fr(13, 20))
        self.assertGreater(km.best_probability(km.walking_home(reliability=Fr(11, 17)), 3), Fr(13, 20))
        self.assertEqual(km.best_probability(km.walking_home(reliability=Fr(9, 17)), 3), Fr(13, 20))
        self.assertFalse(km.usable_robust(km.walking_home(reliability=Fr(99, 100)), 3))  # never robust

    def test_more_information_can_dissolve_a_voluntary_coupling(self):
        # P3 (Hirshleifer): with concave utility, information before consent removes the whole surplus
        for name in ("sqrt (risk-averse)", "log (more risk-averse)"):
            u = km.UTILITIES[name]
            self.assertGreater(km.surplus(u, 0.0, "pool"), 0.05, name)
            self.assertAlmostEqual(km.surplus(u, 0.0, "voluntary-after-information"), 0.0, places=12)

    def test_the_surplus_comes_from_concavity_not_from_the_coupling(self):
        lin = km.UTILITIES["linear (risk-neutral)"]
        for c in (0.0, 0.125, 0.25):
            self.assertAlmostEqual(km.surplus(lin, c), 0.0, places=12)

    def test_common_cause_exposure_removes_the_surplus(self):
        u = km.UTILITIES["sqrt (risk-averse)"]
        s = [km.surplus(u, c) for c in (0.0, 0.0625, 0.125, 0.1875, 0.25)]
        self.assertTrue(all(a > b for a, b in zip(s, s[1:])), s)
        self.assertAlmostEqual(s[-1], 0.0, places=12)

    def test_a_mandate_restores_the_surplus_by_overriding_the_lucky_household(self):
        u = km.UTILITIES["sqrt (risk-averse)"]
        self.assertAlmostEqual(km.surplus(u, 0.0, "mandate"), km.surplus(u, 0.0, "pool"), places=12)
        self.assertEqual(km.voluntary_after_information((1, 0)), (2.0, 10.0))
        self.assertEqual(km.wealth((1, 0), "pool"), (6.0, 6.0))

    def test_coupling_opens_a_new_reachable_outcome_only_without_common_cause(self):
        # P5: at threshold 0.9 neither household alone keeps >= 4; together they do, unless c = p
        theta = 0.9
        self.assertLess(km.p_floor("autarky", 0.0), theta)
        self.assertGreaterEqual(km.p_floor("pool", 0.0), theta)
        self.assertLess(km.p_floor("pool", 0.25), theta)
        self.assertAlmostEqual(km.p_floor("pool", 0.25), km.p_floor("autarky", 0.25), places=12)

    def test_redundancy_improvement_vanishes_under_common_cause(self):
        self.assertAlmostEqual(km.redundancy_failure(0.25, 0.0), 0.0625, places=12)
        self.assertAlmostEqual(km.redundancy_failure(0.25, 0.25), 0.25, places=12)


class TimingFrictionAndScale(unittest.TestCase):
    def test_correction_closes_at_the_first_step_of_the_optimistic_route(self):
        rows = km.correction_window(km.walking_home(), 3, km.optimistic_replanner, "w2")
        self.assertEqual([k for _, _, k in rows], [True, False, False, False])
        self.assertIsNone(km.simulate(km.walking_home(), 3, km.optimistic_replanner, "w2")[0])
        self.assertEqual(km.simulate(km.walking_home(), 3, km.optimistic_replanner, "w1")[0], 2)

    def test_least_friction_is_undefined_without_a_declared_order(self):
        front = km.pareto(km.robust_tradeoffs(km.walking_home(), 5))
        self.assertEqual(front, [(3, 4), (4, 0)])
        (t1, e1), (t2, e2) = front
        self.assertTrue(t1 < t2 and e1 > e2)  # neither dominates

    def test_a_lumped_coarse_model_preserves_existence_but_not_usability(self):
        coarse, fine = km.lumped_short_route(), km.walking_home(stranger=False)
        for H in (1, 2, 3):
            self.assertEqual(km.route_exists(coarse, H), km.route_exists(fine, H), H)
        self.assertTrue(km.usable_robust(coarse, 2))
        self.assertFalse(km.usable_robust(fine, 2))


class NegativeControls(unittest.TestCase):
    """Each check above must be able to fail: break one assumption and watch the result change."""

    def test_ignoring_partial_observation_would_hide_the_gap(self):
        self.assertTrue(km.usable_robust(km.walking_home(stranger=False, full_view=True), 2))
        self.assertFalse(km.usable_robust(km.walking_home(stranger=False), 2))

    def test_a_policy_that_sees_the_hidden_world_would_look_perfect(self):
        oracle = lambda task, s, t, S: {"S": "A", "A": "Hm"}[s]
        self.assertIsNone(km.simulate(km.walking_home(), 3, oracle, "w2")[0])  # the blind route fails in w2
        self.assertEqual(km.best_probability(km.walking_home(stranger=False, full_view=True), 2), 1)

    def test_linear_utility_reports_no_surplus_even_without_common_cause(self):
        self.assertAlmostEqual(km.surplus(km.UTILITIES["linear (risk-neutral)"], 0.0), 0.0, places=12)
        self.assertGreater(km.surplus(km.UTILITIES["sqrt (risk-averse)"], 0.0), 0.0)


if __name__ == "__main__":
    unittest.main()
