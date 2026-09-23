#!/usr/bin/env python3
"""Verify reader-test excerpts are faithful to the current released-reader source."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BOOK_PATH = ROOT / "MECHANICAL_ETHICS.md"
BOOK = BOOK_PATH.read_text(encoding="utf-8")
EXPECTED_BOOK_BLOB = "0be2ea2aeb178b8387eedf0b72da2d325c6c5caf"
actual_blob = subprocess.check_output(["git", "hash-object", str(BOOK_PATH)], text=True).strip()
assert actual_blob == EXPECTED_BOOK_BLOB, f"reader source blob moved: {actual_blob}"
HERE = Path(__file__).resolve().parent
STUDY = (HERE / "study.html").read_text(encoding="utf-8")

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
assert isolated in STUDY, "study HTML drifted from source reader"

for fragment in context_fragments:
    assert fragment in BOOK, f"source reader missing expected fragment: {fragment}"
    assert fragment in B, f"condition B missing source fragment: {fragment}"
    assert fragment in STUDY, f"study HTML missing source fragment: {fragment}"

for label in ("UNIVERSAL_EACH_BEING", "DEFEASIBLE_DEFAULT", "UNCLEAR"):
    assert label not in BOOK, f"test vocabulary leaked into released reader: {label}"
    assert label not in A, f"priming label leaked into condition A: {label}"
    assert label not in B, f"priming label leaked into condition B: {label}"
    assert label not in STUDY, f"priming label leaked into study HTML: {label}"

print("READER_PRESSURE_SOURCE_BINDING_PASS")
print(f"book_blob = {actual_blob}")
print("condition_a = exact practical-demand paragraph")
print("condition_b = source-faithful conclusion fragments + fixed questions")
print("study_html = source-faithful local-only presentation")
