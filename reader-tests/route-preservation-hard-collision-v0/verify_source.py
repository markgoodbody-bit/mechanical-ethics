#!/usr/bin/env python3
"""Verify reader-test excerpts are faithful to the current released-reader source."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOK = (ROOT / "MECHANICAL_ETHICS.md").read_text(encoding="utf-8")
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
print("condition_a = exact practical-demand paragraph")
print("condition_b = source-faithful conclusion fragments + fixed questions")
