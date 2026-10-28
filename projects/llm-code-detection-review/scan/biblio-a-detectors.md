# Slice A: detectors

Bibliography slice A of the [search protocol](search-protocol.md): zero-shot statistical detectors, trained classifiers, and benchmarks or datasets of human vs LLM code. Inclusion criteria are the **Scope** section of the [project README](../README.md). Searched 2026-10-28 by the slice-A bibliography agent.

## Screening rules applied in this slice

These rules interpret the Scope criteria. They are applied to every entry below. Each one is a judgement call, so the caller should confirm them.

- **Candidate.** A record is a candidate when its title passes a slice-A title screen: it is about code, mentions LLM, AI or machine generation, and is about detection, classification, a benchmark or a dataset. Only candidates get entries. Title-screen counts are logged per index below.
- **Date.** The date that counts is the first public version: arXiv `[v1]`, or else the earliest dated publisher or preprint record. OpenAlex `publication_date` is never used for this, because it often gives the venue year instead (for example 2025-04 for DetectCodeGPT, whose arXiv v1 is 2024-01).
- **Setting: coding-problem data.** APPS, CodeNet, CodeContests/TACO, LeetCode, Codeforces, CodeChef, AtCoder, HackerEarth, Google Code Jam and Rosetta Code count, and so do textbook or course exercises. **HumanEval and MBPP also count**, because each item is a problem statement paired with a reference solution. A paper evaluated only on CodeSearchNet, The Stack, GitHub repositories or pull requests, or synthetic programs fails Setting.
- **Setting: mixed benchmarks.** A paper whose evaluation data includes a coding-problem or "algorithmic" split passes Setting, even when other splits are general code. This covers CoDet-M4, DroidCollection, AICD Bench and SemEval-2026 Task 13.
- **Provisional exclude.** When the only readable text is an abstract that does not name the data, Setting cannot be judged. The paper is marked `exclude (provisional)` and listed for a full-text re-screen. It is not silently dropped.
- **Headline result.** The number comes from the paper's own page: arXiv HTML, a PDF, or the abstract on the publisher or index record. If the readable text gives no number, the field says "not reported".
- **Access.** `open` means the full text was readable to the agent, or the publisher flags the paper as open access. `paywalled` means only the abstract or metadata could be read. Where a publisher blocked automated fetching (HTTP 403 or a bot check), identity was verified against the Semantic Scholar or Crossref API record, and that record is named in the entry.

## Queries

### Indexes and runs

All runs were on 2026-10-28. For every index, only the **top 100 records by relevance** were screened, so the larger totals below are index-wide match counts, not screened records.

**Semantic Scholar** (keyless Graph API `/paper/search`, filter `publicationDateOrYear=2023-01-01:`, top 100 screened)

| Query | Hits | Status |
| --- | --- | --- |
| zero-shot detection LLM-generated code perplexity | 1,309 | ok |
| detecting AI-generated code perturbation likelihood curvature | 44 | ok |
| detecting ChatGPT-generated code classifier | 579 | ok |
| AI-generated code detection CodeBERT fine-tuned | 1,772 | ok |
| LLM-generated code detector trained classifier | 3,757 | ok |
| zero-shot detection machine-generated code | — | HTTP 429. Retried 6× with 5–30 s backoff, then 8× with 15–120 s backoff; killed after about 40 min |
| DetectGPT code detection | — | HTTP 429, same as above |
| machine-generated code detection dataset benchmark | — | HTTP 429, same as above |
| human-written versus AI-generated code dataset | — | HTTP 429, same as above |
| AI-generated source code detection | — | HTTP 429, same as above |
| LLM-generated code detection LeetCode | — | HTTP 429, same as above |
| AI-generated code detection APPS CodeNet | — | HTTP 429, same as above |
| ChatGPT generated code detection Codeforces competitive programming | — | HTTP 429, same as above |
| distinguishing human and LLM written code | — | HTTP 429, same as above |
| authorship detection AI-generated programs | — | HTTP 429, same as above |
| detecting LLM-generated code (probe query, no date filter, top 50) | 33,184 | ok |

The 429s were shared-IP rate limiting: sibling slice agents were querying the same API at the same time. Every failed S2 query string was also run on OpenAlex (below), so no query family is missing a logged run. The S2 batch endpoint (`/paper/batch`, one request) and the per-paper references and citations endpoints did work, and were used for verification and snowballing.

**OpenAlex** (`api.openalex.org/works?search=`, filter `from_publication_date:2023-01-01`, top 100 screened). OpenAlex is not in the protocol's source list. It was used as a **supplementary** index to cover the S2 failures.

| Query | Hits |
| --- | --- |
| zero-shot detection machine-generated code | 55,425 |
| detecting AI-generated code perplexity | 7,657 |
| DetectGPT code detection | 877 |
| detecting ChatGPT-generated code | 67,602 |
| LLM-generated code detection | 85,518 |
| AI-generated code detection classifier | 140,546 |
| machine-generated code detection dataset benchmark | 163,651 |
| human-written AI-generated code dataset | 102,921 |
| AI-generated source code detection | 251,078 |
| LLM-generated code detection LeetCode | 438 |
| AI-generated code detection APPS CodeNet | 71 |
| ChatGPT code detection competitive programming Codeforces | 137 |
| distinguishing human and LLM written code | 29,596 |

**arXiv**

- The export API (`export.arxiv.org/api/query`) ran 6 fielded queries, for example `abs:(detect* AND ("AI-generated code" OR "LLM-generated code" OR "machine-generated code"))`. All of them got HTTP 429, retried 5× with 20–100 s backoff, and the job was killed after about 40 min.
- The same query families were then rerun on the arxiv.org search page. Their counts are under "arXiv search-page rerun" at the end of the snowballing section.
- Every arXiv paper in this file was verified by fetching its `arxiv.org/abs/<id>` page (title, authors, `[v1]` date) and its `arxiv.org/html/<id>` full text (dataset and number checks).

**DBLP**

- The `dblp.org/search/publ/api` JSON API returned HTTP 429 (retry-after 60). After waiting, it returned HTTP 202 with an Anubis "Making sure you're not a bot!" challenge page.
- WebFetch of `dblp.org/search?q=machine-generated+code+detection` got the same Anubis "Access Denied" page.
- **DBLP could not be searched.** The bot check was not circumvented. Queries attempted: "machine-generated code detection", "AI-generated code detection" and "LLM-generated code detection" (each failed after 4 tries). The planned "ChatGPT generated code detect", "zero-shot detection code", "AI-generated code dataset", "detecting code generated", "human-written AI-generated code" and "SemEval-2026 Task 13" were not run.

**Google Scholar**

Scholar cannot be fetched directly. Nine runs used **WebSearch as a Scholar proxy**; each returned about 9 links. Their summaries were used only as leads. Every paper was then opened at its own URL, and no number comes from a search summary.

1. detecting LLM-generated code benchmark dataset human-written arXiv 2024 2025
2. zero-shot detection machine-generated code perplexity DetectGPT code paper
3. scholar.google.com AI-generated code detection LeetCode Codeforces ChatGPT classifier
4. CodeGPTSensor detecting ChatGPT-generated code contrastive learning
5. "machine-generated code" detection benchmark multilingual generators 2025 arXiv
6. "AI-generated code" detector evaluation APPS CodeNet human solutions GPT-4 fine-tuned CodeT5 UniXcoder
7. "Who wrote this code" LLM-generated code detection
8. AI-generated code detection benchmark 2026 arXiv large-scale detectors generalization unseen LLMs
9. detecting AI-generated code student programming solutions trained classifier dataset human GPT

Three targeted lookups followed, for DualCodeDetect datasets, "Hiding in Plain Sight" and Bukhari et al. 2023. None of them resolved the Setting question.

### Title screen

- **Records:** 1,283 unique titles, from S2 (412 records) and OpenAlex (1,019 records), merged on lower-cased title.
- **Regex title screen:** a title passed when it matched `(code|program|source)` AND `(generated|written|authored|authorship|ChatGPT|LLM|AI|machine)` AND `(detect|distinguish|identif|classif|sniff|discrimin|benchmark|dataset|uncover|human)`, and did not match an off-topic list (vulnerability, bug, test case, clone, smell, hallucination, repair, security, malware, summarization, translation, completion, defect, essay). **153 of 1,283 passed.**
- **Manual title screen to slice-A candidates:** the 153 included many off-topic records, such as code-generation benchmarks, image detectors and code-mixed memes. Manual screening, plus leads from WebSearch and the papers' related-work sections, gave **63 slice-A candidates with entries below**.
- **Handed to other slices:** these titles passed the screen but belong to another slice's query family. They have no entries here.
  - **To slice B** (education and contests), 14 titles:
    - Detecting ChatGPT-Generated Code in a CS1 Course
    - Detecting ChatGPT-Generated Code Submissions in a CS1 Course Using Machine Learning Models
    - Leveraging LLM for Detecting and Explaining LLM-generated Code in Python Programming Courses
    - LLM-Based Explainable Detection of LLM-Generated Code in Python Programming Courses
    - Detecting AI assisted submissions in introductory programming via code anomaly
    - Using pseudo-AI submissions for detecting AI-generated code
    - AI-Generated Code Detection: An Examination of Current Tools in Education
    - Detection of GenAI-produced and student-written C# code
    - Multi-Layer Feature Fusion for Detecting AI-Generated Code in Programming Education
    - Detecting AI-Generated Code in Introductory Programming Courses
    - Detection of AI-Generated Source Code in Programming Assignments
    - A Structural and Behavioral Hybrid Framework for Detecting AI-Generated Code in Programming Education
    - What are the differences between student and ChatGPT-generated pseudocode?
    - NPC: Automated Tool for Detecting and Explaining ChatGPT-Generated Programs
  - **To slice C** (watermarks and robustness), 3 titles:
    - Marking Code Without Breaking It
    - Detecting LLM-Generated Source Code via Robust Watermarking
    - Efficient and Universal Watermarking for LLM-Generated Code Detection
