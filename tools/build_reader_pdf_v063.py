#!/usr/bin/env python3
from pathlib import Path
import re, subprocess, sys

if len(sys.argv) != 3:
    print('usage: build_reader_pdf_v063.py input.md output.pdf', file=sys.stderr)
    raise SystemExit(2)

src = Path(sys.argv[1]).resolve()
out_pdf = Path(sys.argv[2]).resolve()
work = out_pdf.parent
work.mkdir(parents=True, exist_ok=True)
figdir = (Path(__file__).resolve().parent / 'figures').resolve()
text = src.read_text(encoding='utf-8')
text = text.replace('\\newpage', '<div class="pagebreak"></div>')

title_block = '''# Mechanical Ethics: When Correction Arrives Too Late

**Human Reader v0.6.3 - REVIEW SCOPE AND BOUNDED ANSWERABILITY REPAIR CANDIDATE**

*A human-facing Mechanical Ethics reader*'''
title_html = '''<section class="title-page">
<div class="book-title">Mechanical Ethics</div>
<div class="book-subtitle">When Correction Arrives Too Late</div>
<div class="book-version">HUMAN READER V0.6.3</div>
<div class="book-status">REVIEW SCOPE AND BOUNDED ANSWERABILITY REPAIR CANDIDATE</div>
<div class="book-deck">A human-facing Mechanical Ethics reader</div>
</section>'''
if title_block not in text: raise SystemExit('title block not found')
text = text.replace(title_block, title_html, 1)

figs = {
    1: ('THE FILE AND THE LIFE', 'Figure 1. The file and the life: two factual accounts of the same night that are not equivalent.'),
    2: ('THE CORRECTION WINDOW', 'Figure 2. The correction window: effective protection must be in place before the threatened path hardens beyond comparable repair.'),
    3: ('TWO FLATS, ONE WALL', 'Figure 3. Two flats, one wall: the same cause reaches an owner with authority and is repaired within the month, while the tenant route returns a reference number and closes on move-out.'),
    4: ('MACHINE SPEED VERSUS HUMAN CORRECTION', 'Figure 4. Machine speed and human correction: the machine completes its action at scale before human correction has finished assembling.'),
}
for n, (marker, caption) in figs.items():
    exact = f'<!-- FIGURE {n}: {marker} -->\n*{caption}*'
    replacement = f'<figure class="diagram figure-{n}">\n<img src="{(figdir / f"figure-{n}.svg").as_uri()}" alt="{marker.title()}">\n<figcaption>{caption}</figcaption>\n</figure>'
    if exact not in text: raise SystemExit(f'figure {n} block not found')
    text = text.replace(exact, replacement, 1)

text = text.replace('# Contents\n\n', '# Contents\n\n<div class="contents-start"></div>\n\n', 1)
text = text.replace('\n<div class="pagebreak"></div>\n\n# Opening - Let Us Begin with an Entity', '\n<div class="contents-end"></div>\n\n<div class="pagebreak"></div>\n\n# Opening - Let Us Begin with an Entity', 1)

