# LLM code detection review

Literature review for my supervisor on detecting LLM-generated code in coding problems. **Due 30 Nov 2026.** Schedule in [PLAN.md](PLAN.md); deliverable in [review.md](review.md).

## Brief

Survey papers from the last 3 years on telling LLM-written solutions apart from human-written ones in coding problems. Deliver an annotated bibliography plus a thematic synthesis, in English, APA 7.

**Form: scoping review.** Run with ARS `lit-review` mode, which has no scoping-specific protocol, so we follow the PRISMA-ScR checklist ourselves. Search protocol and per-run logs: [scan/search-protocol.md](scan/search-protocol.md).

## Scope

A paper is **in** when all of these hold:
- **Date**: first public version between Nov 2023 and Oct 2026. arXiv preprints count and are labelled "arXiv preprint". Older foundational papers (e.g. DetectGPT, GPTSniffer) are cited as background only, outside the core corpus.
- **Setting**: programming education (assignments, exams, academic integrity) or competitive programming (online judges, contests). A general-code detector is in when it is evaluated on coding-problem data (LeetCode, APPS, CodeNet, Codeforces and similar).
- **Method**: any of zero-shot statistical detectors, trained classifiers, stylometric / AST-feature methods, watermarking at generation time, or robustness studies (paraphrase, obfuscation, human-edited AI code).

Target: 25–40 core papers.

### Scope decisions (28 Oct 2026)

- **SemEval-2026 Task 13**: the task overview and the 6 system papers already verified stay in the corpus; the other ~21 system papers are not screened. The method section states this as a limitation.
- **Watermarking**: kept at its current weight (5 core papers plus 2 robustness papers, 17 more as table rows). The synthesis notes that watermarks need the LLM provider's cooperation, which an educator using ChatGPT submissions does not have. Whether any watermark paper tests on real student code is still to check while annotating.
- **Corpus size**: all included papers stay. Core papers (about 36) get full annotations in `review.md`; the rest get one table row each.

## Where things live

- Papers: one Source note each in [machine-learning/llm-generated-code-detection/sources/](../../machine-learning/llm-generated-code-detection/sources/). Paywalled ones are listed in [no-access.md](../../machine-learning/llm-generated-code-detection/sources/no-access.md) for download on university wifi.
- Open Questions this review raises: the [Topic README](../../machine-learning/llm-generated-code-detection/README.md).
- Raw literature-scan reports: [scan/](scan/). They are search leads, not citable; every paper in them is verified before it gets a Source note.