- **SemEval-2026 Task 13 system papers: open policy question.** OpenAlex returned about 25 system-description papers for SemEval-2026 Task 13 (ACL Anthology volume `2026.semeval-1`).
  - The task overview and the four system papers that have arXiv versions were verified and have entries.
  - The other ~21 were **not opened**, so under the verification rule they have no entries.
  - All of them pass Setting, because the task data has an algorithmic split. Including them all would make SemEval system papers the largest group in the corpus. This is flagged for the caller to decide, not resolved here.

## Included

### SemEval-2026 Task 13: Detecting Machine-Generated Code with Multiple Programming Languages, Generators, and Application Scenarios
- **Authors**: Daniil Orel, Dilshod Azizov, Indraneil Paul, Yuxia Wang, Iryna Gurevych, Preslav Nakov
- **Year / first public**: 2026-07
- **Venue**: Proceedings of the 20th International Workshop on Semantic Evaluation (SemEval-2026), pp. 3640–3658
- **URL**: https://aclanthology.org/2026.semeval-1.445/
- **Access**: open (PDF read)
- **Setting**: general code on coding-problem data. The training data is the algorithmic domain (CodeNet, TACO, LeetCode, Codeforces); research and deployed code are unseen test domains.
- **Method family**: dataset/benchmark (shared task)
- **Dataset**: built on DroidCollection plus the LeetCode and Codeforces problems from CoDet-M4. Trained on C++, Python and Java; tested additionally on Go, PHP, C#, C and JavaScript. Subtask A is binary, B is generator-family attribution, C is 4-way (human, machine, hybrid, adversarial).
- **Headline result**: on Subtask A, the top system reached Macro-F 0.997 and most of the 81 teams scored between 0.50 and 0.70. The best Subtask B system reached 0.508.
- **Limitation**: test labels were withheld after the competition, so the reported scores cannot be re-derived independently [reader-inferred].
- **Decision**: include. Benchmark with an algorithmic coding-problem split; first public version in range.

### Distinguishing LLM-generated from Human-written Code by Contrastive Learning (CodeGPTSensor)
- **Authors**: Xiaodan Xu, Chao Ni, Xinrong Guo et al.
- **Year / first public**: 2024-11
- **Venue**: ACM Transactions on Software Engineering and Methodology (DOI 10.1145/3705300); arXiv preprint 2411.04704
- **URL**: https://arxiv.org/abs/2411.04704
- **Access**: open
- **Setting**: general code on coding-problem data. The main corpus is CodeSearchNet; §6.3 adds a secondary evaluation on GPTSniffer's Java textbook-exercise set.
- **Method family**: trained classifier (contrastive learning, UniXcoder encoder) + dataset/benchmark (HMCorp)
- **Dataset**: HMCorp, 550K human/ChatGPT pairs (288K Python, 222K Java) built from CodeSearchNet docstrings; plus D_α-C8, 1,484 Java snippets from end-of-chapter book exercises.
- **Headline result**: on the D_α-C8 coding-exercise test set, accuracy 0.936, F1 0.934, AUC 0.976, ahead of GPTSniffer at F1 0.929 (Table 12).
- **Limitation**: the coding-problem evidence rests on one small Java set; the main results are on CodeSearchNet functions [reader-inferred].
- **Decision**: include. Trained detector evaluated on coding-exercise data; first public version 2024-11.

### AIGCodeSet: A New Annotated Dataset for AI Generated Code Detection
- **Authors**: Basak Demirok, Mucahid Kutlu
- **Year / first public**: 2024-12
- **Venue**: SIU 2025 (IEEE Signal Processing and Communications Applications Conference); arXiv preprint 2412.16594
- **URL**: https://arxiv.org/abs/2412.16594
- **Access**: open
- **Setting**: general code on coding-problem data (CodeNet)
- **Method family**: dataset/benchmark
- **Dataset**: CodeNet Python problems; 4,755 human-written and 2,828 AI-generated Python files from CodeLlama 34B, Codestral 22B and Gemini 1.5 Flash. Covers generation from scratch, fixing runtime errors, and fixing incorrect outputs.
- **Headline result**: a Bayesian classifier scored best, with F1 0.63 on the test set (Table 3).
- **Limitation**: Python only and three generators; baselines are shallow, with no fine-tuned code encoders [reader-inferred].
- **Decision**: include. CodeNet-based detection dataset; first public version 2024-12.

