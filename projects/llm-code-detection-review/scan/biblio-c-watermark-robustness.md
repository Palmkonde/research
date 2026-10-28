# Slice C — watermarks and robustness

Bibliography log for slice C of the [search protocol](search-protocol.md): generation-time watermarking of code, evasion by paraphrase, obfuscation or refactoring, human-edited or mixed-authorship code, and detector reliability. Inclusion criteria are the **Scope** section of the [review README](../README.md). Searches were run and pages opened on **2026-10-28**.

How the Scope was applied in this slice:

- **Date.** The first public version decides, not the venue year. A paper first posted before Nov 2023 is **background**, even if a conference published it later. SWEET is the main case: first on arXiv in May 2023, published at ACL 2024.
- **Watermark scope.** A watermark is in when the LLM provider applies it to the model's code output, either during decoding or as a post-processing step on generated code, **and** the paper evaluates it on coding-problem data (HumanEval, MBPP, APPS, CodeContests, CodeNet and similar). Out of scope: watermarks that prove ownership of arbitrary source code, watermarks on training datasets, and backdoor watermarks that verify ownership of a model. General-text watermarks that use HumanEval or MBPP as their low-entropy testbed are in, and their Decision says when code was only one task among several.
- **Detector and robustness papers.** These are in when their human-written code comes from coding problems: LeetCode, Codeforces, CodeNet, TACO, course assignments and similar. They are out when it comes only from GitHub repository functions or CodeSearchNet. Overlap with slices A and B is expected and is not a reason to exclude a paper.
- **Background** means the paper is cited for context outside the core corpus: it is pre-Nov-2023 foundational work, it covers text only, or it is in date and setting but reports no detection experiment (an experience report).
- **Verification.** Each entry's URL was opened and its title, authors and date were checked against the page. For most arXiv papers the abs page was opened and the PDF was read (text extracted locally). Four entries were read from the abstract page only: Krishna et al., Sadasivan et al., SrcMarker and CodeGenGuard. A paper whose landing page could not be opened was left out, as the protocol requires. The count of such papers is in the log below.
- **Limitations.** `[author-acknowledged]` means the sentence paraphrases the paper's own Limitations or Threats section, or its body. `[reader-inferred]` marks my reading and has not been checked against the paper.

## Queries

### Database searches

| # | Source | Query (exact) | Hits | Notes |
| --- | --- | --- | --- | --- |
| 1 | arXiv API | `all:watermark AND (all:"code generation" OR ti:code)` | 83 | top 60 screened by title |
| 2 | arXiv API | `abs:watermark AND abs:"LLM-generated code"` | 8 | |
| 3 | arXiv API | `abs:watermark AND abs:HumanEval` | 3 | |
| 4 | arXiv API | `abs:watermark AND (abs:MBPP OR abs:APPS OR abs:LeetCode)` | 7 | |
| 5 | arXiv API | `abs:"AI-generated code" AND (abs:robust OR abs:robustness OR abs:evasion OR abs:adversarial)` | 13 | |
| 6 | arXiv API | `abs:"LLM-generated code" AND (abs:robust OR abs:robustness OR abs:evasion OR abs:adversarial OR abs:paraphras*)` | 34 | |
| 7 | arXiv API | `abs:"machine-generated code" AND (abs:robust OR abs:adversarial OR abs:evade OR abs:obfuscat*)` | 4 | |
| 8 | arXiv API | `abs:code AND abs:detector AND (abs:obfuscation OR abs:paraphrasing OR abs:refactoring) AND (abs:LLM OR abs:ChatGPT)` | 31 | |
| 9 | arXiv API | `abs:code AND (abs:"human-AI" OR abs:"mixed authorship" OR abs:hybrid OR abs:"human-edited" OR abs:"co-authored") AND (abs:"AI-generated" OR abs:"LLM-generated" OR abs:"machine-generated") AND abs:detect*` | 32 | |
| 10 | arXiv API | `abs:code AND abs:"false positive*" AND (abs:"AI-generated" OR abs:"LLM-generated" OR abs:ChatGPT) AND abs:detect*` | 31 | almost all off-topic (security tools) |
| 11 | arXiv API | `ti:code AND (ti:detection OR ti:detecting OR ti:detector*) AND (ti:robust* OR ti:adversarial OR ti:evasion OR ti:attack*) AND (abs:LLM OR abs:ChatGPT OR abs:"AI-generated")` | 7 | |
| 12 | arXiv API | `abs:ChatGPT AND abs:code AND abs:detector* AND (abs:evade OR abs:evasion OR abs:bypass OR abs:"semantic-preserving")` | 2 | |
| 13 | arXiv API | `abs:code AND (abs:"AI-generated" OR abs:"LLM-generated" OR abs:"machine-generated") AND abs:detect* AND (abs:"semantic-preserving" OR abs:"semantics-preserving" OR abs:"code transformation*")` | 6 | |
| 14 | arXiv API | `abs:watermark* AND abs:code AND (abs:LLM OR abs:"large language model*") AND (abs:attack OR abs:removal OR abs:robust*)` | 88 | top 80 screened by title |
| 15 | arXiv API | `abs:"code" AND abs:detect* AND (abs:"AI-generated" OR abs:"LLM-generated") AND (abs:"out-of-distribution" OR abs:generaliz* OR abs:reliab*) AND (abs:LeetCode OR abs:CodeNet OR abs:APPS OR abs:Codeforces)` | 0 | empty |
| 16 | arXiv API | `ti:"SemEval-2026 Task 13"` | 4 | participant system papers only |
| 17 | arXiv API | `ti:"Entropy-based Text Watermarking Detection"` | 1 | known-item check (EWD) |
| 18 | arXiv API | `abs:code AND (abs:"AI-generated" OR abs:"LLM-generated" OR abs:"machine-generated") AND abs:detect* AND (abs:"fine-grained" OR abs:"line-level" OR abs:"partially" OR abs:"co-authored" OR abs:collaborat*)` | 50 | |
| 19 | arXiv API | `abs:code AND abs:detector* AND (abs:"AI-generated" OR abs:"LLM-generated") AND (abs:"humaniz*" OR abs:"prompt engineering" OR abs:"style transfer" OR abs:"code style")` | 0 | empty |
| 20 | arXiv API | `(ti:watermark* OR ti:watermarking) AND (ti:code OR ti:program* OR ti:coding)` | — | failed: HTTP 429 (rate limit); queries 1, 2 and 14 cover the same titles |
| 21 | Semantic Scholar search | `watermark LLM-generated code detection` | — | failed: HTTP 429 after 8 retries; S2 was then used only for citation and reference lookups, which succeeded |
| 22 | DBLP API + web | `watermark code generation`, `watermarking LLM code`, `code watermark`, `AI-generated code detection robust`, `LLM-generated code detection`, `machine-generated code detection`, `hybrid code authorship` | — | failed: blocked by the Anubis bot check (API and web) |
| 23 | ACL Anthology (web search `site:aclanthology.org`) | `watermark code generation LLM` | 9 | gave SWEET (ACL 2024), CodeIP (EMNLP Findings 2024), STONE (EACL Findings 2026) |
| 24 | ACL Anthology (web search `site:aclanthology.org`) | `SemEval-2026 Task 13 detecting machine-generated code task description paper` | 10 | led to the task paper, 2026.semeval-1.445 |
| 25 | Google Scholar (direct fetch) | `watermarking LLM-generated code robustness` | — | failed: redirected to the Google "sorry" CAPTCHA; Scholar was covered only through general web search (rows 26–32) |
| 26 | Web search | `AI-generated code detectors robustness paraphrasing obfuscation evasion empirical study` | 9 | |
| 27 | Web search | `human-AI co-authored code detection hybrid LLM-edited code detection arXiv` | 10 | |
| 28 | Web search | `watermark code generation HumanEval MBPP low-entropy LLM code watermark 2024 2025` | 9 | |
| 29 | Web search | `"Is watermarking of LLM-generated code robust" OR "code watermark" removal attack semantic-preserving transformation detection` | 9 | |
| 30 | Web search | `LLM-generated code detector false positives students reliability evaluation GPTZero code assignments` | 9 | |
| 31 | Web search | `adversarial attack AI-generated code detection "code detectors" evade LLM rewriting 2025` | 9 | |
| 32 | Web search | `"Practical and effective code watermarking for large language models" Guo Cheng`; `"Large language models are effective code watermarkers"`; `"CodeGenGuard" watermark for code generation models` | 9 / 9 / 9 | known-item checks on titles found by backward snowballing |
| 33 | OpenAlex (extra source, used for snowballing) | free-text `watermarking code generation` | 21,251 | top 5 read, used to get OpenAlex IDs |

