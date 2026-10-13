"""A flat, two-step oracle, deliberately separate from recursive enumeration.

100 seeded synthetic models are a bounded differential check, not a proof.
The oracle shares the declared observation/cost contract, not solver helpers.
"""
from itertools import product
from fractions import Fraction
import random
import unittest
from dataclasses import replace
from unittest.mock import patch

import navigator
from navigator import Binding, Cost, Move, Scenario, State, analyse, replay


def fixture(seed):
    rng = random.Random(seed)
    states, moves = {}, {}
    for w in ("A", "B"):
        states[w] = State("hidden world")
        first = []
        for a in ("left", "right"):
            middle = w + a
            states[middle] = State("notice" + str(rng.randrange(2)))
            first.append(Move(a, middle, Cost(1, rng.randrange(2)), rng.choice((True, True, False))))
            second = []
            for b in ("left", "right"):
                target = middle + b
                good = rng.choice((True, False))
                states[target] = State("finished", "good" if good else "bad")
                second.append(Move(b, target, Cost(rng.randrange(1, 3), rng.randrange(2),
                                                  rng.randrange(2), rng.randrange(2)),
                                   rng.choice((True, True, False))))
            moves[middle] = tuple(second)
        moves[w] = tuple(first)
    mode = "robust" if seed % 2 == 0 else "probability"
    weight = Fraction(seed % 5, 4)  # Includes zero-weight initial worlds, still robustly admissible.
    return Scenario("seed " + str(seed), ("synthetic two-step model",), states, moves,
                    ("A", "B"), rng.randrange(2, 5),
                    Cost(0, rng.randrange(4), rng.randrange(3), rng.randrange(3)),
                    Binding(frozenset({"good"}), mode, Fraction((seed % 4) + 1, 4)),
                    {"A": weight, "B": 1 - weight})


def allowed(s, move, spent):
    after = tuple(x + y for x, y in zip(spent, move.cost.vector()))
    ok = move.authorised and after[0] <= s.horizon and all(
        x <= y for x, y in zip(after[1:], s.budget.vector()[1:]))
    return ok, after


def flat_oracle(s):
    """Enumerate root choices and all second-stage observable decision tables.

No analyse/enumerate/permitted/observation_key/success/probability calls.
An observation group must take a common legal action, or stop if none exists.
"""
    root_options = []
    for a in ("left", "right"):
        if all(allowed(s, next(m for m in s.moves[w] if m.action == a), (0, 0, 0, 0))[0]
               for w in s.starts):
            root_options.append(a)
    if not root_options:
        return set()
    accepted = set()
    for a in root_options:
        groups = {}
        for w in s.starts:
            m = next(m for m in s.moves[w] if m.action == a)
            spent = m.cost.vector()
            # Observable action history and resources; hidden IDs are not keys.
            key = (a, s.states[m.target].observation, spent)
            groups.setdefault(key, []).append((w, m.target, spent))
        options = []
        for key, frames in sorted(groups.items()):
            common = []
            for b in ("left", "right"):
                if all(allowed(s, next(m for m in s.moves[state] if m.action == b), spent)[0]
                       for _, state, spent in frames):
                    common.append(b)
            options.append((frames, common or [None]))
        for choices in product(*(choices for _, choices in options)):
            ends = []
            for (frames, _), b in zip(options, choices):
                for w, state, spent in frames:
                    if b is None:
                        ends.append((w, None, spent, True))
                    else:
                        m = next(m for m in s.moves[state] if m.action == b)
                        _, after = allowed(s, m, spent)
                        ends.append((w, s.states[m.target].outcome, after, False))
            good = [w for w, outcome, _, stopped in ends if outcome == "good" and not stopped]
            ok = (len(good) == len(s.starts) if s.binding.mode == "robust"
                  else sum((s.prior[w] for w in good), Fraction(0)) >= s.binding.threshold)
            if ok:
                accepted.add(tuple(sorted(ends)))
    return accepted


def signature(s, ends):
    return tuple(sorted((f.origin, None if f.stopped else s.states[f.state].outcome,
                         f.cost.vector(), bool(f.stopped)) for f in ends))


class GeneratedChecks(unittest.TestCase):
    def test_100_seeded_models_against_flat_oracle_and_frozen_replay(self):
        for seed in range(100):
            with self.subTest(seed=seed):
                s = fixture(seed)
                expected = flat_oracle(s)
                r = analyse(s)
                actual = {signature(s, p.ends) for p in r.accepted}
                self.assertEqual(actual, expected)
                self.assertEqual(r.selected is not None, bool(expected))
                for p in r.policies:
                    self.assertEqual(signature(s, replay(s, p)), signature(s, p.ends))
                if expected:
                    rank = lambda ends: tuple(max(e[2][i] for e in ends) for i in range(4))
                    self.assertEqual(rank(signature(s, r.selected.ends)), min(map(rank, expected)))

    def test_flat_oracle_detects_four_deliberate_solver_corruptions(self):
        original = navigator.permitted
        key = navigator.observation_key
        mutations = (
            ("observation_key", lambda s, f: key(s, f) + (f.state,)),
            ("permitted", lambda s, f, m: original(s, f, replace(m, authorised=True))),
            ("permitted", lambda s, f, m: original(replace(s, horizon=8), f, m)),
            ("permitted", lambda s, f, m: original(replace(s, budget=Cost(0, 99, 99, 99)), f, m)),
        )
        for index, (name, corrupted) in enumerate(mutations):
            with self.subTest(mutation=index), patch.object(navigator, name, corrupted):
                differences = []
                for seed in range(100):
                    s = fixture(seed)
                    r = analyse(s)
                    actual = {signature(s, p.ends) for p in r.accepted}
                    if actual != flat_oracle(s):
                        differences.append(seed)
                self.assertTrue(differences, "Flat oracle failed to detect corruption")


if __name__ == "__main__":
    unittest.main()
