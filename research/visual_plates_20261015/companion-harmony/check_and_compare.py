"""Bounded source/render/meaning regressions; never an art or reader certificate."""
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
NS={'s':'http://www.w3.org/2000/svg'}
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
parser=argparse.ArgumentParser()
parser.add_argument('--verify-sources',action='store_true')
parser.add_argument('--repeat-render',action='store_true')
parser.add_argument('--node',default='node')
args=parser.parse_args()
old_pngs={p.name:digest(p) for p in ROOT.glob('*.png')} if args.repeat_render else {}
if args.repeat_render:
    assert len(old_pngs)==9,'Generate the first contact sheet before repeat check'
    subprocess.run([args.node,str(ROOT/'render.mjs')],check=True)
originals={
 'who-draws-the-map':('02-who-draws-the-map','c15527e99beaf2d051b1433f5f30dc3f2514052f0e9358d70b5972a44b6fc649'),
 'growing-room':('03-growing-room','ef30105a0730cf24c02aee3a87088a83455c3abb4a57ebaeb1f646dc75720b00')}
for filename,sha in originals.values():assert digest(PARENT/f'{filename}.svg')==sha
assert digest(PARENT/'two-clocks-v3/two-clocks-v3.svg')=='1fb6547d8fcb73eab3beb7e0da591df5cbf04bf4ee37678fc7e649d473f76a10'
source_status='NOT_RUN (optional --verify-sources)'
if args.verify_sources:
    selected=[s for s in json.loads((PARENT/'source-map.json').read_text(encoding='utf-8'))['sources'] if s['edition'] in ['ME09-RC3A-20261015','ME10-DEV2-20261015']]
    for source in selected:
        obj=json.loads(subprocess.check_output(['gh','api',f"repos/markgoodbody-bit/mechanical-ethics/contents/{source['path']}?ref={source['commit']}"]))
        data=base64.b64decode(obj['content'])
        assert hashlib.sha256(data).hexdigest()==source['sha256']
        lines=data.decode('utf-8').splitlines()
        for number,needle in source['sentinels'].items():assert needle in lines[int(number)-1]
    source_status='PASS: immutable RC3A and DEV2 hashes plus 23 line sentinels'

def label_text(root):return [''.join(n.itertext()) for n in root.findall('.//s:text',NS)]
trees={}
metrics={}
for name,(oldname,_) in originals.items():
    root=ET.parse(ROOT/f'{name}.svg').getroot();trees[name]=root
    raw=(ROOT/f'{name}.svg').read_text(encoding='utf-8')
    assert root.attrib['width']=='126mm' and root.attrib['height']=='78.4mm'
    assert root.attrib['viewBox']=='0 0 900 560' and root.attrib['role']=='img'
    assert root.find('s:title',NS).text and root.find('s:desc',NS).text
    assert all(s not in raw.lower() for s in ['<script','<image','<foreignobject','@import','<!entity','stroke-dasharray'])
    ids=[n.attrib['id'] for n in root.iter() if 'id' in n.attrib]
    assert len(ids)==len(set(ids))
    for node in root.iter():
        if 'href' in node.attrib:assert node.attrib['href'].startswith('#') and node.attrib['href'][1:] in ids
        if 'marker-end' in node.attrib:assert node.attrib['marker-end'].removeprefix('url(#').removesuffix(')') in ids
        assert node.attrib.get('font-weight','400')=='400'
    boxes=[]
    for node in root.findall('.//s:text',NS):
        size=int(node.attrib.get('font-size','32' if name=='growing-room' else '30'))
        assert size>=30
        font=ImageFont.truetype(str(Path('C:/Windows/Fonts')/('georgiai.ttf' if node.attrib.get('font-style')=='italic' else 'georgia.ttf')),size)
        x,y=float(node.attrib['x']),float(node.attrib['y'])
        if node.attrib.get('text-anchor')=='middle':x-=font.getlength(node.text)/2
        a,b,c,d=font.getbbox(node.text,anchor='ls')
        box=(x+a,y+b,x+c,y+d,node.text)
        assert box[0]>=15 and box[1]>=15 and box[2]<=885 and box[3]<=545,box
        boxes.append(box)
    for i,a in enumerate(boxes):
        for b in boxes[i+1:]:assert not(min(a[2],b[2])>max(a[0],b[0]) and min(a[3],b[3])>max(a[1],b[1])),(a,b)
    for suffix in ['', '-mono']:
        full=Image.open(ROOT/f'{name}{suffix}.png').convert('RGB')
        book=Image.open(ROOT/f'{name}{suffix}-book-width.png').convert('RGB')
        assert full.size==(1488,926) and book.size==(714,444)
        if suffix:assert all(r==g==b for r,g,b in book.resize((120,75)).get_flattened_data())
        # Ink must not reach an image edge; this is a coarse clipping sentinel.
        assert full.crop((0,0,full.width,8)).getextrema()==((255,255),(255,255),(255,255))
        assert full.crop((full.width-8,0,full.width,full.height)).getextrema()==((255,255),(255,255),(255,255))
    previous=ET.parse(PARENT/f'{oldname}.svg').getroot()
    metrics[name]={'visible_words_before':len(' '.join(label_text(previous)).split()),'visible_words_after':len(' '.join(label_text(root)).split()),'label_count':len(boxes),'minimum_label_pt':round(30*126*72/25.4/900,2),'bold_labels':0}

