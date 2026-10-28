# Search protocol

Scoping review protocol for the [LLM code detection review](../README.md). Inclusion criteria are the **Scope** section of that README. This file records how the search runs, so the review's method section (PRISMA-ScR items 7–10) can be written from it.

## Sources searched

arXiv, Semantic Scholar, ACL Anthology, ACM Digital Library, IEEE Xplore, DBLP, Google Scholar. Backward and forward snowballing from each included paper.

## Search slices

The search runs as three parallel slices. Each slice owns its query families; overlap between slices is expected and removed at dedupe.

| Slice | Owns | Output |
| --- | --- | --- |
| A — detectors | zero-shot statistical detectors (perplexity, perturbation, likelihood curvature), trained classifiers (CodeBERT / CodeT5 / LLM fine-tunes), benchmarks and datasets of human vs LLM code | [biblio-a-detectors.md](biblio-a-detectors.md) |
| B — education and contests | studies in programming courses, exams, academic integrity, plagiarism tools (MOSS, JPlag, Dolos) facing LLM code, competitive programming and online judges, stylometry / AST / authorship attribution | [biblio-b-education-contests.md](biblio-b-education-contests.md) |
| C — watermarks and robustness | generation-time watermarking of code, evasion by paraphrase / obfuscation / refactoring, human-edited or mixed-authorship code, detector reliability and false positives | [biblio-c-watermark-robustness.md](biblio-c-watermark-robustness.md) |

Query terms per slice combine a setting term (`code`, `program`, `programming assignment`, `source code`, `competitive programming`, `LeetCode`, `Codeforces`) with a task term (`AI-generated`, `LLM-generated`, `machine-generated`, `ChatGPT`, `detection`, `detector`, `authorship`, `watermark`). Each slice logs the exact queries it ran in its output file.

## Per-paper entry

Every candidate gets one entry, whether kept or dropped:

```markdown
### <Title>
- **Authors**: <all, or first three + et al.>
- **Year / first public**: <YYYY-MM of first arXiv or publication version>
- **Venue**: <venue name> | arXiv preprint
- **URL**: <arXiv abs / DOI / anthology URL you opened>
- **Access**: open | paywalled
- **Setting**: education | competitive programming | general code on coding-problem data | out of scope
- **Method family**: zero-shot | trained classifier | stylometry/AST | watermark | robustness study | dataset/benchmark | empirical study
- **Dataset**: <name, languages, size>
- **Headline result**: <one sentence with the number, e.g. "AUROC 0.94 on APPS Python">
- **Limitation**: <one sentence, marked [author-acknowledged] or [reader-inferred]>
- **Decision**: include | background | exclude — <reason against the Scope criteria>
```

## Verification rule

A paper enters a slice file only after its URL was opened and the title, authors and date on that page match the entry. A paper that cannot be confirmed this way is left out entirely.
