# Annotations — batch D

### Evaluating Software Plagiarism Detection in the Age of AI: Automated Obfuscation and Lessons for Academic Integrity
**Reference (APA 7):** Sağlam, T., & Schmid, L. (2025). Evaluating software plagiarism detection in the age of AI: Automated obfuscation and lessons for academic integrity. *arXiv preprint* arXiv:2505.20158. https://arxiv.org/abs/2505.20158
**Source note:** [saglam-2025-evaluating-software-plagiarism-detection](../../../machine-learning/llm-generated-code-detection/sources/saglam-2025-evaluating-software-plagiarism-detection.md)
- **Setting:** Education: programming assignments from university courses (Java, C/C++). Not a watermark paper.
- **Method:** Tests whether two defences added to the JPlag similarity detector (Token Sequence Normalization, Subsequence Match Merging, and both) resist algorithmic and GPT-4 obfuscation, and separate GPT-4-generated from human programs by mutual similarity (§4, §5.5).
- **Data:** Real student code: six datasets of 18 to 626 programs (Table 1); over 4.1 million pairwise comparisons (§4); GPT-4 (version not given), 15 obfuscation prompts (§4.4); 50 GPT-4 programs for each of PROGpedia-19, PROGpedia-56 and TicTacToe (Table 2).
- **Headline result:** Median similarity gap, GPT-4 pairs vs human pairs, JPlag baseline vs Subsequence Match Merging: 15.04 vs 23.58 (PROGpedia-19), 33.13 vs 34.47 (PROGpedia-56), 14.57 vs 21.10 points (TicTacToe) (Table 10).
- **Limitation:** The signal exists only if several students submit output from the same model, and full generation works only below 300 to 400 lines [author-acknowledged, §5.5, §7].
- **Relation:** Calls current AI-code detectors unreliable, citing Pan et al. (2024) and Suh et al. (2025, reported to beat GPTSniffer), and names watermarking as open research (§7.3.3, §8.4).
- **Note:** Text gives 787 plagiarised programs (§4.4); the Table 2 caption gives 851.

### Disappearing Ink: Obfuscation Breaks N-gram Code Watermarks in Theory and Practice
**Reference (APA 7):** Zhang, G., Li, M., Bagdasarian, E., Ma, S., & Zhai, J. (2025). Disappearing ink: Obfuscation breaks N-gram code watermarks in theory and practice. *arXiv preprint* arXiv:2507.05512. https://arxiv.org/abs/2507.05512
**Source note:** [zhang-2025-disappearing-ink-obfuscation-breaks](../../../machine-learning/llm-generated-code-detection/sources/zhang-2025-disappearing-ink-obfuscation-breaks.md)
- **Setting:** General code on coding-problem data: function-level benchmarks.
- **Method:** Models obfuscation as a Markov random walk and proves that, assuming "distribution consistency", an N-gram watermark detector fails with rate approaching 1 − ϵpos (Theorems 3.3, 3.4); tests it with off-the-shelf obfuscators.
- **Data:** SWEET, WLLM, SynthID; LLaMA-3.1-8B-Instruct, DeepSeek-Coder-33B-Base; HumanEval, MBPP+, HumanEval-X-JS, MBPP-JS; four obfuscators (§4.1); 50 SWE-bench Verified tasks (App. M). Per-benchmark counts not reported. Student/contest code: no, only HumanEval/MBPP-family.
- **Headline result:** Post-obfuscation AUROC clusters near 0.5; only 9 of 1,280 obfuscated data points fall outside (0.4, 0.6) (§4.2). Distribution consistency holds in 1,557 of 1,620 spaces, 96.11% (Table 1).
- **Limitation:** Covers only N-gram-based schemes, and scores code quality only by test passing [author-acknowledged, Limitations].
- **Relation:** SWEET is one of the three attacked schemes (§4.1); App. O reports the ACW-s variant of Guo and Cheng (2025) falling to AUROC 52.92% under Python-Minifier.
- **Note:** Read v2 (PDF; its HTML is unavailable), five authors. v1 has four authors and reports the consistency test as 98.10% on 158 segments (§1, §6.4).

### Is The Watermarking Of LLM-Generated Code Robust?
**Reference (APA 7):** Suresh, T., Ugare, S., Singh, G., & Misailovic, S. (2024). Is the watermarking of LLM-generated code robust? *arXiv preprint* arXiv:2403.17983. https://arxiv.org/abs/2403.17983
**Source note:** [suresh-2024-watermarking-llm-generated-code](../../../machine-learning/llm-generated-code-detection/sources/suresh-2024-watermarking-llm-generated-code.md)
- **Setting:** General code on coding-problem data: HumanEval completions.
- **Method:** An AST-walking algorithm applies d = 5 random semantics-preserving edits (AddDeadCode, InsertPrint, Rename, WrapTryCatch, Mixed) to watermarked Python and measures the drop in detection (§2.2, §3).
- **Data:** LLaMA-7B, CodeLlama-7B on HumanEval; UMD and Unigram watermarks (γ = 0.25); 3 completions pooled, z > 3; mean of 3 runs (§3.3, §4.1). Problem count not reported. Student/contest code: no, only HumanEval.
- **Headline result:** LLaMA-7B TPR falls from 0.79 to 0.22 (UMD, WrapTryCatch) and 0.76 to 0.01 (Unigram, AddDeadCode) (Table 2); CodeLlama-7B 0.82 to 0.28 and 0.72 to 0.03 (Table 3).
- **Limitation:** Python only, two 7B models, two text-derived watermarks; no code-specific scheme is tested [reader-inferred].
- **Relation:** Describes DetectGPT as needing white-box access and costly perturbations, and SWEET as needing regeneration at detection (§5); tests neither.
- **Note:** PDF header reads "ICLR 2024"; the text names no track, so the Source note's "Tiny Papers" is unverified.

