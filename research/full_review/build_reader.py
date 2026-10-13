"""Whole source-preserving author-review assembly; no new narrative or website.

Reuses Build's complete-book block renderer, copied unchanged from COM PR820
d33f4709853c1792d7501603f125eb42da3f1485. Only article()/CSS are called; its
PSFH produce()/main() and public path configuration are never executed.
"""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re

from . import renderer_owner as owner

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BOOK = ROOT / "MECHANICAL_ETHICS.md"
CORE = ROOT / "research/compact_core/START.md"
OUTPUT = HERE / "author_review.html"
MAP = HERE / "CHAPTER_MAP.json"
OWNER_BLOB = "df14757ed2a7b20c5d6dfbcacc49df2fdba34358"
FIGURE_BLOBS = (
    "828de31780ef8765b2a0136ac3a327083d0c751a",
    "181a3fc05dfec7e5be88deaf505f11422deff1e4",
    "7e71dbb9b2fbe3e3df1a4421160a42a1aaf1a4f7",
    "eab574b5c8f26544eaf0d6a1a754d9df0037d9ab",
)


def blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def optional_core(text):
    """Render retained core as an optional appendix, not a new compulsory preface."""
    result, paragraph, fenced, code = [], [], False, []
    def core_inline(value):
        formatted = owner.inline(value)
        def link(match):
            label, target = match.groups()
            if not (target.startswith(("https://", "../", "../../")) or target == "CASES.md"):
                raise ValueError("Unexpected optional-core link: " + target)
            if target == "CASES.md":
                target = "../compact_core/CASES.md"
            return '<a href="' + target + '">' + label + '</a>'
        return re.sub(r"\[([^\]]+)\]\(([^\s)]+)\)", link, formatted)
    def flush():
        if paragraph:
            result.append("<p>" + core_inline(" ".join(paragraph)) + "</p>")
            paragraph.clear()
    for line in text.splitlines():
        if line.startswith("```"):
            flush()
            if fenced:
                result.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
                code.clear()
            fenced = not fenced
        elif fenced:
            code.append(line)
        elif not line.strip():
            flush()
        elif re.match(r"^#{1,3} ", line):
            flush()
            title = re.sub(r"^#+ ", "", line)
            level = min(3, len(line.split()[0]) + 1)
            result.append(f"<h{level}>" + core_inline(title) + f"</h{level}>")
        else:
            paragraph.append(line.strip())
    flush()
    if fenced:
        raise ValueError("Unclosed optional-core code block")
    return "\n".join(result)


def produce():
    raw = BOOK.read_bytes()
    if hashlib.sha256(raw).hexdigest() != owner.BOOK_SHA256:
        raise ValueError("Original book changed: author decision required")
    renderer_raw = (HERE / "renderer_owner.py").read_bytes()
    if blob(renderer_raw) != OWNER_BLOB:
        raise ValueError("Retained owner renderer changed")
    for name, expected in zip(owner.FIGURES, FIGURE_BLOBS):
        if blob((ROOT / "figures" / name).read_bytes()) != expected:
            raise ValueError("Original figure changed: " + name)
    body, headings, _ = owner.article(raw.decode("utf-8"))
    body = body.replace("/resources/mechanical-ethics/figures/", "../../figures/")
    core_raw = CORE.read_bytes()
    appendix = optional_core(core_raw.decode("utf-8"))
    nav = "\n".join(f'<li class="depth-{level}"><a href="#{ident}">{html.escape(title)}</a></li>'
                    for level, title, ident in headings)
    by_title = {title: ident for _, title, ident in headings}
    creation = by_title["Interlude - The Saturday Workshop"]
    protection = by_title["A Timing Condition"]
    source_lines = raw.decode("utf-8").splitlines()
    starts = [(n + 1, line.lstrip("# ")) for n, line in enumerate(source_lines)
              if re.match(r"^#{1,3} ", line)]
    chapter_map = {"book_commit": owner.BOOK_COMMIT, "book_sha256": owner.BOOK_SHA256,
                   "renderer_commit": "d33f4709853c1792d7501603f125eb42da3f1485",
                   "renderer_blob": OWNER_BLOB, "core_sha256": hashlib.sha256(core_raw).hexdigest(),
                   "original_sections": [
                       {"heading": title, "start_line": start,
                        "end_line": starts[i+1][0]-1 if i+1 < len(starts) else len(source_lines),
                        "anchor": headings[i][2], "before": "released v0.8 original",
                        "after": "same text/order in full review body", "rewrite": "NONE"}
                       for i, (start, title) in enumerate(starts)],
                   "proposed_addition": {"anchor": "optional-core", "author": "Codex Windows proposal",
                                         "placement": "optional appendix after all original appendices"}}
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mechanical Ethics — complete v0.9 author-review assembly</title><style>{owner.CSS}
@media print{{details>section{{display:block}}details>summary{{font-weight:bold}}}}
</style></head><body><a class="skip" href="#book">Skip to complete original book</a>
<header><p class="eyebrow">Complete author-review assembly · research only · not a released v0.9 edition</p>
<p>Full ME v0.8 text retained, plus one separately attributed optional compact-core appendix.
The original book below is Mark’s released work; the appendix is a Codex proposal for his editorial decision.</p>
<nav aria-label="Choose a reading route"><a href="#book">Read the complete book</a> ·
<a href="#{protection}">Protection and correction</a> · <a href="#{creation}">Creation and formation</a> ·
<a href="#optional-core">Optional compact core</a> · <a href="EDITORIAL_DECISION.md">Before/after and author choices</a></nav>
<p><a href="../../MECHANICAL_ETHICS.md">Unchanged original Markdown</a> ·
<a href="../../MECHANICAL_ETHICS.pdf">Released PDF</a> · <a href="CHAPTER_MAP.json">55-section custody map</a></p>
</header><main id="book" tabindex="-1"><details class="contents"><summary>Complete book contents</summary>
<nav aria-label="Original chapter navigation"><ol>{nav}</ol></nav></details>
<article id="original-book" aria-label="Unchanged original Mechanical Ethics v0.8 book">{body}</article>
<details id="optional-core"><summary>Optional v0.9 proposal — compact core, by Codex Windows</summary>
<section aria-label="Proposed AI-assisted addition, not approved by the human author">
<p>This appendix is not Mark-authored or released, and is not required to read the book.
<a href="../compact_core/START.md">Inspect its exact Markdown</a> ·
<a href="../compact_core/CASES.md">Five complete challenge cases</a></p>{appendix}</section></details></main>
<footer><p>Original book source: {owner.BOOK_COMMIT}; SHA-256 {owner.BOOK_SHA256}.
All original safety, authorship, historical notes and rights/status passages are retained in the body.
Presentation and appendix selection confer no new rights or release authority.</p></footer></body></html>
'''
    return page.encode("utf-8"), (json.dumps(chapter_map, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    page, mapping = produce()
    if args.check:
        if OUTPUT.read_bytes() != page or MAP.read_bytes() != mapping:
            raise SystemExit("Generated author review differs from its source")
        print("PASS deterministic whole author-review assembly and chapter map")
    else:
        OUTPUT.write_bytes(page)
        MAP.write_bytes(mapping)
        print(json.dumps({"bytes": len(page), "book_sha256": owner.BOOK_SHA256,
                          "original_sections": 55, "original_figures": 4,
                          "source_changed": False, "human_comprehension": "NOT_TESTED"}))


if __name__ == "__main__":
    main()
