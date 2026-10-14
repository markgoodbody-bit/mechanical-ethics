#!/usr/bin/env python3
"""Mechanical Ethics COMPLETE author-review PDF: released v0.8 + concise B.

Copies the existing released PDF pages without re-typesetting them, inserting
only the separately AI-attributed concise proposal before the original
Conclusion. Does not edit release sources, tags, rights or public services.
Only ReportLab and pypdf, already used by the project's original PDF builder.
No browser, server, provider, download or package installer is invoked.
"""
from __future__ import annotations

import argparse
import hashlib
import html
from io import BytesIO
import json
from pathlib import Path
import re

from pypdf import PdfReader, PdfWriter
from pypdf.generic import Destination
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ORIGINAL_PDF = ROOT / "MECHANICAL_ETHICS.pdf"
ORIGINAL_MD = ROOT / "MECHANICAL_ETHICS.md"
PROPOSAL = HERE / "BRIDGE_CONCISE.md"
OUTPUT = HERE / "complete_author_review_concise_b.pdf"
ORIGINAL_MD_SHA = "e3267c3e41e7fdfb44c9a9279250a1a7a38d5b9c389a594fef40cfea75fdbe76"
EXPECTED = ("The horizon is not the instruction", "A stepping stone at the workshop",
            "The camera that could settle everything", "Powerful helpers, unfinished relationships")
PAGE = (432, 648)
INK, ACCENT = colors.HexColor("#18242D"), colors.HexColor("#A9643A")


def sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def styles():
    base = dict(fontName="Times-Roman", textColor=INK, allowWidows=0, allowOrphans=0)
    return {
        "title": ParagraphStyle("TitleB", **base, fontSize=19, leading=24, spaceAfter=14, keepWithNext=True),
        "section": ParagraphStyle("SectionB", **{**base, "fontName": "Times-Bold", "textColor": ACCENT},
                                  fontSize=12.2, leading=16, spaceBefore=16, spaceAfter=8, keepWithNext=True),
        "body": ParagraphStyle("BodyB", **base, fontSize=10, leading=14.5, spaceAfter=9),
        "notice": ParagraphStyle("NoticeB", **{**base, "fontName": "Helvetica-Bold", "textColor": ACCENT},
                                 fontSize=8.6, leading=12, spaceAfter=13),
    }


def inline(text: str) -> str:
    safe = html.escape(text, quote=False)
    safe = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", safe)
    return re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", safe)


