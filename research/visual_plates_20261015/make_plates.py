"""Original editable geometry; no manuscript edits, external assets or API calls."""
from pathlib import Path
import html
import json

ROOT=Path(__file__).resolve().parent
INK='#27312F'
ACCENT='#27584F'
PAPER='#ffffff'
WASH='#E8EFEB'

def text(x,y,lines,size=26,anchor='start',bold=False):
    if isinstance(lines,str):lines=[lines]
    spans=''.join(f'<tspan x="{x}" dy="{0 if i==0 else round(size*1.28,2)}">{html.escape(line)}</tspan>' for i,line in enumerate(lines))
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{700 if bold else 400}">{spans}</text>'

def line(x1,y1,x2,y2,color=INK,width=2.5,extra=''):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" {extra}/>'

def circle(x,y,r=7,fill=PAPER,color=INK):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{color}" stroke-width="2.5"/>'

def rect(x,y,w,h,fill='none',color=INK):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{color}" stroke-width="2.5"/>'

def person(x,y,scale=1):
    return f'<g transform="translate({x} {y}) scale({scale})">'+circle(0,-65,13)+line(0,-52,0,-10)+line(0,-10,-17,20)+line(0,-10,17,20)+line(0,-40,-25,-23)+line(0,-40,25,-23)+'</g>'