ACM Digital Library and IEEE Xplore were not searched directly. Their records came in through OpenAlex and Semantic Scholar snowballing. The IEEE and ACM landing pages tried with WebFetch returned no content.

### Snowballing

| Seed paper(s) | Direction | Method | Records returned |
| --- | --- | --- | --- |
| SWEET (both OpenAlex records) | forward | OpenAlex `cites:` | 54 |
| ACW-Li 2402.07518, Suresh 2403.17983, CodeIP, STONE, Pan 2401.03676 | forward | OpenAlex `cites:` | 78 |
| All 27 arXiv-indexed included papers (OpenAlex IDs resolved by DOI) | forward | OpenAlex `cites:` | 93 (sparse; OpenAlex indexes few 2025–26 arXiv citations) |
| CoDet-M4 (ACL Findings record) | forward | OpenAlex `cites:` | 4 |
| Suresh / ACW-Li / STONE / Disappearing Ink / Droid / Pan / CoDet-M4 / AICD Bench | forward | Semantic Scholar `/citations` | 11 / 8 / 18 / 0 / 42 / 85 / 41 / 25 |
| SemEval-2026 Task 13 / MALTO / ACW-Guo (NeurIPS) / Sağlam & Schmid / MedHastra | forward | Semantic Scholar `/citations` by DOI or arXiv ID | 40 / 1 / 2 / 2 / 1 |
| Disappearing Ink | backward | Semantic Scholar `/references` | 72 |
| All 33 included papers (cached PDF text) | backward | reference lists filtered for watermark, generated-code, obfuscation, paraphrase, hybrid and adversarial terms (2023–26) | 623 matching reference strings across 29 PDFs in the first pass; then 62 / 4 / 7 / 1 for ACW-Guo / MALTO / Sağlam & Schmid / MedHastra |

Snowballing added these entries: ACW-Guo (NeurIPS 2025), CodeGenGuard, SrcMarker, the earlier title of CLASP, the SemEval-2026 Task 13 overview, MALTO, MedHastra, CodeGPTSensor (HMCorp source check) and Sağlam & Schmid.

The SemEval forward set has 38 participant system papers. They were screened by title, and only those whose titles name hybrid or adversarial code (MALTO, MedHastra) were opened. The rest target Subtask A distribution shift, which belongs to slice A.

### Left out under the verification rule

**12** candidates found through OpenAlex or Semantic Scholar metadata were left out because their landing pages could not be opened.

Tried, and the page failed:
- 4 Springer chapters: authentication redirect; the bot check was not circumvented.
- 1 SSRN paper: HTTP 403.
- 1 ScienceDirect article: HTTP 403.
- 1 MDPI article: HTTP 403.
- 1 IEEE Xplore document: the page returned no content.

Not attempted, after the IEEE and Elsevier failures above:
- 2 further IEEE conference papers.
- 1 further Elsevier journal article.
- 1 ACM conference paper.

Their titles are in the handback report as leads for manual retrieval.

### Screening counts (slice C)

All counts are before deduplication. Deduplication was not done within this slice, because the protocol removes overlap across slices.

- **Records identified by database and web searches: 510.**
  - arXiv: 404 returned, 373 screened by title (rows 1 and 14 were cut to their top 60 and top 80).
  - ACL Anthology `site:` searches: 19.
  - Web searches: 82.
  - OpenAlex search: 5 read.
- **Records from snowballing: 577.**
  - OpenAlex forward: 229.
  - Semantic Scholar forward: 276.
  - Semantic Scholar backward: 72.
  - Also 697 keyword-matched reference strings from the PDF reference lists. These were screened by eye and are not records.
- **Assessed in full: 54 entries below.** 50 were read in full text and 4 from the abstract page only.
- **Included: 33. Background: 9. Excluded: 12.**

## Included

### Efficient and Universal Watermarking for LLM-Generated Code Detection
- **Authors**: Boquan Li, Zirui Fu, Mengdi Zhang et al.
- **Year / first public**: 2024-02
- **Venue**: IEEE Transactions on Software Engineering (accepted, per arXiv comment); earlier arXiv titles "Resilient Watermarking for LLM-Generated Codes" (v1) and "ACW: Enhancing traceability of AI-generated codes based on watermarking". This is not the same method as ACW-Guo (NeurIPS 2025) below.
- **URL**: https://arxiv.org/abs/2402.07518
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (post-hoc, training-free semantic-preserving transformations on LLM output)
- **Dataset**: MBPP, APPS, HumanEval, SRDD with GPT-4, GPT-4o and Qwen outputs (Python)
- **Headline result**: ACC 98.97%, TPR 97.94%, FPR 0% on MBPP-GPT-4; ACC over 97% and FPR below 1% on all datasets.
- **Limitation**: Failures come from very simple code with almost no logic for transformations to act on [author-acknowledged, results discussion].
- **Decision**: include — post-Nov-2023 output watermark evaluated on MBPP, APPS and HumanEval.

