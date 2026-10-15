"""Read-only source-PDF crop, actual-size comparison and bounded regression tests."""
import argparse
import base64
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont
import pdfplumber
import pypdfium2 as pdfium

ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent
NS={'s':'http://www.w3.org/2000/svg'}
hashfile=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
parser=argparse.ArgumentParser()
parser.add_argument('--before-pdf',default='C:/Users/markg/Downloads/ME10_DEV2_UK_A4_Style_Proof_Final(1).pdf')
parser.add_argument('--verify-sources',action='store_true')
options=parser.parse_args()
before_pdf=Path(options.before_pdf)
PDF_HASH='80fce3d8640bb12b4f561aed729aafbaf07f4cd6f77dc3a58d156bde6a460646'
ORIGINAL_HASH='f5569ab32165c85e5e8646a6a7016d450cd0c164705b4870ec570446103347ef'
assert hashfile(before_pdf)==PDF_HASH,'Not the exact human-reviewed A4 proof'
assert hashfile(PARENT/'01-two-clocks.svg')==ORIGINAL_HASH,'Original changed'
source_status='NOT_RUN in this invocation'
if options.verify_sources:
    source_map=json.loads((PARENT/'source-map.json').read_text(encoding='utf-8'))
    selected=[s for s in source_map['sources'] if s['edition'] in ['ME09-RC3A-20261015','ME10-DEV2-20261015']]
    assert len(selected)==2
    for source in selected:
        payload=json.loads(subprocess.check_output(['gh','api',f"repos/markgoodbody-bit/mechanical-ethics/contents/{source['path']}?ref={source['commit']}"]))
        raw_source=base64.b64decode(payload['content'])
        assert hashlib.sha256(raw_source).hexdigest()==source['sha256']
        source_lines=raw_source.decode('utf-8').splitlines()
        for number,needle in source['sentinels'].items():
            assert needle in source_lines[int(number)-1]
    source_status=f'PASS: 2 immutable full-file hashes and {sum(len(s["sentinels"]) for s in selected)} line sentinels'

with pdfplumber.open(before_pdf) as doc:
    assert len(doc.pages)==3
    page=doc.pages[2]
    regions=[r for r in page.rects if abs((r['x1']-r['x0'])-126*72/25.4)<.1 and r['top']>270]
    assert len(regions)==1,'Figure region not uniquely established'
    r=regions[0]
    bbox=[r['x0'],r['top'],r['x1'],r['bottom']]
pdf=pdfium.PdfDocument(before_pdf)
page=pdf[2].render(scale=2).to_pil().convert('RGB')
before=page.crop(tuple(round(v*2) for v in bbox))
before=before.resize((714,604),Image.Resampling.LANCZOS)
before.save(ROOT/'before-p3-figure.png')
after=Image.open(ROOT/'two-clocks-v2-book-width.png').convert('RGB')
assert after.size==(714,309)
canvas=Image.new('RGB',(778,1089),'white')
draw=ImageDraw.Draw(canvas)
ui=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',23)
draw.text((32,20),'Before: figure in the reviewed A4 proof',font=ui,fill='#27312F')
canvas.paste(before,(32,62))
draw.line((32,690,746,690),fill='#d4d4d4',width=1)
draw.text((32,714),'After: sparse alternative at the same width',font=ui,fill='#27312F')
canvas.paste(after,(32,760))
canvas.save(ROOT/'before-after.png')

svg=ET.parse(ROOT/'two-clocks-v2.svg').getroot()
original=ET.parse(PARENT/'01-two-clocks.svg').getroot()
assert svg.attrib['width']=='126mm' and svg.attrib['height']=='54.6mm'
assert svg.attrib['viewBox']=='0 0 900 390'
assert svg.attrib['aria-labelledby']=='clock-v2-title clock-v2-desc'
assert svg.find('s:title',NS) is not None and svg.find('s:desc',NS) is not None
raw=(ROOT/'two-clocks-v2.svg').read_text(encoding='utf-8')
assert all(s not in raw.lower() for s in ['<script','<image','<foreignobject','href=','@import','<!entity','stroke-dasharray'])
labels=[n.text for n in svg.findall('.//s:text',NS)]
assert labels==['Payment','Housing','Funds usable','Loss hardens','Home lost','Same start']
assert len(svg.findall('.//s:rect',NS))==1,'Only the white page rect; no warning cards'
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',30)
boxes=[]
for node in svg.findall('.//s:text',NS):
    assert not list(node),'No hidden extra tspan labels'
    assert node.attrib.get('font-weight','400')=='400'
    x,y=float(node.attrib['x']),float(node.attrib['y'])
    if node.attrib.get('text-anchor')=='middle': x-=font.getlength(node.text)/2
    left,top,right,bottom=font.getbbox(node.text,anchor='ls')
    box=(x+left,y+top,x+right,y+bottom,node.text)
    assert box[0]>=20 and box[1]>=20 and box[2]<=880 and box[3]<=375,box
    boxes.append(box)
