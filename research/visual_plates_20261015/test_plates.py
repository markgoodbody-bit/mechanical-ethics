"""Bounded checks, not visual comprehension or accessibility certification."""
import argparse
import base64
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET
from PIL import Image, ImageFont

ROOT=Path(__file__).resolve().parent
NS={'s':'http://www.w3.org/2000/svg'}
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
args=argparse.ArgumentParser()
args.add_argument('--verify-sources',action='store_true')
options=args.parse_args()
meta=json.loads((ROOT/'plate-metadata.json').read_text(encoding='utf-8'))
captions=(ROOT/'captions.md').read_text(encoding='utf-8')
source_map=json.loads((ROOT/'source-map.json').read_text(encoding='utf-8'))
results={}
source_result='NOT_RUN (use --verify-sources for immutable GitHub API bytes)'
if options.verify_sources:
    for source in source_map['sources']:
        payload=json.loads(subprocess.check_output(['gh','api',f"repos/markgoodbody-bit/mechanical-ethics/contents/{source['path']}?ref={source['commit']}"]))
        data=base64.b64decode(payload['content'])
        assert hashlib.sha256(data).hexdigest()==source['sha256']
        lines=data.decode('utf-8').splitlines()
        for number,needle in source['sentinels'].items():
            assert needle in lines[int(number)-1],f'{source["edition"]}:{number} anchor drift'
    source_result=f'PASS: {len(source_map["sources"])} full-file SHA256 values and {sum(len(s["sentinels"]) for s in source_map["sources"])} edition-specific line sentinels'

text_total=0
for item in meta:
    path=ROOT/f'{item["id"]}.svg'
    raw=path.read_text(encoding='utf-8')
    svg=ET.fromstring(raw)
    assert svg.attrib['viewBox']=='0 0 900 760'
    assert svg.attrib['width']=='126mm' and svg.attrib['role']=='img'
    assert svg.find('s:title',NS).text==item['title']
    assert svg.find('s:desc',NS).text==item['alt']
    assert all(token not in raw.lower() for token in ['<script','<image','<foreignobject','href=','@import','data:','<!entity'])
    assert 'stroke-dasharray' not in raw, 'No unexplained dashed uncertainty marks'
    ids=[e.attrib['id'] for e in svg.iter() if 'id' in e.attrib]
    assert len(ids)==len(set(ids))
    # Installed Arial measurement is a bounded check; final platform fallback can differ.
    boxes=[]
    for node in svg.findall('.//s:text',NS):
        size=float(node.attrib['font-size'])
        assert size>=26, 'Label below approximately 10.3pt at intended width'
        face='arialbd.ttf' if node.attrib.get('font-weight')=='700' else 'arial.ttf'
        font=ImageFont.truetype(str(Path('C:/Windows/Fonts')/face),round(size))
        baseline=float(node.attrib['y'])
        for span in node:
            baseline+=float(span.attrib['dy'])
            value=span.text or ''
            x=float(span.attrib['x'])
            width=font.getlength(value)
            if node.attrib.get('text-anchor')=='middle': x-=width/2
            left,top,right,bottom=font.getbbox(value,anchor='ls')
            box=(x+left,baseline+top,x+right,baseline+bottom,value)
            assert box[0]>=15 and box[2]<=885 and box[1]>=15 and box[3]<=745,box
            boxes.append(box)
            text_total+=1
    for a,b in [(a,b) for i,a in enumerate(boxes) for b in boxes[i+1:]]:
        overlap_x=min(a[2],b[2])-max(a[0],b[0])
        overlap_y=min(a[3],b[3])-max(a[1],b[1])
        assert not(overlap_x>1 and overlap_y>1),f'Label overlap: {a[4]} / {b[4]}'
    for suffix in ['', '-mono']:
        image=Image.open(ROOT/f'{item["id"]}{suffix}.png').convert('RGB')
        assert image.width==1488 and image.height==1257
        assert image.getpixel((0,0))==(255,255,255)
        if suffix:
            # Near-neutral gray wash is allowed, no chromatic category coding.
            assert max(abs(r-g)+abs(g-b) for r,g,b in image.resize((100,85)).get_flattened_data())==0
    results[item['id']]='PASS: XML, metadata, safe resources, text bounds/overlap, raster shape, monochrome'

svg=ET.parse(ROOT/'01-two-clocks.svg').getroot()
def check_timing(svg):
    byid={e.attrib['id']:e for e in svg.iter() if 'id' in e.attrib}
    assert byid['shared-origin'].attrib['x1']==byid['shared-origin'].attrib['x2']=='35'
    assert byid['payment-axis'].attrib['x1']==byid['housing-axis'].attrib['x1']=='35'
    assert byid['shared-origin'].attrib['y1']=='245' and byid['shared-origin'].attrib['y2']=='472'
    effect=float(byid['payment-effect'].attrib['cx'])
    assert effect==float(byid['same-payment-effect'].attrib['cx'])
    assert float(byid['acknowledgement'].attrib['cx'])<effect<float(byid['payment-hardening'].attrib['x1'])
    assert float(byid['housing-hardening'].attrib['x1'])<effect
    assert byid['acknowledgement'].attrib['fill']!='#27312F' and byid['payment-effect'].attrib['fill']=='#27312F'
    visible=' '.join(n.text or '' for n in svg.findall('.//s:tspan',NS))
    assert 'UNKNOWN' in visible and 'orders neither a stop nor continuation' in visible
check_timing(svg)
controls=[('housing-axis','x1','200'),('payment-hardening','x1','535'),('payment-effect','cx','800'),('acknowledgement','fill','#27312F'),('housing-hardening','x1','650'),('same-payment-effect','cx','600')]
for ident,attribute,value in controls:
    mutant=copy.deepcopy(svg)
    node=next(n for n in mutant.iter() if n.attrib.get('id')==ident)
    node.attrib[attribute]=value
    try: check_timing(mutant)
    except AssertionError: pass
    else: raise AssertionError(f'Negative control escaped: {ident}/{attribute}')
for phrase in ['strictly before','not sufficient','UNKNOWN','not a guaranteed remedy','legal veto','not automatic progress','retention or transfer','refuse']:
    # Specific source-facing semantic guards, not an automated proof of interpretation.
    assert phrase in captions,phrase
before={p.name:digest(p) for p in ROOT.glob('*.svg')}
subprocess.run([sys.executable,str(ROOT/'make_plates.py')],check=True,capture_output=True)
assert before=={p.name:digest(p) for p in ROOT.glob('*.svg')}, 'Generator not deterministic'
report={'status':'PASS_BOUNDED_SOURCE_AND_RASTER_CHECKS','plates':results,'labels_checked':text_total,'minimum_intended_label_pt':round(26*126*72/25.4/900,2),'semantic_geometry':'PASS: common t0; acknowledgement distinct; same effect precedes one loss and follows coupled loss','negative_controls_rejected':len(controls),'source_custody':source_result,'deterministic_svg_regeneration':'PASS','unverified':['Physical printing','Actual novice comprehension','Assistive-technology/browser behavior','Final DEV2 editorial placement','Safe effective challenge route in any actual institution'],'files':{p.name:digest(p) for p in sorted(ROOT.iterdir()) if p.suffix in ['.svg','.png','.py','.mjs','.md','.json'] and p.name!='checks.json'}}
(ROOT/'checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='files'},indent=2))