### Is The Watermarking Of LLM-Generated Code Robust?
- **Authors**: Tarun Suresh, Shubham Ugare, Gagandeep Singh, Sasa Misailovic
- **Year / first public**: 2024-03
- **Venue**: Tiny Papers track, ICLR 2024 (as cited by later papers; the PDF header reads "ICLR 2024") | arXiv preprint
- **URL**: https://arxiv.org/abs/2403.17983
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: robustness study
- **Dataset**: HumanEval completions (Python) from LLaMA-7B and CodeLlama-7B, watermarked with UMD/KGW and Unigram
- **Headline result**: On LLaMA-7B HumanEval code, mixed semantic-preserving transformations cut TPR from 0.79 to 0.34 (UMD) and from 0.76 to 0.14 (Unigram).
- **Limitation**: The study covers two logit-based schemes and five simple AST transformations on short Python completions [reader-inferred].
- **Decision**: include — robustness study of code watermarks on HumanEval.

### An Entropy-based Text Watermarking Detection Method
- **Authors**: Yijian Lu, Aiwei Liu, Dianzhi Yu et al.
- **Year / first public**: 2024-03
- **Venue**: ACL 2024 (main)
- **URL**: https://arxiv.org/abs/2403.13485
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (detection-side, entropy-weighted)
- **Dataset**: HumanEval, MBPP (low-entropy code), plus text corpora
- **Headline result**: Best F1 0.859 on HumanEval and 0.878 on MBPP, against 0.842 and 0.865 for SWEET.
- **Limitation**: Only two low-entropy code datasets were tested [author-acknowledged, Limitations].
- **Decision**: include — general-text watermark detector; code is its low-entropy testbed and one of its main evaluation settings.

### Watermarking Low-entropy Generation for Large Language Models: An Unbiased and Low-risk Method
- **Authors**: Minjia Mao, Dongjun Wei, Zeyu Chen et al.
- **Year / first public**: 2024-05
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2405.14604
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (unbiased, STA-1)
- **Dataset**: HumanEval (low-entropy code) and C4 (text)
- **Headline result**: not reported (the abstract gives no number; HumanEval results are in its Table 3).
- **Limitation**: Watermarking low-entropy tasks remains hard, and robustness to paraphrasing is not established [author-acknowledged, Limitations].
- **Decision**: include — general-text watermark; HumanEval is one of its two evaluation tasks.

### Marking Code Without Breaking It: Code Watermarking for Detecting LLM-Generated Code
- **Authors**: Jungin Kim, Shinwoo Park, Yo-Sub Han
- **Year / first public**: 2025-02
- **Venue**: Findings of EACL 2026
- **URL**: https://arxiv.org/abs/2502.18851
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (syntax-aware, STONE)
- **Dataset**: MBPP+, HumanEval+, HumanEvalPack C++ and Java
- **Headline result**: Detectability AUROC 0.982 on MBPP+, against 0.867 for SWEET; correctness 7.57% higher than SWEET on average.
- **Limitation**: Capacity depends on how many non-syntactic tokens there are, so unconventional coding styles can reduce it [author-acknowledged, Limitations].
- **Decision**: include — code watermark evaluated on HumanEval and MBPP variants.

### Robust and Secure Code Watermarking for Large Language Models via ML/Crypto Codesign
- **Authors**: Ruisi Zhang, Neusha Javidnia, Nojan Sheybani, Farinaz Koushanfar
- **Year / first public**: 2025-02
- **Venue**: ACM TAISAP (accepted, per arXiv comment)
- **URL**: https://arxiv.org/abs/2502.02068
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (learned insertion with CodeT5, RoSeMary; zero-knowledge verification)
- **Dataset**: HumanEval, MBXP (MBPP, MBCPP, MBJP), EvalPlus
- **Headline result**: Detection AUROC 0.97 while preserving functionality; verification takes about 120 ms.
- **Limitation**: Detectability is reported against non-watermarked samples, not against a human-written baseline [reader-inferred].
- **Decision**: include — output watermark on HumanEval and MBXP.

### Invisible Entropy: Towards Safe and Efficient Low-Entropy LLM Watermarking
- **Authors**: Tianle Gu, Zongqi Wang, Kexin Huang et al.
- **Year / first public**: 2025-05
- **Venue**: EMNLP 2025 (main), per the OpenAlex record | arXiv preprint
- **URL**: https://arxiv.org/abs/2505.14112
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (entropy-tagger replaces the original LLM)
- **Dataset**: HumanEval, MBPP
- **Headline result**: Performance on par with state-of-the-art methods on HumanEval and MBPP, with 99% fewer parameters (abstract).
- **Limitation**: The entropy tagger's accuracy still lags precise entropy calculation [author-acknowledged, Limitations].
- **Decision**: include — low-entropy watermark evaluated only on HumanEval and MBPP.

### Disappearing Ink: Obfuscation Breaks N-gram Code Watermarks in Theory and Practice
- **Authors**: Gehao Zhang, Mingzhe Li, Eugene Bagdasarian et al.
- **Year / first public**: 2025-07
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2507.05512
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: robustness study
- **Dataset**: HumanEval, MBPP, HumanEval-X, MBPP+, with two LLMs, two languages and four obfuscators
- **Headline result**: After obfuscation, detectors collapse to AUROC of about 0.5. For each language, at least one attack leaves every post-obfuscation AUROC below 0.6.
- **Limitation**: The proof covers N-gram-based schemes only [author-acknowledged, Limitations]. An appendix also breaks ACW-Guo, not ACW-Li.
- **Decision**: include — theory plus empirical evasion study on coding benchmarks.

### Optimizing Token Choice for Code Watermarking: An RL Approach
- **Authors**: Zhimeng Guo, Huaisheng Zhu, Siyuan Xu et al.
- **Year / first public**: 2025-08
- **Venue**: ICML 2026 (per arXiv comment); v1 title "...: A RL Approach"
- **URL**: https://arxiv.org/abs/2508.11925
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (RL-trained policy, CodeTracer)
- **Dataset**: HumanEval, MBPP
- **Headline result**: AUROC 77.71 and TPR 32.32 on HumanEval at Pass@1 62.65, against 65.42 unwatermarked. Post-hoc detectors score 47.59–52.00 AUROC.
- **Limitation**: TPR stays near one third, so most watermarked samples go undetected at the chosen threshold [reader-inferred].
- **Decision**: include — code watermark on HumanEval and MBPP.

### Practical and Effective Code Watermarking for Large Language Models
- **Authors**: Zhimeng Guo, Minhao Cheng
- **Year / first public**: 2025-12 (NeurIPS 2025 proceedings; no arXiv version found, and earlier OpenReview versions were not checked)
- **Venue**: NeurIPS 2025 (main track). This is a different method from ACW-Li (2402.07518), though both are called ACW.
- **URL**: https://proceedings.neurips.cc/paper_files/paper/2025/hash/6b4cb812f234a92ab757d1544912b4a8-Abstract-Conference.html
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (AST-guided learned watermark policy network)
- **Dataset**: HumanEval, MBPP, plus Java, C++ and JS variants
- **Headline result**: AUROC 84.43 on HumanEval at Pass@1 64.02 (unwatermarked 65.42); AUROC 81.18 on MBPP.
- **Limitation**: Disappearing Ink's appendix reports that obfuscation also removes this watermark [reader-inferred from 2507.05512 App. O].
- **Decision**: include — code watermark on HumanEval and MBPP; found by backward snowballing.

