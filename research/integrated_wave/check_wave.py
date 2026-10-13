"""One source-custody and regression entry point. No service or model calls.

Requires a Git checkout with the pinned source objects; an exported archive is
not sufficient to establish historical correspondence. Tests remain synthetic.
"""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
RELEASE = "e2ef746e931161cb70ac46a4eaa122442134e86b"
ORIGINS = (
    ("Codex navigator/game", "a46e9bc274a8a4b3c833c87332603bf1de207575",
     ("research/navigator_toy/", "research/possibility_game/")),
    ("Claude mathematics", "42eb1fb1ef8ecc31ef81dea980154a77419b9f19",
     ("research/math_kernel_cc/", "research/ME_V0_9_MATH_KERNEL_CC.md")),
    ("Build joint lab", "d03cde561f0fe063f8eff2adbc77792766cbd027",
     ("research/kernel_lab/",)),
    ("Framework integration", "3a162512d9f898ed62db17fc9232dfd95424db1f",
     ("research/ME_V0_9_CAMPFIRE_", "research/ME_V0_9_FIELD_CASE_",
      "research/ME_V0_9_HUMAN_EDITORIAL_", "research/ME_V0_9_NAVIGATION_READER_")),
    ("Build retention", "8655e8475c47188b6d07cb32dd15c3328c9bce2a",
     ("research/ME_V0_9_BUILD_CROSS_", "research/ME_V0_9_HUMAN_NAVIGATOR_",
      "research/ME_V0_9_V08_TRACE_")),
    ("Build archaeology", "a29eac1a309ba6d1ee5449d63a9e4608d0942ca3",
     ("research/ME_V0_9_COLD_BOOTSTRAP_",)),
    ("Build human companion", "0f604a71d99ca22d7a5d1c9994447e3a76ebe068",
     ("research/human_review/", "research/offline_review/")),
)
SUITES = (
    ("navigator", ("-m", "unittest", "discover", "-s", "research/navigator_toy", "-v")),
    ("possibility game", ("-m", "unittest", "research.possibility_game.test_game", "-v")),
    ("mathematics", ("-m", "unittest", "discover", "-s", "research/math_kernel_cc", "-v")),
    ("joint lab", ("-m", "unittest", "discover", "-s", "research/kernel_lab", "-v")),
    ("human companion source/HTML", ("-m", "unittest", "discover", "-s", "research/offline_review", "-v")),
    ("integration seams", ("-m", "unittest", "research.integrated_wave.test_seams", "-v")),
    ("compact core whole cases", ("-m", "unittest", "research.compact_core.test_examples", "-v")),
    ("navigator negative controls", ("research/navigator_toy/mutation_check.py",)),
    ("game negative controls", ("-m", "research.possibility_game.mutation_check")),
    ("mathematics negative controls", ("research/math_kernel_cc/mutation_check.py",)),
    ("deterministic HTML", ("research/offline_review/build_review.py", "--check")),
)


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def tree(commit):
    result = {}
    for line in git("ls-tree", "-r", commit).splitlines():
        info, path = line.split("\t", 1)
        result[path] = info.split()[2]
    return result


def check_paths(expected, actual, paths):
    """Reject missing/changed blobs, not merely missing headings."""
    faults = [p for p in paths if actual.get(p) != expected[p]]
    if faults:
        raise ValueError("source custody mismatch: " + ", ".join(faults))
    return len(paths)


def custody():
    # Working-file hashes respect repository Git filters, including CRLF rules.
    current = tree("HEAD")
    actual = {}
    for path in current:
        if (ROOT / path).is_file():
            actual[path] = git("hash-object", "--path=" + path, path)
    released = tree(RELEASE)
    results = {"released_files_unchanged": check_paths(released, actual, released)}
    for label, sha, prefixes in ORIGINS:
        origin = tree(sha)
        paths = [p for p in origin if p.startswith(prefixes)]
        if not paths:
            raise ValueError("empty source selection: " + label)
        results[label] = {"source": sha, "files_unchanged": check_paths(origin, actual, paths)}
    return results


def main():
    try:
        receipt = custody()
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"status": "SOURCE_CUSTODY_FAILED_OR_UNKNOWN", "detail": str(exc)}))
        return 1
    print(json.dumps({"custody": receipt, "python": sys.version.split()[0]}, indent=2), flush=True)
    passed = []
    for label, args in SUITES:
        print("CHECK: " + label, flush=True)
        try:
            result = subprocess.run([sys.executable, *args], cwd=ROOT, timeout=180)
        except subprocess.TimeoutExpired:
            print(json.dumps({"status": "CHECK_TIMEOUT", "check": label, "passed": passed}))
            return 1
        if result.returncode:
            print(json.dumps({"status": "CHECK_FAILED", "check": label, "passed": passed}))
            return 1
        passed.append(label)
    print(json.dumps({"status": "SOURCE_CONSOLIDATION_CHECKS_PASS", "checks": passed,
                      "human_use": "NOT_TESTED", "normative_foundation": "UNRESOLVED",
                      "release": "NOT_AUTHORISED"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
