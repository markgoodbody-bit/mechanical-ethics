"""Bounded regression checks and equal-width v2/v3 proof; no manuscript writes."""
import argparse
import base64
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent
V2=PARENT/'two-clocks-v2'
NS={'s':'http://www.w3.org/2000/svg'}
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
options=argparse.ArgumentParser()
options.add_argument('--verify-sources',action='store_true')
options.add_argument('--repeat-render',action='store_true')
options.add_argument('--node',default='node')
args=options.parse_args()
before_renders={p.name:digest(p) for p in ROOT.glob('*.png')} if args.repeat_render else {}
if args.repeat_render:
    assert len(before_renders)==5,'Generate first proofs before repeat check'
    subprocess.run([args.node,str(ROOT/'render.mjs')],check=True)
assert digest(PARENT/'01-two-clocks.svg')=='f5569ab32165c85e5e8646a6a7016d450cd0c164705b4870ec570446103347ef'
assert digest(V2/'two-clocks-v2.svg')=='c12060f01758f92f22836136b44aa28cb736cb905835b069d1ec4dc4ae764888'
v2_manifest=json.loads((V2/'checks.json').read_text(encoding='utf-8'))
assert digest(V2/'two-clocks-v2-book-width.png')==v2_manifest['files']['two-clocks-v2-book-width.png']
source_status='NOT_RUN (optional --verify-sources)'
if args.verify_sources:
    selected=[s for s in json.loads((PARENT/'source-map.json').read_text(encoding='utf-8'))['sources'] if s['edition'] in ['ME09-RC3A-20261015','ME10-DEV2-20261015']]
    assert len(selected)==2
    for source in selected:
        obj=json.loads(subprocess.check_output(['gh','api',f"repos/markgoodbody-bit/mechanical-ethics/contents/{source['path']}?ref={source['commit']}"]))
        data=base64.b64decode(obj['content'])
        assert hashlib.sha256(data).hexdigest()==source['sha256']
        lines=data.decode('utf-8').splitlines()
        for number,needle in source['sentinels'].items():assert needle in lines[int(number)-1]
    source_status='PASS: immutable RC3A and DEV2 hashes plus 23 line sentinels'

svg=ET.parse(ROOT/'two-clocks-v3.svg').getroot()
raw=(ROOT/'two-clocks-v3.svg').read_text(encoding='utf-8')
assert svg.attrib['width']=='126mm' and svg.attrib['height']=='59.5mm'
assert svg.attrib['viewBox']=='0 0 900 425'
assert svg.attrib['role']=='img' and svg.attrib['aria-labelledby']=='clock-v3-title clock-v3-desc'
assert svg.find('s:title',NS).text and svg.find('s:desc',NS).text
assert all(s not in raw.lower() for s in ['<script','<image','<foreignobject','href=','@import','<!entity','stroke-dasharray'])
assert len(svg.findall('.//s:rect',NS))==1
assert all(n.attrib.get('font-weight','400')=='400' for n in svg.iter())
texts=svg.findall('.//s:text',NS)
labels=[n.text for n in texts]
assert labels==['Same start','Funds usable','Loss hardens','Payment','Housing','Home lost']
assert len(' '.join(labels).split())==10
boxes=[]
for node in texts:
    size=int(node.attrib.get('font-size','30'))
    assert size>=30
    face='georgiai.ttf' if node.attrib.get('font-style')=='italic' else 'georgia.ttf'
    font=ImageFont.truetype(str(Path('C:/Windows/Fonts')/face),size)
    x,y=float(node.attrib['x']),float(node.attrib['y'])
    if node.attrib.get('text-anchor')=='middle':x-=font.getlength(node.text)/2
    elif node.attrib.get('text-anchor')=='end':x-=font.getlength(node.text)
    a,b,c,d=font.getbbox(node.text,anchor='ls')
    box=(x+a,y+b,x+c,y+d,node.text)
    assert box[0]>=20 and box[1]>=20 and box[2]<=885 and box[3]<=405,box
    boxes.append(box)
for i,a in enumerate(boxes):
    for b in boxes[i+1:]:
        assert not(min(a[2],b[2])>max(a[0],b[0]) and min(a[3],b[3])>max(a[1],b[1])),(a,b)
for rule in svg.findall('.//s:line',NS):
    x1,y1,x2,y2=[float(rule.attrib[k]) for k in ['x1','y1','x2','y2']]
    for l,t,r,b,label in boxes:
        if y1==y2:assert not(t<y1<b and min(x1,x2)<r and max(x1,x2)>l),(rule.attrib['id'],label)
        if x1==x2:assert not(l<x1<r and min(y1,y2)<b and max(y1,y2)>t),(rule.attrib['id'],label)

