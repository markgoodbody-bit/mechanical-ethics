from pathlib import Path
import re, hashlib
from weasyprint import HTML
import argparse
ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, default=ROOT/"Mechanical_Ethics_Casebook_2026-10-26.pdf")
args = parser.parse_args()
src=(ROOT/'source-reader.html').read_text()
assert hashlib.sha256(src.encode()).hexdigest()=='e534524f3ea9f2317cbbeacbe27d396ed1d4736cefee8673b31f1fe1cde31a0e'
nav=re.search(r'<nav.*?</nav>',src,re.S).group()
nav=nav.replace('<details>','<div>').replace('</details>','</div>').replace('<summary>','<h2>').replace('</summary>','</h2>')
header='''<header class="cover"><p class="eyebrow">Mechanical Ethics · Casebook</p><h1>Case studies and<br>technical analysis</h1><p class="intro">Institutional information disclosure<br>Wildfire protective action<br>Supervision capacity in technical employment</p><p class="edition">Reading edition · 26 October 2026</p><p class="scope">Two historical studies and one constructed design study.<br>Includes source limitations and editorial notes.</p><p class="small">A maintained supplement to Mechanical Ethics 1.0.<br>These cases do not establish field effectiveness.</p></header><section class="contents" id="contents"><h1>Contents</h1>'''+nav+'''<p class="small provenance">PDF derived from the integrated repository reading copy at commit 9f2a2f79118320211c7d62ab22e1ee494afb283f. Its twelve source documents are pinned to 0a281d0dd729a0110d5c2c5ecd358502da413821. Source and historical editorial wording is retained; newer unintegrated drafts are excluded. External source links require a connection.</p></section>'''
src=re.sub(r'<header.*?</header>',header,src,flags=re.S)
src=re.sub(r'<a class="skip".*?</a>','',src)
css='''
@page {size:A4; margin:20mm 19mm 20mm; @bottom-left{content:"MECHANICAL ETHICS · CASEBOOK";font:7pt sans-serif;color:#65716e} @bottom-right{content:counter(page);font:9pt sans-serif;color:#365b56}}
@page:first{@bottom-left{content:none}@bottom-right{content:none}}
body{background:white;color:#202927;font:10.4pt/1.5 "DejaVu Serif",serif}
header, main,footer {max-width:none;margin:0;padding:0}
.cover {height:245mm;box-sizing:border-box;padding-top:28mm;border:0;break-after:page}
.cover h1{font:30pt/1.17 "DejaVu Serif";margin:12mm 0 14mm;color:#214e47}
.eyebrow{font:9pt sans-serif;letter-spacing:1.6pt;color:#42675f}
.cover .intro{font:13pt/1.7 "DejaVu Serif";margin-bottom:20mm}
.edition{font:10pt sans-serif;margin-top:18mm}.scope{font:10pt/1.6 sans-serif}.small{font:8.4pt/1.5 sans-serif;color:#52625d}
.contents{break-after:page}.contents h1{font-size:25pt}.contents nav{display:block!important;font:10pt/1.7 sans-serif}.contents nav li{padding:1.3mm 0;list-style:none}.contents ol,.contents ul{padding-left:0}.contents a{display:block;text-decoration:none}.contents a::after{content:leader('.') target-counter(attr(href),page)}.contents h2{font-size:13pt;margin-top:9mm}.provenance{margin-top:12mm;overflow-wrap:anywhere}
article{padding:0;border:0;break-before:page}article h1{font:22pt/1.25 "DejaVu Serif";color:#214e47;margin:0 0 8mm;bookmark-level:1}h2{font:15pt/1.3 "DejaVu Serif";margin:8mm 0 3mm;bookmark-level:2}h3{font:11.5pt/1.35 sans-serif;margin:6mm 0 2mm;bookmark-level:3}h1,h2,h3,h4{break-after:avoid}p{margin:0 0 3mm;orphans:3;widows:3}li{margin:1.4mm 0}a{color:#285f58;text-decoration:none;overflow-wrap:anywhere}.page-top{display:none!important}
table{table-layout:fixed;width:100%;min-width:0;font:8pt/1.4 "DejaVu Sans",sans-serif;margin:3mm 0}th,td{padding:2mm;overflow-wrap:anywhere;border-bottom:.4pt solid #cbd7d1}th{background:#eef3f0;font-weight:bold}thead{display:table-header-group}tr{break-inside:avoid}.table-wrap{overflow:visible;margin:3mm 0}code{font:8.5pt/1.5 "DejaVu Sans Mono";overflow-wrap:anywhere}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:8pt;padding:3mm;background:#f4f6f4;break-inside:auto}blockquote{margin:4mm 0;padding-left:4mm;border-left:1pt solid #aac0b5}footer{font-size:8pt;margin-top:8mm} .cover h1,.contents h1{bookmark-level:none}
'''

src=src.replace('</head>', '<style>'+css+'</style></head>')
HTML(string=src,base_url=str(ROOT)).write_pdf(args.output)
print('PDF written')
