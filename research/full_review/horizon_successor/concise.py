"""Second, shorter AI-attributed Part VI author-review OPTION; no source rewrite.

Reuses the fully verified full candidate and replaces only its bounded AI aside.
Does not touch the released v0.8, PR67 original, full proposal or conclusion.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
import re

from research.full_review.horizon_successor import build

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "BRIDGE_CONCISE.md"
OUTPUT = HERE.parent / "positive_successor_concise.html"
EXPECTED_HEADINGS = (
    "The horizon is not the instruction",
    "A stepping stone at the workshop",
    "The camera that could settle everything",
    "Powerful helpers, unfinished relationships",
)
ASIDE = re.compile(r'<aside id="horizon-successor"[^>]*>.*?</aside>\n', flags=re.S)


def chapters(raw: bytes) -> tuple[str, list[str]]:
    text = raw.decode("utf-8")
    blocks = re.split(r"\n\s*\n", text.strip())
    if not blocks or blocks[0] != "# A Future Worth Building — proposed Part VI bridge":
        raise ValueError("Concise candidate title/custody marker changed")
    headings: list[str] = []
    rendered: list[str] = []
    for block in blocks[1:]:
        if block.startswith("## "):
            if "\n" in block:
                raise ValueError("Concise heading not isolated")
            heading = block[3:].strip()
            headings.append(heading)
            rendered.append(f'<h2 id="horizon-{build.owner.slug(heading)}">AI-assisted proposal — {html.escape(heading)}</h2>')
        elif block.startswith(("#", "!", "<")):
            raise ValueError("Unsupported concise proposal block")
        else:
            line = " ".join(x.strip() for x in block.splitlines())
            if re.search(r"(?<!\\)[<>]", line):
                raise ValueError("Unexpected raw markup in concise source")
            rendered.append("<p>" + build.owner.inline(line) + "</p>")
    if tuple(headings) != EXPECTED_HEADINGS:
        raise ValueError("Concise proposal headings or order changed")
    return "\n".join(rendered), headings


def assert_kept_scenes_verbatim():
    full = build.SOURCE.read_text(encoding="utf-8")
    brief = SOURCE.read_text(encoding="utf-8")
    def sections(source):
        parts = re.split(r"(?=^## )", source, flags=re.M)
        return {m.group(1): part.strip() for part in parts[1:]
                if (m := re.match(r"## ([^\n]+)", part))}
    a, b = sections(full), sections(brief)
    for title in EXPECTED_HEADINGS[1:]:
        if a.get(title) != b.get(title):
            raise ValueError("Kept scene changed versus full candidate: " + title)
    return {title: hashlib.sha256(b[title].encode("utf-8")).hexdigest()
            for title in EXPECTED_HEADINGS[1:]}


def produce() -> tuple[bytes, dict]:
    kept = assert_kept_scenes_verbatim()
    full_bytes, full_receipt = build.produce()
    if full_bytes != build.OUTPUT.read_bytes():
        raise ValueError("Full candidate not current; preserve first, then derive")
    full = full_bytes.decode("utf-8")
    matches = ASIDE.findall(full)
    if len(matches) != 1:
        raise ValueError("Exactly one bounded full AI insertion expected")
    original_aside = matches[0]
    if "END OF AI-ASSISTED PROPOSAL — MARK’S ORIGINAL CONCLUSION FOLLOWS" not in original_aside:
        raise ValueError("Full proposal source/author boundary missing")
    proposal_source = SOURCE.read_bytes()
    proposal, headings = chapters(proposal_source)
    sha = hashlib.sha256(proposal_source).hexdigest()
    entries = "".join(
        f'<li><a href="#horizon-{build.owner.slug(title)}">AI-assisted proposal — {html.escape(title)}</a></li>'
        for title in headings
    )
    short_aside = (
        '<aside id="horizon-successor" class="author-proposal" '
        'aria-label="Unapproved concise AI-assisted Part VI editorial alternative" '
        f'data-source-sha256="{sha}">'
        '<p class="status">AI-ASSISTED PROPOSAL · NOT MARK-AUTHORED · NOT RELEASED · CONCISE OPTION</p>'
        '<nav class="proposal-nav" aria-label="Four AI-assisted proposed sections">'
        '<p>Proposed sections</p><ul>' + entries + '</ul></nav>'
        + proposal
        + '<p class="proposal-end">END OF AI-ASSISTED PROPOSAL — MARK’S ORIGINAL CONCLUSION FOLLOWS</p>'
        '<p>Compare <a href="horizon_successor/BRIDGE_CONCISE.md">exact concise source</a> '
        'and <a href="horizon_successor/A_B_DECISION.md">A/B decision sheet</a>.</p>'
        '</aside>\n'
    )
    short = full.replace(original_aside, short_aside)
    if short == full or short.count('<h1 id="conclusion">Conclusion</h1>') != 1:
        raise ValueError("Concise proposal failed to preserve original Conclusion")
    if short.replace(short_aside, original_aside, 1) != full:
        raise ValueError("Concise proposal is not a single reversible insertion replacement")
    # Keep the full candidate untouched byte-for-byte, including all its labels
    # and metadata; only the concise derivative has the alternative wording.
    return short.encode("utf-8"), {
        "full_candidate_sha256": hashlib.sha256(full_bytes).hexdigest(),
        "full_source_sha256": full_receipt["proposed_bridge_sha256"],
        "concise_source_sha256": sha,
        "concise_section_count": len(headings),
        "verbatim_scene_sha256": kept,
        "released_source_changed": False,
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
            raise SystemExit("DRIFT: concise candidate output differs from pinned sources")
    else:
        OUTPUT.write_bytes(page)
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()