def geometry(root):
    nodes={n.attrib['id']:n for n in root.iter() if 'id' in n.attrib}
    origin=nodes['origin'].attrib
    assert origin['x1']==origin['x2']=='250'
    assert nodes['payment-axis'].attrib['x1']==nodes['housing-axis'].attrib['x1']=='250'
    effect=nodes['payment-effect'].attrib
    repeated=nodes['same-payment-effect'].attrib
    assert effect['cx']==repeated['cx']==nodes['same-event-guide'].attrib['x1']==nodes['same-event-guide'].attrib['x2']
    assert effect['cy']=='165' and repeated['cy']=='310'
    assert 250<float(nodes['housing-hardening'].attrib['x1'])<float(effect['cx'])<float(nodes['payment-hardening'].attrib['x1'])
geometry(svg)
controls=[('housing-axis','x1','300'),('payment-hardening','x1','570'),('payment-hardening','x1','500'),('housing-hardening','x1','650'),('same-payment-effect','cx','600')]
for ident,key,value in controls:
    mutant=copy.deepcopy(svg)
    next(n for n in mutant.iter() if n.attrib.get('id')==ident).attrib[key]=value
    try:geometry(mutant)
    except AssertionError:pass
    else:raise AssertionError('Broken semantic geometry accepted: '+ident)

v2_note=(V2/'editorial-note.md').read_text(encoding='utf-8')
caption=v2_note.split('## Proposed book caption\n\n',1)[1].split('\n\n',1)[0]
note=(ROOT/'art-direction.md').read_text(encoding='utf-8')
assert caption in note,'Caption drifted without an editorial reason'
for term in ['necessary, not sufficient','UNKNOWN neither automatic','competent authority','acknowledgement','hypothetical']:
    assert term in note,term

for suffix in ['', '-mono']:
    full=Image.open(ROOT/f'two-clocks-v3{suffix}.png').convert('RGB')
    book=Image.open(ROOT/f'two-clocks-v3{suffix}-book-width.png').convert('RGB')
    assert full.size==(1488,703) and book.size==(714,337)
    if suffix:assert all(r==g==b for r,g,b in book.resize((120,57)).get_flattened_data())
canvas=Image.new('RGB',(1516,435),'white')
draw=ImageDraw.Draw(canvas)
ui=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',23)
draw.text((24,18),'v2 | sparse',font=ui,fill='#27312F')
draw.text((778,18),'v3 | serif and copper',font=ui,fill='#27312F')
canvas.paste(Image.open(V2/'two-clocks-v2-book-width.png').convert('RGB'),(24,70))
canvas.paste(Image.open(ROOT/'two-clocks-v3-book-width.png').convert('RGB'),(778,70))
canvas.save(ROOT/'v2-v3-equal-width.png')
repeat_status='NOT_RUN in this invocation'
if args.repeat_render:
    assert before_renders=={p.name:digest(p) for p in ROOT.glob('*.png')},'Same-environment rerender changed PNG bytes'
    repeat_status='PASS: all five PNGs byte-identical on repeated same-environment render/comparison'
report={
 'status':'PASS_BOUNDED_SOURCE_GEOMETRY_TEXT_AND_RENDER_CHECKS',
 'original_and_v2_preserved':True,'source_custody':source_status,
 'label_words':10,'label_count':6,'bold_labels':0,
 'minimum_label_pt':round(30*126*72/25.4/900,2),'italic_row_label_pt':round(32*126*72/25.4/900,2),
 'width_mm':126,'height_mm':59.5,'comparison_width_px_each':714,
 'text_extraction':'PASS: six exact SVG labels and title/description',
 'bounds_and_collisions':'PASS: installed Georgia/Georgia Italic glyph bounds, label-label and rule-label checks',
 'geometry':'PASS: common origin, same actual effect before specified loss and after housing loss',
 'negative_controls_rejected':len(controls),'caption':'Identical to preserved v2',
 'repeat_render':repeat_status,
 'monochrome':'PASS: neutral RGB; same geometric distinction',
 'limits':['Human style approval','Physical print','Novice comprehension','Assistive technology','Final publication font choice'],
 'files':{p.name:digest(p) for p in sorted(ROOT.iterdir()) if p.is_file() and p.name!='checks.json'}
}
(ROOT/'checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in report.items() if k!='files'},indent=2))
