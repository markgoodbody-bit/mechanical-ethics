#!/usr/bin/env python3
from pathlib import Path
import html

OUT=Path(__file__).resolve().parent/'figures'
OUT.mkdir(parents=True, exist_ok=True)
GOLD='#b87500'; GREY='#84847f'; LIGHT='#b7b4ad'; BOX='#f2f1ed'; TXT='#111111'

def svg_start(w,h):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="white"/><style>text{{font-family:Arial,Arimo,sans-serif;fill:{TXT}}}.title{{font-size:48px}}.sub{{font-size:39px}}.body{{font-size:38px}}.small{{font-size:31px}}.tiny{{font-size:27px}}.box{{fill:{BOX};stroke:{LIGHT};stroke-width:3}}</style>'''
def t(x,y,s,cls='body',anchor='start',rotate=None):
    tr=f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ''
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{tr}>{html.escape(s)}</text>'

def line(x1,y1,x2,y2,color=GREY,width=8,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d}/>'
def circ(x,y,r,color): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'
def rect(x,y,w,h,rx=8): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="box"/>'

def write(n,body,w=1600,h=900):
    (OUT/f'figure-{n}.svg').write_text(svg_start(w,h)+body+'</svg>',encoding='utf-8')

b=[]
b += [t(35,75,'The file and the life','title'), t(35,135,'the same night behind one wall, two records of it','sub')]
b += [t(80,230,'the file','sub'),t(80,290,'what the system records','sub'),t(930,230,'the life','sub'),t(930,290,'what she carries','sub')]
b.append(line(810,225,810,780,LIGHT,4))
left=['category: damp and mould','logged at 01:17','reference number issued','the request entered a queue','status: pending']
right=["Mia's cough in the dark",'the smell in the room','the money left after rent','a shift starting in six hours','the fear of being called difficult']
for i,s in enumerate(left):
    y=390+i*100;b += [f'<rect x="82" y="{y-24}" width="22" height="22" rx="3" fill="{GREY}"/>',t(142,y,s,'body')]
for i,s in enumerate(right):
    y=390+i*100;b += [circ(935,y-12,14,GOLD),t(985,y,s,'body')]
b.append(t(800,865,'both accounts are factual; they are not equivalent','sub','middle'))
write(1,''.join(b))

b=[t(80,70,'The correction window','title'),t(80,125,'effective protection must be in place before hardening','sub')]
b += [t(80,295,'protected in time','sub'), t(80,545,'too late','sub')]
b += [line(280,375,1120,375,GREY,10),line(280,620,1480,620,GREY,10),line(1240,180,1240,760,TXT,4,'14 12')]
for x,label,col in [(360,'notice',GREY),(650,'route',GREY),(1050,'protect',GOLD)]: b += [circ(x,375,22,col),t(x,445,label,'sub','middle')]
for x,label,col in [(360,'notice',GREY),(820,'route',GREY),(1430,'correct',GOLD)]: b += [circ(x,620,22,col),t(x,690,label,'sub','middle')]
b += [t(1240,160,'practical hardening boundary','sub','middle'),t(1350,385,'path remains open','sub'),t(1320,565,'accurate, but too late','sub'),line(80,735,1600,735,LIGHT,5),t(80,750,'time','sub')]
write(2,''.join(b),1650,800)

b=[t(70,70,'Two flats, one wall','title'),t(70,130,'the same damp enters two systems of attention','sub'),t(100,235,'upstairs: owner','sub'),t(1110,235,'downstairs: tenant','sub')]
for y,s in [(320,'emails managing agent'),(455,'contractor visits in 3 days'),(590,'cause found; repair begins')]:
    b += [rect(90,y-55,520,85),t(350,y,s,'body','middle')]
b += [line(350,350,350,400,LIGHT,5),line(350,485,350,535,LIGHT,5)]
for y,s in [(320,'reports on portal'),(455,'reference number issued'),(590,'case closes on move-out')]:
    b += [rect(1070,y-55,500,85),t(1320,y,s,'body','middle')]
b += [line(1320,350,1320,400,LIGHT,5),line(1320,485,1320,535,LIGHT,5)]
b += [f'<rect x="755" y="235" width="175" height="500" fill="{BOX}" stroke="{LIGHT}" stroke-width="3"/>',t(842,470,'one wall','sub','middle'),t(842,530,'water, one joint','sub','middle'),line(70,775,1600,775,GOLD,5),t(835,835,'a rent-increase letter arrives one week after the report','sub','middle'),t(350,890,'route reaches authority','sub','middle'),t(1320,890,'route returns a record, then closes','sub','middle')]
write(3,''.join(b),1680,930)

b=[t(155,95,'Machine speed versus human correction','title'),t(155,150,'the machine completes the action before correction has assembled','sub')]
b += [line(200,230,200,680,LIGHT,5),line(200,680,1650,680,LIGHT,5),t(70,250,'how far each','sub','middle',-90),t(1570,740,'time','sub')]
b += [f'<polyline points="230,635 650,330 870,245 1130,220 1550,215" fill="none" stroke="{GOLD}" stroke-width="14"/>',f'<polyline points="230,640 470,610 700,565 920,500 1160,415 1550,280" fill="none" stroke="{GREY}" stroke-width="14"/>',line(1320,205,1320,680,TXT,4,'14 12')]
b += [t(1170,190,'machine action, already at scale','sub'),t(1090,480,'human correction, still assembling','sub'),t(1270,795,'by this point, the machine has finished','sub','middle')]
write(4,''.join(b),1750,830)
print(OUT)