def map_guard(root):
    nodes={n.attrib['id']:n for n in root.iter() if 'id' in n.attrib}
    assert set(label_text(root))=={'Assessor','Opening hours','versus','Current timetable','Selected account','Review','Visitor','Last bus missed','Challenge'}
    assert 'selected-boundary' in nodes
    assert float(nodes['visitor-account'].attrib['cy'])>338
    assert 'M 510 230 H 669' in nodes['account-review'].attrib['d']
    assert nodes['challenge-review'].attrib['d'].endswith('750 273')
    assert len([n for n in root.iter() if 'marker-end' in n.attrib])==2,'No automatic verdict edge'
map_guard(trees['who-draws-the-map'])
map_controls=[('remove','selected-boundary'),('remove','challenge-review'),('inside','visitor-account'),('label','Challenge'),('label','Review')]
for action,key in map_controls:
    mutant=copy.deepcopy(trees['who-draws-the-map'])
    if action=='remove':
        for parent in mutant.iter():
            for child in list(parent):
                if child.attrib.get('id')==key:parent.remove(child)
    elif action=='inside':next(n for n in mutant.iter() if n.attrib.get('id')==key).attrib['cy']='250'
    else:next(n for n in mutant.findall('.//s:text',NS) if n.text==key).text='Guaranteed remedy'
    try:map_guard(mutant)
    except (AssertionError,KeyError):pass
    else:raise AssertionError('Map negative control accepted: '+key)

def growing_guard(root):
    nodes={n.attrib['id']:n for n in root.iter() if 'id' in n.attrib}
    assert label_text(root)==['Notice','Practise','Another plant','Someone keeps the room usable.']
    assert 'supporting-adult' in nodes and 'practice-tray' in nodes and 'another-tray-and-pot' in nodes
    assert len(root.findall('.//s:use[@href="#room"]',NS))==3
    assert len(root.findall('.//s:use[@href="#child"]',NS))==3
    assert len(root.findall('.//s:use[@href="#sprout"]',NS))==2
    assert not any('marker-end' in n.attrib for n in root.iter()),'No progress-flowchart arrows'
growing_guard(trees['growing-room'])
growing_controls=['supporting-adult','practice-tray','another-tray-and-pot']
for key in growing_controls:
    mutant=copy.deepcopy(trees['growing-room'])
    next(n for n in mutant.iter() if n.attrib.get('id')==key).attrib['id']='removed-control'
    try:growing_guard(mutant)
    except AssertionError:pass
    else:raise AssertionError('Growing-room negative control accepted: '+key)
note=(ROOT/'captions-and-placement.md').read_text(encoding='utf-8')
for phrase in ['not yet selected','predetermined verdict','safe and usable','no legal veto','not proof of independent performance','retention and transfer','free to change direction','Physical printing']:
    assert phrase in note,phrase

canvas=Image.new('RGB',(1516,1440),'white')
draw=ImageDraw.Draw(canvas);ui=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',23)
for i,(name,(oldname,_)) in enumerate(originals.items()):
    y=18+i*710
    title='Who draws the map?' if i==0 else 'Growing room'
    draw.text((24,y),title+' | original',font=ui,fill='#27312F')
    draw.text((778,y),title+' | harmonised candidate',font=ui,fill='#27312F')
    old=Image.open(PARENT/f'{oldname}.png').convert('RGB').resize((714,603),Image.Resampling.LANCZOS)
    canvas.paste(old,(24,y+50))
    canvas.paste(Image.open(ROOT/f'{name}-book-width.png').convert('RGB'),(778,y+50))
    if i==0:draw.line((24,y+676,1492,y+676),fill='#dededb',width=1)
canvas.save(ROOT/'before-after.png')
repeat='NOT_RUN in this invocation'
if args.repeat_render:
    assert old_pngs=={p.name:digest(p) for p in ROOT.glob('*.png')}
    repeat='PASS: all nine PNGs byte-identical on repeated same-environment rendering/comparison'
report={'status':'PASS_BOUNDED_SOURCE_SEMANTIC_AND_RENDER_CHECKS','sources':source_status,'original_plates_and_clock_v3':'UNCHANGED_HASHES_PASS','plate_metrics':metrics,'minimum_type_pt':11.91,'width_mm':126,'height_mm':78.4,'comparison_width_px_each':714,'negative_controls_rejected':len(map_controls)+len(growing_controls),'map_regressions':'PASS: selected account versus outside consequence; two paths to review, no verdict edge','formation_regressions':'PASS: repeated child/room; help/tray; another plant; same sprout reused, no escalating progress symbols','neutral_monochrome':'PASS','repeat_render':repeat,'limits':['Human aesthetic/placement selection','Physical print','Novice comprehension','Assistive technology','Final book typography'],'files':{p.name:digest(p) for p in sorted(ROOT.iterdir()) if p.is_file() and p.name!='checks.json'}}
(ROOT/'checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in report.items() if k!='files'},indent=2))
