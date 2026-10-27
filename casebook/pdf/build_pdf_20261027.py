"""Build the five-case reading edition from pinned local Markdown; no network."""
import argparse,hashlib,html,json,pathlib,re,subprocess
from weasyprint import HTML
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parent
REF='9acb06fb9ca07814076b7462cca0ee2f08ae4cbb'
FILES=['01-institutional-trust.md','02-camp-fire.md','03-paid-first-rung.md',
 '06-gitlab-recovery.md','07-nls-reading-access.md','04-reading-across-cases.md',
 '08-reading-across-five-cases.md']+sorted(str(p.relative_to(ROOT)) for p in (ROOT/'sources').glob('*.md'))
IDS={p:'doc-'+str(i) for i,p in enumerate(FILES)}
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=pathlib.Path,default=HERE/'Mechanical_Ethics_Casebook_2026-10-27.pdf')
args=parser.parse_args()
manifest={'source_commit':REF,'files':{p:{'bytes':len((ROOT/p).read_bytes()),'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in FILES}}
lock=HERE/'source-manifest-20261027.json'
if lock.exists() and json.loads(lock.read_text())!=manifest: raise ValueError('Pinned source snapshot differs')
lock.write_text(json.dumps(manifest,indent=2)+'\n')
def transform(n,path):
 if isinstance(n,list): return [transform(x,path) for x in n]
 if not isinstance(n,dict): return n
 n={k:transform(v,path) for k,v in n.items()}
 if n.get('t')=='Header': n['c'][1][0]=IDS[path]+'-'+n['c'][1][0]
 if n.get('t')=='Link':
  url=n['c'][2][0]
  if not re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',url):
   target,_,fragment=url.partition('#')
   resolved=((ROOT/path).parent/target).resolve() if target else (ROOT/path).resolve()
   try: relative=str(resolved.relative_to(ROOT.resolve()))
   except ValueError: relative=None
   if relative in IDS: n['c'][2][0]='#'+IDS[relative]+('-'+fragment if fragment else '')
   else:
    repo_path=str(resolved.relative_to(ROOT.parent.resolve()))
    n['c'][2][0]=f'https://github.com/markgoodbody-bit/mechanical-ethics/blob/{REF}/{repo_path}'+('#'+fragment if fragment else '')
 return n
sections=[];toc=[]
for i,path in enumerate(FILES):
 raw=(ROOT/path).read_bytes()
 title=next(x.lstrip('# ').strip() for x in raw.decode().splitlines() if x.startswith('# '))
 ast=json.loads(subprocess.check_output(['pandoc','-f','gfm','-t','json'],input=raw))
 rendered=subprocess.check_output(['pandoc','-f','json','-t','html5','--wrap=none'],input=json.dumps(transform(ast,path)).encode()).decode()
 sections.append(f'<article id="{IDS[path]}">{rendered}</article>')
 if i==7: toc.append('<h2>Source notes and editorial history</h2>')
 toc.append(f'<p><a href="#{IDS[path]}">{html.escape(title)}</a></p>')
css=(HERE/'print-20261027.css').read_text()
cover='''<header class="cover"><p class="eyebrow">Mechanical Ethics · Casebook</p><h1>Case studies and<br>technical analysis</h1><p class="intro">Institutional information disclosure<br>Wildfire protective action<br>Technical employment design<br>Database recovery<br>Accessible reading services</p><p class="edition">Five-case reading edition · 27 October 2026</p><p class="scope">Four source-based studies and one constructed design study.<br>With comparative analysis, source notes and editorial history.</p><p class="small">A supplement to Mechanical Ethics 1.0.<br>These studies do not establish field effectiveness.</p></header>'''
scope=f'''<section class="contents" id="contents"><h1>Contents</h1>{''.join(toc)}<p class="small provenance">Markdown source pinned to {REF}. Study texts are unchanged. The original three-case comparison and dated editorial history are retained alongside the later five-case comparison; historical statements describe their own edition. Legal and other source cutoffs remain those stated in each study. This document changes reading format, not evidence or rights. External sources require a connection.</p></section>'''
page='<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Mechanical Ethics: five-case reading edition</title><style>'+css+'</style></head><body>'+cover+scope+''.join(sections)+'</body></html>'
(HERE/'source-reader-20261027.html').write_text(page)
def offline_fetch(url,*a,**kw): raise ValueError('Remote resource fetch disabled: '+url)
HTML(string=page,base_url=str(HERE),url_fetcher=offline_fetch).write_pdf(args.output)
print(args.output)
