# Five-minute author review and go/no-go sheet

**Framework Build · 13 October 2026 · research companion only · not approved for release or publication.**

## Read the actual page

Open [human_review_offline.html](human_review_offline.html) from this folder (file:///; no server or scripts required). It is intentionally ONE 29–35 KB-range self-contained HTML file with embedded CSS and selectable text, derived from [PR63's exact Workshop-first reading text](../human_review/ME_V0_9_SHORT_HUMAN_REVIEW_CANDIDATE_20261013.md). The original released [Mechanical Ethics v0.8.0](https://github.com/markgoodbody-bit/mechanical-ethics/blob/e2ef746e931161cb70ac46a4eaa122442134e86b/MECHANICAL_ETHICS.md) stays complete and separately accessible.

This is a **companion candidate** rather than a successor edition: it changes *entry/order and compression*, not a moral theorem. It starts from Nia's repaired bicycle and learned repair capability, then tests that constructive idea against Leah/Mia's deteriorating room, a closing clock, power and legitimate refusal. Source custody, the four original diagrams, human author note and full historical notes are **not** smuggled into this shorter page or declared unnecessary.

## Five-minute walkthrough for a cold, uncoached human reader (synthetic QA script, NOT completed human study)

1. **0:00–1:00** Open offline page on a narrow mobile viewport. Read the visible research/unreleased label and use the **Skip to reading text** keyboard link. Ask: “Is this clearly an optional research companion, not the complete released book?”
2. **1:00–2:00** Read section **1. More than a repaired bicycle**. Ask: “Why are a fixed item, a person's usable new repair skill, and a continuing shared workshop three different improvements?” **Expected grounded answer:** one immediate object works, one actor may act independently later, and maintaining a shared place/skills can give several people repeatable routes. No claim these later outcomes were empirically observed.
3. **2:00–3:00** Read section **2. The future does not wait for our account of it**. Ask: “If Leah's room is unsafe and learning the reporting system takes longer than a protective window, what comes first?” **Expected:** an actually usable timely protective route through the responsible human/service; optional education later, not a new proof burden for the tenant. A corrected file alone doesn't dry a wall.
4. **3:00–4:00** Read sections **4–6** and ask: “Does being cooperative prove consent? Does a true record settle a harmful situation? Does a later apology erase residue?” **Expected:** no; distribution of power, privacy, actual consequences and ability to refuse/answer back matter.
5. **4:00–5:00** Follow a Contents link and a released-source link; inspect print view. Ask: “Is the whole v0.8 book, with authorial voice, figures and historical sources, still clearly reachable?” **Expected:** yes (external URLs require network). Ask if this companion genuinely reduces burden compared with reading v0.8 directly. That last question needs **actual independent reader feedback**, not the deterministic test suite.

No participant was recruited and no real cold human test was conducted by this script. A passing machine audit does not answer whether the shorter explanation is better.

## Author's actual decisions

- **OPTION A — no published delta:** Keep released v0.8 alone. It already teaches formation, timely correction, refusal and hope. This is the strongest low-burden baseline.
- **OPTION B — offer as clearly marked research companion:** Separate optional reading file with no formal edition claim. Only after Mark decides wording, authorship/provenance and appropriate licence/public release route.
- **OPTION C — select a short bridge for a future human-edited v0.9:** Integrate just the earned formation-vs-protection distinction into a complete edited manuscript **after** source-by-source custody review, rather than silently replacing original material.

Current choice by Build: **HOLD / AUTHOR REVIEW**, not publication. Mark is the human originator and release gate. No title, version, licence, PDF, website deployment, training permission or release right was created here.

## Potential editorial weaknesses and falsifiers

- **Narrative placement:** Workshop-first is deliberately different from v0.8's entity-first start. It may improve first contact, or it may weaken the original human force of Leah/Mia. Compare with equivalent reading time.
- **Reduction:** This companion leaves full composites, the four original figures, author note, source appendix and history **only in v0.8**, not duplicated. As a future replacement edition, that would be a major unacceptable content loss unless Mark deliberately reconciles it.
- **Safety:** Teaching under an imminent restriction can shift the deadline burden to the person at risk. CC's specific correction is included in the source. If a reader takes “learn your own way out” from the page while the protective door is closing, revise or discard.
- **False novelty/authority:** Sen, Nussbaum, Robeyns and other capability owners predate this work. TRACE and synthetic Possibility Game experiments do not award ethical standing or prove scale invariance. If this page implies either, revise.
- **Practical advantage:** A readable page and green tests do not demonstrate value for actual people. If released v0.8 and stronger existing owner guidance give clearer/faster safe next steps, choose NO DELTA.

## Source recipe, reproducibility and limitations

From the repository root:

    python research/offline_review/build_review.py --check
    python -m unittest discover -s research/offline_review -p 'test_review.py' -v

To regenerate (after a deliberate new source-author decision only):

    python research/offline_review/build_review.py

The generator currently **refuses any source different from the exact PR63 Git blob** \`5b435896169f8de7d2508ed658ce5047f84ceebb\`. The page is checked in as identical deterministic output. Its HTML contains no script, form, network request, interactive posting surface, private data or remotely loaded font. Plain anchors, screen-reader landmarks and CSS print rules are used. Browser QA uses Chromium with real viewport and keyboard/print tests; evidence belongs to the exact commit's CI run and must not be presumed green before checking it.

The review's evidence and source/historical custody are tracked in [PR63's editorial ledger](../human_review/EDITORIAL_CUSTODY_DECISIONS_20261013.md). Nothing in this repository grants permission to copy the released diagrams or protected human testimony into a new publication.

## The next warranted experiment

If Mark is willing later, give **one person who hasn't followed the project** a choice of this 5-minute optional page and the corresponding released v0.8 sections. Ask whether they can distinguish a repaired item, a learned skill and a timely protection, and what the next legitimate human action would be. Obtain real consent first. Do not turn this suggestion into outreach without explicit human authority.
