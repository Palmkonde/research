# Re-screen of slice A provisional exclusions

14 papers re-screened: 2 include, 0 background, 1 exclude, 11 unresolved (no readable full text). Full text read for 3 (Boukili, Pordanesh, Gunawardhana); the other 11 only have an abstract or metadata.

Search trail for every paper: arXiv API title search (no arXiv version exists for any of the 14), Semantic Scholar (abstract only; its open-access link is the blocked publisher DOI), OpenAlex and Crossref (no repository copy), WebSearch, and the publisher page where the paper is flagged open access. Publisher pages that refused automated access were not worked around.

Leads for the caller: the De Carli lab page (https://ldklab.github.io/publications/) hosts a PDF and data link for Bukhari et al. 2023, "Distinguishing AI- and Human-Generated Code: A Case Study" (https://ldklab.github.io/assets/papers/scored23-aicode.pdf), a still-unresolved provisional exclusion in biblio-a-detectors.md. Dauber's Zenodo dataset (https://zenodo.org/records/17983716) is the only evidence on the Dauber paper's data.

### DualCodeDetect: Zero-Shot LLM-Generated Code Detection via Dual-Channel Perturbation
- **Authors**: Zhengdao Li, Xiuwei Shang, Zhenkan Fu et al.
- **Year / first public**: 2026-06
- **Venue**: Proceedings of the ACM on Software Engineering (DOI 10.1145/3808166)
- **URL**: https://doi.org/10.1145/3808166
- **Access**: paywalled (flagged CC-BY open access, but dl.acm.org returned 403 to WebFetch; abstract only, via Semantic Scholar)
- **Setting**: not determinable; the abstract says "two datasets" without naming them
- **Method family**: zero-shot
- **Dataset**: two unnamed datasets; Python, cross-language Java, C++, JavaScript
- **Headline result**: average AUROC 0.8477 on Python at T=0.2 and T=1.0, FPR 0.0430, FNR 0.0552
- **Limitation**: not reported (full text not read)
- **Decision**: unresolved — needs full text. Sources tried: arXiv API (title and phrase queries, none), Semantic Scholar, OpenAlex, Crossref, ACM page (403), WebSearch (CiteDrive listing repeats the abstract only). Include if either dataset is HumanEval, MBPP or APPS.

### Hiding in Plain Sight: On the Robustness of AI-Generated Code Detection
- **Authors**: Saman Pordanesh, Sufiyan Bukhari, Benjamin Tan, Lorenzo De Carli
- **Year / first public**: 2025-04 (OSF preprint osf.io/jahxs; DIMVA chapter 2025-07)
- **Venue**: DIMVA 2025, Springer LNCS 15748 (DOI 10.1007/978-3-031-97623-0_3)
- **URL**: https://ldklab.github.io/assets/papers/dimva25-aicode.pdf (authors' copy, 20 pages, read in full)
- **Access**: open
- **Setting**: general code on coding-problem data (IBM Project CodeNet, AIZU Online Judge and AtCoder problems with accepted human solutions); the second dataset, CodeSearchNet, is not coding-problem data
- **Method family**: robustness study
- **Dataset**: Project CodeNet (2,984 Python problem/solution pairs) and CodeSearchNet (3,042 pairs). AI solutions from GPT-4o, Gemini 1.5 Flash and Claude 3.5 Sonnet, generated from the same problem statements. Python only.
- **Headline result**: on CodeNet with GPT-4o code, GPTSniffer reaches F1 0.99 (AUC 1.00) and Bukhari et al. F1 0.95, while the zero-shot Ye et al. and DetectCodeGPT reach only F1 0.69 and 0.67 (AUC 0.71 and 0.51); training-based accuracy drops sharply when the training and evaluation problem domains differ.
- **Limitation**: Python only, and only fully human versus fully AI-generated code, no mixed authorship [author-acknowledged].
- **Decision**: include — evaluated on Project CodeNet online-judge problems (the "IBM dataset"); fits the general-detector-on-coding-problem-data clause of the Scope. Also belongs to slice C (robustness).

### EX-CODE: A Robust and Explainable Model to Detect AI-Generated Code
- **Authors**: Luana Bulla, Alessandro Midolo, Misael Mongiovì, Emiliano Tramontana
- **Year / first public**: 2024-12
- **Venue**: Information (MDPI), 15(12), 819 (DOI 10.3390/info15120819)
- **URL**: https://doi.org/10.3390/info15120819
- **Access**: paywalled (MDPI is open access, but www.mdpi.com returned 403 to WebFetch and the PDF link returned an access-denied page; abstract only)
- **Setting**: not determinable; the abstract says "a heterogeneous real-world dataset"
- **Method family**: trained classifier (token-probability features, explainable)
- **Dataset**: not reported
- **Headline result**: not reported
- **Limitation**: not reported (full text not read)
- **Decision**: unresolved — needs full text. Sources tried: arXiv API (none), Semantic Scholar, OpenAlex (lists the MDPI PDF only), Crossref, Europe PMC (no record), the University of Catania repository (a bot-check page), WebSearch (abstract only). Save the MDPI PDF by hand from a browser.

### Detecting Code from Evolving LLMs: Temporal Drift, Generalization, and Adaptation
- **Authors**: Edwin Dauber
- **Year / first public**: 2026-01
- **Venue**: IEEE CCWC 2026 (DOI 10.1109/CCWC67433.2026.11393797)
- **URL**: https://doi.org/10.1109/ccwc67433.2026.11393797
- **Access**: paywalled
- **Setting**: not determinable from the paper; the companion dataset (see Dataset) points to competitive programming
- **Method family**: trained classifier / robustness study (temporal drift across LLM generations)
- **Dataset**: paper's data not reported. The companion Zenodo record (doi 10.5281/zenodo.17983716, MIT licence, 2025-12) holds 5,575 Python samples from 9 LLMs answering 710 Google Code Jam problems; it states it supplements this CCWC paper.
- **Headline result**: not reported; the abstract states a generalization gap without a number
- **Limitation**: not reported (full text not read)
- **Decision**: unresolved — needs full text. Leans include, since Google Code Jam is a programming contest, but this rests on the Zenodo record and not the paper. Sources tried: arXiv API (none), Semantic Scholar (abstract), OpenAlex, WebSearch, Zenodo, IEEE page (closed).

### A dataset for human-written and AI-generated code source classification
- **Authors**: Ghizlane Boukili, Said El Garouani, J. Riffi
- **Year / first public**: 2026-01 (Data in Brief; PMC12907682)
- **Venue**: Data in Brief (DOI 10.1016/j.dib.2026.112527)
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC12907682/ (full text, read in full)
- **Access**: open
- **Setting**: general code on coding-problem data (competitive programming; human code from CodeNet's AIZU Online Judge and AtCoder submissions)
- **Method family**: dataset/benchmark
- **Dataset**: 10,000 samples (5,000 human, 5,000 AI) in Python, Java, C and C++. Human code: accepted CodeNet submissions for 937 problems, up to 2 users per language per task. AI code: ChatGPT-3.5 and GPT-4 (Oct–Dec 2024), prompted from the CodeNet problem statements, plus extra non-competitive tasks (games, OOP, security, ML, finance, data analysis, file handling).
- **Headline result**: baseline classifiers on the dataset: LSTM accuracy 98.37%, AUC 99.42%; XGBoost accuracy 94.55%, AUC 98.63%.
- **Limitation**: single generator family (ChatGPT) and in-distribution baselines only; the AI half includes non-competitive tasks that the human half lacks, which a classifier could exploit [reader-inferred].
- **Decision**: include — human samples are CodeNet online-judge solutions and AI samples answer the same CodeNet problem statements; the dataset is competitive-programming data with education as the stated motivation.

### Understanding AI Code Detection: A Feature-Level Analysis of Human, AI-Generated, and Hybrid Python Code
- **Authors**: Alexander Chandra, Benediktus Albert Chandra, Michelle Divine Winata et al.
- **Year / first public**: 2026-08
- **Venue**: ICISS 2026 (IEEE), DOI 10.1109/ICISS71466.2026.11715288
- **URL**: https://doi.org/10.1109/iciss71466.2026.11715288
- **Access**: paywalled
- **Setting**: not determinable; the abstract names no data source
- **Method family**: stylometry/AST + trained classifier (three-class: human, AI, machine-refined hybrid)
- **Dataset**: not reported
- **Headline result**: fused SVM (stylometric + TF-IDF + CodeBERT) accuracy and F1 both 0.79
- **Limitation**: not reported (full text not read)
- **Decision**: unresolved — needs full text. Sources tried: arXiv API (none), Semantic Scholar (abstract), OpenAlex (closed), Crossref, WebSearch (no match), IEEE page.

### Who Wrote This Code? Investigating Human and AI Programming Patterns
- **Authors**: Nitika, Ramesh Narwal
- **Year / first public**: 2025-11
- **Venue**: ICIIP 2025 (DOI 10.1109/ICIIP68302.2025.11346257)
- **URL**: https://doi.org/10.1109/ICIIP68302.2025.11346257
- **Access**: paywalled
- **Setting**: not determinable; the abstract is general motivation and names no data
- **Method family**: empirical study
- **Dataset**: not reported
- **Headline result**: not reported
- **Limitation**: not reported (full text not read)
- **Decision**: unresolved — needs full text. Sources tried: arXiv API (the only "Who Wrote this Code?" hit is the unrelated watermarking paper 2305.15060), Semantic Scholar (abstract), OpenAlex (closed), Crossref, WebSearch (an library catalogue record (hebis) without author or abstract), IEEE page.

### MMAIGCD — Multimodal multilingual AI-generated code detection
- **Authors**: Hamza Boulibya, Laila El Ouedeghyry, Youssef Azami et al.
- **Year / first public**: 2026 (month not confirmed)
- **Venue**: Journal of Systems and Software (DOI 10.1016/j.jss.2026.113038)
- **URL**: https://doi.org/10.1016/j.jss.2026.113038
- **Access**: paywalled
- **Setting**: not determinable; no abstract on any index
- **Method family**: trained classifier (from the title)
- **Dataset**: not reported
- **Headline result**: not reported
- **Limitation**: not reported (no text)
- **Decision**: unresolved — needs full text. Sources tried: arXiv API (none), Semantic Scholar (no abstract), OpenAlex (closed), Crossref, WebSearch (no match for the title or author).

### A hybrid approach for machine-generated code detection based on statistical, authorship, and semantic feature extraction
- **Authors**: Marzieh Hajizadeh Tahan
- **Year / first public**: 2026-03
- **Venue**: Information and Software Technology (DOI 10.1016/j.infsof.2026.108102)
- **URL**: https://doi.org/10.1016/j.infsof.2026.108102
- **Access**: paywalled
- **Setting**: not determinable; no abstract on any index
- **Method family**: trained classifier (from the title)
- **Dataset**: not reported
- **Headline result**: not reported
- **Limitation**: not reported (no text)
- **Decision**: unresolved — needs full text. Sources tried: arXiv API (none), Semantic Scholar (no abstract), OpenAlex (closed), Crossref, WebSearch.

### The dual-encoder detector for AI-generated go code
- **Authors**: Guozhao Liao, Yang Hou, Lujia Chai et al.
- **Year / first public**: 2026-03
- **Venue**: Journal of King Saud University – Computer and Information Sciences (DOI 10.1007/s44443-026-00626-5)
- **URL**: https://doi.org/10.1007/s44443-026-00626-5
- **Access**: paywalled (flagged CC-BY-NC-ND open access, but Springer redirected to a cookie/login handshake that I did not follow; abstract only)
- **Setting**: not determinable; the abstract does not name the source of the Go human code
- **Method family**: trained classifier (CodeBERT + UniXcoder feature fusion)
- **Dataset**: Go code generated by GPT-3.5-Turbo, CodeLlama-34B, WizardCoder-34B and WizardCoder-15B; human-code source and sizes not reported
- **Headline result**: about 7.6% higher average F1 than the strongest baselines on the three main Go datasets (no absolute number in the abstract)
- **Limitation**: not reported (full text not read)
- **Decision**: unresolved — needs full text. Sources tried: arXiv API (none), Semantic Scholar (abstract), OpenAlex, Springer page and PDF (redirect), WebSearch (no snippet of the data section).

### LiMO: Line-level Machine-generated Code Detection for Diverse Programming Languages
- **Authors**: Taekhyung Kim, Hyejoon Jang, Suyoung Kim et al.
- **Year / first public**: 2026-03
- **Venue**: ACM SAC 2026 (DOI 10.1145/3748522.3779718)
- **URL**: https://doi.org/10.1145/3748522.3779718
- **Access**: paywalled (flagged CC-BY-NC-ND open access, but dl.acm.org blocked automated access; abstract only)
- **Setting**: not determinable; the abstract names education as motivation, but the source of the human code in HMGC is not stated
- **Method family**: trained classifier (line-wise perplexity + coding-convention deviation, e.g. PEP 8)
- **Dataset**: HMGC (Human-Machine Generated Codes), built with GPT-3.5, GPT-4 and Gemini in Python, Java and C++; human source and size not reported
- **Headline result**: "best performance across all evaluation metrics" at document and line level; no number in the abstract
- **Limitation**: not reported (full text not read)
- **Decision**: unresolved — needs full text. Sources tried: arXiv API (the "LiMO" hits are unrelated lidar papers), Semantic Scholar (abstract), OpenAlex, Crossref, ACM page (blocked), WebSearch.

### A Hybrid Framework for AI-Generated Code Detection with Integrated Developer Support Tools
- **Authors**: Manikandan Parasuraman, Skanda Manjunath Harve, Mebin Rajan Thomas et al.
- **Year / first public**: 2026-04
- **Venue**: TQCEBT 2026 (IEEE), DOI 10.1109/TQCEBT67648.2026.11681507
- **URL**: https://doi.org/10.1109/TQCEBT67648.2026.11681507
- **Access**: paywalled
- **Setting**: not determinable; the abstract describes a system (AST + stylometry + transformer embeddings, editor and browser extensions) and names no evaluation data
- **Method family**: stylometry/AST + trained classifier (system description)
- **Dataset**: not reported
- **Headline result**: not reported ("high accuracy" without a number)
- **Limitation**: not reported (full text not read)
- **Decision**: unresolved — needs full text. Leans exclude, since the abstract reads as a tool paper and mentions "scholarly and business applications" only. Sources tried: arXiv API (none), Semantic Scholar (abstract), OpenAlex (closed), Crossref, WebSearch.

### Agentic AI Code Generation vs. Human Authorship: Stylometric Detection in Firmware Written for Arduino Platform
- **Authors**: Rajani Navoda Gunawardhana, Thareendhra Keerthi Wijayasiriwardhane
- **Year / first public**: 2026-10 (received 2026-04, accepted 2026-06, issue published 2026-10-22)
- **Venue**: Computers, Materials & Continua 89(3), 52 (DOI 10.32604/cmc.2026.084610)
- **URL**: https://www.techscience.com/cmc/v89n3/69296/html (full text, read in full)
- **Access**: open
- **Setting**: out of scope — STEM-education motivation, but the data is not student work or coding problems
- **Method family**: stylometry/AST
- **Dataset**: 204 Arduino firmware samples: 102 human-written from 35 public Arduino libraries (committed before 2019) and 102 generated by ChatGPT-4o, Gemini 2.5 Flash and Perplexity AI from the same project descriptions, in five prompt styles
- **Headline result**: XGBoost on lexical + syntactic bigram features reaches accuracy 0.9413 and F1 0.9423
- **Limitation**: no real student submissions, only three LLMs, and no test on edited or hybrid AI code [author-acknowledged]
- **Decision**: exclude — human samples come from published Arduino libraries "rather than authentic student submissions", and no coding-problem data is used; fails Setting.

### Detecting Adversarial Prompted AI-Generated Code on Stack Overflow: A Benchmark Dataset and an Enhanced Detection Approach
- **Authors**: Aman Swaraj, Krishna Agarwal, A. Joshi, Sandeep Kumar
- **Year / first public**: 2025-09
- **Venue**: ICSME 2025 (DOI 10.1109/ICSME64153.2025.00089)
- **URL**: https://doi.org/10.1109/ICSME64153.2025.00089
- **Access**: paywalled
- **Setting**: out of scope per the abstract — Stack Overflow answers; the abstract itself contrasts them with "long code samples from repositories and assignments"
- **Method family**: dataset/benchmark + robustness study
- **Dataset**: 3,500 Stack Overflow / ChatGPT answer pairs and 4,500 adversarially prompted AI responses
- **Headline result**: not reported as a number; existing code models detect standard AI answers but fail on adversarially prompted ones, and a stylometry + embedding ensemble improves detection
- **Limitation**: not reported (full text not read)
- **Decision**: unresolved — needs full text. Leans exclude, since the abstract fixes the data as Stack Overflow Q&A snippets. Sources tried: arXiv API (none), Semantic Scholar (abstract read), OpenAlex (closed), Crossref, WebSearch, IEEE page.
