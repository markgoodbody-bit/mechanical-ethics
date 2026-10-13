"""Source-preserving, AI-attributed Part VI human successor draft; no release.

Builds on PR67's pinned original v0.8 and complete reader without changing it.
Only a clearly bounded proposed bridge is inserted before the original Conclusion.
No browser, network, provider, package install or protected source mutation.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
import re

from research.full_review import build_reader as original
from research.full_review import renderer_owner as owner

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "BRIDGE.md"
OUTPUT = HERE / "positive_successor.html"
MARKER = '<h1 id="conclusion">Conclusion</h1>'
PR67_LABEL = 'aria-label="Unchanged original Mechanical Ethics v0.8 book"'
NEW_LABEL = 'aria-label="Complete original v0.8 book with one clearly bounded AI-proposed editorial insertion"'
OLD_ROUTE = '<a href="#optional-core">Optional compact core</a>'
NEW_ROUTE = '<a href="#horizon-successor">Proposed positive-futures bridge</a> · ' + OLD_ROUTE


def proposal_html(raw: bytes) -> tuple[str, list[str]]:
    """Render deliberately small, explicitly controlled Markdown subset."""
    text = raw.decode("utf-8")
    blocks = re.split(r"\n\s*\n", text.strip())
    if not blocks or blocks[0] != "# A Future Worth Building — proposed Part VI bridge":
        raise ValueError("Proposed bridge title/custody marker changed")
    rendered = []
    headings = []
    for block in blocks[1:]:
        if block.startswith("## "):
            if "\n" in block:
                raise ValueError("Proposed heading not isolated")
            title = block[3:].strip()
            ident = "horizon-" + owner.slug(title)
            if ident in headings:
                raise ValueError("Duplicate proposed heading")
            headings.append(ident)
            rendered.append(f'<h2 id="{ident}">{html.escape(title)}</h2>')
        elif block.startswith("#") or block.startswith("!") or block.startswith("<"):
            raise ValueError("Unsupported proposal block; review source")
        else:
            line = " ".join(s.strip() for s in block.splitlines())
            if re.search(r"(?<!\\)[<>]", line):
                raise ValueError("Raw markup in proposal rejected")
            rendered.append("<p>" + owner.inline(line) + "</p>")
    if len(headings) != 6:
        raise ValueError(f"Expected six complete thematic subsections, got {len(headings)}")
    for essential in ("horizon-the-camera-that-could-settle-everything",
                      "horizon-powerful-helpers-unfinished-relationships",
                      "horizon-the-future-remains-answerable"):
        if essential not in headings:
            raise ValueError("Essential ethical tension absent")
    return "\n".join(rendered), headings


def produce() -> tuple[bytes, dict]:
    base, chapter_map = original.produce()
    if base != original.OUTPUT.read_bytes() or chapter_map != original.MAP.read_bytes():
        raise ValueError("PR67 original reader/source map drift")
    page = base.decode("utf-8")
    if page.count(MARKER) != 1 or page.count(PR67_LABEL) != 1 or page.count(OLD_ROUTE) != 1:
        raise ValueError("PR67 source/target changed: do not guess insertion point")
    if page.index('<h2 id="what-this-can-build">') > page.index(MARKER):
        raise ValueError("Original Part VI order changed")
    raw = SOURCE.read_bytes()
    proposal, heads = proposal_html(raw)
    digest = hashlib.sha256(raw).hexdigest()
    insert = ('<aside id="horizon-successor" class="author-proposal" '
              'aria-label="Unapproved AI-assisted Part VI editorial candidate" '
              f'data-source-sha256="{digest}">'
              '<p class="status">PROPOSED AI-ASSISTED TEXT · NOT MARK-AUTHORED · NOT RELEASED</p>'
              '<p><a href="BRIDGE.md">Read exact source and edit separately</a>. '
              'The complete released book is unchanged in its original file; '
              'this bracketed passage may be accepted, revised, relocated or removed by its human author.</p>'
              + proposal + '</aside>\n')
    page = page.replace(MARKER, insert + MARKER)
    page = page.replace(PR67_LABEL, NEW_LABEL)
    page = page.replace(OLD_ROUTE, NEW_ROUTE)
    # Keep PR67 original and original custody route, but do not misdescribe this derivative.
    page = page.replace(
        'Full ME v0.8 text retained, plus one separately attributed optional compact-core appendix.',
        'Full ME v0.8 text retained; a clearly marked AI-assisted Part VI bridge is proposed '
        'before the original Conclusion, and the separate compact-core appendix remains optional.')
    page = page.replace(
        'The original book below is Mark’s released work; the appendix is a Codex proposal for his editorial decision.',
        'Mark’s original words and four figures are preserved, with the unapproved bridge '
        'clearly bounded and attributed; the optional appendix remains a Codex proposal.')
    if page.count('id="horizon-successor"') != 1 or page.count(MARKER) != 1:
        raise ValueError("Derived reader lost insertion boundary")
    return page.encode("utf-8"), {
        "original_release_sha256": owner.BOOK_SHA256,
        "original_reader_sha256": hashlib.sha256(base).hexdigest(),
        "proposed_bridge_sha256": digest,
        "proposed_section_count": len(heads),
        "original_chapter_count": len(json.loads(chapter_map)["original_sections"]),
        "released_source_changed": False,
        "new_authorship": "AI-assisted; awaiting Mark's decision",
        "original_reader_unmodified": True,
        "browser_visual_qa": "UNRUN",
        "human_acceptance": "UNRUN",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    page, receipt = produce()
    if args.check:
        if OUTPUT.read_bytes() != page:
            raise SystemExit("DRIFT: generated successor differs from authored source")
    else:
        OUTPUT.write_bytes(page)
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()
