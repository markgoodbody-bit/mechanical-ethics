#!/usr/bin/env python3
"""Deterministically render the exact PR63 human research text to offline HTML.

No network, Markdown dependency, browser scripts, third-party fonts or telemetry.
This supports only the Markdown constructs present in the frozen review source.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = ROOT / "human_review" / "ME_V0_9_SHORT_HUMAN_REVIEW_CANDIDATE_20261013.md"
TEMPLATE = HERE / "layout.html"
OUTPUT = HERE / "human_review_offline.html"
EXPECTED_SOURCE_BLOB = "5b435896169f8de7d2508ed658ce5047f84ceebb"


def blob_id(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def heading_id(label: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def inline(value: str) -> str:
    result = html.escape(value, quote=True)
    def link(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2)
        if not (url.startswith(("https://", "http://")) or
                re.fullmatch(r"[A-Za-z0-9_./-]+", url)):
            raise ValueError("unsupported link scheme or characters")
        return '<a href="' + url + '">' + label + '</a>'
    result = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+|[A-Za-z0-9_./-]+)\)", link, result)
    result = re.sub(r"\x60([^\x60]+)\x60", r"<code>\1</code>", result)
    result = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", result)
    result = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", result)
    return result


def article_and_toc(markdown: str) -> tuple[str, str]:
    result: list[str] = []
    contents: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    heading_seen: set[str] = set()

    def flush_paragraph() -> None:
        if paragraph:
            result.append("<p>" + inline(" ".join(paragraph)) + "</p>")
            paragraph.clear()

    def flush_list() -> None:
        if list_items:
            result.append("<ul>")
            result.extend("<li>" + inline(item) + "</li>" for item in list_items)
            result.append("</ul>")
            list_items.clear()

    for line in markdown.splitlines():
        if not line.strip():
            flush_paragraph()
            flush_list()
            continue
        match = re.fullmatch(r"(#{1,3}) (.+)", line)
        if match:
            flush_paragraph()
            flush_list()
            level, title = len(match.group(1)), match.group(2)
            slug = heading_id(title)
            if slug in heading_seen:
                raise ValueError("duplicate heading anchor: " + slug)
            heading_seen.add(slug)
            result.append(f'<h{level} id="{slug}">{inline(title)}</h{level}>')
            if level == 3:
                contents.append(f'<li><a href="#{slug}">{html.escape(title, quote=True)}</a></li>')
            continue
        if line == "---":
            flush_paragraph()
            flush_list()
            result.append("<hr>")
            continue
        if line.startswith("- "):
            flush_paragraph()
            list_items.append(line[2:])
            continue
        if line.startswith(("# ", "## ", "### ")):
            raise ValueError("unsupported heading")
        if list_items:
            flush_list()
        paragraph.append(line.strip())

    flush_paragraph()
    flush_list()
    return "\n".join(result), "\n".join(contents)


def produce() -> bytes:
    raw = SOURCE.read_bytes()
    source_blob = blob_id(raw)
    if source_blob != EXPECTED_SOURCE_BLOB:
        raise ValueError(f"source text changed: {source_blob} != {EXPECTED_SOURCE_BLOB}")
    text = raw.decode("utf-8")
    article, toc = article_and_toc(text)
    template = TEMPLATE.read_text(encoding="utf-8")
    for marker in ("@@ARTICLE@@", "@@CONTENTS@@", "@@SOURCE_BLOB@@"):
        if marker not in template:
            raise ValueError("missing template marker " + marker)
    page = template.replace("@@ARTICLE@@", article).replace(
        "@@CONTENTS@@", toc).replace("@@SOURCE_BLOB@@", source_blob)
    if "@@" in page:
        raise ValueError("unexpanded marker")
    return page.encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if committed HTML differs")
    args = parser.parse_args()
    page = produce()
    if args.check:
        if OUTPUT.read_bytes() != page:
            raise SystemExit("FAIL: committed HTML differs from deterministic source")
        print("PASS exact deterministic source-to-HTML equality", len(page), "bytes")
    else:
        OUTPUT.write_bytes(page)
        print("WROTE", OUTPUT, len(page), "bytes")


if __name__ == "__main__":
    main()