### CoDet-M4: Detecting Machine-Generated Code in Multi-Lingual, Multi-Generator and Multi-Domain Settings
- **Authors**: Daniil Orel, Dilshod Azizov, Preslav Nakov
- **Year / first public**: 2025-03
- **Venue**: Findings of ACL 2025 (https://aclanthology.org/2025.findings-acl.550/); arXiv preprint 2503.13733
- **URL**: https://arxiv.org/abs/2503.13733
- **Access**: open
- **Setting**: general code on coding-problem data (LeetCode and Codeforces splits, plus GitHub)
- **Method family**: dataset/benchmark + trained classifier
- **Dataset**: C++, Python and Java from LeetCode, Codeforces and GitHub, with multiple open LLM generators. The MIPRO 2026 paper below reports CoDet-M4 as 500,552 samples. Includes out-of-domain, unseen-generator and hybrid-authorship tests.
- **Headline result**: UniXcoder reached F1 96.54 on the Codeforces split and 97.87 on the LeetCode split (Table 4); authorship identification reached F1 66.33 (Table 7).
- **Limitation**: telling which LLM wrote the code is much harder than binary detection (best F1 66.33 against about 97 for binary), so per-generator attribution claims are weak [reader-inferred from Tables 4 and 7].
- **Decision**: include. Benchmark with competitive-programming domains; first public version 2025-03.

### Droid: A Resource Suite for AI-Generated Code Detection
- **Authors**: Daniil Orel, Indraneil Paul, Iryna Gurevych, Preslav Nakov
- **Year / first public**: 2025-07
- **Venue**: EMNLP 2025 (https://aclanthology.org/2025.emnlp-main.1593/); arXiv preprint 2507.10583
- **URL**: https://arxiv.org/abs/2507.10583
- **Access**: open
- **Setting**: general code on coding-problem data (competitive-programming "algorithmic" domain, plus GitHub and research code)
- **Method family**: dataset/benchmark + trained classifier (DroidDetect encoders)
- **Dataset**: DroidCollection, over 1M samples in 7 languages from 43 generators, across three domains, including human-AI co-authored and adversarial samples.
- **Headline result**: DroidDetect had weighted F1 99.18 (Base) / 99.25 (Large) on the 2-class task (Table 6). In the out-of-domain evaluation, DroidDetect-CLS-Base trained only on the algorithmic domain scored 98.26 on algorithmic code but 49.63 on general code (OOD results table).
- **Limitation**: most detectors are easily evaded by "humanised" generations unless some adversarial data is in training [author-acknowledged, quote: "most detectors are easily compromised by humanising the output distributions"].
- **Decision**: include. Benchmark with an algorithmic coding-problem domain; first public version 2025-07.

### AICD Bench: A Challenging Benchmark for AI-Generated Code Detection
- **Authors**: Daniil Orel, Dilshod Azizov, Indraneil Paul et al.
- **Year / first public**: 2026-02
- **Venue**: EACL 2026 (https://aclanthology.org/2026.eacl-long.325/); arXiv preprint 2602.02079
- **URL**: https://arxiv.org/abs/2602.02079
- **Access**: open
- **Setting**: general code on coding-problem data. The seen domain is algorithmic code, including CodeNet-based generations; research and general-purpose code are unseen domains.
- **Method family**: dataset/benchmark
- **Dataset**: 2M examples from 77 generators in 11 families, 9 languages. Tasks: robust binary classification, model-family attribution, and fine-grained human/machine/hybrid/adversarial classification.
- **Headline result**: in Task 1, average Macro-F1 was 0.63 in the seen domain and language, falling to 0.20–0.21 in unseen domains (Table 5).
- **Limitation**: performance "remains far below practical usability" under distribution shift [author-acknowledged, abstract].
- **Decision**: include. Benchmark with an algorithmic split; first public version 2026-02.

### An Empirical Study on Automatically Detecting AI-Generated Source Code: How Far Are We?
- **Authors**: Hyunjae Suh, Mahan Tafreshipour, Jiawei Li et al.
- **Year / first public**: 2024-11
- **Venue**: ICSE 2025; arXiv preprint 2411.04299
- **URL**: https://arxiv.org/abs/2411.04299
- **Access**: open
- **Setting**: general code on coding-problem data (MBPP, HumanEval-X, plus CodeSearchNet)
- **Method family**: empirical study + trained classifier
- **Dataset**: MBPP (974 Python problems), HumanEval-X and CodeSearchNet, with code from several LLMs at several temperatures; Java, C++ and Python.
- **Headline result**: existing detectors performed poorly; the best proposed model reached F1 82.55 and beat GPTSniffer.
- **Limitation**: problem-level data is limited to two small function-synthesis benchmarks [reader-inferred].
- **Decision**: include. Detector evaluation on MBPP and HumanEval coding problems; first public version 2024-11.

### Uncovering LLM-Generated Code: A Zero-Shot Synthetic Code Detector via Code Rewriting
- **Authors**: Tong Ye, Yangkai Du, Tengfei Ma et al.
- **Year / first public**: 2024-05
- **Venue**: AAAI 2025; arXiv preprint 2405.16133
- **URL**: https://arxiv.org/abs/2405.16133
- **Access**: open
- **Setting**: general code on coding-problem data (APPS, MBPP)
- **Method family**: zero-shot
- **Dataset**: APPS (test split only, to avoid training-data overlap) and MBPP. Generators: CodeLlama, StarChat and GPT-3.5 (770 samples each) and GPT-4 (100 samples).
- **Headline result**: AUROC improved over the prior best synthetic-content detector by 20.5% on APPS and 29.1% on MBPP.
- **Limitation**: the GPT-4 subset has only 100 samples because of cost [author-acknowledged, section: dataset construction].
- **Decision**: include. Zero-shot detector on APPS and MBPP; first public version 2024-05.

### Zero-Shot Detection of LLM-Generated Code via Approximated Task Conditioning
- **Authors**: Maor Ashkenazi, Ofir Brenner, Tal Furman Shohet et al.
- **Year / first public**: 2025-06
- **Venue**: ECML-PKDD 2025 (Springer LNCS); arXiv preprint 2506.06069
- **URL**: https://arxiv.org/abs/2506.06069
- **Access**: open
- **Setting**: general code on coding-problem data (MBPP, APPS)
- **Method family**: zero-shot
- **Dataset**: MBPP and APPS, in Python, C++ and Java.
- **Headline result**: with N = 4 approximated tasks and CodeLlama-13B as the detector LLM, mean AUROC 94.22 on MBPP and 93.82 on APPS (§4.2).
- **Limitation**: the method needs a capable instruction LLM to approximate the task, which adds inference cost per snippet [reader-inferred].
- **Decision**: include. Zero-shot detector on coding-problem benchmarks; first public version 2025-06.

### ChatGPT Code Detection: Techniques for Uncovering the Source of Code
- **Authors**: Marc Oedingen, Raphael C. Engelhardt, Robin Denz et al.
- **Year / first public**: 2024-05
- **Venue**: AI (MDPI), 2024, 5(3), 1066–1094; arXiv preprint 2405.15512
- **URL**: https://arxiv.org/abs/2405.15512
- **Access**: open
- **Setting**: competitive programming (APPS, CodeChef, HackerEarth, among others)
- **Method family**: trained classifier
- **Dataset**: balanced set of 3.14 × 10⁴ human and GPT-3.5 Python solutions to coding problems, with the train/test split made by problem.
- **Headline result**: embedding features with supervised learners reached about 98% accuracy; the interpretable white-box Bayes classifier reached 85–88%.
- **Limitation**: one generator (ChatGPT/GPT-3.5) and one language [reader-inferred].
- **Decision**: include. Classifier on contest-problem solutions; first public version 2024-05.

### Whodunit: Classifying Code as Human Authored or GPT-4 Generated — A case study on CodeChef problems
- **Authors**: Oseremen Joy Idialu, Noble Saji Mathews, Rungroj Maipradit, Joanne M. Atlee, Mei Nagappan
- **Year / first public**: 2024-03
- **Venue**: MSR 2024 (DOI 10.1145/3643991.3644926); arXiv preprint 2403.04013. These are two versions of one paper, merged here.
- **URL**: https://arxiv.org/abs/2403.04013
- **Access**: open
- **Setting**: competitive programming (CodeChef)
- **Method family**: stylometry/AST + trained classifier
- **Dataset**: human CodeChef solutions submitted before 2021, and GPT-4 solutions to the same problems, in Python.
- **Headline result**: F1 and AUC-ROC 0.91; 0.89 without gameable whitespace features.
- **Limitation**: one generator (GPT-4); slightly worse on harder problems [author-acknowledged, abstract].
- **Decision**: include. Classifier on contest data; first public version 2024-03. Overlaps slice B (stylometry).

### One Size Does Not Fit All: Investigating Efficacy of Perplexity in Detecting LLM-Generated Code
- **Authors**: Jinwei Xu, He Zhang, Yanjing Yang et al.
- **Year / first public**: 2024-12
- **Venue**: ACM TOSEM (DOI 10.1145/3748506); arXiv preprint 2412.16525
- **URL**: https://arxiv.org/abs/2412.16525
- **Access**: open
- **Setting**: general code on coding-problem data (CodeNet)
- **Method family**: empirical study (zero-shot perplexity vs feature- and pre-training-based detectors)
- **Dataset**: 729 CodeNet programming puzzles in 8 languages; 11,664 GPT-3.5 solutions plus at least two human solutions per puzzle per language.
- **Headline result**: perplexity-based detection trailed GPTSniffer in all 8 languages, for example Python AUC 63.89% vs 95.17%, but generalised best.
- **Limitation**: one generator (GPT-3.5) [reader-inferred].
- **Decision**: include. Detector comparison on CodeNet; first public version 2024-12.

### CodeVision: Detecting LLM-Generated Code Using 2D Token Probability Maps and Vision Models
- **Authors**: Zhenyu Xu, Victor S. Sheng
- **Year / first public**: 2025-01
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2501.03288
- **Access**: open
- **Setting**: general code on coding-problem data (CodeNet)
- **Method family**: trained classifier (vision models over log-probability maps)
- **Dataset**: from CodeNet, 28,342 samples (15,633 GPT-3.5/GPT-4, 12,709 human) in C, C++, Go, Java, Python and Ruby.
- **Headline result**: ResNet AUC 0.96–0.99 and ViT AUC 0.94–0.99 across the six languages, against DetectGPT at 0.66–0.97 (Table 1).
- **Limitation**: AUC drops when the scoring model's generator differs from lower-quality code LLMs [author-acknowledged, section: cross-model results].
- **Decision**: include. Detector on CodeNet; first public version 2025-01.

### Detection of LLM-Generated Java Code Using Discretized Nested Bigrams
- **Authors**: Timothy Paek, Chilukuri Mohan
- **Year / first public**: 2025-02
- **Venue**: CSCI 2024 proceedings (Springer); arXiv preprint 2502.15740
- **URL**: https://arxiv.org/abs/2502.15740
- **Access**: open
- **Setting**: competitive programming (Google Code Jam, "GPT GCJ" dataset)
- **Method family**: stylometry/AST + trained classifier
- **Dataset**: 976 GPT-rewritten Java files (GPT-3.5 and GPT-4); a 40-author set of 3,021 files; GCJ, 76,089 files from more than 1,000 authors with GPT-4o.
- **Headline result**: 99% accuracy and 0.999 AUC on 76,089 GCJ files with GPT-4o, using 227 features.
- **Limitation**: the generated code is GPT *rewriting* of human files, not generation from the problem statement, which may make it easier to tell apart [reader-inferred].
- **Decision**: include. Detector on Code Jam data; first public version 2025-02.

### Whitespaces Don't Lie: Feature-Driven and Embedding-Based Approaches for Detecting Machine-Generated Code
- **Authors**: Syed Mehedi Hasan Nirob, Shamim Ehsan, Moqsadur Rahman et al.
- **Year / first public**: 2026-01
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2601.19264
- **Access**: open
- **Setting**: general code on coding-problem data (DroidCollection, which has an algorithmic domain)
- **Method family**: stylometry/AST + trained classifier
- **Dataset**: 600K human and AI samples from DroidCollection.
- **Headline result**: feature-based models reached ROC-AUC 0.995 and F1 0.971; CodeBERT embeddings reached ROC-AUC 0.994 and F1 0.965.
- **Limitation**: in-distribution evaluation only, on one benchmark, with whitespace cues that formatting can remove [reader-inferred].
- **Decision**: include under the mixed-benchmark rule; first public version 2026-01.

### LLMSniffer: Detecting LLM-Generated Code via GraphCodeBERT and Supervised Contrastive Learning
- **Authors**: Mahir Labib Dihan, Abir Muhtasim
- **Year / first public**: 2026-04
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2604.16058
- **Access**: open
- **Setting**: competitive programming (Whodunit CodeChef set) and textbook exercises (GPTSniffer set)
- **Method family**: trained classifier
- **Dataset**: the GPTSniffer and Whodunit benchmark datasets.
- **Headline result**: accuracy rose from 91% to 94.65% on Whodunit and from 70% to 78% on GPTSniffer.
- **Limitation**: both benchmarks are small and use single generators [reader-inferred].
- **Decision**: include. Classifier on contest and exercise data; first public version 2026-04.

### DuoLens: A Framework for Robust Detection of Machine-Generated Multilingual Text and Code
- **Authors**: Shriyansh Agrawal, Aidan Lau, Sanyam Shah et al.
- **Year / first public**: 2025-10
- **Venue**: NeurIPS 2025 Workshop on Deep Learning for Code; arXiv preprint 2510.18904
- **URL**: https://arxiv.org/abs/2510.18904
- **Access**: open
- **Setting**: general code on coding-problem data (curated from AIGCD, DroidCollection and CodeMirage)
- **Method family**: trained classifier (fine-tuned RoBERTa / CodeBERTa)
- **Dataset**: code in 7 languages, plus multilingual text.
- **Headline result**: AUROC 0.97–0.99 and macro-F1 0.89–0.94; at least 92% of clean AUROC is kept under cross-generator and adversarial shifts.
- **Limitation**: the paper does not report performance separately for the coding-problem subset [reader-inferred].
- **Decision**: include under the mixed-benchmark rule; first public version 2025-10.

### Is This You, LLM? Recognizing AI-written Programs with Multilingual Code Stylometry
- **Authors**: Andrea Gurioli, Maurizio Gabbrielli, Stefano Zacchiroli
- **Year / first public**: 2024-12
- **Venue**: SANER 2025; arXiv preprint 2412.14611
- **URL**: https://arxiv.org/abs/2412.14611
- **Access**: open
- **Setting**: general code on coding-problem data (Rosetta Code tasks)
- **Method family**: trained classifier + dataset/benchmark
- **Dataset**: H-AIRosettaMP, 121,247 snippets in 10 languages. Human snippets are Rosetta Code solutions; AI snippets are StarCoder2 translations of a human solution from another language.
- **Headline result**: 84.1% ± 3.8% average accuracy across the 10 languages.
- **Limitation**: AI samples come from translation by one model (StarCoder2), not from the problem statement [reader-inferred].
- **Decision**: include. Classifier on Rosetta Code programming tasks; first public version 2024-12. Overlaps slice B (stylometry).

### Code Detectors Have a Half-Life: Obsolescence and Metric Illusions in LLM-Generated Code Detection
- **Authors**: Alberick Euraste Djire
- **Year / first public**: 2026-10
- **Venue**: ASE 2026 (DOI 10.1145/3832783.3844566); arXiv preprint 2610.01664
- **URL**: https://arxiv.org/abs/2610.01664
- **Access**: open
- **Setting**: general code on coding-problem data (AI-Human-Generated-Program-Code dataset: 18 programming problems)
- **Method family**: empirical study (LLM judges vs dedicated detectors)
- **Dataset**: Idrisov & Schlippe (2024). 18 problems in C++, Python and Java; each has one human solution and one solution from each of 7 generators (StarCoder, ChatGPT, Bing AI Chat, Code Llama, CodeWhisperer, Copilot, InstructCodeT5+).
- **Headline result**: DetectCodeGPT and GPTSniffer reached accuracy 0.50 but F1 0.00 across all generators, because they label almost everything AI-generated. General-purpose LLM judges did better.
- **Limitation**: 18 problems is a very small sample [reader-inferred].
- **Decision**: include. Detector evaluation on programming-problem data; first public version 2026-10.

### Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming
- **Authors**: Runlong Ye, Jing Fan, Angela Zavaleta Bernuy et al.
- **Year / first public**: 2026-10
- **Venue**: Koli Calling '26 (DOI 10.1145/3856208.3856226); arXiv preprint 2610.00863
- **URL**: https://arxiv.org/abs/2610.00863
- **Access**: open
- **Setting**: education (ten introductory Python labs, 2021, 2023 and 2025 cohorts)
- **Method family**: empirical study (matching against a reference bank of generated solutions, with MOSS and AST analysis)
- **Dataset**: 29,970 student submissions; 90,000 solution attempts from three frontier LLMs.
- **Headline result**: student submissions matched the generated references more often in later cohorts, and on tightly specified functions the LLMs converged on a few exact AST forms. The readable text gives no single detection metric (not reported).
- **Limitation**: attributing AI use to an individual submission "would require additional evidence" [author-acknowledged, abstract].
- **Decision**: include. Detection study in programming education; first public version 2026-10. Overlaps slice B.

### Fine-Tuning Pre-Trained Code Models for AI-Generated Code Detection (Archaeology at SemEval-2026 Task 13)
- **Authors**: Jany-Gabriel Ispas, Sergiu Nisioi
- **Year / first public**: 2026-05
- **Venue**: SemEval-2026 (DOI 10.18653/v1/2026.semeval-1.383); arXiv preprint 2605.01596
- **URL**: https://arxiv.org/abs/2605.01596
- **Access**: open
- **Setting**: general code on coding-problem data (SemEval-2026 Task 13 data)
- **Method family**: trained classifier (CodeBERT, GraphCodeBERT, UniXcoder, CodeT5+)
- **Dataset**: SemEval-2026 Task 13, Subtasks A and B.
- **Headline result**: macro-F1 0.737 on Subtask A (6th of 81) and 0.422 on Subtask B (7th of 34).
- **Limitation**: shared-task system paper; the results apply to one benchmark's splits [reader-inferred].
- **Decision**: include. See the SemEval policy flag in the Queries section; first public version 2026-05.

### mcdok at SemEval-2026 Task 13: Finetuning LLMs for Detection of Machine-Generated Code
- **Authors**: Adam Skurla, Dominik Macko, Jakub Simko
- **Year / first public**: 2026-04
- **Venue**: SemEval-2026; arXiv preprint 2604.21365
- **URL**: https://arxiv.org/abs/2604.21365
- **Access**: open
- **Setting**: general code on coding-problem data (SemEval-2026 Task 13 data)
- **Method family**: trained classifier (fine-tuned LLMs)
- **Dataset**: SemEval-2026 Task 13, Subtasks A, B and C.
- **Headline result**: not reported in the abstract; the systems are described as "competitive" with "significant" margins to the top systems.
- **Limitation**: same as above [reader-inferred].
- **Decision**: include. See the SemEval policy flag; first public version 2026-04.

### FMI_SU_Yotkova_Kastreva at SemEval-2026 Task 13: Lightweight Detection of LLM-Generated Code via Stylometric Signals
- **Authors**: Elitsa Yotkova, Violeta Kastreva, Dimitar Dimitrov et al.
- **Year / first public**: 2026-05
- **Venue**: SemEval-2026 (DOI 10.18653/v1/2026.semeval-1.275); arXiv preprint 2605.04157
- **URL**: https://arxiv.org/abs/2605.04157
- **Access**: open
- **Setting**: general code on coding-problem data (SemEval-2026 Task 13 data)
- **Method family**: stylometry/AST + trained classifier (shallow decision tree)
- **Dataset**: SemEval-2026 Task 13, Subtask A.
- **Headline result**: not reported in the abstract (it stresses CPU-only training and near-instant inference).
- **Limitation**: same as above [reader-inferred].
- **Decision**: include. See the SemEval policy flag; first public version 2026-05.

### Dream at SemEval-2026 Task 13: SALSA for Single-Pass Machine-Generated Code Detection
- **Authors**: Ruslan Berdichevsky, Shai Nahum-Gefen, Elad Ben-Zaken
- **Year / first public**: 2026-06
- **Venue**: SemEval-2026 (DOI 10.18653/v1/2026.semeval-1.52); arXiv preprint 2606.25102
- **URL**: https://arxiv.org/abs/2606.25102
- **Access**: open
- **Setting**: general code on coding-problem data (SemEval-2026 Task 13 data)
- **Method family**: trained classifier (parameter-efficient fine-tuned LLM emitting a single-token label)
- **Dataset**: SemEval-2026 Task 13, Subtask A.
- **Headline result**: out-of-distribution F1 0.789 on the official leaderboard, against the CodeBERT baseline at 0.305.
- **Limitation**: same as above [reader-inferred].
- **Decision**: include. See the SemEval policy flag; first public version 2026-06.

### CodeRipple: Wavelet-Based Detection of LLM-Generated Code
- **Authors**: Xingyu Yao, Zhendong Mao, Quan Wang
- **Year / first public**: 2026-07
- **Venue**: ACL 2026 (Long Papers), pp. 38351–38364
- **URL**: https://aclanthology.org/2026.acl-long.1777/
- **Access**: open (PDF read)
- **Setting**: general code on coding-problem data (AI Code Detection Education dataset of Pan et al. 2024, HumanEval, CoDet-M4)
- **Method family**: zero-shot
- **Dataset**: three benchmarks: ChatGPT code under 13 evasion strategies; HumanEval code from 5 recent LLMs; CoDet-M4 (Python, Java, C++).
- **Headline result**: AUROC 0.925 on AI Code Detection Education (Strategy 1), against Fast-DetectGPT 0.800 and DetectCodeGPT 0.600 (Table 6).
- **Limitation**: struggles on very short snippets and on highly templated human code [author-acknowledged, section: Failure Mode Analysis].
- **Decision**: include. Zero-shot detector on coding-problem data; first public version 2026-07 (ACL Anthology).

### Codetector: A Framework for Zero-Shot Detection of AI-Generated Code
- **Authors**: Nadim Adham, Henning Duwe, Holger H. Hoos
- **Year / first public**: 2025. The month is not confirmed; it appears in the Learning and Intelligent Optimization (LION) proceedings, Springer LNCS.
- **Venue**: LION (Springer LNCS), DOI 10.1007/978-3-032-09192-5_11
- **URL**: https://ada.liacs.leidenuniv.nl/papers/AdhEtAl25.pdf. This is the author copy, which was read; the Springer page redirected to a login.
- **Access**: open (author PDF)
- **Setting**: general code on coding-problem data (LeetCode, plus Stack Overflow and other sources)
- **Method family**: zero-shot (comparison of five methods) + dataset/benchmark
- **Dataset**: 113,776 code samples generated by 17 LLMs from six datasets and sources, with newly collected time-stamped samples to control for data leakage.
- **Headline result**: AUROC up to 97%, averaging about 83%, with newer zero-shot methods (Conclusions).
- **Limitation**: detection depends strongly on generation parameters such as temperature [author-acknowledged, section: Conclusions].
- **Decision**: include. Zero-shot evaluation that includes LeetCode problems; first public version 2025.

### MAGECODE: Machine-Generated Code Detection Method Using Large Language Models
- **Authors**: H. Pham, Huyen Ha, Van Tong et al.
- **Year / first public**: 2024 (month not confirmed)
- **Venue**: IEEE Access (DOI 10.1109/ACCESS.2024.3509987)
- **URL**: https://doi.org/10.1109/access.2024.3509987. The publisher page served a bot check, so identity and abstract were verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/access.2024.3509987
- **Access**: open (journal is open access; agent read the abstract only)
- **Setting**: education / coding problems ("code solutions generated by LLMs for programming problems"; motivated by student assignments)
- **Method family**: trained classifier (CodeT5+ features with log-likelihood and rank metrics)
- **Dataset**: more than 45,000 LLM solutions (GPT-4, Gemini, Code-bison-32k) to programming problems, in Python, Java and C++.
- **Headline result**: up to 98.46% accuracy, with false-positive rate below 1%.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: include. Detector on programming-problem solutions; first public version 2024.

### Detecting AI-Generated Code Assignments Using Perplexity of Large Language Models
- **Authors**: Zhenyu Xu, Victor S. Sheng
- **Year / first public**: 2024-03
- **Venue**: AAAI 2024 (DOI 10.1609/aaai.v38i21.30361)
- **URL**: https://doi.org/10.1609/aaai.v38i21.30361. The OJS page timed out for WebFetch, so the paper was verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1609/aaai.v38i21.30361
- **Access**: open (AAAI OJS; agent read the abstract only)
- **Setting**: education (student code assignments)
- **Method family**: zero-shot (targeted-masking perturbation with a perplexity and burstiness score)
- **Dataset**: code submissions generated by text-davinci-003 versus human submissions; the abstract gives no size.
- **Headline result**: average AUC 0.87, against the GPTZero baseline at 0.56.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: include. Zero-shot detector for programming assignments; first public version 2024-03. Overlaps slice B.

### Assessing AI Detectors in Identifying AI-Generated Code: Implications for Education
- **Authors**: Wei-Hung Pan, M. Chok, J. L. Wong et al.
- **Year / first public**: 2024-01
- **Venue**: ICSE-SEET 2024 (DOI 10.1145/3639474.3640068)
- **URL**: https://doi.org/10.1145/3639474.3640068. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3639474.3640068, because the ACM page blocks automated fetch.
- **Access**: open (S2 flags it open access; agent read the abstract only)
- **Setting**: education; coding problems from LeetCode, Kaggle and Quescol
- **Method family**: empirical study / robustness study of five AIGC detectors
- **Dataset**: 5,069 problems with human Python solutions (1,725 LeetCode, 3,264 Kaggle, 80 Quescol); ChatGPT outputs under 13 prompt variants.
- **Headline result**: existing AIGC detectors "perform poorly"; the abstract gives no number (not reported).
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: include. Detector evaluation on LeetCode-style problems; first public version 2024-01. Found by snowballing from CodeRipple's datasets. Overlaps slices B and C.

### Detecting AI-Generated Text and Code: An Empirical Study of Cross-Generator and Cross-Domain Generalization
- **Authors**: Neethika Alluri, Pardha Saradhi Varma Gottumukkala, H. Indukuri
- **Year / first public**: 2026-08
- **Venue**: AI (MDPI), DOI 10.3390/ai7080319
- **URL**: https://doi.org/10.3390/ai7080319. MDPI returned 403 to automated fetch, so the paper was verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/ai7080319
- **Access**: open (MDPI open access; agent read the abstract only)
- **Setting**: general code on coding-problem data (MBPP, HumanEval, plus CodeSearchNet)
- **Method family**: empirical study + trained classifier
- **Dataset**: 22,141 instances from HC3, CodeSearchNet, MBPP and HumanEval, plus Mix-Eval (997 notebook-style samples).
- **Headline result**: in-distribution AUROC 1.0000; under domain shift to MBPP+HumanEval, GraphCodeBERT fell to 0.85 and CodeBERT-base to 0.67.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: include. Evaluation on MBPP and HumanEval; first public version 2026-08.

### From Syntax Trees to Embeddings: A Comparative Study of AI-Generated Code Detection
- **Authors**: Marino Jakimoski, M. Toshevska, S. Gievska
- **Year / first public**: 2026-05
- **Venue**: MIPRO 2026 (IEEE), DOI 10.1109/MIPRO70003.2026.11591667
- **URL**: https://doi.org/10.1109/mipro70003.2026.11591667. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/mipro70003.2026.11591667, because IEEE Xplore returned a bot-check response.
- **Access**: paywalled
- **Setting**: general code on coding-problem data (CoDet-M4)
- **Method family**: stylometry/AST + trained classifier (CST features, CodeBERT embeddings, graph models)
- **Dataset**: CoDet-M4, 500,552 samples in Java, Python and C++.
- **Headline result**: embedding-based models scored highest; the abstract gives no number (not reported).
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: include. Classifier on CoDet-M4; first public version 2026-05.

### Deep Learning Techniques for Differentiating Human-Written and AI-Generated Source Codes
- **Authors**: K. D. H. Apsara, R. Rupasingha, B. Kumara
- **Year / first public**: 2026-02
- **Venue**: ICARC 2026 (IEEE), DOI 10.1109/ICARC68737.2026.11453890
- **URL**: https://doi.org/10.1109/icarc68737.2026.11453890. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/icarc68737.2026.11453890
- **Access**: paywalled
- **Setting**: competitive programming (GPTGCJ Java dataset, Google Code Jam)
- **Method family**: trained classifier (ANN, CNN, XGBoost over AST, token, TF-IDF and embedding features)
- **Dataset**: 20,000 balanced samples from GPTGCJ Java.
- **Headline result**: a CNN on code embeddings reached 94.97% accuracy.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: include. Classifier on Code Jam data; first public version 2026-02.

### LevDetectCode: Zero-Shot Detection of AI-Generated Code Using Levenshtein Distance
- **Authors**: Jiazhou Fu, Guohua Shen, Zhiqiu Huang, Yaoshen Yu, Yu Zhao
- **Year / first public**: 2025-09
- **Venue**: International Journal of Software Engineering and Knowledge Engineering (DOI 10.1142/S0218194025500524)
- **URL**: https://doi.org/10.1142/s0218194025500524. World Scientific returned 403, so identity and abstract were read from the Crossref record https://api.crossref.org/works/10.1142/s0218194025500524
- **Access**: paywalled
- **Setting**: general code on coding-problem data (MBPP-train, HumanEval, CodeContest Java test split)
- **Method family**: zero-shot
- **Dataset**: Python from MBPP and HumanEval and Java from CodeContests, generated by GPT-3.5, GPT-4 and DeepSeek-V3; plus a C++ case study.
- **Headline result**: AUROC 5–10 points above other zero-shot baselines, and about 3,000× faster.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: include. Zero-shot detector on coding-problem benchmarks; first public version 2025-09.

### MultiAIGCD: A Comprehensive Dataset for AI Generated Code Detection Covering Multiple Languages, Models, Prompts, and Scenarios
- **Authors**: Basak Demirok, Mucahid Kutlu, Selin Mergen
- **Year / first public**: 2025-07
- **Venue**: Neural Computing and Applications (DOI 10.1007/s00521-026-12336-0); arXiv preprint 2507.21693
- **URL**: https://arxiv.org/abs/2507.21693
- **Access**: open
- **Setting**: general code on coding-problem data (CodeNet problem definitions and human solutions)
- **Method family**: dataset/benchmark
- **Dataset**: 121,271 AI-generated and 32,148 human snippets in Python, Java and Go, from six LLMs (including o3-mini), three prompts, and three scenarios: generate from the problem, fix runtime errors, fix wrong outputs.
- **Headline result**: not reported (the abstract gives no number; the tables were not extracted).
- **Limitation**: inherits AIGCodeSet's CodeNet-only problem source [reader-inferred].
- **Decision**: include. CodeNet-based detection benchmark; first public version 2025-07. Found by forward snowballing from AIGCodeSet.

### UCSC-NLP at SemEval-2026 Task 13: Multi-View Generalization and Diagnostic Analysis of Machine-Generated Code Detection
- **Authors**: Kargi Chauhan, Sadiba Nusrat Nur
- **Year / first public**: 2026-04
- **Venue**: SemEval-2026; arXiv preprint 2604.26990
- **URL**: https://arxiv.org/abs/2604.26990
- **Access**: open
- **Setting**: general code on coding-problem data (SemEval-2026 Task 13 data)
- **Method family**: trained classifier (UniXcoder with multi-view, generator-invariant training)
- **Dataset**: SemEval-2026 Task 13, Subtasks A and B.
- **Headline result**: Subtask A macro-F1 was 0.993 on validation and 0.845 on the test set (unseen languages and domains). Subtask B macro-F1 was 0.086 under standard fine-tuning and 0.345 with class weighting.
- **Limitation**: Subtask B class imbalance (88.4% human, 221:1) makes accuracy misleading [author-acknowledged, abstract].
- **Decision**: include. See the SemEval policy flag; first public version 2026-04. Found by forward snowballing.

### Comparative Analysis of Rewriting-Based Large Language Model-Generated Synthetic Code Detection
- **Authors**: Maulana Arya Alambana, Arif Nurwidyantoro
- **Year / first public**: 2026-09
- **Venue**: IEEE ICAIIA 2026 (DOI 10.1109/ICAIIA70172.2026.11691940)
- **URL**: https://doi.org/10.1109/ICAIIA70172.2026.11691940. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ICAIIA70172.2026.11691940
- **Access**: paywalled
- **Setting**: general code on coding-problem data ("a problem–answer dataset written in Python")
- **Method family**: zero-shot (rewriting-similarity detector, extending Ye et al. 2024 with CodeT5)
- **Dataset**: Python problem–answer pairs with code variants; the abstract does not name the source.
- **Headline result**: mean AUROC 0.5805 for CodeT5 configurations against 0.5731 for GraphCodeBERT; the margin was not tested for significance.
- **Limitation**: no significance testing [author-acknowledged, abstract].
- **Decision**: include. Zero-shot detector on problem–answer data; first public version 2026-09. Found by forward snowballing from Ye et al.

### iJudge: A style-controlled educational dataset for evaluating human–LLM code authorship detection under distribution shift
- **Authors**: Chayatorn Chuon, Patteera Leechat, Sirion Vittayakorn
- **Year / first public**: 2026-10
- **Venue**: Information and Software Technology (DOI 10.1016/j.infsof.2026.108364)
- **URL**: https://doi.org/10.1016/j.infsof.2026.108364. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.infsof.2026.108364, which has no abstract.
- **Access**: open (S2 flags it open access; agent read title and metadata only)
- **Setting**: education (the title says it is an "educational dataset")
- **Method family**: dataset/benchmark
- **Dataset**: not known beyond the title.
- **Headline result**: not reported (no abstract readable).
- **Limitation**: not assessed (read scope: title only).
- **Decision**: include, on title evidence only: an educational authorship-detection benchmark first public 2026-10. **Confirm on full text.** Found by forward snowballing. Overlaps slice B.

## Background

### Zero-Shot Detection of Machine-Generated Codes (DetectGPT4Code)
- **Authors**: Xianjun Yang, Kexun Zhang, Haifeng Chen et al.
- **Year / first public**: 2023-10
- **Venue**: arXiv preprint (comment: "work in progress")
- **URL**: https://arxiv.org/abs/2310.05103
- **Access**: open
- **Setting**: general code on coding-problem data (CodeContests, APPS)
- **Method family**: zero-shot
- **Dataset**: Python solutions from CodeContests and APPS by text-davinci-003, GPT-3.5 and GPT-4; Java generalisation test.
- **Headline result**: "state-of-the-art detection results"; the abstract gives no number (not reported).
- **Limitation**: preprint only, marked work in progress [author-acknowledged, comments field].
- **Decision**: background. First public version 2023-10-08 is before the Nov 2023 start date. It is the first zero-shot code detector and the baseline that several included papers compare against.

### Is this Snippet Written by ChatGPT? An Empirical Study with a CodeBERT-Based Classifier (GPTSniffer)
- **Authors**: Phuong T. Nguyen, Juri Di Rocco, Claudio Di Sipio et al.
- **Year / first public**: 2023-07
- **Venue**: arXiv preprint 2307.09381. The journal version is "GPTSniffer: A CodeBERT-based classifier to detect source code written by ChatGPT", Journal of Systems and Software, 2024-08 (DOI 10.1016/j.jss.2024.112059, checked via Crossref). These are two versions of one paper, merged here.
- **URL**: https://arxiv.org/abs/2307.09381
- **Access**: open
- **Setting**: education (Java textbook end-of-chapter exercises)
- **Method family**: trained classifier (CodeBERT)
- **Dataset**: paired human and ChatGPT Java solutions to book exercises.
- **Headline result**: beats GPTZero and the OpenAI Text Classifier; the abstract gives no number (not reported).
- **Limitation**: the human solutions may be in ChatGPT's training data [author-acknowledged, section IV-B2].
- **Decision**: background. First public version 2023-07 is before Nov 2023. The project README names it as foundational.

### Between Lines of Code: Unraveling the Distinct Patterns of Machine and Human Programmers (DetectCodeGPT)
- **Authors**: Yuling Shi, Hongyu Zhang, Chengcheng Wan, Xiaodong Gu
- **Year / first public**: 2024-01
- **Venue**: ICSE 2025; arXiv preprint 2401.06461
- **URL**: https://arxiv.org/abs/2401.06461
- **Access**: open
- **Setting**: out of scope (CodeSearchNet and The Stack functions only)
- **Method family**: zero-shot
- **Dataset**: 10,000 CodeSearchNet Python functions and Python from The Stack.
- **Headline result**: "significantly outperforms state-of-the-art techniques"; the abstract gives no number (not reported).
- **Limitation**: the authors chose real-world project code "rather than simple programming problems, akin to those in the HumanEval or MBPP" [author-acknowledged, section III-C].
- **Decision**: background. It is in date but fails Setting, because there is no coding-problem evaluation. Kept as method background because included papers use it as a baseline (CodeRipple, Code Detectors Have a Half-Life, One Size Does Not Fit All).

### Evaluating AIGC Detectors on Code Content
- **Authors**: Jian Wang, Shangqing Liu, Xiaofei Xie, Yi Li
- **Year / first public**: 2023-04
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2304.05193
- **Access**: open
- **Setting**: general code on coding-problem data (APPS, plus Q&A and summarization content)
- **Method family**: empirical study
- **Dataset**: 492.5K ChatGPT samples (Q&A 115K, summarization 126K, code generation 226.5K).
- **Headline result**: AIGC detectors do worse on code than on natural language; the abstract gives no number (not reported).
- **Limitation**: not assessed (background).
- **Decision**: background. First public version 2023-04 is before Nov 2023. This is an early evaluation of text detectors on code.

### Discriminating Human-authored from ChatGPT-Generated Code Via Discernable Feature Analysis
- **Authors**: Li Ke, Hong Sheng, Fu Cai et al.
- **Year / first public**: 2023-06
- **Venue**: ISSREW 2023; arXiv preprint 2306.14397
- **URL**: https://arxiv.org/abs/2306.14397
- **Access**: open
- **Setting**: out of scope (open-source repositories)
- **Method family**: stylometry/AST + trained classifier
- **Dataset**: about 10,000 lines of ChatGPT code; human code cleaned from open-source repositories.
- **Headline result**: "high accuracy"; the abstract gives no number (not reported).
- **Limitation**: not assessed (background).
- **Decision**: background. First public version 2023-06 is before Nov 2023, and the data is not coding problems. Early feature-based work.

### The "code" of Ethics: A Holistic Audit of AI Code Generators
- **Authors**: Wanlun Ma, Yiliao Song, Minhui Xue et al.
- **Year / first public**: 2023-05
- **Venue**: IEEE TDSC 2024; arXiv preprint 2305.12747
- **URL**: https://arxiv.org/abs/2305.12747
- **Access**: open
- **Setting**: general code on coding-problem data (APPS, MBPP, HumanEval)
- **Method family**: trained classifier (neural-code detection and attribution in the CodeForensic framework)
- **Dataset**: APPS, MBPP and HumanEval code from CodeGen, InCoder, PolyCoder, GPT-Neo and CodeT5.
- **Headline result**: the abstract gives no number (not reported).
- **Limitation**: not assessed (background).
- **Decision**: background. First public version 2023-05 is before Nov 2023.

## Excluded

### Detecting LLM-generated Code with Subtle Modification by Adversarial Training (CodeGPTSensor+)
- **Authors**: Xin Yin, Xinrui Li, Chao Ni et al.
- **Year / first public**: 2025-07
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2507.13123
- **Access**: open
- **Setting**: out of scope (HMCorp, which is CodeSearchNet-derived, only)
- **Method family**: robustness study + trained classifier
- **Dataset**: HMCorp, 288,508 Python and 222,335 Java pairs, plus adversarial variants.
- **Headline result**: not reported in the abstract.
- **Limitation**: not assessed (excluded).
- **Decision**: exclude. Fails Setting: evaluated only on CodeSearchNet functions. It is also a slice C topic.

### Automatic Detection of LLM-Generated Code: A Comparative Case Study of Contemporary Models Across Function and Class Granularities
- **Authors**: Musfiqur Rahman, SayedHassan Khatoonabadi, Ahmad Abdellatif et al.
- **Year / first public**: 2024-09
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2409.01382
- **Access**: open
- **Setting**: out of scope (CodeSearchNet functions and classes)
- **Method family**: trained classifier (CatBoost on software metrics)
- **Dataset**: 14,485 functions and 11,913 classes from CodeSearchNet.
- **Headline result**: AUC-ROC 0.96 for GPT-3.5 against about 0.68–0.80 for newer models.
- **Limitation**: not assessed (excluded).
- **Decision**: exclude. Fails Setting.

### CodeMirage: A Multi-Lingual Benchmark for Detecting AI-Generated and Paraphrased Source Code from Production-Level LLMs
- **Authors**: Hanxi Guo, Siyuan Cheng, Kaiyuan Zhang et al.
- **Year / first public**: 2025-05
- **Venue**: arXiv preprint (also listed at NeurIPS 2025)
- **URL**: https://arxiv.org/abs/2506.11059
- **Access**: open
- **Setting**: out of scope (human code from the CodeParrot GitHub-Code-Clean dataset)
- **Method family**: dataset/benchmark
- **Dataset**: about 210,000 samples, with 10,000 human GitHub files in 10 languages and outputs from 10 production LLMs, original and paraphrased.
- **Headline result**: not reported in the abstract (it reports nine qualitative findings).
- **Limitation**: not assessed (excluded).
- **Decision**: exclude. Fails Setting, because there are no coding problems. It is widely used, so slice C may still want it as robustness background.

### Detection of LLM-Paraphrased Code and Identification of the Responsible LLM Using Coding Style Features
- **Authors**: Shinwoo Park, Hyundong Jin, Jeong-won Cha et al.
- **Year / first public**: 2025-02
- **Venue**: Engineering Applications of Artificial Intelligence, vol. 162 (2025); arXiv preprint 2502.17749
- **URL**: https://arxiv.org/abs/2502.17749
- **Access**: open
- **Setting**: out of scope (human code crawled from GitHub repositories created in 2019)
- **Method family**: stylometry/AST + dataset/benchmark (LPcode)
- **Dataset**: LPcode, pairs of human-written C, C++, Java and Python code and their LLM paraphrases.
- **Headline result**: F1 improved by 2.64% and 15.17% over the best baselines on the two tasks.
- **Limitation**: not assessed (excluded).
- **Decision**: exclude. Fails Setting.

### From Tokens to Files: Multi-Granularity Detection and Localization of AI-Involved Code
- **Authors**: Yue Xu, Xiyang Wang, Hui Liu et al.
- **Year / first public**: 2026-10
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2610.27863
- **Access**: open
- **Setting**: out of scope (repository files)
- **Method family**: trained classifier (token-level log-likelihood ratio between two LoRA adapters)
- **Dataset**: 11,773 AI-involved files and 2,541 human files; HybridCodeAuthorship; 19,445 human files from repositories created before 2022.
- **Headline result**: 72.4 macro-F1 at 1% FPR.
- **Limitation**: not assessed (excluded).
- **Decision**: exclude. Fails Setting. Its mixed-authorship angle is relevant to slice C.

### RealAIGC: Towards More Realistic Evaluation of AI-Generated Code Detection in Real-World Code Repository
- **Authors**: Wen-Tao Chen, Yu-Fei Chen, Hui-Qun Yu et al.
- **Year / first public**: 2026-10
- **Venue**: ASE 2026 (DOI 10.1145/3832783.3834411)
- **URL**: https://doi.org/10.1145/3832783.3834411. ACM returned 403, so the paper was verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3832783.3834411
- **Access**: open (S2 flags it open access; agent read the abstract only)
- **Setting**: out of scope (GitHub pull requests from coding agents)
- **Method family**: dataset/benchmark
- **Dataset**: more than 4M functions across 8 languages; pull requests by five coding agents.
- **Headline result**: "perplexity based methods are nearly ineffective in realistic settings"; the abstract gives no number (not reported).
- **Limitation**: not assessed (excluded).
- **Decision**: exclude. Fails Setting.

### Graph Neural Networks with Code Structure Embeddings for Model-Agnostic Multi-Class Detection of AI-Generated Programs
- **Authors**: Hayder Kareem Algabri
- **Year / first public**: 2026-09
- **Venue**: International Journal of Computer Information Systems and Industrial Management Applications (DOI 10.70917/ijcisim-2026-5572)
- **URL**: https://doi.org/10.70917/ijcisim-2026-5572. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.70917/ijcisim-2026-5572
- **Access**: open (S2 flags it open access; agent read the abstract only)
- **Setting**: out of scope (a controlled synthetic corpus of 2,500 Python programs with generator-family *proxies*)
- **Method family**: trained classifier (graph attention)
- **Dataset**: synthetic, 2,500 programs.
- **Headline result**: 92.1% macro-F1 in-distribution; mean AUROC at most 0.65 on unseen families.
- **Limitation**: not assessed (excluded).
- **Decision**: exclude. Fails Setting, because the data is synthetic rather than real coding problems.

### DualCodeDetect: Zero-Shot LLM-Generated Code Detection via Dual-Channel Perturbation
- **Authors**: Zhengdao Li, Xiuwei Shang, Zhenkan Fu et al.
- **Year / first public**: 2026-06
- **Venue**: Proceedings of the ACM on Software Engineering (DOI 10.1145/3808166)
- **URL**: https://doi.org/10.1145/3808166. ACM returned 403, so identity and abstract were read from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3808166 and the Crossref record.
- **Access**: open (S2 flags it open access; agent read the abstract only)
- **Setting**: not determinable. The abstract says "two datasets and ten representative code LLMs" without naming them.
- **Method family**: zero-shot
- **Dataset**: two unnamed datasets; Python, with cross-language tests on Java, C++ and JavaScript.
- **Headline result**: average AUROC 0.8477 on Python, with FPR 0.0430 and FNR 0.0552.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: exclude (provisional). Setting cannot be judged from the abstract. **Re-screen on full text**: if either dataset is HumanEval, MBPP or APPS, it is in.

### Distinguishing AI- and Human-Generated Code: A Case Study
- **Authors**: Sufiyan Bukhari, Benjamin Tan, Lorenzo De Carli
- **Year / first public**: 2023-11 (S2: 2023-11-26)
- **Venue**: SCORED '23 workshop at ACM CCS (DOI 10.1145/3605770.3625215)
- **URL**: https://doi.org/10.1145/3605770.3625215. ACM returned 403, so the paper was verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3605770.3625215
- **Access**: open (S2 flags it open access; agent read the abstract only)
- **Setting**: not determinable. The abstract says the evaluation is "on a standardized task" without naming it.
- **Method family**: stylometry/AST (lexical and syntactic features)
- **Dataset**: not named in the abstract.
- **Headline result**: accuracy up to 92%.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: exclude (provisional). In date, since 2023-11 is inside the window, but Setting cannot be judged. **Re-screen on full text.**

### Hiding in Plain Sight: On the Robustness of AI-Generated Code Detection
- **Authors**: Saman Pordanesh, Sufiyan Bukhari, Benjamin Tan, Lorenzo De Carli
- **Year / first public**: 2025-04. The OSF preprint (osf.io/jahxs) is dated 2025-04-29 in OpenAlex, but its page did not render for the agent. The DIMVA 2025 chapter is dated 2025-07-10.
- **Venue**: DIMVA 2025, Springer LNCS (DOI 10.1007/978-3-031-97623-0_3)
- **URL**: https://doi.org/10.1007/978-3-031-97623-0_3. Springer redirected to a login, so identity was read from the Crossref record https://api.crossref.org/works/10.1007/978-3-031-97623-0_3, which has no abstract.
- **Access**: paywalled
- **Setting**: not determinable (no abstract readable)
- **Method family**: robustness study
- **Dataset**: not known.
- **Headline result**: not reported.
- **Limitation**: not assessed (no text).
- **Decision**: exclude (provisional). Nothing beyond the title was readable. This is a slice C topic; **re-screen on full text.**

### EX-CODE: A Robust and Explainable Model to Detect AI-Generated Code
- **Authors**: Luana Bulla, Alessandro Midolo, Misael Mongiovì, Emiliano Tramontana
- **Year / first public**: 2024-12
- **Venue**: Information (MDPI), 15(12), 819 (DOI 10.3390/info15120819)
- **URL**: https://doi.org/10.3390/info15120819. MDPI returned 403, so the paper was verified from the Crossref and S2 records.
- **Access**: open (MDPI open access; agent read the abstract only)
- **Setting**: not determinable ("a heterogeneous real-world dataset")
- **Method family**: trained classifier (token-probability features, explainable)
- **Dataset**: not named in the abstract.
- **Headline result**: not reported in the abstract.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: exclude (provisional). Setting cannot be judged. **Re-screen on full text.**

### Detecting Code from Evolving LLMs: Temporal Drift, Generalization, and Adaptation
- **Authors**: Edwin Dauber
- **Year / first public**: 2026-01
- **Venue**: IEEE CCWC 2026 (DOI 10.1109/CCWC67433.2026.11393797)
- **URL**: https://doi.org/10.1109/ccwc67433.2026.11393797. IEEE returned a bot-check response, so the paper was verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ccwc67433.2026.11393797
- **Access**: paywalled
- **Setting**: not determinable (the abstract does not name the data)
- **Method family**: trained classifier / robustness study (temporal drift across LLM generations)
- **Dataset**: not named.
- **Headline result**: not reported; the abstract states a "generalization gap" without a number.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: exclude (provisional). Setting cannot be judged. **Re-screen on full text.**

### A dataset for human-written and AI-generated code source classification
- **Authors**: Ghizlane Boukili, Said El Garouani, J. Riffi
- **Year / first public**: 2026-01
- **Venue**: Data in Brief (DOI 10.1016/j.dib.2026.112527)
- **URL**: https://doi.org/10.1016/j.dib.2026.112527. The Elsevier landing page returned a redirect stub, so the paper was verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.dib.2026.112527
- **Access**: open (S2 flags it open access; agent read the abstract only)
- **Setting**: not determinable. The motivation is education, but the human samples come "from a public repository" that the abstract does not identify.
- **Method family**: dataset/benchmark
- **Dataset**: 10,000 samples (5,000 human, 5,000 ChatGPT) in Python, Java, C and C++.
- **Headline result**: not reported (dataset paper).
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: exclude (provisional). Setting cannot be judged. **Re-screen on full text.**

### CDUP: Detecting AI Generated Code Using Abstract Syntax Tree Analyst
- **Authors**: Ștefan Păuleț, Alex Moruz
- **Year / first public**: 2025
- **Venue**: Procedia Computer Science (KES 2025), DOI 10.1016/j.procs.2025.09.329
- **URL**: https://doi.org/10.1016/j.procs.2025.09.329. Identity was read from the Crossref and S2 records; neither has an abstract.
- **Access**: open (S2 flags it open access; agent read no abstract)
- **Setting**: not determinable
- **Method family**: stylometry/AST
- **Dataset**: not known.
- **Headline result**: not reported.
- **Limitation**: not assessed (no text).
- **Decision**: exclude (provisional). Nothing beyond the title and authors was readable. **Re-screen on full text.**

### Understanding AI Code Detection: A Feature-Level Analysis of Human, AI-Generated, and Hybrid Python Code
- **Authors**: Alexander Chandra, Benediktus Albert Chandra, Michelle Divine Winata et al.
- **Year / first public**: 2026-08
- **Venue**: ICISS 2026 (IEEE), DOI 10.1109/ICISS71466.2026.11715288
- **URL**: https://doi.org/10.1109/iciss71466.2026.11715288. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/iciss71466.2026.11715288
- **Access**: paywalled
- **Setting**: not determinable (the source of the Python code is not named)
- **Method family**: stylometry/AST + trained classifier (three-class: human, AI, hybrid)
- **Dataset**: not named.
- **Headline result**: the fused SVM reached accuracy and F1 0.79.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: exclude (provisional). Setting cannot be judged. **Re-screen on full text.**

### HybridCodeAuthorship: A Benchmark Dataset for Line-Level Code Authorship Detection
- **Authors**: Luke Patterson, Li Wang, Adam Faulkner
- **Year / first public**: 2026-06
- **Venue**: LREC 2026, pp. 1520–1532; arXiv preprint 2606.12620
- **URL**: https://arxiv.org/abs/2606.12620
- **Access**: open
- **Setting**: out of scope (CodeSearchNet repository files with interleaved human and AI lines)
- **Method family**: dataset/benchmark (mixed authorship)
- **Dataset**: Python files from CodeSearchNet repositories.
- **Headline result**: the best detector (AIGCode Detector) reached F1 0.48 at chunk level and 0.56 at line level.
- **Limitation**: not assessed (excluded).
- **Decision**: exclude. Fails Setting; the authors deliberately move away from "LeetCode-style problems". Relevant to slice C (mixed authorship). Found by forward snowballing.

### Detecting Adversarial Prompted AI-Generated Code on Stack Overflow: A Benchmark Dataset and an Enhanced Detection Approach
- **Authors**: Aman Swaraj, Krishna Agarwal, A. Joshi, Sandeep Kumar
- **Year / first public**: 2025-09
- **Venue**: ICSME 2025 (DOI 10.1109/ICSME64153.2025.00089)
- **URL**: https://doi.org/10.1109/ICSME64153.2025.00089. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ICSME64153.2025.00089
- **Access**: paywalled
- **Setting**: out of scope (Stack Overflow answers)
- **Method family**: dataset/benchmark + robustness study
- **Dataset**: 3,500 Stack Overflow / ChatGPT answer pairs and 4,500 adversarially prompted AI responses.
- **Headline result**: not reported in the abstract.
- **Limitation**: not assessed (excluded).
- **Decision**: exclude. Fails Setting: Q&A snippets, not coding problems. Found by forward snowballing.

### Who Wrote This Code? Investigating Human and AI Programming Patterns
- **Authors**: Nitika, Ramesh Narwal
- **Year / first public**: 2025-11
- **Venue**: ICIIP 2025 (DOI 10.1109/ICIIP68302.2025.11346257)
- **URL**: https://doi.org/10.1109/ICIIP68302.2025.11346257. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ICIIP68302.2025.11346257
- **Access**: paywalled
- **Setting**: not determinable (the abstract names no data)
- **Method family**: empirical study
- **Dataset**: not named.
- **Headline result**: not reported.
- **Limitation**: not assessed (read scope: abstract only).
- **Decision**: exclude (provisional). Setting cannot be judged. **Re-screen on full text.**

### MMAIGCD — Multimodal multilingual AI-generated code detection
- **Authors**: Hamza Boulibya, Laila El Ouedeghyry, Youssef Azami et al.
- **Year / first public**: 2026 (month not confirmed)
- **Venue**: Journal of Systems and Software (DOI 10.1016/j.jss.2026.113038)
- **URL**: https://doi.org/10.1016/j.jss.2026.113038. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.jss.2026.113038, which has no abstract.
- **Access**: paywalled
- **Setting**: not determinable
- **Method family**: trained classifier (from the title)
- **Dataset**: not known.
- **Headline result**: not reported.
- **Limitation**: not assessed (no text).
- **Decision**: exclude (provisional). **Re-screen on full text.** Found by forward snowballing.

### A hybrid approach for machine-generated code detection based on statistical, authorship, and semantic feature extraction
- **Authors**: Marzieh Hajizadeh Tahan
- **Year / first public**: 2026-03
- **Venue**: Information and Software Technology (DOI 10.1016/j.infsof.2026.108102)
- **URL**: https://doi.org/10.1016/j.infsof.2026.108102. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.infsof.2026.108102, which has no abstract.
- **Access**: paywalled
- **Setting**: not determinable
- **Method family**: trained classifier (from the title)
- **Dataset**: not known.
- **Headline result**: not reported.
- **Limitation**: not assessed (no text).
- **Decision**: exclude (provisional). **Re-screen on full text.** Found by forward snowballing.

### The dual-encoder detector for AI-generated go code
- **Authors**: Guozhao Liao, Yang Hou, Lujia Chai et al.
- **Year / first public**: 2026-03
- **Venue**: Journal of King Saud University – Computer and Information Sciences (DOI 10.1007/s44443-026-00626-5)
- **URL**: https://doi.org/10.1007/s44443-026-00626-5. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s44443-026-00626-5
- **Access**: open (S2 flags it open access; agent read the abstract only)
- **Setting**: not determinable (the source of the Go datasets is not named)
- **Method family**: trained classifier (CodeBERT + UniXcoder feature fusion)
- **Dataset**: Go code generated by GPT-3.5-Turbo, CodeLlama-34B, WizardCoder-34B and WizardCoder-15B.
- **Headline result**: average F1 about 7.6% above the strongest baselines.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: exclude (provisional). Setting cannot be judged. **Re-screen on full text.** Found by forward snowballing.

### LiMO: Line-level Machine-generated Code Detection for Diverse Programming Languages
- **Authors**: Taekhyung Kim, Hyejoon Jang, Suyoung Kim et al.
- **Year / first public**: 2026-03
- **Venue**: ACM SAC 2026 (DOI 10.1145/3748522.3779718)
- **URL**: https://doi.org/10.1145/3748522.3779718. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3748522.3779718
- **Access**: open (S2 flags it open access; agent read the abstract only)
- **Setting**: not determinable. The motivation is education, but the source of the human code in the HMGC dataset is not named.
- **Method family**: trained classifier (line-wise perplexity + coding-convention features)
- **Dataset**: HMGC (Human-Machine Generated Codes): GPT-3.5, GPT-4 and Gemini code in Python, Java and C++.
- **Headline result**: "best performance across all evaluation metrics"; the abstract gives no number (not reported).
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: exclude (provisional). Setting cannot be judged. **Re-screen on full text.** Found by forward snowballing.

### A Hybrid Framework for AI-Generated Code Detection with Integrated Developer Support Tools
- **Authors**: Manikandan Parasuraman, Skanda Manjunath Harve, Mebin Rajan Thomas et al.
- **Year / first public**: 2026-04
- **Venue**: TQCEBT 2026 (IEEE), DOI 10.1109/TQCEBT67648.2026.11681507
- **URL**: https://doi.org/10.1109/TQCEBT67648.2026.11681507. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/TQCEBT67648.2026.11681507
- **Access**: paywalled
- **Setting**: not determinable (no evaluation data named)
- **Method family**: stylometry/AST + trained classifier (system description)
- **Dataset**: not named.
- **Headline result**: not reported.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: exclude (provisional). Setting cannot be judged. **Re-screen on full text.** Found by forward snowballing.

### Agentic AI Code Generation vs. Human Authorship: Stylometric Detection in Firmware Written for Arduino Platform
- **Authors**: R. Gunawardhana, T. Wijayasiriwardhane
- **Year / first public**: 2026 (month not confirmed)
- **Venue**: Computers, Materials & Continua (DOI 10.32604/cmc.2026.084610)
- **URL**: https://doi.org/10.32604/cmc.2026.084610. Verified from the S2 record https://api.semanticscholar.org/graph/v1/paper/DOI:10.32604/cmc.2026.084610
- **Access**: open (S2 flags it open access; agent read the abstract only)
- **Setting**: not determinable. The motivation is STEM education, but the abstract does not say the human firmware comes from student assignments.
- **Method family**: stylometry/AST
- **Dataset**: human and LLM Arduino firmware; size not given.
- **Headline result**: accuracy 0.9413.
- **Limitation**: method weaknesses not assessed (read scope: abstract only).
- **Decision**: exclude (provisional). **Re-screen on full text**; if the human data is coursework, this belongs to slice B. Found by forward snowballing.
