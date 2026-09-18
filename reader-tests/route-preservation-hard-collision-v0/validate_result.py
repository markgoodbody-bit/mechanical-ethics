#!/usr/bin/env python3
"""Validate a local reader-test result without network access."""
from __future__ import annotations
import json
import sys
from datetime import datetime
from pathlib import Path

Q1 = {"UNIVERSAL_EACH_BEING", "DEFEASIBLE_DEFAULT", "UNCLEAR"}
Q2 = {"YES", "NO", "UNCLEAR"}
BOOK = "e232a29c5b6492930ff5b94b005c948f67ba6067"
PROTOCOL = "me-route-preservation-reader-v0"

def fail(msg: str) -> None:
    raise SystemExit("INVALID: " + msg)

def main() -> int:
    if len(sys.argv) != 2:
        fail("usage: validate_result.py result.json")
    p = Path(sys.argv[1])
    data = json.loads(p.read_text(encoding="utf-8"))
    allowed = {"protocol","source_book_blob","condition","q1","q2","q3","q4","completed_at","reader_note"}
    if set(data) - allowed:
        fail("unknown top-level keys: " + ", ".join(sorted(set(data)-allowed)))
    if data.get("protocol") != PROTOCOL: fail("protocol")
    if data.get("source_book_blob") != BOOK: fail("source_book_blob")
    if data.get("condition") not in {"A","B"}: fail("condition")
    if data.get("q1") not in Q1: fail("q1")
    if data.get("q2") not in Q2: fail("q2")
    if not isinstance(data.get("q3"), str) or not data["q3"].strip(): fail("q3")
    if not isinstance(data.get("q4"), str) or not data["q4"].strip(): fail("q4")
    try:
        datetime.fromisoformat(data["completed_at"].replace("Z","+00:00"))
    except Exception:
        fail("completed_at")
    if data.get("reader_note") is not None and not isinstance(data["reader_note"], str):
        fail("reader_note")
    print("VALID_READER_PRESSURE_RESULT")
    print(f"condition={data['condition']} q1={data['q1']} q2={data['q2']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
