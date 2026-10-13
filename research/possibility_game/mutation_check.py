"""Deliberately break seven seams in memory; no source edits or provider access."""
from dataclasses import replace
import io
import unittest
from unittest.mock import patch
from . import engine
from .test_game import GameTests


def main():
    original_project = engine.Game.project
    original_run = engine.run
    original_baseline = engine.baseline
    original_branch = engine.branch

    def authority_leak(self, *args, **kwargs):
        s = original_project(self, *args, **kwargs)
        return replace(s, moves={key: tuple(replace(m, authorised=True) for m in moves)
                                 for key, moves in s.moves.items()})

    def future_launder(*args, **kwargs):
        return dict(original_run(*args, **kwargs), evidence="OBSERVED")

    def null_clock(*args, **kwargs):
        j = original_run(*args, **kwargs)
        for step in j["steps"]:
            if step["action"] == "wait":
                step["after"]["clock"] = step["before"]["clock"]
        return j

    def hidden_observation_collapse(self, *args, **kwargs):
        s = original_project(self, *args, **kwargs)
        if self.name == "betsy":
            return replace(s, states={key: replace(n, observation="No answer available")
                                      if key.endswith("_asked") else n for key, n in s.states.items()})
        return s

    def shared_history(game, journal, *args, **kwargs):
        return dict(original_branch(game, journal, *args, **kwargs), original=journal)

    mutations = (
        ("authority treated as capability", patch.object(engine.Game, "project", authority_leak)),
        ("fabricated future promoted to observed", patch.object(engine, "run", future_launder)),
        ("null freezes world clock", patch.object(engine, "run", null_clock)),
        ("journal verification bypass", patch.object(engine, "verify", lambda *args: True)),
        ("observations cannot distinguish answered preferences", patch.object(engine.Game, "project", hidden_observation_collapse)),
        ("baseline laundered into future evidence", patch.object(engine, "baseline", lambda: dict(original_baseline(), future_worlds="OBSERVED"))),
        ("paired report aliases caller's original history", patch.object(engine, "branch", shared_history)),
    )
    killed = 0
    for label, mutation in mutations:
        with mutation:
            result = unittest.TextTestRunner(stream=io.StringIO()).run(
                unittest.defaultTestLoader.loadTestsFromTestCase(GameTests))
        # An exception alone is not a successful falsification receipt.
        caught = bool(result.failures)
        killed += caught
        print(f"{'CAUGHT' if caught else 'SURVIVED'}: {label}; assertions={len(result.failures)}; errors={len(result.errors)}")
    print(f"{killed}/{len(mutations)} faulty variants caught by assertions")
    if killed != len(mutations):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