for i,a in enumerate(boxes):
    for b in boxes[i+1:]:
        assert not(min(a[2],b[2])>max(a[0],b[0]) and min(a[3],b[3])>max(a[1],b[1])),(a,b)

def check_geometry(root):
    nodes={n.attrib['id']:n for n in root.iter() if 'id' in n.attrib}
    start=nodes['origin'].attrib
    assert start['x1']==start['x2']=='65'
    assert nodes['payment-axis'].attrib['x1']==nodes['housing-axis'].attrib['x1']=='65'
    a=nodes['payment-effect'].attrib
    b=nodes['same-payment-effect'].attrib
    assert a['cx']==b['cx']==nodes['same-event-guide'].attrib['x1']==nodes['same-event-guide'].attrib['x2']
    assert a['cy']=='150' and b['cy']=='280'
    assert float(nodes['housing-hardening'].attrib['x1'])<float(a['cx'])<float(nodes['payment-hardening'].attrib['x1'])
check_geometry(svg)
controls=[('housing-axis','x1','100'),('payment-hardening','x1','540'),('payment-hardening','x1','500'),('housing-hardening','x1','600'),('same-payment-effect','cx','600')]
for ident,key,value in controls:
    mutant=copy.deepcopy(svg)
    next(n for n in mutant.iter() if n.attrib.get('id')==ident).attrib[key]=value
    try:check_geometry(mutant)
    except AssertionError:pass
    else:raise AssertionError('Corrupted geometry accepted: '+ident)
note=(ROOT/'editorial-note.md').read_text(encoding='utf-8')
assert 'acknowledgement is omitted' in note and 'necessary, not sufficient' in note
assert 'UNKNOWN' in note and 'neither holding nor continuing' in note
assert 'declared, contestable loss criterion' in note
assert 'Illustrative' in svg.find('s:desc',NS).text or 'synthetic' in svg.find('s:desc',NS).text

for name in ['two-clocks-v2.png','two-clocks-v2-mono.png']:
    image=Image.open(ROOT/name).convert('RGB')
    assert image.size==(1488,645)
    if '-mono' in name:
        assert all(r==g==b for r,g,b in image.resize((150,65)).get_flattened_data())
old_words=len(re.findall(r'\S+',' '.join(n.text or '' for n in original.findall('.//s:tspan',NS))))
new_words=len(' '.join(labels).split())
assert new_words<old_words/3
assert hashfile(PARENT/'01-two-clocks.svg')==ORIGINAL_HASH
report={
 'status':'PASS_BOUNDED_GEOMETRY_TEXT_AND_PREVIEW_CHECKS',
 'source_pdf_sha256':PDF_HASH,'source_pdf_page':3,'source_pdf_figure_bbox_pt':bbox,
 'source_pdf_used_read_only':True,'original_svg_sha256':ORIGINAL_HASH,
 'manuscript_source_custody':source_status,
 'comparison_width_px_each':714,'before_height_px':604,'after_height_px':309,
 'visible_label_words_before':old_words,'visible_label_words_after':new_words,
 'label_count_after':len(labels),'bold_labels_after':0,
 'label_pt_before':round(26*126*72/25.4/900,2),'label_pt_after':round(30*126*72/25.4/900,2),
 'negative_controls_rejected':len(controls),'geometry':'PASS: same origin, same actual effect, before specified payment-related hardening, after housing loss',
 'source_text_extraction':'PASS: six SVG text labels exact and descriptions present; no PDF output authored',
 'label_bounds_and_overlap':'PASS with installed Arial; no browser/AT claim',
 'monochrome':'PASS: neutral RGB, marks retain shape distinction',
 'unverified':['Physical printing','Novice comprehension','Final human art selection','Final publication font','Assistive-technology behaviour'],
 'files':{p.name:hashfile(p) for p in sorted(ROOT.iterdir()) if p.is_file() and p.name!='checks.json'}
}
(ROOT/'checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in report.items() if k!='files'},indent=2))
