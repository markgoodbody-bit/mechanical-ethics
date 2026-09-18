#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from datetime import datetime
from pathlib import Path

BOOK="e232a29c5b6492930ff5b94b005c948f67ba6067"
PROTOCOL="me-route-preservation-reader-v0.1"
TEXT_FIELDS=("requirement","limit","conflict","phrases","misreading")
ALLOWED={"protocol","source_book_blob","condition",*TEXT_FIELDS,"completed_at","reader_note"}

def fail(msg): raise SystemExit("INVALID: "+msg)

def main():
    if len(sys.argv)!=2: fail("usage: validate_result.py result.json")
    data=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if set(data)-ALLOWED: fail("unknown top-level keys")
    if data.get("protocol")!=PROTOCOL: fail("protocol")
    if data.get("source_book_blob")!=BOOK: fail("source_book_blob")
    if data.get("condition") not in {"A","B"}: fail("condition")
    for key in TEXT_FIELDS:
        if not isinstance(data.get(key),str) or not data[key].strip(): fail(key)
    try: datetime.fromisoformat(data["completed_at"].replace("Z","+00:00"))
    except Exception: fail("completed_at")
    if data.get("reader_note") is not None and not isinstance(data["reader_note"],str): fail("reader_note")
    print("VALID_READER_PRESSURE_RESULT_V0_1")
    print("condition="+data["condition"])
    return 0

if __name__=="__main__": raise SystemExit(main())