def svg(name,title,desc,parts,height=760):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="126mm" height="{126*height/900:.3f}mm" viewBox="0 0 900 {height}" role="img" aria-labelledby="{name}-title {name}-desc">
<title id="{name}-title">{html.escape(title)}</title>
<desc id="{name}-desc">{html.escape(desc)}</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 1 1 L 9 5 L 1 9" fill="none" stroke="{INK}" stroke-width="1.5"/></marker></defs>
<rect width="900" height="{height}" fill="{PAPER}"/>
<g font-family="Arial, Helvetica, sans-serif" fill="{INK}" stroke-linecap="round" stroke-linejoin="round">
{''.join(parts)}
</g></svg>\n'''

plates=[]

alt1='Two aligned paths share one declared start. Funds become usable before one specified loss hardens, but after an earlier housing loss. Acknowledgement is a distinct earlier event. An unsupported clock remains UNKNOWN.'
p=[text(55,72,'Two clocks, one start',44,bold=True),text(55,120,'Compare the effect with the particular loss.'),line(55,148,845,148)]
p += [text(55,193,'Payment path',26,bold=True),line(35,275,820,275,extra='id="payment-axis"'),line(35,245,35,472,extra='id="shared-origin"'),circle(260,275).replace('<circle','<circle id="acknowledgement"'),circle(535,275,9,INK).replace('<circle','<circle id="payment-effect"'),line(790,257,790,293,width=4,extra='id="payment-hardening"')]
p += [text(62,265,'t0',26,'middle'),text(660,320,'Effect strictly before loss',26,'middle'),text(260,234,'Acknowledged',26,'middle'),text(535,222,['Funds','usable'],26,'middle',True),text(790,222,['Specified loss','hardens'],26,'middle')]
p += [text(55,382,'Coupled housing path',26,bold=True),line(35,445,820,445,extra='id="housing-axis"'),line(405,427,405,463,width=4,extra='id="housing-hardening"'),circle(535,445,9,INK).replace('<circle','<circle id="same-payment-effect"'),text(405,411,'Housing loss',26,'middle'),text(535,492,['Same funds usable;','housing already lost'],26,'middle'),text(55,520,'t0 = declared start',26)]
p += [rect(55,558,790,144,WASH,color=ACCENT),text(80,598,'UNKNOWN',28,bold=True),text(80,640,['Without supported starts or bounds, no window is established.','That alone orders neither a stop nor continuation.'],26)]
plates.append(('01-two-clocks','Two clocks, one start',alt1,p))

alt2='An institution selects an account comparing evening opening hours with the current timetable. Outside its selected account, a visitor faces a missed last bus. A labelled evidence and challenge route leads to an authorised reviewer; it does not predetermine the response.'
p=[text(55,72,'Who draws the map?',44,bold=True),text(55,120,'An account selects. The consequences extend beyond it.'),line(55,148,845,148)]
p += [text(75,198,'Institution / assessor',28,bold=True),line(285,214,285,250,extra='marker-end="url(#arrow)"')]
p += [f'<path d="M 75 268 H 480 L 525 313 V 460 H 75 Z M 480 268 V 313 H 525" fill="{WASH}" stroke="{INK}" stroke-width="2.5"/>',text(100,310,'Selected account',26,bold=True),text(100,356,['Evening opening hours','versus current timetable'],26),line(100,403,490,403),text(100,440,'Whose scope? Which period?',26)]
p += [line(535,338,625,338,extra='marker-end="url(#arrow)"'),rect(645,268,195,176),text(742,314,['Authorised','reviewer'],28,'middle',True),text(742,392,['Considers','the evidence'],26,'middle')]
p += [person(135,591),text(75,654,['Affected','visitor'],26),rect(290,523,180,82),line(300,545,460,545),line(330,523,330,545),line(380,523,380,545),circle(325,609,12,INK),circle(435,609,12,INK),text(275,654,['Last bus','already left'],26)]
p += [f'<path d="M 490 558 H 742 V 455" fill="none" stroke="{INK}" stroke-width="2.5" marker-end="url(#arrow)"/>',text(505,517,['Evidence /','challenge route'],26),text(55,728,'The account is not the whole situation.',28,bold=True)]
plates.append(('02-who-draws-the-map','Who draws the map?',alt2,p))

alt3='Three illustrative panels revisit a child, a glass and a planted pot by a window. First the child notices conditions; then an adult helps the child practise with a tray; finally the child tries another plant while help and tools remain available. Learning is possible, not guaranteed, and continuing upkeep has people behind it.'
p=[text(55,72,'Growing room',44,bold=True),text(55,120,'Capability can be formed, not merely handed over.'),line(55,148,845,148)]
for i,x in enumerate([55,345,635]):
    p += [text(x,204,['1 · Notice','2 · Practise','3 · Adapt'][i],30,bold=True)]
    # Each panel repeats the same window, table, glass and main pot; no stock icons.
    p += [rect(x+57,241,150,130),line(x+132,241,x+132,371),line(x+57,306,x+207,306),line(x+48,429,x+217,429),line(x+68,429,x+68,476),line(x+200,429,x+200,476)]
    p += [f'<path d="M {x+76} 383 L {x+81} 421 H {x+105} L {x+110} 383 Z" fill="none" stroke="{INK}" stroke-width="2.5"/>',line(x+81,402,x+105,402,color=ACCENT)]
    p += [f'<path d="M {x+145} 400 H {x+191} L {x+184} 425 H {x+152} Z" fill="{WASH}" stroke="{INK}" stroke-width="2.5"/>']
    if i==0:
        p += [circle(x+168,395,3,INK)]
    else:
        p += [line(x+168,400,x+168,367 if i==1 else 348,color=ACCENT),f'<path d="M {x+168} 381 Q {x+143} 356 {x+147} 376 Q {x+155} 388 {x+168} 381 M {x+168} 373 Q {x+194} 347 {x+190} 368 Q {x+182} 382 {x+168} 373" fill="{WASH}" stroke="{INK}" stroke-width="2.5"/>',rect(x+140,429,57,9)]
    p += [person(x+23,460,.8),line(x,476,x+253,476,color=INK,width=1.5)]
    if i==1:
        p += [person(x+239,455,1.05)]
    if i==2:
        # A second pot marks transfer to a different plant, not automatic mastery.
        p += [f'<path d="M {x+112} 451 H {x+150} L {x+145} 474 H {x+118} Z" fill="none" stroke="{INK}" stroke-width="2.5"/>',line(x+132,451,x+132,437,color=ACCENT)]
    labels=[['Water, light,','time.'],['Tools, help,','feedback.'],['Try another plant.','Choose a direction.']][i]
    p += [text(x,535,labels,26)]
p += [line(55,604,845,604),text(55,648,'Someone keeps the room usable.',30,bold=True),text(55,691,['Practice may form capability. It can also fail.','Support leaves room to refuse, change course or outgrow it.'],26)]
plates.append(('03-growing-room','Growing room',alt3,p))

metadata=[]
for name,title,alt,parts in plates:
    (ROOT/f'{name}.svg').write_text(svg(name,title,alt,parts),encoding='utf-8')
    metadata.append({'id':name,'title':title,'alt':alt})
(ROOT/'plate-metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated 3 editable SVG candidates; semantic status OPTIONAL_REVIEW_ONLY.')
