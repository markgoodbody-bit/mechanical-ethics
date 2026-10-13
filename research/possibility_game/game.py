"""Run with python -m research.possibility_game.game. Standard library only."""
import argparse
import json
from pathlib import Path
from .engine import baseline, branch, explore, run, verify
from .scenarios import FACTORIES


def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline authored-world explorer; no predicted future welfare")
    parser.add_argument("scenario", choices=FACTORIES, nargs="?", default="raft")
    parser.add_argument("--goal")
    parser.add_argument("--horizon", type=int)
    parser.add_argument("--origin", help="Manual auditor branch initial world; omitted uses first declared world")
    parser.add_argument("--actions", nargs="*", help="Exact manual actions; not a policy proof")
    parser.add_argument("--save", help="Create a NEW journal file; will not overwrite")
    parser.add_argument("--replay", help="Verify a saved journal against the exact source model")
    parser.add_argument("--branch-at", type=int)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    game = FACTORIES[args.scenario]()
    try:
        if args.replay:
            journal = json.loads(Path(args.replay).read_text(encoding="utf-8"))
            verify(game, journal)
            if args.branch_at is not None:
                if args.horizon is not None or args.origin is not None:
                    raise ValueError("Branch preserves horizon and origin; create a new experiment to change these")
                result = branch(game, journal, args.branch_at, args.actions or (), args.goal)
            else:
                if args.actions is not None or args.goal is not None or args.horizon is not None:
                    raise ValueError("Replay cannot silently change actions, goal or horizon; use branch-at")
                result = journal
        elif args.branch_at is not None:
            raise ValueError("A branch needs a verified replay journal")
        elif args.actions is not None:
            result = run(game, args.origin or game.starts[0], args.actions, args.goal, args.horizon)
        else:
            if args.origin is not None or args.save:
                raise ValueError("Origin/save requires a manual journal via --actions")
            result = explore(game, args.goal, args.horizon)
        if args.save:
            if "receipt_sha256" not in result:
                raise ValueError("Save requires a single journal, not a paired branch report")
            with open(args.save, "x", encoding="utf-8") as stream:
                json.dump(result, stream, indent=2)
        output = {"local_baseline": baseline(), "result": result}
        if args.json or "comparisons" not in result:
            print(json.dumps(output, indent=2))
        else:
            print(f"{game.name}: {result['status']} | goal={result['goal']} | horizon={result['horizon']}")
            print("All future transitions: STIPULATED. Full-world rows below are AUDITOR views.")
            print("Disagreement: " + game.disagreement)
            print(f"Per-world route (oracle only): {result['per_world_route_oracle_only']}")
            for label, comparison in result["comparisons"].items():
                print("\n" + label.upper())
                for end in comparison.get("audit_worlds", ()):
                    print(f"  {end['origin']}: {' -> '.join(end['path']) or 'STOP'} => {end['outcome']}; "
                          f"time/effort/money/imposed={end['cost']}; stop={end['stopped']}")
                    print("  entities: " + json.dumps(end["entities"]))
                if "status" in comparison:
                    print("  " + comparison["status"])
            print("\n--json exposes assumptions, observation-policy keys, rejected authority and exact model hash.")
        return 0
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as error:
        parser.exit(2, "STOP: " + str(error) + "\n")


if __name__ == "__main__":
    main()