def insertion():
    src = PROPOSAL.read_text(encoding="utf-8")
    parts = re.split(r"\n\s*\n", src.strip())
    if parts.pop(0) != "# A Future Worth Building — proposed Part VI bridge":
        raise ValueError("Unexpected concise proposal title")
    s = styles()
    story = [Paragraph("A Future Worth Building", s["title"]),
             Paragraph("AI-ASSISTED PROPOSAL · NOT MARK-AUTHORED · NOT RELEASED", s["notice"])]
    headings = []
    for block in parts:
        if block.startswith("## "):
            title = block[3:].strip()
            headings.append(title)
            story.append(Paragraph(inline(title), s["section"]))
        elif block.startswith(("#", "<", "!")):
            raise ValueError("Unreviewed Markdown/HTML in proposal")
        else:
            text = " ".join(line.strip() for line in block.splitlines())
            story.append(Paragraph(inline(text), s["body"]))
    if tuple(headings) != EXPECTED:
        raise ValueError("Four expected proposed scenes must remain in source order")
    story.append(Spacer(1, 8))
    story.append(Paragraph("END OF AI-ASSISTED PROPOSAL — MARK'S ORIGINAL CONCLUSION FOLLOWS", s["notice"]))

    def furniture(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#D8D1C6"))
        canvas.line(51, 608, 381, 608)
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(INK)
        canvas.drawString(51, 616, "MECHANICAL ETHICS / AUTHOR REVIEW")
        canvas.drawCentredString(PAGE[0] / 2, 27, f"B{canvas.getPageNumber()}")
        canvas.drawRightString(381, 27, "UNAPPROVED AI-ASSISTED INSERTION")
        canvas.restoreState()

    buf = BytesIO()
    SimpleDocTemplate(buf, pagesize=PAGE, leftMargin=51, rightMargin=51,
                      topMargin=51, bottomMargin=48).build(
                          story, onFirstPage=furniture, onLaterPages=furniture)
    return PdfReader(BytesIO(buf.getvalue())), headings, src


def cover(source_md: bytes, proposal: str):
    s = styles()
    buf = BytesIO()
    story = [
        Paragraph("AUTHOR REVIEW COPY — NOT A v0.9 RELEASE", s["notice"]), Spacer(1, 28),
        Paragraph("Mechanical Ethics", s["title"]),
        Paragraph("When Correction Arrives Too Late", s["section"]),
        Paragraph("Complete released v0.8 original and concise AI-assisted positive-futures proposal (Option B)", s["body"]),
        Spacer(1, 22),
        Paragraph("<b>All 57 original pages are retained unchanged.</b> The five or more "
                  "separately marked proposed pages are placed after What This Can Build "
                  "and before Mark's original Conclusion.", s["body"]),
        Paragraph("Use the PDF bookmarks to navigate. Original printed page numbers and "
                  "Contents remain those of released v0.8; the additional pages are labelled B1 onwards.", s["body"]),
        Paragraph("Only Mark can accept, rewrite, reject, attribute or release any proposed text. "
                  "This is a reading draft, not ethical validation or publishing permission.", s["body"]),
        Spacer(1, 15),
        Paragraph(f"Released Markdown SHA-256: {sha(source_md)[:24]}…", s["notice"]),
        Paragraph(f"AI proposal SHA-256: {sha(proposal.encode('utf-8'))[:24]}…", s["notice"]),
    ]
    SimpleDocTemplate(buf, pagesize=PAGE, leftMargin=54, rightMargin=54,
                      topMargin=57, bottomMargin=44).build(story)
    return PdfReader(BytesIO(buf.getvalue()))


def conclusion_page(original):
    # The original TOC also prints the word "Conclusion": ignore front matter.
    found = [i for i, page in enumerate(original.pages) if i > 10 and
             re.search(r"(?m)^Conclusion\s*$", page.extract_text() or "")]
    if len(found) != 1 or found[0] == 0:
        raise ValueError("The original Conclusion is not on exactly one page")
    before = "\n".join(x.extract_text() or "" for x in original.pages[max(0, found[0] - 3):found[0]])
    if "What This Can Build" not in before:
        raise ValueError("Part VI predecessor not in released original")
    return found[0]


def reproduce(output: Path):
    source_bytes = ORIGINAL_MD.read_bytes()
    if sha(source_bytes) != ORIGINAL_MD_SHA:
        raise ValueError("Original source hash mismatch")
    original = PdfReader(str(ORIGINAL_PDF))
    if len(original.pages) != 57:
        raise ValueError("Original PDF must contain 57 pages")
    split = conclusion_page(original)
    bridge, headings, raw = insertion()
    intro = cover(source_bytes, raw)
    writer = PdfWriter()
    writer.add_page(intro.pages[0])
    for page in original.pages[:split]:
        writer.add_page(page)
    for page in bridge.pages:
        writer.add_page(page)
    for page in original.pages[split:]:
        writer.add_page(page)

    writer.add_outline_item("AUTHOR REVIEW — Important provenance", 0)
    original_root = writer.add_outline_item("Original Mechanical Ethics v0.8", 1)

    def original_outline(items, parent):
        current = parent
        for item in items:
            if isinstance(item, list):
                original_outline(item, current)
            elif isinstance(item, Destination):
                position = original.get_destination_page_number(item)
                position += 1 + (len(bridge.pages) if position >= split else 0)
                current = writer.add_outline_item(item.title, position, parent=parent)
    original_outline(original.outline, original_root)
    proposed_root = writer.add_outline_item(
        "PROPOSED AI-assisted positive futures — Option B", 1 + split)
    for title in headings:
        pos = next((i for i, p in enumerate(bridge.pages)
                    if title in (p.extract_text() or "")), None)
        if pos is None:
            raise ValueError("Missing proposed heading: " + title)
        writer.add_outline_item(title, 1 + split + pos, parent=proposed_root)

    writer.add_metadata({
        "/Title": "Mechanical Ethics — COMPLETE author-review Option B (unreleased)",
        "/Author": "Original book: Mark; inserted proposal: AI-assisted",
        "/Subject": "Released v0.8 PDF pages unchanged; added AI-assisted draft, NOT released v0.9",
    })
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as f:
        writer.write(f)

    check = PdfReader(str(output))
    assert len(check.pages) == 1 + 57 + len(bridge.pages)
    for i, source_page in enumerate(original.pages):
        j = i + 1 + (len(bridge.pages) if i >= split else 0)
        if source_page.extract_text() != check.pages[j].extract_text():
            raise AssertionError(f"Original page text changed: {i + 1}")
    proposed_text = "\n".join(
        x.extract_text() or "" for x in check.pages[1 + split:1 + split + len(bridge.pages)])
    for title in headings:
        if title not in proposed_text:
            raise AssertionError("Lost concise section " + title)
    if not re.search(r"(?m)^Conclusion\s*$",
                     check.pages[1 + split + len(bridge.pages)].extract_text() or ""):
        raise AssertionError("Original Conclusion not immediately after proposal")
    return {
        "status": "UNRELEASED_AUTHOR_REVIEW_ONLY",
        "complete_original_pdf_pages_preserved": 57,
        "original_markdown_sha256": sha(source_bytes),
        "proposal_sha256": sha(raw.encode("utf-8")),
        "added_review_front_matter": 1,
        "added_proposal_pages": len(bridge.pages),
        "total_pdf_pages": len(check.pages),
        "original_diagrams_preserved": 4,
        "pdf_sha256": sha(output.read_bytes()),
        "output": str(output),
        "bytes": output.stat().st_size,
        "browser_keyboard_print_human_review": "NOT_ESTABLISHED",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    print(json.dumps(reproduce(parser.parse_args().output), indent=2))
