"""Deterministic, portable, complete ME author-review reading package.

Source-only. Never alters the released book, PR67 reader, artwork or PDF.
Keeps the original relative layout, attributes all proposed material explicitly,
and includes the independent custody/reader-decision record.
"""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import posixpath
from urllib.parse import urlsplit
from zipfile import ZipFile, ZipInfo, ZIP_STORED

from research.full_review.horizon_successor import build
from research.full_review import renderer_owner as owner
from research.full_review import build_reader as original

ROOT = build.original.ROOT
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "ME_v0_9_COMPLETE_AUTHOR_REVIEW_OFFLINE.zip"
STAGING = HERE / "offline_bundle"
MANIFEST = "PACKAGE_MANIFEST.json"
ENTRY = "OPEN_THIS_FIRST.html"
INSTRUCTIONS = "OPEN_THIS_FIRST.txt"

FILES = (
    "research/full_review/positive_successor.html",
    "research/full_review/author_review.html",
    "research/full_review/CHAPTER_MAP.json",
    "research/full_review/EDITORIAL_DECISION.md",
    "research/full_review/horizon_successor/BRIDGE.md",
    "research/full_review/horizon_successor/EDITORIAL_ROUTE.md",
    "research/full_review/horizon_successor/READER_DECISION.md",
    "research/compact_core/START.md",
    "research/compact_core/CASES.md",
    "research/integrated_wave/ARCHITECTURE.md",
    "MECHANICAL_ETHICS.md",
    "MECHANICAL_ETHICS.pdf",
    "README.md",
    "AI_TRAINING_PERMISSION.md",
    *(f"figures/{name}" for name in owner.FIGURES),
)
BINARY = {"MECHANICAL_ETHICS.pdf", *(f"figures/{name}" for name in owner.FIGURES)}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def entry_page() -> bytes:
    text = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mechanical Ethics — complete author-review reading copy</title>
