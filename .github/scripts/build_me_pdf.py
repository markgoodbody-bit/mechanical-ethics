#!/usr/bin/env python3
"""Build the reader-facing Mechanical Ethics PDF from the Markdown source.

This is a layout transform only. The Markdown remains the editable source.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import re
from pathlib import Path

from PIL import Image as PILImage
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    Image,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
)
from reportlab.platypus.tableofcontents import TableOfContents


PAGE_SIZE = (6 * inch, 9 * inch)
INK = colors.HexColor("#18242D")
MUTED = colors.HexColor("#64727A")
ACCENT = colors.HexColor("#A9643A")
PALE = colors.HexColor("#F2EEE7")
LINE = colors.HexColor("#D8D1C6")
WHITE = colors.white


class Rule(Flowable):
    def __init__(self, width: float, color=LINE, thickness: float = 0.6):
        super().__init__()
        self.width = width
        self.height = 6
        self.color = color
        self.thickness = thickness

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 3, self.width, 3)


class BookDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="book",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(
            [
                PageTemplate(id="cover", frames=[frame], onPage=self._cover_page),
                PageTemplate(id="body", frames=[frame], onPage=self._body_page),
            ]
        )

    def _cover_page(self, canvas, doc):
        canvas.saveState()
        canvas.setFillColor(INK)
        canvas.rect(0, 0, PAGE_SIZE[0], PAGE_SIZE[1], stroke=0, fill=1)
        canvas.setFillColor(ACCENT)
        canvas.rect(0, PAGE_SIZE[1] - 16 * mm, PAGE_SIZE[0], 16 * mm, stroke=0, fill=1)
        canvas.setFillColor(colors.HexColor("#C8B8A7"))
        canvas.rect(0, 0, PAGE_SIZE[0], 6 * mm, stroke=0, fill=1)
        canvas.restoreState()

    def _body_page(self, canvas, doc):
        canvas.saveState()
        page = canvas.getPageNumber() - 1
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(doc.leftMargin, PAGE_SIZE[1] - 14 * mm, PAGE_SIZE[0] - doc.rightMargin, PAGE_SIZE[1] - 14 * mm)
        canvas.setFont("Helvetica", 7.2)
        canvas.setFillColor(MUTED)
        canvas.drawString(doc.leftMargin, PAGE_SIZE[1] - 10.8 * mm, "MECHANICAL ETHICS")
        status = "WORKING CANDIDATE - NOT VALIDATED"
        canvas.drawRightString(PAGE_SIZE[0] - doc.rightMargin, 9.5 * mm, status)
        canvas.setFillColor(INK)
        canvas.setFont("Helvetica-Bold", 8)
        canvas.drawCentredString(PAGE_SIZE[0] / 2, 9.5 * mm, str(page))
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        name = flowable.style.name
        if name not in {"H1", "H2"}:
            return
        level = 0 if name == "H1" else 1
        text = flowable.getPlainText()
        key = f"heading-{level}-{self.page}-{hashlib.sha1(text.encode('utf-8')).hexdigest()[:10]}"
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=level, closed=False)
        self.notify("TOCEntry", (level, text, self.page - 1, key))


def make_styles():
    base = getSampleStyleSheet()
    return {
        "cover_kicker": ParagraphStyle(
            "CoverKicker",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#D8C2AE"),
            tracking=1.2,
            spaceAfter=15,
        ),
        "cover_title": ParagraphStyle(
            "CoverTitle",
            parent=base["Title"],
            fontName="Times-Bold",
            fontSize=30,
            leading=34,
            textColor=WHITE,
            alignment=TA_LEFT,
            spaceAfter=18,
        ),
        "cover_subtitle": ParagraphStyle(
            "CoverSubtitle",
            parent=base["Normal"],
            fontName="Times-Italic",
            fontSize=14,
            leading=19,
            textColor=colors.HexColor("#E9E3DB"),
            spaceAfter=24,
        ),
        "cover_status": ParagraphStyle(
            "CoverStatus",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.2,
            leading=12,
            textColor=colors.HexColor("#C8B8A7"),
        ),
        "H1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Times-Bold",
            fontSize=20,
            leading=23,
            textColor=INK,
            keepWithNext=True,
            spaceBefore=0,
            spaceAfter=10,
        ),
        "H2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12.5,
            leading=15,
            textColor=ACCENT,
            keepWithNext=True,
            spaceBefore=13,
            spaceAfter=6,
        ),
        "H3": ParagraphStyle(
            "H3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            textColor=INK,
            keepWithNext=True,
            spaceBefore=10,
            spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=9.7,
            leading=13.5,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=7,
            allowWidows=0,
            allowOrphans=0,
        ),
        "quote": ParagraphStyle(
            "Quote",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=9.2,
            leading=13.1,
            textColor=INK,
            leftIndent=10,
            rightIndent=5,
            borderColor=ACCENT,
            borderWidth=0.6,
            borderPadding=(8, 9, 8, 12),
            backColor=PALE,
            spaceBefore=5,
            spaceAfter=9,
            allowWidows=0,
            allowOrphans=0,
        ),
        "caption": ParagraphStyle(
            "Caption",
            parent=base["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=7.6,
            leading=10.2,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceBefore=3,
            spaceAfter=11,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=9.5,
            leading=13,
            textColor=INK,
            leftIndent=0,
            firstLineIndent=0,
            spaceAfter=3.5,
        ),
        "equation": ParagraphStyle(
            "Equation",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=13,
            textColor=INK,
            alignment=TA_CENTER,
            borderColor=LINE,
            borderWidth=0.5,
            borderPadding=8,
            backColor=colors.HexColor("#F8F6F2"),
            spaceBefore=5,
            spaceAfter=9,
        ),
        "safety": ParagraphStyle(
            "Safety",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=11,
            leading=16,
            textColor=INK,
            borderColor=ACCENT,
            borderWidth=1,
            borderPadding=14,
            backColor=PALE,
            spaceAfter=12,
        ),
        "toc_title": ParagraphStyle(
            "TOCTitle",
            parent=base["Heading1"],
            fontName="Times-Bold",
            fontSize=22,
            leading=26,
            textColor=INK,
            spaceAfter=16,
        ),
    }


def math_markup(value: str) -> str:
    value = value.strip().rstrip(".")
    replacements = {
        r"\mathcal{K}_{C,H}": "K<sub>C,H</sub>",
        r"V_{C,H}(s)": "V<sub>C,H</sub>(s)",
        r"R_H(s)": "R<sub>H</sub>(s)",
        r"T_{protect}(a)": "T<sub>protect</sub>(a)",
        r"T_{harden}(a)": "T<sub>harden</sub>(a)",
        r"T_{det}": "T<sub>det</sub>",
        r"T_{route}": "T<sub>route</sub>",
        r"T_{corr}": "T<sub>corr</sub>",
        r"T_{irr}": "T<sub>irr</sub>",
        r"\tau": "tau",
        r"\in": "in",
        r"\mid": "|",
        r"\neq": "!=",
        r"\varnothing": "empty set",
        r"\{": "{",
        r"\}": "}",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    value = re.sub(r"\\text\{([^}]*)\}", r"\1", value)
    value = re.sub(r"_\{([^}]*)\}", r"<sub>\1</sub>", value)
    value = html.escape(value, quote=False).replace("&lt;sub&gt;", "<sub>").replace("&lt;/sub&gt;", "</sub>")
    return value


def inline_markup(value: str) -> str:
    value = html.escape(value, quote=False)
    value = re.sub(r"\$([^$]+)\$", lambda m: f'<font name="Times-Italic">{math_markup(html.unescape(m.group(1)))}</font>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    value = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', value)
    return value


def source_parts(text: str):
    lines = text.splitlines()
    title_index = lines.index("# Mechanical Ethics: When Correction Arrives Too Late")
    opening_index = lines.index("# Opening - Let Us Begin with an Entity")
    safety_lines = [x for x in lines[1:title_index] if x.strip() and x.strip() != r"\newpage"]
    status = next(x.strip("*") for x in lines[title_index + 1 : opening_index] if x.startswith("**"))
    subtitle = next(x.strip("*") for x in lines[title_index + 1 : opening_index] if x.startswith("*") and not x.startswith("**"))
    return safety_lines, status, subtitle, lines[opening_index:]


def parse_body(lines: list[str], styles, source_dir: Path, content_width: float):
    story = []
    i = 0
    first_h1 = True
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped or stripped.startswith("<!--"):
            i += 1
            continue
        if stripped == r"\newpage":
            if not story or not isinstance(story[-1], PageBreak):
                story.append(PageBreak())
            i += 1
            continue
        if stripped == "$$":
            equation = []
            i += 1
            while i < len(lines) and lines[i].strip() != "$$":
                equation.append(lines[i].strip())
                i += 1
            story.append(Paragraph(math_markup(" ".join(equation)), styles["equation"]))
            i += 1
            continue
        if stripped.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                q = lines[i].lstrip()[1:].strip()
                quote.append(inline_markup(q) if q else "")
                i += 1
            story.append(Paragraph("<br/><br/>".join(x for x in quote if x), styles["quote"]))
            continue
        image_match = re.match(r"!\[([^]]*)\]\(([^)]+)\)", stripped)
        if image_match:
            image_path = source_dir / image_match.group(2)
            with PILImage.open(image_path) as im:
                width, height = im.size
            display_width = content_width
            display_height = display_width * height / width
            story.extend([Spacer(1, 5), Image(str(image_path), width=display_width, height=display_height)])
            i += 1
            continue
        heading = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading:
            level = len(heading.group(1))
            title = inline_markup(heading.group(2))
            if level == 1:
                if not first_h1 and (not story or not isinstance(story[-1], PageBreak)):
                    story.append(PageBreak())
                first_h1 = False
                story.extend([Paragraph(title, styles["H1"]), Rule(content_width, ACCENT, 1.1), Spacer(1, 4)])
            elif level == 2:
                story.append(Paragraph(title, styles["H2"]))
            else:
                story.append(Paragraph(title, styles["H3"]))
            i += 1
            continue
        if re.match(r"^\s*-\s+", raw):
            items = []
            while i < len(lines) and re.match(r"^\s*-\s+", lines[i]):
                match = re.match(r"^(\s*)-\s+(.+)$", lines[i])
                indent = len(match.group(1)) // 2
                para = Paragraph(inline_markup(match.group(2)), styles["bullet"])
                items.append(ListItem(para, leftIndent=indent * 12))
                i += 1
            story.append(
                ListFlowable(
                    items,
                    bulletType="bullet",
                    start="circle",
                    leftIndent=15,
                    bulletFontName="Helvetica",
                    bulletFontSize=6.5,
                    bulletColor=ACCENT,
                    spaceAfter=6,
                )
            )
            continue
        paragraph = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith("#") or nxt.startswith(">") or nxt == "$$" or nxt == r"\newpage" or nxt.startswith("<!--") or re.match(r"^\s*-\s+", lines[i]) or re.match(r"!\[", nxt):
                break
            paragraph.append(nxt)
            i += 1
        joined = " ".join(paragraph)
        style = styles["caption"] if re.fullmatch(r"\*Figure \d+\..*\*", joined) else styles["body"]
        story.append(Paragraph(inline_markup(joined), style))
    return story


def build(source: Path, output: Path):
    text = source.read_text(encoding="utf-8")
    safety, status, subtitle, body_lines = source_parts(text)
    styles = make_styles()
    output.parent.mkdir(parents=True, exist_ok=True)

    doc = BookDocTemplate(
        str(output),
        pagesize=PAGE_SIZE,
        leftMargin=17 * mm,
        rightMargin=17 * mm,
        topMargin=19 * mm,
        bottomMargin=18 * mm,
        title="Mechanical Ethics: When Correction Arrives Too Late",
        author="Mechanical Ethics project",
        subject="Human Reader v0.7.0 working candidate",
        creator="Mechanical Ethics reproducible PDF builder",
        invariant=1,
    )

    story = [
        Spacer(1, 38 * mm),
        Paragraph("MECHANICAL ETHICS", styles["cover_kicker"]),
        Paragraph("When Correction<br/>Arrives Too Late", styles["cover_title"]),
        Paragraph(html.escape(subtitle), styles["cover_subtitle"]),
        Rule(doc.width, colors.HexColor("#6E7D83"), 0.7),
        Spacer(1, 12),
        Paragraph(html.escape(status), styles["cover_status"]),
        Spacer(1, 5),
        Paragraph("WORKING / NOT BASELINE / NOT RELEASE / NOT CANON / NOT VALIDATED", styles["cover_status"]),
        NextPageTemplate("body"),
        PageBreak(),
    ]

    story.extend(
        [
            Paragraph("Safety note for a reader inside harm", styles["H1"]),
            Rule(doc.width, ACCENT, 1.1),
            Spacer(1, 10),
            Paragraph(inline_markup(" ".join(safety)), styles["safety"]),
            PageBreak(),
            Paragraph("Contents", styles["toc_title"]),
        ]
    )
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOC1",
            fontName="Times-Bold",
            fontSize=9.2,
            leading=13,
            textColor=INK,
            leftIndent=0,
            firstLineIndent=0,
            spaceBefore=4,
        ),
        ParagraphStyle(
            "TOC2",
            fontName="Times-Roman",
            fontSize=8.4,
            leading=11.5,
            textColor=MUTED,
            leftIndent=12,
            firstLineIndent=0,
            spaceBefore=1,
        ),
    ]
    story.extend([toc, PageBreak()])
    story.extend(parse_body(body_lines, styles, source.parent, doc.width))
    doc.multiBuild(story)

    reader = PdfReader(str(output))
    if len(reader.pages) < 20:
        raise RuntimeError(f"Unexpectedly short PDF: {len(reader.pages)} pages")
    extracted = "\n".join((page.extract_text() or "") for page in reader.pages)
    required = [
        "Mechanical Ethics",
        "Effective protection must be in place",
        "The Door Out",
        "Futures Still Reachable",
        "What Remains Unfinished",
        "WORKING CANDIDATE",
    ]
    missing = [item for item in required if item not in extracted]
    if missing:
        raise RuntimeError(f"Required PDF text missing: {missing}")
    print(f"Built {output} ({len(reader.pages)} pages, {output.stat().st_size} bytes)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.source.resolve(), args.output.resolve())


if __name__ == "__main__":
    main()
