#!/usr/bin/env python3
"""Verify reader-test excerpts are faithful to the current released-reader source."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BOOK_PATH = ROOT / "MECHANICAL_ETHICS.md"
BOOK = BOOK_PATH.read_text(encoding="utf-8")
EXPECTED_BOOK_BLOB = "e232a29c5b6492930ff5b94b005c948f67ba6067"
actual_blob = subprocess.check_output(["git", "hash-object", str(BOOK_PATH)], text=True).strip()
assert actual_blob == EXPECTED_BOOK_BLOB, f"reader source blob moved: {actual_blob}"
HERE = Path(__file__).resolve().parent

A = (HERE / "condition-a.txt").read_text(encoding="utf-8")
B = (HERE / "condition-b.txt").read_text(encoding="utf-8")

isolated = (
    "The practical demand is modest to state and difficult to meet: keep the affected being present in the decision. "
    "Keep at least one genuinely usable route open. Place the burden of complexity and delay on those with the power "
    "to carry it. And act before correction becomes only an account of what was lost."
)

context_fragments = [
    "This framework does not tell anyone what makes a life meaningful.",
    "Several protected paths may also conflict.",
    "Mechanical Ethics can expose those competing clocks and burdens, but it does not supply a universal rule for ranking them.",
    isolated,
]

assert isolated in BOOK, "source reader no longer contains isolated practical-demand text"
assert isolated in A, "condition A drifted from source reader"
assert isolated in B, "condition B drifted from source reader"

for fragment in context_fragments:
    assert fragment in BOOK, f"source reader missing expected fragment: {fragment}"
    assert fragment in B, f"condition B missing source fragment: {fragment}"

assert "UNIVERSAL_EACH_BEING" not in BOOK, "test vocabulary leaked into released reader"
assert "DEFEASIBLE_DEFAULT" not in BOOK, "test vocabulary leaked into released reader"

print("READER_PRESSURE_SOURCE_BINDING_PASS")
print(f"book_blob = {actual_blob}")
print("condition_a = exact practical-demand paragraph")
print("condition_b = source-faithful conclusion fragments + fixed questions")