### CODE ACROSTIC: Robust Watermarking for Code Generation
- **Authors**: Li Lin, Siyuan Xin, Yang Cao, Xiaochun Cao
- **Year / first public**: 2025-12
- **Venue**: WISE 2025 (Springer LNCS), per the OpenAlex and Semantic Scholar records | arXiv preprint
- **URL**: https://arxiv.org/abs/2512.14753
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (cue-list guided; resists comment removal)
- **Dataset**: HumanEval
- **Headline result**: AUROC 0.772 on HumanEval, against 0.685 for KGW and 0.692 for SWEET, at Pass@1 51.20 (raw 53.05).
- **Limitation**: Evaluated on HumanEval only [reader-inferred].
- **Decision**: include — code watermark on HumanEval.

### SWaRL: Safeguard Code Watermarking via Reinforcement Learning
- **Authors**: Neusha Javidnia, Ruisi Zhang, Ashish Kundu, Farinaz Koushanfar
- **Year / first public**: 2026-01
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2601.02602
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (RL co-training with compiler feedback, LoRA)
- **Dataset**: HumanEval, MBPP, HumanEval+, MBPP+
- **Headline result**: AUROC 0.725 on HumanEval and 0.908 on MBPP, at Pass@1 58.22 and 53.40 (base+SFT 55.23 and 52.52).
- **Limitation**: Source code only; compiled or binary code is left for future work [author-acknowledged, Limitations].
- **Decision**: include — code watermark on HumanEval and MBPP.

### Semantic Differentiation for Tackling Challenges in Watermarking Low-Entropy Constrained Generation Outputs
- **Authors**: Nghia T. Le, Alan Ritter, Kartik Goyal
- **Year / first public**: 2026-01
- **Venue**: COLM 2026 (per arXiv comment)
- **URL**: https://arxiv.org/abs/2601.11629
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (sequence-level, SeqMark)
- **Dataset**: MBPP (code), plus translation, summarisation and C4
- **Headline result**: On MBPP, F1 80.7, against 70.2 for SWEET, at pass@1 33.6 (unwatermarked 33.8).
- **Limitation**: Detection needs access to the language model and an exact reproduction of the sampled generations [author-acknowledged, Limitations].
- **Decision**: include — general watermark; code (MBPP) is one of four constrained tasks.

### MATRIX: Multi-Layer Code Watermarking via Dual-Channel Constrained Parity-Check Encoding
- **Authors**: Yuqing Nie, Chong Wang, Guosheng Xu et al.
- **Year / first public**: 2026-04
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2604.16001
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (post-hoc dual-channel: naming plus transformations, BCH-coded)
- **Dataset**: Python code generated by several Code LLMs on HumanEval, MBPP, APPS
- **Headline result**: Average detection accuracy 99.20%, with 0–0.14% functionality loss and 7.70–26.67% better robustness against attacks.
- **Limitation**: Detection needs syntactically valid code [author-acknowledged, Limitations].
- **Decision**: include — output watermark on HumanEval, MBPP and APPS.

### SSG: Logit-Balanced Vocabulary Partitioning for LLM Watermarking
- **Authors**: Chenxi Gu, Xiaoning Du, John Grundy
- **Year / first public**: 2026-04
- **Venue**: ACL 2026 (main), per arXiv comment
- **URL**: https://arxiv.org/abs/2604.22438
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (vocabulary partitioning add-on to KGW, SWEET and EWD)
- **Dataset**: HumanEval, MBPP, plus math reasoning
- **Headline result**: not reported (the abstract gives no number; per-model gains are in Table 1).
- **Limitation**: Limited experimental scope, and detection depends on access to the original prompt [author-acknowledged, Limitations].
- **Decision**: include — general watermark; code is one of two low-entropy domains.

### Signature filtering: a lightweight enhancement for statistical watermark detection in large language models
- **Authors**: Chih-Duo Hong, Yen-Pang Chen, Fang Yu
- **Year / first public**: 2026-06
- **Venue**: arXiv preprint (OpenAlex links a journal version that was not opened)
- **URL**: https://arxiv.org/abs/2606.18430
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (detection-time filtering)
- **Dataset**: MBPP, HumanEval, CodeSearchNet, C4; six LLMs; KGW, SWEET, Unigram, EXP
- **Headline result**: Detection rates in weak-signal and low-entropy settings rise from 8–31% to 78–99%. The figure pools code and text corpora.
- **Limitation**: The guarantees fail if an attacker can infer token colours [author-acknowledged, Limitations].
- **Decision**: include — general watermark detector; HumanEval and MBPP are two of four corpora.

### PromptMark: A Prompt-Guided Iterative-Feedback Framework for Source Code Watermarking
- **Authors**: Istiaq Ahmed Fahad, Mridha Md. Nafis Fuad, Kazi Sakib
- **Year / first public**: 2026-06
- **Venue**: ENASE 2026 (per arXiv comment)
- **URL**: https://arxiv.org/abs/2606.20835
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (black-box, prompt-guided)
- **Dataset**: MBPP, HumanEval
- **Headline result**: AUROC of about 0.90–0.98, with TPR above 90% at 1–5% FPR in most configurations.
- **Limitation**: Light maintenance edits leave the lexical signal intact, but systematic renaming or large refactoring removes it [author-acknowledged, §5 Discussion].
- **Decision**: include — black-box output watermark on MBPP and HumanEval.

### Multi-Channel Spread-Spectrum Code Watermarking
- **Authors**: Soohyeon Choi, Debin Gao, Yue Duan
- **Year / first public**: 2026-07
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2607.06009
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (post-hoc, 24-bit payload, Reed–Solomon)
- **Dataset**: 1,750 Python files from CodeNet plus GPT-4.1 and Llama-4 generations
- **Headline result**: 100% clean-detection accuracy with zero false positives; identifier recovered at 97.6% under 8 renames. The strongest post-hoc baseline falls to 0% under any single-transform attack.
- **Limitation**: Asking a strong LLM to refactor the code removes the watermark: survival is 0.0% after GPT-4.1 refactoring and 0.4% after GPT-4o-mini [author-acknowledged, §6.7 Table 10].
- **Decision**: include — post-hoc output watermark evaluated on CodeNet.

