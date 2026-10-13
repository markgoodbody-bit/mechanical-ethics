#!/usr/bin/env python3
"""Complete v0.8 Mechanical Ethics web edition from PSFH's frozen release copies.
Never rewrites source, substitutes another manuscript, downloads, or publishes.
"""
from __future__ import annotations
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "public/resources/mechanical-ethics/MECHANICAL_ETHICS.md"
FIG_DIR = ROOT / "public/resources/mechanical-ethics/figures"
OUT = ROOT / "out/read/me-v0.8.html"
BOOK_SHA256 = "e3267c3e41e7fdfb44c9a9279250a1a7a38d5b9c389a594fef40cfea75fdbe76"
BOOK_COMMIT = "e2ef746e931161cb70ac46a4eaa122442134e86b"
FIGURES = (
    "figure-1-file-and-life.png",
    "figure-2-correction-window.png",
    "figure-3-two-flats-one-wall.png",
    "figure-4-machine-speed-human-correction.png",
)
BACKTICK = chr(96)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def inline(source):
    text = html.escape(source, quote=True)
    text = re.sub(re.escape(BACKTICK) + r"([^" + re.escape(BACKTICK) + r"]+)" +
                  re.escape(BACKTICK), r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def slug(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def article(source):
    lines = source.replace("\r\n", "\n").split("\n")
    blocks, headings, images = [], [], []
    used = {}
    def paragraph(parts):
        if parts:
            blocks.append("<p>" + inline(" ".join(p.strip() for p in parts)) + "</p>")
    i = 0
    while i < len(lines):
        l = lines[i]
        t = l.strip()
        if not t or t == r"\newpage" or t.startswith("<!-- FIGURE"):
            i += 1
            continue
        heading = re.fullmatch(r"(#{1,3}) (.+)", l)
        if heading:
            level, title = len(heading[1]), heading[2]
            ident = slug(title)
            used[ident] = used.get(ident, 0) + 1
            if used[ident] > 1:
                ident += "-" + str(used[ident])
            headings.append((level, title, ident))
            blocks.append("<h%d id=\"%s\">%s</h%d>" % (level, ident, inline(title), level))
            i += 1
            continue
        figure = re.fullmatch(r"!\[(.+)]\((figures/[a-z0-9.-]+\.png)\)", t)
        if figure:
            if Path(figure[2]).name not in FIGURES:
                raise ValueError("Figure not in released inventory: " + figure[2])
            images.append(figure[2])
            blocks.append('<figure class="book-figure"><img src="%s" alt="%s" loading="lazy"></figure>' %
                          (html.escape("/resources/mechanical-ethics/" + figure[2]), html.escape(figure[1], quote=True)))
            i += 1
            continue
        if t.startswith(BACKTICK * 3):
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith(BACKTICK * 3):
                j += 1
            if j == len(lines):
                raise ValueError("Unclosed code block")
            blocks.append('<pre class="book-code"><code>' +
                          html.escape("\n".join(lines[i+1:j])) + '</code></pre>')
            i = j + 1
            continue
        if t == "$$":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "$$":
                j += 1
            if j == len(lines):
                raise ValueError("Unclosed math block")
            blocks.append('<pre class="book-math" aria-label="Mathematical notation from released source">' +
                          html.escape("\n".join(lines[i+1:j])) + '</pre>')
            i = j + 1
            continue
        if l.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(re.sub(r"^>\s?", "", lines[i]).strip())
                i += 1
            paras, p = [], []
            for line in quote + [""]:
                if not line:
                    if p:
                        paras.append("<p>" + inline(" ".join(p)) + "</p>")
                        p = []
                else:
                    p.append(line)
            blocks.append("<blockquote>" + "\n".join(paras) + "</blockquote>")
            continue
        if re.match(r"^\s*- ", l):
            entries = []
            while i < len(lines):
                current = lines[i]
                if not current.strip() and i+1 < len(lines) and re.match(r"^\s*- ", lines[i+1]):
                    i += 1
                    continue
                match = re.fullmatch(r"(\s*)- (.+)", current)
                if not match:
                    break
                entries.append((len(match[1]), match[2]))
                i += 1
            # Preserve actual Markdown list hierarchy. A nested <ul> must be
            # inside its parent <li>, not directly beneath another <ul>.
            result = []
            depth = 0
            for indent, value in entries:
                if indent not in (0, 2):
                    raise ValueError("Unsupported list indentation: " + str(indent))
                target = 1 if indent == 0 else 2
                if depth == 0:
                    if target != 1:
                        raise ValueError("Nested item without a parent")
                    result.extend(["<ul>", "<li>" + inline(value)])
                    depth = 1
                elif target == depth + 1:
                    result.extend(["<ul>", "<li>" + inline(value)])
                    depth = target
                elif target == depth:
                    result.extend(["</li>", "<li>" + inline(value)])
                elif target < depth:
                    while depth > target:
                        result.extend(["</li>", "</ul>"])
                        depth -= 1
                    result.extend(["</li>", "<li>" + inline(value)])
                else:
                    raise ValueError("List nesting skipped a parent level")
            while depth:
                result.extend(["</li>", "</ul>"])
                depth -= 1
            blocks.append("\n".join(result))
            continue
        if t.startswith("!") or t.startswith("<") or t.startswith(BACKTICK*3):
            raise ValueError("Unsupported or unsafe block at line %d: %s" % (i+1, t[:80]))
        paragraph_lines = []
        while i < len(lines) and lines[i].strip():
            current = lines[i]
            ct = current.strip()
            if (re.match(r"^#{1,3} ", current) or current.startswith(">") or
                re.match(r"^\s*- ", current) or ct in ("$$", r"\newpage") or
                ct.startswith("<!-- FIGURE") or ct.startswith("![") or
                ct.startswith(BACKTICK*3)):
                break
            paragraph_lines.append(ct)
            i += 1
        if not paragraph_lines:
            raise ValueError("Unhandled line %d" % (i + 1))
        paragraph(paragraph_lines)
    if len([h for h in headings if h[0] == 1]) != 17:
        raise ValueError("Lost released h1 headings")
    if len([h for h in headings if h[0] == 2]) != 38:
        raise ValueError("Lost released h2 headings")
    if len(images) != 4 or len(set(images)) != 4:
        raise ValueError("Four original book diagrams must be preserved once")
    return "\n".join(blocks), headings, images


CSS = """
:root{color-scheme:light dark;--bg:#fffdf7;--ink:#223137;--muted:#526169;--accent:#795319;--line:#9daab0}
@media(prefers-color-scheme:dark){:root{--bg:#182126;--ink:#f3f0e8;--muted:#bac5c9;--accent:#ecc386;--line:#687982}}
*{box-sizing:border-box}html{font-size:100%}body{margin:0;background:var(--bg);color:var(--ink);font:1.05rem/1.7 system-ui,sans-serif}
a{color:var(--accent);overflow-wrap:anywhere;text-underline-offset:.2em}a:focus-visible{outline:3px solid var(--accent);outline-offset:4px}
.skip{position:absolute;top:-8rem;left:1rem;padding:.6rem;background:var(--bg)}.skip:focus{top:1rem;z-index:2}
header,main,footer{width:min(calc(100% - 2rem),55rem);margin-inline:auto}header{border-bottom:1px solid var(--line);padding-block:1.5rem}
h1,h2,h3{font-family:Georgia,serif;line-height:1.23;scroll-margin-top:1rem}
h1{font-size:clamp(1.8rem,4.5vw,2.5rem);margin:2.2rem 0 1rem}h2{font-size:clamp(1.4rem,3vw,1.9rem);margin:2rem 0 1rem}
.eyebrow{color:var(--muted);text-transform:uppercase;letter-spacing:.08em;font-size:.82rem}.status{padding-inline-start:1rem;border-inline-start:3px solid var(--accent);font-weight:700}
p{margin:0 0 1.1rem}li{margin:.3rem 0}.contents{border:1px solid var(--line);padding:1rem;margin:1.5rem 0 2rem}
.contents summary{min-height:2.75rem;cursor:pointer;font-weight:700}.contents ol{columns:2;column-gap:2.5rem;padding-left:1.5rem}
.contents li{break-inside:avoid}.contents li.depth-2{margin-left:1rem}blockquote{border-left:3px solid var(--line);padding-left:1rem;margin:1.4rem 0}
.book-figure{text-align:center;margin:1.6rem 0;break-inside:avoid}.book-figure img{display:block;max-width:100%;height:auto;margin-inline:auto}
pre{white-space:pre-wrap;overflow-wrap:anywhere;background:rgba(128,128,128,.08);padding:1rem;max-width:100%}
footer{color:var(--muted);border-top:1px solid var(--line);padding:2rem 0 3rem;margin-top:3rem}
@media(max-width:680px){.contents ol{columns:1}.contents li.depth-2{margin-left:.25rem}body{font-size:1rem}}
@media print{@page{size:A4;margin:18mm}body{font:11pt/1.45 Georgia,serif;color:#000;background:#fff}.contents,.skip{display:none}
header,main,footer{width:100%}h1,h2,h3{break-after:avoid}p,li{orphans:3;widows:3}.book-figure img{max-height:210mm}}
"""


def produce():
    raw = SOURCE.read_bytes()
    if sha(raw) != BOOK_SHA256:
        raise ValueError("Released Mechanical Ethics Markdown changed: STOP")
    text = raw.decode("utf-8")
    content, headings, images = article(text)
    inventory = json.loads((ROOT / "public/resources/inventory.json").read_text(encoding="utf-8"))
    known = {}
    for project in inventory["projects"]:
        for entry in project["files"]:
            if entry.get("current","").startswith("/resources/mechanical-ethics/figures/"):
                known[Path(entry["current"]).name] = entry["sha256"]
    for entry in inventory.get("generated_files", []):
        if entry.get("path","").startswith("mechanical-ethics/figures/"):
            known[Path(entry["path"]).name] = entry["sha256"]
    for figure in FIGURES:
        body = (FIG_DIR / figure).read_bytes()
        if sha(body) != known.get(figure):
            raise ValueError("Figure missing or does not match released source: " + figure)
    nav = "\n".join('<li class="depth-%d"><a href="#%s">%s</a></li>' %
                    (level, ident, html.escape(title)) for level,title,ident in headings)
    header = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="source-sha256" content="%s"><title>Mechanical Ethics v0.8.0 — complete released book</title>
<link rel="canonical" href="https://pleasestartfromhere.com/read/me-v0.8.html">
<style>%s</style></head><body>
<a class="skip" href="#book">Skip to the book</a>
<header><p class="eyebrow"><a href="/">Please Start From Here</a> · Released human reader</p>
<p><a href="/resources/mechanical-ethics/MECHANICAL_ETHICS.md">Original Markdown</a> · <a href="/resources/mechanical-ethics/MECHANICAL_ETHICS.pdf">Released PDF</a></p>
<p class="status">Mechanical Ethics v0.8.0 · RELEASED BASELINE · NOT VALIDATED · ORIGINAL BOOK, NOT v0.9 RESEARCH</p>
<p>Complete formatted version of the released book. The original safety note, all chapters and cases,
four diagrams, the author’s note, historical sources and appendices remain in order.
This web presentation creates no new permission, moral authority, clinical or legal advice.
<a href="/resources/mechanical-ethics/README.md">Source, licence and edition status</a>.</p>
</header><main id="book" tabindex="-1"><details class="contents"><summary>Contents — jump to a chapter</summary>
<nav aria-label="Complete book contents"><ol>%s</ol></nav></details>
<article aria-label="Mechanical Ethics released v0.8 complete source reading">%s</article></main>
<footer><p>Source: complete Mechanical Ethics v0.8.0, GitHub commit
<a href="https://github.com/markgoodbody-bit/mechanical-ethics/blob/%s/MECHANICAL_ETHICS.md">%s</a>.
Original Markdown SHA-256 <code>%s</code>. A released baseline is not ethical validation, an independent
human-comprehension study or a training-rights grant.</p>
<p><a href="/">Return to Please Start From Here</a> · <a href="/resources/mechanical-ethics/MECHANICAL_ETHICS.pdf">Original released PDF</a></p>
</footer></body></html>
""" % (BOOK_SHA256, CSS, nav, content, BOOK_COMMIT, BOOK_COMMIT, BOOK_SHA256)
    return header.encode("utf-8"), headings, images


def main():
    raw, headings, images = produce()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(raw)
    print(json.dumps({"path":str(OUT),"sha256":sha(raw),"bytes":len(raw),
                      "source_sha256":BOOK_SHA256,"headings":len(headings),"figures":len(images)}))


if __name__ == "__main__":
    main()