### Efficient and Universal Watermarking for LLM-Generated Code Detection
**Reference (APA 7):** Li, B., Fu, Z., Zhang, M., Zhang, P., Sun, J., & Wang, X. (2026). Efficient and universal watermarking for LLM-generated code detection. *IEEE Transactions on Software Engineering*. https://doi.org/10.1109/TSE.2026.3710556
**Source note:** [li-2024-efficient-universal-watermarking-llm](../../../machine-learning/llm-generated-code-detection/sources/li-2024-efficient-universal-watermarking-llm.md)
- **Setting:** General code on coding-problem data: MBPP, APPS, HumanEval+ prompts and SRDD projects; students named as motivation (§I).
- **Method:** ACW post-processes LLM output with 46 idempotent semantics-preserving transformations (§IV-A); detection checks whether they were applied. No model access needed.
- **Data:** GPT-4, GPT-4o, Qwen2.5-Coder-14B-FP16; 974 MBPP, 3,035 APPS, 164 HumanEval+ outputs per LLM, 500 SRDD projects (7,465 functions) per GPT-4 and GPT-4o; human negatives are the benchmarks' own solutions and CodeSearchNet (§IV-A). Student code: no. APPS (listed in this review's scope as coding-problem data) is the only contest-style set in the batch; the paper does not describe its provenance.
- **Headline result:** ACC 97.25 to 100%, TPR 94.51 to 100%, FPR at most 0.17% on all sets; APPS-Qwen: ACW ACC 98.15, TPR 96.47, FPR 0.17 vs SWEET 71.20, 47.80, 5.40 (Table II).
- **Limitation:** The 46 transformations are shown only for Python [author-acknowledged, §VII].
- **Relation:** Table II compares against SWEET and STONE (Kim et al., this batch), WLLM and WaterMax; baselines run on Qwen only.
- **Note:** Venue and DOI come from the arXiv record (v5); volume and pages not reported.

### Practical and Effective Code Watermarking for Large Language Models
**Reference (APA 7):** Guo, Z., & Cheng, M. (2025). Practical and effective code watermarking for large language models. In *Advances in Neural Information Processing Systems* (Vol. 38). https://doi.org/10.52202/085713-2485
**Source note:** [guo-2025-practical-effective-code-watermarking](../../../machine-learning/llm-generated-code-detection/sources/guo-2025-practical-effective-code-watermarking.md)
- **Setting:** General code on coding-problem data: HumanEval, MBPP, HumanEvalPack.
- **Method:** ACW (AST-guided Code Watermarking) trains a Watermark Partitioning Network on AST-derived substitutable positions; detection needs only the code, not the LLM or prompt (§4).
- **Data:** OpenCoder-1.5B-Instruct (main), DeepSeek-Coder-1.3B-instruct (App. F.1), OpenCoder-8B-Instruct (Table 3); HumanEval, MBPP (Python); HumanEvalPack Java, C++, JavaScript (Table 2). Counts not reported. Student/contest code: no, only HumanEval/MBPP-family.
- **Headline result:** AUROC / TPR@5%FPR 84.43 / 45.12 (HumanEval) and 81.18 / 44.20 (MBPP) vs WLLM 70.17 / 20.73 and 76.44 / 27.80; DetectGPT 51.12 and 46.15 AUROC (Table 1).
- **Limitation:** Weaker for languages with complex type systems, and vulnerable to sophisticated code-transformation attacks [author-acknowledged, App. I].
- **Relation:** Runs SWEET as an oracle reference (AUROC 83.10, HumanEval) and DetectGPT as a post-hoc baseline (Table 1).
- **Note:** Not the "ACW" of Li et al. (above); Guo and Cheng cite that work only as a format-altering method (§2).

