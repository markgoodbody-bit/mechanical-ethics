#!/usr/bin/env python3
"""Build an offline reading copy from an explicitly pinned Markdown snapshot.
Requires Python 3 and pandoc 3.1.3. No network, Javascript, or telemetry.
"""
import hashlib, html, json, pathlib, re, subprocess
ROOT = pathlib.Path(__file__).resolve().parents[1]
REF = 'eaa908bb72f0c094fc74ee63690d9fc6574de8b5'
FILES = ['README.md','00-start-where-you-are.md','05-try-another-account.md',
 '01-institutional-trust.md','02-camp-fire.md','03-paid-first-rung.md',
 '04-reading-across-cases.md'] + sorted(str(p.relative_to(ROOT)) for p in (ROOT/'sources').glob('*.md'))
IDS = {p:'page-'+str(i) for i,p in enumerate(FILES)}
LABELS = ['About this book','Start where you are','Try another account','Confidentiality and addresses','Camp Fire','A paid first rung','Reading across cases']
CSS = '''
:root{color-scheme:light;--paper:#f8f6f0;--ink:#292c28;--muted:#5a625a;--accent:#285a49}
*{box-sizing:border-box}html{scroll-behavior:auto}body{margin:0;background:var(--paper);color:var(--ink);font:18px/1.75 Georgia,serif}
a{color:var(--accent);text-underline-offset:.2em;overflow-wrap:anywhere}a:focus-visible,summary:focus-visible{outline:3px solid #a35b25;outline-offset:5px}
.skip{position:absolute;left:1rem;top:-6rem;background:white;padding:.5rem;z-index:5}.skip:focus{top:1rem}
header,main,footer{max-width:780px;margin:auto;padding:2rem 1.5rem}header{padding-top:4rem;border-bottom:1px solid #d7d9cf}
.eyebrow,.meta,nav,.page-top,summary,.evidence{font: .88rem/1.6 system-ui,sans-serif}.eyebrow{letter-spacing:.13em;text-transform:uppercase;color:var(--muted)}
header h1{font-size:clamp(2.4rem,7vw,3.8rem);line-height:1.1;font-weight:normal;margin:1rem 0}.intro{font-size:1.2rem;max-width:34em}
.meta{color:var(--muted)}nav ol{padding-left:1.4rem}nav li{padding:.18rem 0}summary{cursor:pointer;padding:.5rem 0}
article{padding:3rem 0;border-bottom:1px solid #d7d9cf;scroll-margin-top:1rem}article h1{font-size:2rem;line-height:1.25}h2{font-size:1.45rem;line-height:1.35;margin-top:2.3rem}h3{font-size:1.2rem}
p,li{overflow-wrap:anywhere}blockquote{border-left:3px solid #a3b8a4;margin:1.5rem 0;padding:0 1rem;color:#465247}li{margin:.4rem 0}
.table-wrap{overflow-x:auto;margin:1.5rem 0}table{border-collapse:collapse;font: .86rem/1.6 system-ui,sans-serif;width:100%;min-width:480px}th,td{padding:.65rem;text-align:left;vertical-align:top;border-bottom:1px solid #cdd1c6}th{background:#e9ede3}
code{font-size:.8em;overflow-wrap:anywhere}pre{white-space:pre-wrap}.evidence{border-left:3px solid #9aaa90;padding:.5rem 1rem}.page-top{display:flex;flex-wrap:wrap;gap:.6rem 1.5rem}footer{font-size:.9rem}
@media(max-width:480px){body{font-size:17px}header,main,footer{padding-left:1.1rem;padding-right:1.1rem}article{padding:2rem 0}article h1{font-size:1.7rem}}
@media print{body{background:white;font-size:11pt}header,main,footer{max-width:none;padding:0}nav,.skip,.page-top{display:none}article{break-before:page;border:0}table{min-width:0;font-size:9pt}.table-wrap{overflow:visible}a{color:inherit}details> *{display:block}}
'''
def convert_ast(node, path):
    if isinstance(node,list): return [convert_ast(x,path) for x in node]
    if not isinstance(node,dict): return node
    node={k:convert_ast(v,path) for k,v in node.items()}
    if node.get('t')=='Header': node['c'][1][0]=IDS[path]+'-'+node['c'][1][0]
    if node.get('t')=='Link':
        url=node['c'][2][0]
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',url):
            target,_,fragment=url.partition('#')
            resolved=(ROOT/path).parent/target if target else ROOT/path
            rel=str(resolved.resolve().relative_to(ROOT))
            if rel not in IDS: raise ValueError('Unbundled link: '+url)
            node['c'][2][0]='#'+IDS[rel]+('-'+fragment if fragment else '')
    return node