### Preserving Structure, Strengthening Signals: A Grammar-Driven Approach to Optimize the Trade-off Between Quality and Detectability in Code Watermarking
- **Authors**: Licheng Yu, Aiwei Liu, Songze Li
- **Year / first public**: 2026-07
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2607.10210
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (grammar-driven three-level masking, GDW)
- **Dataset**: HumanEval, MBPP+, HumanEvalPack
- **Headline result**: not reported (the paper states GDW has the highest AUTC in all settings; the table columns were not parsed reliably).
- **Limitation**: Incremental parsing adds inference overhead [author-acknowledged, Limitations].
- **Decision**: include — code watermark on HumanEval and MBPP+, tested under seven semantics-preserving attacks.

### SEW: Style-Encoded Watermarking of LLM-Generated Code
- **Authors**: Soohan Lim, Hyundong Jin, Yo-Sub Han
- **Year / first public**: 2026-09
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2609.39414
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (post-hoc code-style rules)
- **Dataset**: CodeContests, three LLMs, three languages
- **Headline result**: Mean relative TPR@FPR5% improvement of 12.44% over baselines; only 0.94% mean relative decrease under four non-LLM editing attacks.
- **Limitation**: Very short programs have too few style sites for reliable detection [author-acknowledged, App. H].
- **Decision**: include — output watermark on CodeContests.

### Grammar-Guided Code Watermarking with Green Temperature
- **Authors**: Hyundong Jin, Hyeseon An, Soohan Lim, Yo-Sub Han
- **Year / first public**: 2026-10
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2610.05323
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (grammar-constrained decoding, GTCW)
- **Dataset**: five benchmarks including HumanEval(+) and MBPP(+); four languages; five models
- **Headline result**: Mean AUROC 73.61%, against 67.83% for the strongest baseline, at mean Pass@1 59.18% (unwatermarked 59.58%).
- **Limitation**: Detection is measured against matched unwatermarked model outputs, not human-written code [author-acknowledged, evaluation notes].
- **Decision**: include — code watermark on HumanEval and MBPP families.

### SynMark: Semantic-Coordinate Multi-Bit Watermarking during LLM Code Generation
- **Authors**: Rui Xu, Weizhi Liu, Zhaoxia Yin
- **Year / first public**: 2026-10
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2610.32017
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (multi-bit, semantic routing)
- **Dataset**: trained on MBPP, evaluated on HumanEval (OpenCoder, CodeLlama, DeepSeek-Coder)
- **Headline result**: Under 100% identifier renaming, BitAcc stays at 82.27% (CodeLlama) and 83.77% (DeepSeek-Coder).
- **Limitation**: Evaluated on HumanEval only, with the same transformation families used in training [reader-inferred].
- **Decision**: include — generation-time multi-bit watermark on HumanEval.

### Assessing AI Detectors in Identifying AI-Generated Code: Implications for Education
- **Authors**: Wei Hung Pan, Ming Jie Chok, Jonathan Leong Shan Wong et al.
- **Year / first public**: 2024-01
- **Venue**: ICSE-SEET 2024
- **URL**: https://arxiv.org/abs/2401.03676
- **Access**: open
- **Setting**: education
- **Method family**: robustness study
- **Dataset**: 5,069 problems with human Python solutions (Quescol 80, Kaggle 3,264, LeetCode 1,725); 13 ChatGPT prompt variants; five AIGC detectors
- **Headline result**: GPTZero and another detector stay near 0.5 accuracy. GLTR accuracy ranges from 0.4841 to 0.7693 across prompt variants.
- **Limitation**: GPTZero is a text detector, so its mismatch with code syntax may cause false positives and false negatives [author-acknowledged, Limitations].
- **Decision**: include — evasion of detectors by prompt variants, on education and LeetCode data.

### CodeVision: Detecting LLM-Generated Code Using 2D Token Probability Maps and Vision Models
- **Authors**: Zhenyu Xu, Victor S. Sheng
- **Year / first public**: 2025-01
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2501.03288
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: trained classifier
- **Dataset**: 28,342 samples from Project CodeNet in six languages (15,633 by GPT-3.5 and GPT-4)
- **Headline result**: Small models (0.5M–20M parameters) reach AUC above 0.97.
- **Limitation**: Depends on OpenAI API log-probabilities [author-acknowledged, Limitations].
- **Decision**: include — in Scope (CodeNet). It came up in the watermark queries but has no robustness component, so it overlaps with slice A.

### CoDet-M4: Detecting Machine-Generated Code in Multi-Lingual, Multi-Generator and Multi-Domain Settings
- **Authors**: Daniil Orel, Dilshod Azizov, Preslav Nakov
- **Year / first public**: 2025-03
- **Venue**: Findings of ACL 2025
- **URL**: https://arxiv.org/abs/2503.13733
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: dataset/benchmark
- **Dataset**: about 500K samples from LeetCode, Codeforces and GitHub; Python, Java, C++; hybrid fill-in and rewrite test (1K per task)
- **Headline result**: On hybrid-generated code, UniXcoder reaches F1 39.36 (baseline 22.91), and performance falls as the share of preserved human code rises.
- **Limitation**: Covers three languages and mostly function- or class-level code [author-acknowledged, Limitations].
- **Decision**: include — mixed-authorship evaluation on coding-problem data.

### Evaluating Software Plagiarism Detection in the Age of AI: Automated Obfuscation and Lessons for Academic Integrity
- **Authors**: Timur Sağlam, Larissa Schmid
- **Year / first public**: 2025-05
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2505.20158
- **Access**: open
- **Setting**: education
- **Method family**: robustness study
- **Dataset**: real-world programming-assignment datasets from several university courses; over 14,000 files and 4 million pairwise comparisons; JPlag with two defence mechanisms
- **Headline result**: The defence mechanisms detect AI-generated programs 8.92 percentage points more often, although they were not designed for that.
- **Limitation**: The main target is AI-assisted plagiarism obfuscation; detecting AI authorship is a side result [author-acknowledged, contributions].
- **Decision**: include — AI-based obfuscation and AI-generated program detection in course data. Partly overlaps with slice B.

### Droid: A Resource Suite for AI-Generated Code Detection
- **Authors**: Daniil Orel, Indraneil Paul, Iryna Gurevych, Preslav Nakov
- **Year / first public**: 2025-07
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2507.10583
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: dataset/benchmark
- **Dataset**: DroidCollection, over 1M samples; 7 languages; 43 models; includes CodeNet, LeetCode, AtCoder and CodeChef sources, human–AI co-authored code and adversarial (humanised) samples
- **Headline result**: DroidDetect-Large reaches weighted F1 99.25 (2-class) and 94.30 (4-class, including adversarial). Most existing detectors are compromised by humanising prompts.
- **Limitation**: New model families with unseen output distributions are a standing coverage problem [author-acknowledged, Limitations].
- **Decision**: include — adversarial and co-authored code on data that includes coding problems.

