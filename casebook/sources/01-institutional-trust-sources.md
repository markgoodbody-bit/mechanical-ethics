# Source receipt for Case 1 (institutional trust)

Companion to `casebook/01-institutional-trust.md`. Prepared by Claude Code on 26 October 2026, from public sources only. Each file was retrieved without credentials (`curl` or a web fetch), and its text was extracted locally with `pdftotext -layout` or an HTML-to-text step. Hashes are of the bytes as retrieved. A later download may differ where a host regenerates the page; the Cornell statute pages are dynamic HTML and are the likeliest to change.

## Files read

| # | Source | Bytes | SHA-256 | How much was read |
|---|---|---|---|---|
| 1a | D.C. Cir. No. 26-5006, opinion, 8 Sept 2026 (CourtListener RECAP doc 2191763) | 248,919 | `a54ebdf96068b8276fc873eab72f09412fa3b29973d132720c4fa5da3ce7e37b` | whole (32 pages) |
| 1b | D.C. Cir. No. 26-5006, judgment, 8 Sept 2026 (doc 2191760) | 61,626 | `0b9e1d4609344f13d602bf83de301de926ecaab32a4539dc8e7dc3274acba179` | whole (1 page) |
| 2 | D.C. Cir. No. 25-5181, *Centro*, opinion, 24 Feb 2026 | 382,675 | `3fac0632bb1d427f171ba4bcbf6f50bbfc6d876c29f304c73c6c1c0d4c738a5b` | **partly**: date, panel, author and the "crystal clear" holding passage. The rest of its holding is taken from CRS (source 4) and from the quotations in source 1a |
| 3 | TIGTA Report 2026-IE-R010, 4 June 2026 | 935,341 | `49b401f5f5e7a6450f67a65d967eaa289b84f7292e6bc3983d7bc4d87251d89e` | whole, including appendices; redactions as published |
| 4 | CRS Legal Sidebar LSB11413, updated 17 Sept 2026 (EveryCRSReport mirror; congress.gov returned HTTP 403 to this fetch) | 34,558 | `49364b6497dcde53b8249341deec92aa331cbb431a3027572cc0a2756ab754a5` | whole |
| 5 | Agreement and IRS declaration, ECF 30-1, No. 1:25-cv-00677 (EPI-hosted copy) | 1,952,703 | `9fb3ed8cf3faf9435944671511c5be6ea9dec6ddf0fbd72e4ef468b2a0763210` | every page with extractable text. Pages 5, 7, 8, 10, 16, 17 and 19 have no text beyond page headers, and pages 1 and 4 are exhibit covers. Those pages were **not** read (no OCR) |
| 6a | 26 U.S.C. §6103, Legal Information Institute page | 832,960 | `2617b29d61d1a5dc3efcf033c2f1671a64bd78b6d1d5273487b32fafd90eef06` | §6103(b)(6), (i)(1)(A), (i)(2)(A)-(C) |
| 6b | 26 U.S.C. §7213 | 65,859 | `4cea041327b718a32bc35572ae807f73e28b287192f08a0e74047b27f385ae64` | (a)(1) |
| 6c | 26 U.S.C. §7431 | 58,165 | `da04797d28c4a9247972412ea17a7261d041c6d6d92e6402bdd85290a19457da` | (c)(1) |
| 7 | *Mechanical Ethics* v1.0.0 master, tag `v1.0.0` | 136,286 | `1315a2c2b500ae2308afd7070d5b3919b23d1390870e65eea54bbc057e6e37a8` | the glossary, Notes, Ch. 6 lines 154-200, Ch. 9 in full, Ch. 10 lines 342-360, Ch. 12 lines 466-484; byte-identical to the released file |

URLs are listed in the case's own source list.

## Claim check

Status key:
- **P**: read in a primary source (statute, court document, agency or Inspector General record).
- **S**: read only in a secondary source (CRS) or a court's quotation of another document.
- **A**: attributed claim, reported as someone's statement, not verified.
- **U**: UNKNOWN in the sources used.