manifest={'source_commit':REF,'files':{}}
lock_path = ROOT/'reader/source-manifest.json'
if lock_path.exists():
    lock = json.loads(lock_path.read_text())
    if lock['source_commit'] != REF or set(lock['files']) != set(FILES):
        raise ValueError('Snapshot identity changed; review and repin before rebuilding')
    for path in FILES:
        raw = (ROOT/path).read_bytes()
        if lock['files'][path] != {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}:
            raise ValueError('Source changed; review and repin before rebuilding: '+path)
sections=[]
for path in FILES:
    raw=(ROOT/path).read_bytes()
    manifest['files'][path]={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    ast=json.loads(subprocess.check_output(['pandoc','-f','gfm','-t','json'],input=raw))
    rendered=subprocess.check_output(['pandoc','-f','json','-t','html5','--wrap=none'],input=json.dumps(convert_ast(ast,path)).encode()).decode()
    rendered=rendered.replace('<table>','<div class="table-wrap" role="region" aria-label="Scrollable comparison table" tabindex="0"><table>').replace('</table>','</table></div>')
    link=f'https://github.com/markgoodbody-bit/mechanical-ethics/blob/{REF}/casebook/{path}'
    sections.append(f'<article id="{IDS[path]}"><div class="page-top"><a href="#contents">Contents</a><a href="{html.escape(link)}">Pinned Markdown source ↗</a></div>{rendered}</article>')
nav=''.join(f'<li><a href="#{IDS[p]}">{html.escape(LABELS[i])}</a></li>' for i,p in enumerate(FILES[:7]))
notes=''.join(f'<li><a href="#{IDS[p]}">{html.escape(p.removeprefix("sources/").removesuffix(".md").replace("-"," "))}</a></li>' for p in FILES[7:])
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'"><title>Mechanical Ethics — A reading room</title><style>{CSS}</style></head><body>
<a class="skip" href="#reading">Skip to the book</a><header id="contents"><p class="eyebrow">Mechanical Ethics · working casebook</p><h1>A reading room</h1><p class="intro">Three situations. Different lives and constraints. A shared invitation to look more closely—and leave room to change your mind.</p><p class="meta">26 October 2026 · v0.1 working supplement · editorial review continuing<br>Reading snapshot: <code>{REF}</code></p><p class="evidence">The institutional and fire cases follow dated public evidence. The paid-work situation is constructed. Interpretations and proposals remain open to challenge; none of these cases establishes field effectiveness.</p><nav aria-label="Book contents"><ol>{nav}</ol><details><summary>Source notes and editorial history</summary><ul>{notes}</ul></details></nav><p class="meta">Everything below is included in this file. External source links need a connection. This is a reading copy, not a live Workshop or team-status view.</p></header><main id="reading">{''.join(sections)}</main><footer><a href="#contents">Back to contents</a><p>Keep the question open: what would change your account?</p></footer></body></html>'''
(ROOT/'reader/index.html').write_text(page,encoding='utf-8')
(ROOT/'reader/source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(f'Built {len(FILES)} documents, {len(page.encode())} UTF-8 bytes')