pre_md = work / (out_pdf.stem + '.prepared.md')
html = work / (out_pdf.stem + '.html')
css = work / 'reader.css'
pre_md.write_text(text, encoding='utf-8')
css.write_text(r'''
@page { size: A4; margin: 17mm 19mm 18mm 19mm; @bottom-center { content: counter(page); font-family: Arimo, sans-serif; font-size: 7.8pt; color: #2f2f2f; } }
html { font-size: 11.15pt; }
body { font-family: Caladea, 'DejaVu Serif', serif; color: #171717; line-height: 1.33; margin: 0; hyphens: none; text-rendering: optimizeLegibility; }
p { margin: 0 0 7.2pt 0; orphans: 2; widows: 2; }
strong { font-weight: 700; } em { font-style: italic; }
h1, h2, h3, h4 { font-family: Caladea, 'DejaVu Serif', serif; color: #151515; font-weight: 700; break-after: avoid; page-break-after: avoid; }
h1 { font-size: 20.2pt; line-height: 1.12; margin: 0 0 15pt 0; }
h2 { font-size: 16.2pt; line-height: 1.16; margin: 14pt 0 8pt 0; }
h3 { font-size: 13.2pt; line-height: 1.18; margin: 12pt 0 6pt 0; }
h4 { font-size: 11.7pt; margin: 10pt 0 5pt 0; }
ul, ol { margin: 2pt 0 7pt 0; padding-left: 1.45em; } li { margin: 0 0 1.2pt 0; } li > p { margin: 0; }
blockquote { margin: 9pt 0 11pt 0; padding: 8pt 12pt 7pt 12pt; border-left: 2.5pt solid #b89144; background: #f1efeb; break-inside: auto; }
blockquote p { margin-bottom: 7pt; } blockquote p:last-child { margin-bottom: 0; }
blockquote p:first-child strong { font-family: Arimo, sans-serif; font-size: 9.2pt; letter-spacing: 1.4pt; color: #8a5b13; }
.pagebreak { break-before: page; page-break-before: always; height: 0; }
.title-page { height: 246mm; display: flex; flex-direction: column; align-items: center; text-align: center; padding-top: 66mm; box-sizing: border-box; }
.book-title { font-family: Caladea, serif; font-size: 34pt; font-weight: 700; line-height: 1.0; }
.book-subtitle { font-family: Caladea, serif; font-size: 17pt; font-style: italic; color: #57524d; margin-top: 9pt; }
.book-version { font-family: Arimo, sans-serif; font-size: 9.3pt; font-weight: 700; letter-spacing: 2.2pt; color: #918b83; margin-top: 39pt; }
.book-status { font-family: Arimo, sans-serif; font-size: 9.3pt; font-weight: 700; letter-spacing: 2.2pt; color: #918b83; margin-top: 4pt; }
.book-deck { font-family: Caladea, serif; font-size: 11.8pt; font-style: italic; color: #57524d; margin-top: 11pt; }
.contents-page h1 { margin-bottom: 10pt; }
.contents-list { font-family: Arimo, sans-serif; font-size: 8.55pt; line-height: 1.13; }
.contents-line { margin: 0; } .contents-line.indent-1 { padding-left: 1.45em; }
figure.diagram { margin: 11pt auto 9pt auto; break-inside: avoid; page-break-inside: avoid; text-align: center; }
figure.diagram img { display: block; max-width: 100%; height: auto; margin: 0 auto; }
figure.figure-1 img { width: 75%; } figure.figure-2 img { width: 85%; } figure.figure-3 img, figure.figure-4 img { width: 90%; }
figure.figure-3, figure.figure-4 { break-before: page; page-break-before: always; break-after: page; page-break-after: always; }
figcaption { font-family: Caladea, serif; font-size: 8.2pt; line-height: 1.3; font-style: italic; color: #66615b; text-align: left; margin-top: 5pt; }
math { font-size: 1.12em; } .display.math { display: block; text-align: center; margin: 7pt 0 9pt 0; }
h1 + p, h2 + p, h3 + p { break-before: avoid; }
#sources-and-references ~ p, #sources-and-references ~ ul { font-size: 9.3pt; }
''', encoding='utf-8')

subprocess.run(['pandoc', str(pre_md), '--from=markdown+raw_html+raw_tex+tex_math_dollars', '--to=html5', '--standalone', '--mathml', '--metadata', 'title=Mechanical Ethics: When Correction Arrives Too Late', '--metadata', 'subject=Human Reader v0.6.3 - Review Scope and Bounded Answerability Repair Candidate', '--css', str(css), '-o', str(html)], check=True)
h = html.read_text(encoding='utf-8')
h = re.sub(r'<header id="title-block-header".*?</header>', '', h, count=1, flags=re.S)
contents_lines = [('Opening - Let Us Begin with an Entity',0),('How to Read This Book',0),('A Timing Condition',0),('Part I - The Door',0),('1. A Door You Cannot Reach',1),('2. Who Builds the Maze',1),('3. Process Becomes Distance',1),('Part II - The Clock',0),('4. Help Before the Loss Sets',1),('5. The Strategic Unknown',1),('6. Slow Harm',1),('Short Case - The Finance Appeal That Arrived Too Late',1),('Part III - The Witness',0),('7. When There Is No Enforcer',1),('8. Custody',1),('9. Residue',1),('Interlude - Two Flats, One Wall',1),('Part IV - The Machine',0),('Before the Machine - The Predator Position',1),('10. Who Pays for Complexity',1),('11. The Second Person',1),('12. Correction Theatre',1),('Historical Note - Challenger and the Cost of Proceeding',1),('The Machine-Speed Brake',1),('Part V - After the Fall',0),('13. Peace as Evidence',1),('14. What Remains Open',1),('15. A Human Standard for Answerability',1),('Part VI - Futures Still Reachable',0),('Interlude - The Saturday Workshop',1),('16. The Conditions of Hope',1),('17. Care Without Possession',1),('18. Kindness as the Placement of Burden',1),('Conclusion',0),("Author's Note - How This Began",0),('Appendix A - Middle-Out Reconstruction Notes',0),('Appendix B - What Remains Unfinished',0),('Appendix C - Status, Lineage, Sources, and the Two-Artifact Pair',0)]
contents_html = '<section class="contents-page"><h1>Contents</h1><div class="contents-list">' + ''.join(f'<div class="contents-line indent-{indent}">{line}</div>' for line, indent in contents_lines) + '</div></section><div class="pagebreak"></div>'
h = re.sub(r'<h1 id="contents">Contents</h1>.*?<div class="pagebreak">\s*</div>', contents_html, h, count=1, flags=re.S)
html.write_text(h, encoding='utf-8')
subprocess.run(['weasyprint', str(html), str(out_pdf)], check=True)
print(out_pdf)
