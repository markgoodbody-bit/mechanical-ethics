"""Each mutant breaks one assumption in kernel_models.py; the test suite must then fail.
Runs on a temporary copy; the real file is never changed.

    python research/math_kernel_cc/mutation_check.py
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MUTANTS = [
    ("route existence allows one step too many", "        for _ in range(H):\n            if task.goal in frontier:",
     "        for _ in range(H + 1):\n            if task.goal in frontier:"),
    ("observations ignored when splitting knowledge", "key = (s2, task.observe(w, s, a, s2))", "key = (s2, None)"),
    ("voluntary pool always forms", "joins = pool[0] >= aut[0] and pool[1] >= aut[1]", "joins = True"),
    ("common cause ignored", "    q = (p - c) / (1 - c)\n    both", "    q = p; c = 0.0\n    both"),
    ("Pareto keeps dominated points", "q != p and q[0] <= p[0] and q[1] <= p[1]", "False"),
    ("stranger always right", "heard = (streets[\"alley\"] if honest else not streets[\"alley\"])",
     "heard = (streets[\"alley\"])"),
]

survived = 0
for name, old, new in MUTANTS:
    tmp = tempfile.mkdtemp(prefix="me-kernel-mut-")
    for f in ("kernel_models.py", "test_kernel_models.py"):
        shutil.copy(os.path.join(HERE, f), tmp)
    path = os.path.join(tmp, "kernel_models.py")
    text = io.open(path, encoding="utf-8").read()
    assert text.count(old) == 1, (name, text.count(old))
    io.open(path, "w", encoding="utf-8").write(text.replace(old, new))
    r = subprocess.run([sys.executable, "-m", "unittest", "test_kernel_models"], cwd=tmp,
                       capture_output=True, text=True)
    killed = r.returncode != 0
    survived += not killed
    print("%-46s %s" % (name, "KILLED" if killed else "SURVIVED"))
    shutil.rmtree(tmp, ignore_errors=True)
print("mutants survived: %d of %d" % (survived, len(MUTANTS)))
sys.exit(1 if survived else 0)
