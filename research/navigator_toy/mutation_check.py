"""Five deliberate mechanism corruptions, in memory; never patch source files."""
import io
import unittest
from dataclasses import replace
from unittest.mock import patch

import navigator
from test_navigator import NavigatorTests


def run():
    original_permitted = navigator.permitted
    original_key = navigator.observation_key
    original_analyse = navigator.analyse

    def hidden_oracle(s, f):
        return original_key(s, f) + (f.state,)

    def ignore_authority(s, f, m):
        return original_permitted(s, f, replace(m, authorised=True))

    def ignore_horizon(s, f, m):
        return original_permitted(replace(s, horizon=8), f, m)

    def ignore_resource(s, f, m):
        return original_permitted(replace(s, budget=navigator.Cost(0, 100, 100, 100)), f, m)

    def invent_value(s):
        if s.binding is None:
            s = replace(s, binding=navigator.Binding(frozenset({"safe_separate"})))
        return original_analyse(s)

    mutations = (("hidden state oracle", "observation_key", hidden_oracle),
                 ("permission ignored", "permitted", ignore_authority),
                 ("elapsed time ignored", "permitted", ignore_horizon),
                 ("resource and partner costs ignored", "permitted", ignore_resource),
                 ("missing value invented", "analyse", invent_value))
    survived = []
    for label, name, implementation in mutations:
        with patch.object(navigator, name, implementation):
            # Tests import analyse directly, so patch that entry point too.
            with patch("test_navigator.analyse", navigator.analyse):
                suite = unittest.defaultTestLoader.loadTestsFromTestCase(NavigatorTests)
                result = unittest.TextTestRunner(stream=io.StringIO()).run(suite)
        failures = len(result.failures) + len(result.errors)
        print(f"{label}: {'DETECTED' if failures else 'SURVIVED'} ({failures} failed checks)")
        if not failures:
            survived.append(label)
    if survived:
        raise SystemExit("Mutation survivors: " + repr(survived))
    print("5/5 specified mutations detected; NOT an exhaustive mutation score.")


if __name__ == "__main__":
    run()