### Marking Code Without Breaking It: Code Watermarking for Detecting LLM-Generated Code
**Reference (APA 7):** Kim, J., Park, S., & Han, Y.-S. (2026). Marking code without breaking it: Code watermarking for detecting LLM-generated code. In *Findings of the Association for Computational Linguistics: EACL 2026*. https://arxiv.org/abs/2502.18851
**Source note:** [kim-2025-marking-code-without-breaking](../../../machine-learning/llm-generated-code-detection/sources/kim-2025-marking-code-without-breaking.md)
- **Setting:** General code on coding-problem data: MBPP+, HumanEval+, HumanEvalPack.
- **Method:** STONE watermarks only non-syntactic tokens, keeping keywords and delimiters intact; the STEM score merges correctness, detectability and imperceptibility (§3).
- **Data:** Qwen2.5-Coder-7B (Llama-3.1-8B in App. B); MBPP+ 399 problems, HumanEval+ 164, HumanEvalPack C++ 164 and Java 164 (Table 1); baselines KGW, EWD, SWEET (§4). Student/contest code: no, only HumanEval/MBPP-family.
- **Headline result:** STONE vs SWEET on MBPP+: pass@1 0.571 vs 0.502, AUROC 0.982 vs 0.867, STEM 0.848 vs 0.787; HumanEval+ AUROC 0.777 vs 0.710 (Table 2).
- **Limitation:** Capacity drops on code with few non-syntactic tokens (obfuscated scripts, code golf), and an algorithm-aware attacker could rename all variables and strip comments [author-acknowledged, Limitations].
- **Relation:** Extends SWEET and tests both against refactoring and GPT-4o paraphrase attacks on HumanEval+ (§6.2, Figure 4); criticises Li et al. (above) for unnatural code but does not run it (§7).
- **Note:** Venue taken from the arXiv comment ("Findings of EACL 2026"); pages not reported.

### CODE ACROSTIC: Robust Watermarking for Code Generation
**Reference (APA 7):** Lin, L., Xin, S., Cao, Y., & Cao, X. (2025). Code Acrostic: Robust watermarking for code generation. *arXiv preprint* arXiv:2512.14753. https://arxiv.org/abs/2512.14753
**Source note:** [lin-2025-code-acrostic-robust-watermarking](../../../machine-learning/llm-generated-code-detection/sources/lin-2025-code-acrostic-robust-watermarking.md)
- **Setting:** General code on coding-problem data: HumanEval (homework programming cited as motivation, §1).
- **Method:** Builds a secret Cue List from 1-gram statistics of a third-party corpus; watermark tokens are injected and detected only after cue tokens, to survive comment removal (§4).
- **Data:** HumanEval, 164 problems; DeepSeek-Coder-1.3b via MarkLLM; baselines KGW, SWEET, EWD (§5.1). Student/contest code: no, only HumanEval.
- **Headline result:** AUROC 0.772 vs KGW 0.685, SWEET 0.692, EWD 0.750; Pass@1 51.20 vs 53.05 unwatermarked (Table 1). Comments excluded from detection: TPR 34.76 vs EWD 20.73, KGW 17.07, SWEET 16.46 (Table 2a).
- **Limitation:** One benchmark and one 1.3B model; with comments included SWEET (87.20) and EWD (87.19) beat it (85.37) (Table 2a) [reader-inferred].
- **Relation:** Cites Suresh et al. (this batch) for the fragility of code watermarks (§2.2) and benchmarks against SWEET; lists Li et al. and Kim et al. only as related work.
- **Note:** The paper names no venue; the Source note's "WISE 2025" comes from OpenAlex and Semantic Scholar, so it is cited here as arXiv preprint.

### Watermarking Low-entropy Generation for Large Language Models: An Unbiased and Low-risk Method
**Reference (APA 7):** Mao, M., Wei, D., Chen, Z., Fang, X., & Chau, M. (2024). Watermarking low-entropy generation for large language models: An unbiased and low-risk method. *arXiv preprint* arXiv:2405.14604. https://arxiv.org/abs/2405.14604
**Source note:** [mao-2024-watermarking-low-entropy-generation](../../../machine-learning/llm-generated-code-detection/sources/mao-2024-watermarking-low-entropy-generation.md)
- **Setting:** General code on coding-problem data: HumanEval, used as the low-entropy test beside C4 text.
- **Method:** STA-1 (Sampling One Then Accepting) is an unbiased watermark with lower risk of bad output in low-entropy steps; STA-M samples more at high-entropy steps to add strength (§3).
- **Data:** HumanEval, 164 Python problems, CodeLLaMA-7B-Instruct; C4 with LLaMA-2-7B (at least 500 sequences); baselines KGW, RDW, Dipmark, γ-reweight; z thresholds 2 and 2.5; 10 runs (§4.1, App. F.1). Student/contest code: no, only HumanEval.
- **Headline result:** HumanEval, z = 2.0: STA-1 AUC 0.677, F1 0.526 (γ-reweight 0.671, 0.522; KGW δ=2 0.775, 0.737) (Table 3).
- **Limitation:** Attacks (copy-paste, GPT-3.5 paraphrase, DIPPER) are run on C4 only, and paraphrase robustness in low-entropy settings is left open [author-acknowledged, §7].
- **Relation:** Table 1 lists Lee et al. (2023, "Who wrote this code?", the SWEET paper) among earlier methods but does not run it.
- **Note:** The paper calls itself a "Preprint"; no venue is given.