| Claim in the case | Source(s) | Status |
|---|---|---|
| Agreement signed 7 Apr 2025; no request made by then | 5 (IRS declaration ¶¶3-5); 3 (App. III) | P |
| Implementing agreement 18 Apr 2025 | 3 (App. III) | P (its text not seen) |
| ICE request for about 1.28 million last known addresses, 27 Jun 2025 | 1a (Lyons letter, Romo Decl. ¶4); 3 ("over 1.2 million"); 4 | P via court record; the letter itself not seen |
| Earlier ICE request about more than 7 million people | 1a, quoting the district court | S |
| 47,289 records disclosed, 7 Aug 2025 | 1a; 3; 4 | P, but every count traces to IRS records and the Romo declaration |
| About 46,965 individuals | 3, footnote 4 | P (TIGTA's own analysis of IRS data) |
| 42,695 (90.3%) matched by taxpayer number | 4; 1a ("more than 90%", "90.3%") | P via court; the declaration itself not seen |
| "Less than 5%" potentially incomplete or insufficient ICE addresses | 3; 4 | A (IRS's own estimate) |
| Only last known address shared, no other tax information | 3 | A (IRS statement to TIGTA) |
| Address sent undated | 1a | P |
| Procedure checked only that fields were non-empty and that the address field had five or nine digits | 1a; 3; 4 | P |
| One point of contact for every request | 1a, quoting the district court | S |
| Reason "more circular than specific" | 1a, quoting the district court | P (appeals court adopting the phrase) |
| Individual review under the IRS manual before 17 Apr 2025 | 1a (IRM 11.3.28.2) | S (manual not read) |
| IRS's earlier position: no provision for immigration enforcement; address-only disclosure prohibited | 1a, quoting 89 Fed. Reg. 93174 and *Centro* | S |
| Government acknowledged unlawful transfers at argument | 1a (Oral Arg. Tr. 8:19-9:3, 15:17-19, 28:11-13) | S (transcript not read) |
| Government counsel not aware what the IRS did to fix the procedure | 1a (Oral Arg. Tr. 46-48) | S |
| District court order 21 Nov 2025 (stay, injunction, advance notice) | 1a (twice), 2, 3, 4 | P; see discrepancy D1 |
| Massachusetts order barring ICE and DHS use, 5 Feb 2026 | 4 | S |
| DHS and ICE confirmed non-use pending the lawsuits | 3 | A (IRS statement to TIGTA) |
| TIGTA concerns Nov-Dec 2025 led to the IRS's manual review; IRS notified DHS 23 Jan 2026 | 3 | P |
| ICE safeguard findings open; corrective plans missing or undated; review postponed | 3 | P for TIGTA's account; A for the IRS's statements within it |
| Center's clinic: "drastic" fall in cases; "nearly 10 percent" of expenses moved to outreach | 1a (Olson Decl. ¶¶41-46, as found by the district court) | S |
| *Centro*: the agreement likely complies on its face; addresses are not taxpayer return information | 2 (holding passage); 4; 1a | P for the passage read, S for the rest |
| Statute text: §6103(i)(2) four request elements, "personally and directly engaged", identity rule, (b)(6) definition, (i)(1) ex parte order | 6a | P |
| Penalties: §7213(a)(1) felony; §7431 the greater of $1,000 per act or actual damages | 6b; 6c | P |
| Congressional letters 12 Feb 2026; hearing 4 Mar 2026 | 4 | S |
| First Circuit argument scheduled 7 Oct 2026 | 4 | S (outcome not checked) |
| Whether any disclosed address was used before 5 Feb 2026 | none | U |
| Whether affected people were notified | none | U |
| A population-level change in filing | none found; one standard web search found advocates' reports, no systematic 2026 data | U |

## Discrepancies found, and how the case treats them

- **D1, order date.** Source 1a cites "Order of Nov. 21, 2025" on its pages 9 and 31. Its conclusion and the judgment (1b) say "order of November 1, 2025". Sources 2, 3 and 4 give 21 November. The case uses 21 November and records the slip.
- **D2, requested count.** TIGTA says "over 1.2 million"; the court and CRS say about 1.28 million. These are compatible; the case gives both.
- **D3, records against individuals.** TIGTA's background text says "approximately 47,289 individuals", but its own footnote finds those records correspond to about 46,965 individuals. The case uses 47,289 *records* and about 46,965 *people*.
- **D4, a search summary's figure.** A web-search result summary gave "47,489" for a third-party case page. That page was not read, and the figure appears in no source read here. It is not used.
- **D5, a model summary's addition.** An automated summary of the CRS sidebar named the IRS's chief executive. The visible CRS text (source 4) does not: the name appears only inside the URL of its link to the hearing page. The case does not use the name.

## Not used

- **The interview with Michael Lewis that prompted this case.** I did not read the transcript. No fact in the case rests on it. Where a figure attributed to it appears (seven million), the case cites the court record instead.
- **Press reports, including the Reuters article cited elsewhere in the project.** I did not read them, and no fact rests on them.
- **Sealed filings, the implementing agreement, the image-only pages of source 5, the oral-argument transcript and the Romo declaration itself.** None was read; each is cited only through a source that quotes it.

## Limits

This receipt records what was read and where each claim comes from. It is not a legal opinion, and no lawyer reviewed it. The court rulings are preliminary. A reader relying on any legal point should check the current docket.

## Build integration note

The tables above preserve Claude Code's original source-reading receipt. Build's
editorial changes to the chapter are recorded in [the whole-casebook review](WHOLE-CASEBOOK-REVIEW.md).
In particular, the original abbreviated damages description is no longer used
as a complete account: Build checked §7431(a)–(e), including liability conditions,
exceptions and mandatory notification triggers. That additional reading is
Build's, not a retroactive extension of CC's reported read of subsection (c)(1).