### DuoLens: A Framework for Robust Detection of Machine-Generated Multilingual Text and Code
- **Authors**: Shriyansh Agrawal, Aidan Lau, Sanyam Shah et al.
- **Year / first public**: 2025-10
- **Venue**: NeurIPS 2025 Workshop on Deep Learning for Code
- **URL**: https://arxiv.org/abs/2510.18904
- **Access**: open
- **Setting**: general code on coding-problem data (mixed: curated from AIGCD, DroidCollection and CodeMirage)
- **Method family**: trained classifier
- **Dataset**: 6,000 human and 6,000 machine samples per language, 7 languages
- **Headline result**: Under adversarial transformations (formatting, renaming), the model keeps at least 92% of its clean AUROC.
- **Limitation**: No result is reported on a split made only of coding-problem data [reader-inferred].
- **Decision**: include — borderline. Its data partly comes from coding problems through DroidCollection, and it reports a robustness evaluation.

### Whitespaces Don't Lie: Feature-Driven and Embedding-Based Approaches for Detecting Machine-Generated Code
- **Authors**: Syed Mehedi Hasan Nirob, Shamim Ehsan, Moqsadur Rahman, Summit Haque
- **Year / first public**: 2026-01
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2601.19264
- **Access**: open
- **Setting**: general code on coding-problem data (the Droid benchmark)
- **Method family**: stylometry/AST
- **Dataset**: 600K human and AI samples from the Droid benchmark
- **Headline result**: Feature-based model ROC-AUC 0.995 and F1 0.971; CodeBERT embeddings ROC-AUC 0.994.
- **Limitation**: Indentation and whitespace features could be neutralised by a code formatter, and this is not tested [reader-inferred].
- **Decision**: include — in Scope through the Droid data. It has no robustness experiment, so it overlaps with slice A.

### AICD Bench: A Challenging Benchmark for AI-Generated Code Detection
- **Authors**: Daniil Orel, Dilshod Azizov, Indraneil Paul et al.
- **Year / first public**: 2026-02
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2602.02079
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: dataset/benchmark
- **Dataset**: 2M examples; 77 models; 9 languages. The seen domain is algorithmic code; Task 3 has human, machine, hybrid and adversarial classes.
- **Headline result**: Best Task 3 macro-F1 is 61.65 (ModernBERT). On Task 1 (robust binary), no detector beats the random baseline of 45.73.
- **Limitation**: The public benchmark may saturate as models are tuned to it [author-acknowledged, Limitations].
- **Decision**: include — hybrid and adversarial classes on data that includes algorithmic problems.

### SemEval-2026 Task 13: Detecting Machine-Generated Code with Multiple Programming Languages, Generators, and Application Scenarios
- **Authors**: Daniil Orel, Dilshod Azizov, Indraneil Paul, Yuxia Wang, Iryna Gurevych, Preslav Nakov
- **Year / first public**: 2026-07
- **Venue**: Proceedings of SemEval-2026 (ACL), pp. 3640–3658
- **URL**: https://aclanthology.org/2026.semeval-1.445/
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: dataset/benchmark (shared task)
- **Dataset**: built on Droid (CodeNet, TACO and others) plus LeetCode and Codeforces problems. Subtask C classes: human, machine, hybrid, adversarial.
- **Headline result**: Top Subtask C macro F-score 0.785, with several systems above 0.65; top Subtask A score 0.997.
- **Limitation**: Participating systems use black-box signals only [author-acknowledged, Limitations].
- **Decision**: include — shared task with hybrid and adversarial code on coding-problem data.

### MALTO at SemEval-2026 Task 13: Detecting Human, AI, and Hybrid Code via Hard Negative Mining and Curriculum-Driven Ensembles
- **Authors**: Hüseyin Arda Arslan, Evren Ayberk Munis, Timofei Khudonogov et al.
- **Year / first public**: 2026-07
- **Venue**: Proceedings of SemEval-2026 (ACL), pp. 2413–2420
- **URL**: https://aclanthology.org/2026.semeval-1.304/
- **Access**: open
- **Setting**: general code on coding-problem data (SemEval-2026 Task 13 data)
- **Method family**: trained classifier
- **Dataset**: SemEval-2026 Task 13 Subtasks B and C
- **Headline result**: Macro-F1 0.616 on the Subtask C hidden test set (CodeBERT baseline 0.481).
- **Limitation**: Feature ablations are missing, and the method depends on Tree-sitter parsers [author-acknowledged, Limitations].
- **Decision**: include — detector for hybrid and adversarial code on the shared-task data.

### MedHastra at SemEval-2026 Task 13: Stylometric Ensembles and Transformer Fine-Tuning for Robust AI Code Detection, Attribution, and Adversarial Analysis
- **Authors**: Shruti Chandrasekar, Vedajanaani R S, Vijayalakshmi P
- **Year / first public**: 2026-07
- **Venue**: Proceedings of SemEval-2026 (ACL), pp. 2098–2103
- **URL**: https://aclanthology.org/2026.semeval-1.264/
- **Access**: open
- **Setting**: general code on coding-problem data (SemEval-2026 Task 13 data)
- **Method family**: trained classifier
- **Dataset**: SemEval-2026 Task 13 Subtasks A, B and C
- **Headline result**: Subtask C macro F1 0.53134 (rank 24 of 32); Subtask A 0.3222 (rank 70 of 81).
- **Limitation**: Handcrafted stylometric features degrade under strong distribution shift [author-acknowledged, abstract].
- **Decision**: include — hybrid and adversarial classification on coding-problem data.

## Background

