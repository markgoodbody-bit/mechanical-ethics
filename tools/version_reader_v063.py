#!/usr/bin/env python3
from pathlib import Path
import hashlib
import subprocess

CURRENT = Path('MECHANICAL_ETHICS_HUMAN_READER_v0_6_2.md')
NEXT = Path('MECHANICAL_ETHICS_HUMAN_READER_v0_6_3.md')
BASE_COMMIT = 'fb2cc9e41107bba6ec66d7788513d6e208af80c5'
REPAIRED_V062_BLOB = 'cb90b3f11d7de80ce4db4400d78150e957700d65'
ORIGINAL_V062_BLOB = '6e06f210a5479ee6f84f5491c151a9d951a0da02'
ORIGINAL_V062_PDF_BLOB = '57d77c870ff90f5f3f448b300b882201a2bed433'


def blob(data: bytes) -> str:
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


repaired = CURRENT.read_bytes()
if blob(repaired) != REPAIRED_V062_BLOB:
    raise SystemExit(f'current repaired source guard failed: {blob(repaired)}')
text = repaired.decode('utf-8')
text = text.replace(
    '**Human Reader v0.6.2 - FORMAL HONESTY AND FACTUAL CORRECTION CANDIDATE**',
    '**Human Reader v0.6.3 - REVIEW SCOPE AND BOUNDED ANSWERABILITY REPAIR CANDIDATE**',
    1,
)
old = '''This is *Mechanical Ethics: When Correction Arrives Too Late*, Human Reader v0.6.2 FORMAL HONESTY AND FACTUAL CORRECTION CANDIDATE.

The v0.6.2 pass preserves the complete v0.6.1 structure and makes a bounded formal-honesty and factual-correction patch. The central timing relation now distinguishes elapsed time to effective protection from time to hardening, while retaining the earlier inequality only as conceptual compression. The viability notation now carries explicit constraint and horizon inputs. The file/life distinction is made two-way, the predator-position threshold is narrowed, the historical notes are less compressed, the enforcement limit is stated, the figure sequence is corrected, the finance case is retitled, and the unsupported doorway equation is removed.

The set $\\mathcal{K}_{C,H}$ is not presented as a definition, score, or optimisation of meaning. It represents the states from which at least one continuation remains available under an explicit filter set $C$ and stated horizon $H$. The result inherits the authorship, uncertainty, and contestability of those inputs. The conclusion limits institutions and automated systems to protecting conditions for usable agency rather than deciding which meaningful life should be chosen.

The v0.5 main-body register repair remains the immediate prose baseline for all unchanged material. No composite scene or case outcome has been altered. The Kelsey and Challenger notes have been narrowed to reflect the institutional authority and decision structure recorded in the cited official sources.'''
new = '''This is *Mechanical Ethics: When Correction Arrives Too Late*, Human Reader v0.6.3 REVIEW SCOPE AND BOUNDED ANSWERABILITY REPAIR CANDIDATE.

The v0.6.3 pass preserves the complete v0.6.2 reader and makes two bounded main-body repairs. Chapter 12 now states that a review can be complete within its own file while still omitting affected people or making unlike cases look like one pattern. Chapter 15 now distinguishes answerability from indefinite reopening while refusing to treat repetition as proof of resolution. No other main-body argument, composite scene, case outcome, formal notation, figure placement, historical source note, or conclusion has been changed.

The v0.6.2 formal-honesty and factual-correction pass remains the immediate technical baseline for all unchanged material. It distinguished elapsed time to effective protection from time to hardening, retained the earlier inequality only as conceptual compression, added explicit constraint and horizon inputs to the viability notation, made the file/life distinction two-way, narrowed the predator-position threshold, reduced historical compression, stated the enforcement limit, corrected the figure sequence, retitled the finance case, and removed the unsupported doorway equation.

The set $\\mathcal{K}_{C,H}$ is not presented as a definition, score, or optimisation of meaning. It represents the states from which at least one continuation remains available under an explicit filter set $C$ and stated horizon $H$. The result inherits the authorship, uncertainty, and contestability of those inputs. The conclusion limits institutions and automated systems to protecting conditions for usable agency rather than deciding which meaningful life should be chosen.

The v0.5 main-body register repair remains the prose baseline beneath the bounded v0.6.2 and v0.6.3 patches. The Kelsey and Challenger notes remain narrowed to reflect the institutional authority and decision structure recorded in the cited official sources.'''
if old not in text:
    raise SystemExit('reader status block guard failed')
text = text.replace(old, new, 1)
if text.count('Human Reader v0.6.3') != 2:
    raise SystemExit('v0.6.3 identity count failed')
NEXT.write_text(text, encoding='utf-8')

original_source = subprocess.check_output(['git', 'show', f'{BASE_COMMIT}:{CURRENT}'])
if blob(original_source) != ORIGINAL_V062_BLOB:
    raise SystemExit('original v0.6.2 source guard failed')
CURRENT.write_bytes(original_source)

original_pdf = subprocess.check_output(['git', 'show', f'{BASE_COMMIT}:Mechanical_Ethics.pdf'])
if blob(original_pdf) != ORIGINAL_V062_PDF_BLOB:
    raise SystemExit('original v0.6.2 PDF guard failed')
Path('Mechanical_Ethics_v0_6_2.pdf').write_bytes(original_pdf)

Path('README.md').write_text('''# Mechanical Ethics

Mechanical Ethics is the human-facing side of this project.

It is an attempt to make ethics structurally understandable: harm, care, responsibility, dignity, trust, repair, closure, and answerability.

Mechanical Ethics is not a doctrine, moral authority, certification system, or finished framework. It is an active attempt to make human ethical ideas clearer by asking what is structurally happening.

Start here:

- `Mechanical_Ethics_v0_6_3.pdf` — current human-reader PDF
- `MECHANICAL_ETHICS_HUMAN_READER_v0_6_3.md` — current plain-Markdown and machine-readable source
- `Mechanical_Ethics.pdf` — convenience alias identical to the v0.6.3 PDF
- `MECHANICAL_ETHICS_HUMAN_READER_v0_6_2.md` and `Mechanical_Ethics_v0_6_2.pdf` — preserved previous version
- `PROJECT/PROJECT.md`
- `PROJECT/MAP.md`

Version rule: any change to the reader source increments the patch version. Previously numbered source and PDF artifacts remain unchanged.
''', encoding='utf-8')
print(NEXT)
