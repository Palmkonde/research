# Plan: LLM code detection review

Goal: hand the supervisor a complete literature review ([review.md](review.md), exported to PDF or Word) by 30 Nov 2026. Scope in [README.md](README.md). **Status: active.**

## Milestones

- [x] **By 4 Nov — scan** (done 28 Oct: 160 papers screened, 89 included, 34 core with Source notes, 24 in no-access): lit-review scan saved in [scan/](scan/); every candidate paper either has a verified Source note (real URL, date fetched, venue or "arXiv preprint", in scope per README), a line in `no-access.md`, or is dropped. Done when ≥25 core papers have Source notes.
- [x] **By 8 Nov — citation check** (done 28 Oct: 89 notes verified by agent, 2 later notes checked on Crossref; report in [scan/citation-check-report.md](scan/citation-check-report.md)): `academic-research-skills:academic-paper` in `citation-check` mode passes on every Source note; failures fixed or removed.
- [x] **By 15 Nov — annotated bibliography** (done 28 Oct: 36 core entries and a 53-row table in [review.md](review.md); iJudge and Sieving are *(pending source)* until downloaded): every core paper has an entry in `review.md` with setting, method, dataset, headline result and limitation. Papers from `no-access.md` downloaded by then are included.
- [ ] **By 25 Nov — synthesis** (first draft of sections 1, 4 and 5 written 28 Oct; still to check against the papers, and the false-positive gap against the 53 table papers): `review.md` has the thematic sections (methods, datasets and benchmarks, robustness, gaps) and every claim sentence cites a paper or is marked *(inference)*.
- [ ] **By 30 Nov — hand-over**: `review.md` exported, sent to the supervisor; follow-up Questions added to the Topic README.

## Working mode

`review.md` cites in APA 7 (in-text plus a reference list). Each reference-list entry links to its Source note, so the vault and the deliverable stay in sync.