### Who Wrote this Code? Watermarking for Code Generation
- **Authors**: Taehyun Lee, Seokhee Hong, Jaewoo Ahn et al.
- **Year / first public**: 2023-05
- **Venue**: ACL 2024 (long)
- **URL**: https://arxiv.org/abs/2305.15060
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: watermark (SWEET, entropy-thresholded)
- **Dataset**: HumanEval, MBPP, DS-1000
- **Headline result**: AUROC 0.943 on HumanEval with 2.4% functionality loss; 0.873 on MBPP.
- **Limitation**: Detection needs the original LLM to compute entropy [reader-inferred; later papers (IE, 2505.14112) state it as SWEET's drawback].
- **Decision**: background — first public May 2023, before the Nov 2023 cutoff. It is the anchor baseline that almost every included watermark paper compares against.

### Zero-Shot Detection of Machine-Generated Codes
- **Authors**: Xianjun Yang, Kexun Zhang, Haifeng Chen et al.
- **Year / first public**: 2023-10
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2310.05103
- **Access**: open
- **Setting**: general code on coding-problem data
- **Method family**: zero-shot
- **Dataset**: CodeContests and APPS (Python), Java generalisation
- **Headline result**: not reported (the abstract gives no number).
- **Limitation**: Labelled "work in progress" by the authors [author-acknowledged, arXiv comment].
- **Decision**: background — first public 8 Oct 2023, before the cutoff. It reports robustness to revision attacks.

### Detecting LLM-Generated Text in Computing Education: A Comparative Study for ChatGPT Cases
- **Authors**: Michael Sheinman Orenstrakh, Oscar Karnalim, Carlos Anibal Suarez, Michael Liut
- **Year / first public**: 2023-07
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2307.07411
- **Access**: open
- **Setting**: education
- **Method family**: empirical study
- **Dataset**: 124 pre-ChatGPT student submissions and 40 ChatGPT submissions; eight text detectors
- **Headline result**: GPTZero gave 52 false positives on 114 human submissions. All detectors were less accurate on code and on paraphrased text.
- **Limitation**: Only text detectors were tested, on a small sample [reader-inferred].
- **Decision**: background — before the cutoff; early evidence on false positives and paraphrase evasion in an education setting.

### Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense
- **Authors**: Kalpesh Krishna, Yixiao Song, Marzena Karpinska et al.
- **Year / first public**: 2023-03
- **Venue**: NeurIPS 2023
- **URL**: https://arxiv.org/abs/2303.13408
- **Access**: open
- **Setting**: out of scope (natural-language text)
- **Method family**: robustness study
- **Dataset**: text from three LLMs; DIPPER paraphraser
- **Headline result**: DIPPER drops DetectGPT's detection accuracy from 70.3% to 4.6% at 1% FPR.
- **Limitation**: Text only [reader-inferred].
- **Decision**: background — foundational paraphrase-evasion result that the code robustness papers cite.

### Can AI-Generated Text be Reliably Detected?
- **Authors**: Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian et al.
- **Year / first public**: 2023-03
- **Venue**: Transactions on Machine Learning Research
- **URL**: https://arxiv.org/abs/2303.11156
- **Access**: open
- **Setting**: out of scope (natural-language text)
- **Method family**: robustness study
- **Dataset**: passages of about 300 tokens
- **Headline result**: not reported (the abstract states qualitatively that recursive paraphrasing significantly reduces detection rates, including for watermarks).
- **Limitation**: Text only [reader-inferred].
- **Decision**: background — foundational evasion and spoofing argument cited by the code watermark papers.

### Towards Code Watermarking with Dual-Channel Transformations
- **Authors**: Borui Yang, Wei Li, Liyao Xiang, Bo Li
- **Year / first public**: 2023-09
- **Venue**: IEEE S&P 2024 (as "SrcMarker")
- **URL**: https://arxiv.org/abs/2309.00860
- **Access**: open
- **Setting**: out of scope (ownership watermark for arbitrary source code)
- **Method family**: watermark (source-code, not LLM output)
- **Dataset**: not extracted
- **Headline result**: not reported
- **Limitation**: not assessed (abstract read only).
- **Decision**: background — before the cutoff, and it watermarks source code for ownership, not LLM output. It is a frequent baseline for post-hoc code watermarks such as ACW-Li, MCSS and SEW.

### CodeMark: Imperceptible Watermarking for Code Datasets against Neural Code Completion Models
- **Authors**: Zhensu Sun, Xiaoning Du, Fu Song, Li Li
- **Year / first public**: 2023-08
- **Venue**: ESEC/FSE 2023
- **URL**: https://arxiv.org/abs/2308.14401
- **Access**: open
- **Setting**: out of scope (dataset watermark)
- **Method family**: watermark (training-data)
- **Dataset**: CodeSearchNet
- **Headline result**: not reported
- **Limitation**: not assessed (abstract read only).
- **Decision**: background — before the cutoff, and it watermarks code datasets rather than generated solutions. Five included papers cite it.

### Towards Tracing Code Provenance with Code Watermarking
- **Authors**: Wei Li, Borui Yang, Yujie Sun et al.
- **Year / first public**: 2023-05
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2305.12461
- **Access**: open
- **Setting**: out of scope (code provenance and dataset watermark)
- **Method family**: watermark
- **Dataset**: CodeSearchNet
- **Headline result**: not reported
- **Limitation**: not assessed (abstract read only).
- **Decision**: background — before the cutoff, and not about LLM output. MATRIX cites it.

### The Failure of Plagiarism Detection in Competitive Programming
- **Authors**: Ethan Dickey
- **Year / first public**: 2025-05
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2505.08244
- **Access**: open
- **Setting**: competitive programming
- **Method family**: empirical study (experience report)
- **Dataset**: none; seven semesters teaching CP1 at Purdue, about 100 students each
- **Headline result**: not reported (qualitative: similarity checkers are thwarted by simple transformations or novel AI-generated code).
- **Limitation**: Experience-based observations with no controlled evaluation [author-acknowledged, abstract].
- **Decision**: background — in date and setting, but it reports no detection experiment. It may suit slice B as context.

## Excluded

### CodeIP: A Grammar-Guided Multi-Bit Watermark for Large Language Models of Code
- **Authors**: Batu Guan, Yao Wan, Zhangqian Bi et al.
- **Year / first public**: 2024-04
- **Venue**: Findings of EMNLP 2024
- **URL**: https://arxiv.org/abs/2404.15639
- **Access**: open
- **Setting**: out of scope
- **Method family**: watermark (multi-bit, grammar-guided)
- **Dataset**: CodeSearchNet docstrings and function declarations; five languages
- **Headline result**: Average watermark extraction rate 0.95.
- **Limitation**: The authors chose not to use HumanEval and MBPP because their code is "too short" for watermark insertion [author-acknowledged, §4.1].
- **Decision**: exclude — evaluated only on CodeSearchNet, not on coding-problem data. STONE's re-run of CodeIP on MBPP+ is STONE's own experiment. It is a widely cited baseline.

### MCGMark: An Encodable and Robust Online Watermark for Tracing LLM-Generated Malicious Code
- **Authors**: Kaiwen Ning, Jiachi Chen, Qingyuan Zhong et al.
- **Year / first public**: 2024-08
- **Venue**: arXiv preprint (OpenAlex links an ACM journal version)
- **URL**: https://arxiv.org/abs/2408.01354
- **Access**: open
- **Setting**: out of scope (malicious-code generation)
- **Method family**: watermark
- **Dataset**: MCGTest, 406 malicious-code prompts in the MBPP and HumanEval prompt format
- **Headline result**: Embedding success rate 88.9% within 400 tokens.
- **Limitation**: Evaluated on MCGTest only [author-acknowledged, §7].
- **Decision**: exclude — the prompts only borrow the HumanEval/MBPP format, and no coding-problem benchmark is evaluated.

### Towards Generalized and Stealthy Watermarking for Generative Code Models
- **Authors**: Haoxuan Li, Jiale Zhang, Xiaobing Sun, Xiapu Luo
- **Year / first public**: 2025-06
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2506.20926
- **Access**: open
- **Setting**: out of scope (model copyright)
- **Method family**: watermark (backdoor, CodeGuard)
- **Dataset**: CodeSearchNet
- **Headline result**: Up to 100% verification rate.
- **Limitation**: not assessed.
- **Decision**: exclude — backdoor watermark for verifying model ownership, evaluated on CodeSearchNet.

### CodeGenGuard: A Watermark for Code Generation Models
- **Authors**: Borui Yang, Mingxuan Ma, Liyao Xiang et al.
- **Year / first public**: 2026 (ICLR 2026 poster)
- **Venue**: ICLR 2026
- **URL**: https://iclr.cc/virtual/2026/poster/10009225
- **Access**: open (abstract page)
- **Setting**: out of scope (model ownership)
- **Method family**: watermark
- **Dataset**: not stated on the page
- **Headline result**: not reported
- **Limitation**: not assessed (abstract read only).
- **Decision**: exclude — the page frames it as model ownership verification, not detection of generated solutions.

### CLASP: Training-Free LLM-Assisted Source Code Watermarking via Semantic-Preserving Transformations
- **Authors**: Rui Xu, Jiawei Chen, Weizhi Liu et al.
- **Year / first public**: 2025-10
- **Venue**: arXiv preprint; v1 titled "Large Language Models Are Effective Code Watermarkers" (CodeMark-LLM)
- **URL**: https://arxiv.org/abs/2510.11251
- **Access**: open
- **Setting**: out of scope (ownership of arbitrary source code)
- **Method family**: watermark (post-hoc, LLM-assisted)
- **Dataset**: CodeSearchNet Java/JS, MBCPP, MBJP, MBJSP, MBPP
- **Headline result**: BitAcc 97.85% on MBPP (no attack).
- **Limitation**: not assessed.
- **Decision**: exclude — it watermarks any source code against unauthorised reuse, not LLM output for provenance, even though it uses MBPP.

### Can we Watermark Low-Entropy LLM Outputs?
- **Authors**: Noam Mazor, Andrew Morgan, Rafael Pass
- **Year / first public**: 2026-04
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2604.12051
- **Access**: open
- **Setting**: out of scope (theory)
- **Method family**: watermark (cryptographic constructions)
- **Dataset**: none
- **Headline result**: not reported
- **Limitation**: not assessed.
- **Decision**: exclude — no evaluation on code or coding-problem data.

### The Patchwork Problem in LLM-Generated Code
- **Authors**: Viraaji Mothukuri, Reza M. Parizi
- **Year / first public**: 2026-07
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2607.08981
- **Access**: open
- **Setting**: out of scope
- **Method family**: empirical study (code-quality verification)
- **Dataset**: repository-level generations from two frontier models
- **Headline result**: not reported
- **Limitation**: not assessed.
- **Decision**: exclude — it studies structural defects, not whether code was written by an LLM.

### Detecting LLM-generated Code with Subtle Modification by Adversarial Training
- **Authors**: Xin Yin, Xinrui Li, Chao Ni et al.
- **Year / first public**: 2025-07
- **Venue**: arXiv preprint (ACM TOSEM format)
- **URL**: https://arxiv.org/abs/2507.13123
- **Access**: open
- **Setting**: out of scope (GitHub functions)
- **Method family**: robustness study (adversarial training, CodeGPTSensor+)
- **Dataset**: HMCorp, 288,508 Python and 222,335 Java human/ChatGPT pairs; human code is docstring-bearing functions from about 17K GitHub projects (per 2411.04704)
- **Headline result**: Accuracy 0.992 on Python and 0.970 on Java; accuracy on adversarial sets improves by 272.8% and 190.8%.
- **Limitation**: not assessed.
- **Decision**: exclude — the human code is GitHub repository functions, not coding problems. Its adversarial-modification result is relevant context.

### Distinguishing LLM-generated from Human-written Code by Contrastive Learning
- **Authors**: Xiaodan Xu, Chao Ni, Xinrong Guo et al.
- **Year / first public**: 2024-11
- **Venue**: ACM TOSEM 2024 (per arXiv comment)
- **URL**: https://arxiv.org/abs/2411.04704
- **Access**: open
- **Setting**: out of scope (GitHub functions)
- **Method family**: trained classifier (CodeGPTSensor)
- **Dataset**: HMCorp (GitHub functions with docstrings, plus ChatGPT counterparts)
- **Headline result**: not extracted (opened only to trace HMCorp's source)
- **Limitation**: not assessed.
- **Decision**: exclude — GitHub-function setting, and no robustness component (slice A may still list it).

### Detection of LLM-Paraphrased Code and Identification of the Responsible LLM Using Coding Style Features
- **Authors**: Shinwoo Park, Hyundong Jin, Jeong-won Cha, Yo-Sub Han
- **Year / first public**: 2025-02
- **Venue**: Engineering Applications of Artificial Intelligence, vol. 162 (Dec 2025)
- **URL**: https://arxiv.org/abs/2502.17749
- **Access**: open
- **Setting**: out of scope (GitHub repositories created 2019)
- **Method family**: stylometry/AST
- **Dataset**: LPcode, human code from GitHub paired with LLM paraphrases
- **Headline result**: F1 improves by 2.64% (paraphrase detection) and 15.17% (LLM identification) over the best baselines.
- **Limitation**: not assessed.
- **Decision**: exclude — GitHub repository code, not coding problems. The paraphrase-detection task is relevant context.

### CodeMirage: A Multi-Lingual Benchmark for Detecting AI-Generated and Paraphrased Source Code from Production-Level LLMs
- **Authors**: Hanxi Guo, Siyuan Cheng, Kaiyuan Zhang et al.
- **Year / first public**: 2025-05
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2506.11059
- **Access**: open
- **Setting**: out of scope (GitHub files)
- **Method family**: dataset/benchmark
- **Dataset**: about 210K samples; 10,000 human files from GitHub; 10 languages; 10 production LLMs; original and paraphrased versions
- **Headline result**: not reported (the abstract gives nine qualitative findings).
- **Limitation**: not assessed.
- **Decision**: exclude — the human code is GitHub files, not coding problems. Paraphrase robustness is relevant context, and DuoLens reuses it.

### HybridCodeAuthorship: A Benchmark Dataset for Line-Level Code Authorship Detection
- **Authors**: Luke Patterson, Li Wang, Adam Faulkner
- **Year / first public**: 2026-06
- **Venue**: LREC 2026, pp. 1520–1532
- **URL**: https://arxiv.org/abs/2606.12620
- **Access**: open
- **Setting**: out of scope (industry-style repositories from CodeSearchNet)
- **Method family**: dataset/benchmark
- **Dataset**: Python files with interleaved human and AI lines, built from CodeSearchNet repositories
- **Headline result**: The best detector (AIGCode Detector) reaches F1 0.48 at chunk level and 0.56 at line level.
- **Limitation**: The authors deliberately avoid LeetCode-style problems [author-acknowledged, abstract].
- **Decision**: exclude — not coding-problem data. It is the only line-level mixed-authorship benchmark found, so it is worth citing as context.