<style>body{max-width:52rem;margin:2rem auto;padding:0 1.25rem;font:1.08rem/1.65 system-ui,sans-serif;color:#243139;background:#faf9f5}a{color:#165a81;overflow-wrap:anywhere}a:focus-visible{outline:3px solid #165a81;outline-offset:3px}h1{line-height:1.2}li{margin:.8rem 0}code{overflow-wrap:anywhere}strong{font-weight:700}</style></head>
<body><main><h1>Mechanical Ethics — one complete review copy</h1>
<p><strong>RESEARCH DRAFT — NOT A RELEASED v0.9 EDITION.</strong> Mark's complete released v0.8 book is retained. A proposed, visibly labelled AI-assisted Part VI bridge and a separate optional Codex appendix are presented for Mark's editorial review. No acceptance, validation, new licence or authorship transfer is implied.</p>
<ol><li><a href="research/full_review/positive_successor.html"><strong>Open the complete formatted author-review book</strong></a> — original full text and four diagrams, proposed bridge clearly labelled, optional appendix</li>
<li><a href="research/full_review/horizon_successor/READER_DECISION.md">What Mark can keep, cut or change</a> — a finite editorial decision sheet and unresolved evidence</li>
<li><a href="MECHANICAL_ETHICS.pdf">Read the original released v0.8 PDF</a> or <a href="MECHANICAL_ETHICS.md">inspect the original Markdown</a></li>
<li><a href="research/full_review/author_review.html">Compare the untouched PR67 complete reader</a> and <a href="research/full_review/CHAPTER_MAP.json">its 55-section map</a></li></ol>
<p>Unzip the entire archive into one folder, then open this HTML file with a local browser. <strong>Do not open it from inside the ZIP preview</strong> if that tool does not extract neighbouring files; the four original pictures and linked review files are stored in their relative folders. Reading does not require an account, server, script, network request or paid service. External references, if followed, may require a connection.</p>
<p>For provenance and version boundaries read <a href="README.md">the source README</a> and <a href="AI_TRAINING_PERMISSION.md">the training-permission notice</a>. The source and ZIP contents have source-level checks; this package does not establish browser/screen-reader usability or moral validity.</p>
<p><a href="research/full_review/horizon_successor/BRIDGE.md">Inspect the AI-proposed prose alone</a> or leave without accepting it.</p></main></body></html>"""
    return (text + "\n").encode("utf-8")


def instructions_text() -> bytes:
    return ("""Mechanical Ethics — complete v0.9 human author-review candidate
============================================================
THIS IS AN AI-ASSISTED RESEARCH DRAFT, NOT MARK'S RELEASED v0.9.

1. Extract the ENTIRE ZIP into a folder, preserving its directories.
2. Open OPEN_THIS_FIRST.html from that extracted folder.
3. Follow "Open the complete formatted author-review book".
4. For the original release, open MECHANICAL_ETHICS.pdf or .md.
5. To make an editorial decision, open
   research/full_review/horizon_successor/READER_DECISION.md.

No server, script, account or internet is required to read the local
book and its four included figures. Internet may be needed for optional
external references. Do not use a ZIP viewer that extracts only the HTML:
its linked source/figures would then be missing.

Released v0.8 source and copyright/permission notices remain intact.
The proposed Part VI bridge is clearly attributed as AI-assisted, and
the optional Codex core remains separately attributed. Actual human
comprehension, accessibility and v0.9 release approval are not claimed.
""").encode("utf-8")


def file_bytes() -> dict[str, bytes]:
    expected, _ = build.produce()
    local = build.OUTPUT.read_bytes()
    if expected != local:
        raise ValueError("Generated proposed whole reader stale: run the build")
    if digest((ROOT / "MECHANICAL_ETHICS.md").read_bytes()) != owner.BOOK_SHA256:
        raise ValueError("Released Markdown source bytes changed")
    if digest(original.OUTPUT.read_bytes()) != digest(original.produce()[0]):
        raise ValueError("Original preserved PR67 reader changed")
    result = {ENTRY: entry_page(), INSTRUCTIONS: instructions_text()}
    for path in FILES:
        file = ROOT / path
        if file.is_symlink() or not file.is_file():
            raise ValueError("Required source missing or unsafe: " + path)
        result[path] = file.read_bytes()
    for name, pin in zip(owner.FIGURES, original.FIGURE_BLOBS):
        raw = result["figures/" + name]
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        if blob != pin:
            raise ValueError("Original figure custody mismatch: " + name)
    return result


class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.urls: list[str] = []
        self.ids: set[str] = set()
    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                raise ValueError("Duplicate html anchor: " + attrs["id"])
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.urls.append(attrs[key])


def check_html_references(blobs: dict[str, bytes]) -> int:
    checked = 0
    for path, raw in blobs.items():
        if not path.endswith(".html"):
            continue
        parser = HTMLLinks()
        parser.feed(raw.decode("utf-8"))
        for value in parser.urls:
            url = urlsplit(value)
            if url.scheme in ("http", "https") or value.startswith("mailto:"):
                continue
            if url.scheme or url.netloc or url.path.startswith("/"):
                raise ValueError("Unsupported local link in package: " + value)
            if not url.path:
                if url.fragment and url.fragment not in parser.ids:
                    raise ValueError("Missing local HTML anchor: " + value)
                continue
            dest = posixpath.normpath(posixpath.join(posixpath.dirname(path), url.path))
            if dest.startswith("../") or dest not in blobs:
                raise ValueError("Offline link not included: " + path + " -> " + value)
            if url.fragment and dest.endswith(".html"):
                target = HTMLLinks()
                target.feed(blobs[dest].decode("utf-8"))
                if url.fragment not in target.ids:
                    raise ValueError("Referenced HTML anchor unavailable: " + value)
            checked += 1
    return checked


def manifest(blobs: dict[str, bytes], links_checked: int) -> bytes:
    return (json.dumps({
        "status": "COMPLETE_LOCAL_AUTHOR_REVIEW_NOT_RELEASED",
        "source": "Mechanical Ethics released v0.8.0 with visibly AI-assisted proposal",
        "released_markdown_sha256": owner.BOOK_SHA256,
        "original_pr67_reader_sha256": digest(original.OUTPUT.read_bytes()),
        "proposed_bridge_sha256": digest(build.SOURCE.read_bytes()),
        "reader_open_path": ENTRY,
        "whole_book_path": "research/full_review/positive_successor.html",
        "html_local_links_checked": links_checked,
        "files": [
            {"path": path, "size": len(data), "sha256": digest(data),
             "role": ("unchanged_original" if path in ("MECHANICAL_ETHICS.md","MECHANICAL_ETHICS.pdf")
                      or path.startswith("figures/") else "editorial_or_support")}
            for path, data in sorted(blobs.items())],
        "evidence_limit": "SOURCE_INTEGRITY_ONLY_NOT_BROWSER_OR_HUMAN_VALIDATION",
    }, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def archive_bytes() -> tuple[bytes, dict]:
    from io import BytesIO
    blobs = file_bytes()
    links = check_html_references(blobs)
    blobs[MANIFEST] = manifest(blobs, links)
    sink = BytesIO()
    with ZipFile(sink, "w", compression=ZIP_STORED) as zipfile:
        for name, raw in sorted(blobs.items()):
            info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_STORED
            info.create_system = 3
            info.external_attr = (0o100644 << 16)
            zipfile.writestr(info, raw)
    return sink.getvalue(), {
        "zip_sha256": digest(sink.getvalue()), "file_count": len(blobs),
        "html_local_links_checked": links,
        "bytes": len(sink.getvalue()), "entry": ENTRY,
        "book": "research/full_review/positive_successor.html",
        "status": "SOURCE_ONLY_OFFLINE_DRAFT",
    }


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--stage", action="store_true", help="Make one-extraction GitHub artifact folder")
    args = parser.parse_args()
    payload, report = archive_bytes()
    if args.check:
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("OFFLINE_ARCHIVE_DRIFT")
    else:
        OUTPUT.write_bytes(payload)
    if args.stage:
        from io import BytesIO
        from shutil import rmtree
        if STAGING.exists():
            rmtree(STAGING)
        with ZipFile(BytesIO(payload)) as book:
            for name in book.namelist():
                path = STAGING / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(book.read(name))
        report["staged_directory"] = str(STAGING)
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
