# Detecting LLM-Generated Code in Programming Education and Competitive Programming: A Scoping Review

*Draft of 2026-10-28. Sections 2 and 3 are assembled from the search records in [scan/](scan/); sections 1, 4 and 5 are first drafts to be checked against the papers.*

## 1. Introduction

Large language models now write working solutions to programming exercises, which leaves instructors and contest organisers unable to assume that a submission is its author's own work. Educators' academic-integrity concerns motivate much of the work reviewed here: Wang et al. (2023) test whether instructors, MOSS, JPlag and GPTZero can tell ChatGPT 3.5 code from student code in CS1 and CS2 courses, and Idialu et al. (2024) frame their study of CodeChef solutions around the same concern. This review maps what 89 papers published between November 2023 and October 2026 show about detecting LLM-generated code in coding problems, covering zero-shot detectors, trained classifiers, stylometric methods, watermarking and robustness studies. Section 2 describes the search, section 3 annotates 36 core papers and tabulates 53 more, and section 4 draws the methods, data and robustness evidence together and lists the gaps.

## 2. Scope and search method

**Form.** This is a scoping review: it maps what has been studied on a topic, the main approaches and the gaps, and does not weigh effects across studies. No protocol was registered, and the PRISMA-ScR checklist was followed informally.

**Question.** What methods exist for telling LLM-written code from human-written code in coding problems, in programming education and in competitive programming, and what do they leave open?

**Inclusion.** A paper is in when all of these hold ([README](README.md#scope)):
- its first public version appeared between November 2023 and October 2026 (arXiv preprints count and are labelled as preprints); older foundational papers are cited for background only;
- its setting is programming education (assignments, exams, academic integrity) or competitive programming (online judges, contests), or it is a general-code detector evaluated on coding-problem data such as APPS, CodeNet, LeetCode, Codeforces, or HumanEval- and MBPP-style problem sets;
- its method is a zero-shot statistical detector, a trained classifier, a stylometric or AST-feature method, generation-time watermarking, or a robustness study.

**Search.** Three slices ran in parallel on 2026-10-28: detectors, education and contests, and watermarks and robustness. Each combined setting terms (code, programming assignment, competitive programming, LeetCode, Codeforces) with task terms (AI-generated, LLM-generated, ChatGPT, detection, authorship, watermark) on arXiv, Semantic Scholar, OpenAlex, Crossref, the ACL Anthology and web search as a stand-in for Google Scholar, followed by backward and forward citation snowballing from every included paper. A paper entered the record only after its page was opened and the title, authors and date matched. The exact queries are in the slice files: [detectors](scan/biblio-a-detectors.md), [education and contests](scan/biblio-b-education-contests.md), [watermarks and robustness](scan/biblio-c-watermark-robustness.md); the protocol is in [scan/search-protocol.md](scan/search-protocol.md).

**Selection.** The three slices recorded 193 entries, which came to 160 distinct papers after duplicates were merged: 89 included, 26 kept as background and 45 excluded ([merged table](scan/merged-candidates.md)). A full-text re-screen of 14 provisional exclusions moved two to inclusion and one to exclusion; 11 stay provisionally excluded for lack of a readable copy ([re-screen](scan/rescreen-a.md)). Of the 89 included papers, 36 are annotated in full in section 3 and 53 appear in a table. All Source notes passed a citation check against Crossref, arXiv and the ACL Anthology ([report](scan/citation-check-report.md)).

**Core selection.** The 36 annotated papers were chosen from the open-access included papers by three rules: full text readable, a direct fit with the scope or a benchmark other papers build on, and coverage of every theme so that no theme is represented only by its largest group.

**Limitations of the search.**
- DBLP and direct Google Scholar fetches were blocked, and ACM Digital Library and IEEE Xplore could not be searched directly; their papers came in through other indexes. Semantic Scholar's search was rate-limited, so OpenAlex and arXiv search pages were used in its place.
- About 21 SemEval-2026 Task 13 system-description papers were not screened; the task overview and six system papers are included.
- Eleven provisional exclusions and 17 leads have no screening decision or no readable copy, and some included papers are paywalled; they are listed in [no-access.md](../../machine-learning/llm-generated-code-detection/sources/no-access.md). Claims that depend on them would be marked *(pending source)*.
- Screening and annotation were carried out by AI agents (Claude models) under the author's direction. The scope, the core selection and the decisions on borderline papers are the author's.

## 3. Annotated bibliography

Each entry gives the paper's setting, method, data, headline result and limitation, with every number taken from the paper and located in a table or section. A limitation is marked *author-acknowledged* when the authors state it and *reader-inferred* when the review infers it.

### 3.1 Benchmarks, datasets and empirical studies

#### SemEval-2026 Task 13: Detecting Machine-Generated Code with Multiple Programming Languages, Generators, and Application Scenarios
**Reference (APA 7):** Orel, D., Azizov, D., Paul, I., Wang, Y., Gurevych, I., & Nakov, P. (2026b). SemEval-2026 task 13: Detecting machine-generated code with multiple programming languages, generators, and application scenarios. In *Proceedings of the 20th International Workshop on Semantic Evaluation (SemEval-2026)* (pp. 3640–3658). Association for Computational Linguistics. https://doi.org/10.18653/v1/2026.semeval-1.445
**Source note:** [orel-2026-semeval-2026-task-13](../../machine-learning/llm-generated-code-detection/sources/orel-2026-semeval-2026-task-13.md)
- **Setting:** general code on coding-problem data. Training is algorithmic code (CodeNet, TACO, LeetCode, CodeForces); the test adds research and generic deployed code (§2–3).
- **Method:** Shared-task overview with three subtasks: A binary human vs machine, B generator-family attribution, C human / AI / hybrid / adversarial (§2).
- **Data:** Subtask A: train 238,475 human + 261,525 AI (Python, Java, C++); test 390,054 human + 109,946 AI (Table 1). B: 45 generators (§2). C: 78 AI generators (Table 3). Teams: 81, 34 and 32 (§4).
- **Headline result:** Top macro-F1 was 0.99708 in A (runner-up 0.82409, baseline 0.30530; Table 4), 0.50819 in B (Table 5) and 0.78546 in C (Table 6). Domain shift hurt more than language shift (§6.1).
- **Limitation:** AST-depth, line-length and size filters remove verbose, complex or very short code common in real repositories [author-acknowledged, §8].
- **Relation:** Builds on Droid for data and on CoDet-M4 for Subtask B (§2–3); releases an enlarged version of the data as AICD Bench (§9).

#### AIGCodeSet: A New Annotated Dataset for AI Generated Code Detection
**Reference (APA 7):** Demirok, B., & Kutlu, M. (2025). AIGCodeSet: A new annotated dataset for AI generated code detection. In *2025 33rd Signal Processing and Communications Applications Conference (SIU)* (pp. 1–4). IEEE. https://doi.org/10.1109/SIU66497.2025.11112334
**Source note:** [demirok-2024-aigcodeset-new-annotated-dataset](../../machine-learning/llm-generated-code-detection/sources/demirok-2024-aigcodeset-new-annotated-dataset.md)
- **Setting:** general code on coding-problem data: 317 problems from CodeNet's 800-problem "Python Benchmark" (§3.1).
- **Method:** Builds a Python dataset in which LLMs write code from scratch, fix runtime errors or correct wrong answers, then tests Ada-embedding, TF-IDF and Bayes baselines (§3.2, §4.1).
- **Data:** 4,755 human files; 2,853 generated, 2,828 after filtering; CodeLlama 34B, Codestral 22B, Gemini 1.5 Flash; random 80/20 split (§3.1–3.3, §4.1).
- **Headline result:** Bayes classifier: F1 0.63, accuracy 0.63, precision 0.52, recall 0.81 (Table 3). Its recall is 0.985 on from-scratch code but 0.677 on fixed runtime errors and 0.769 on corrected outputs (Table 5).
- **Limitation:** Python only, three mid-size generators, and a random sample split not stated to keep a problem's files on one side [reader-inferred].
- **Relation:** Cites Suh et al. (2024) as prior Java work (§2) and reuses the Bayes classifier of Oedingen et al. (§4.1).
- Note: The arXiv text (v3) states no venue; SIU 2025 and the DOI come from Crossref. MultiAIGCD §2 gives this paper's generated count as 2,282; the paper itself says 2,828 (§3.3).

#### CoDet-M4: Detecting Machine-Generated Code in Multi-Lingual, Multi-Generator and Multi-Domain Settings
**Reference (APA 7):** Orel, D., Azizov, D., & Nakov, P. (2025). CoDet-M4: Detecting machine-generated code in multi-lingual, multi-generator and multi-domain settings. In *Findings of the Association for Computational Linguistics: ACL 2025* (pp. 10570–10593). Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.findings-acl.550
**Source note:** [orel-2025-codet-m4-detecting-machine](../../machine-learning/llm-generated-code-detection/sources/orel-2025-codet-m4-detecting-machine.md)
- **Setting:** general code on coding-problem data: LeetCode and CodeForces solutions, plus GitHub code (§3.1).
- **Method:** Builds a large human/LLM corpus, trains SVM, CatBoost and CodeBERT / CodeT5 / UniXcoder detectors, and tests unseen generators, domains, languages and hybrid code (§4).
- **Data:** 499,467 snippets (252,886 human, 246,581 LLM), Python, Java, C++ (Table 1). Generators: CodeLlama 7B, Llama3.1 8B, CodeQwen 1.5 7B, Nxcode-orpo 7B, GPT-4o (§3.2).
- **Headline result:** In distribution, UniXcoder reaches F1 98.65 against 62.03 for the Fast-DetectGPT baseline (Table 2). On unseen domains the best F1 is 58.22 (CodeT5, Table 9); on hybrid code UniXcoder gets F1 39.36 (Table 13).
- **Limitation:** Only three languages, mostly function- and class-level code, and a narrow set of prompts [author-acknowledged, §Limitations].
- **Relation:** Uses Fast-DetectGPT as its zero-shot baseline (§4.1) and reviews GPTSniffer as limited to function-level Python and Java detection (§2).

#### Droid: A Resource Suite for AI-Generated Code Detection
**Reference (APA 7):** Orel, D., Paul, I., Gurevych, I., & Nakov, P. (2025). Droid: A resource suite for AI-generated code detection. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing* (pp. 31263–31289). Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.emnlp-main.1593
**Source note:** [orel-2025-droid-resource-suite-ai](../../machine-learning/llm-generated-code-detection/sources/orel-2025-droid-resource-suite-ai.md)
- **Setting:** general code on coding-problem data: algorithmic solutions from TACO, CodeNet (AtCoder, AIZU), LeetCode and CodeForces, plus GitHub and research code (§3.1).
- **Method:** Builds DroidCollection (human, AI, machine-refined and adversarially humanised code) and trains DroidDetect, ModernBERT encoders of 149M and 396M parameters (§1, §5).
- **Data:** 1.06M samples (Table 1); 43 models, 11 families, 7 languages, 3 domains (§1); 157K preference pairs for adversarial data (§3.4).
- **Headline result:** Average weighted F1: DroidDetectCLS-Large 97.00 (2-class) and 88.78 (3-class), against 67.85 and 64.54 for Fast-DetectGPT (Table 3). Adversarial recall: GPT-Zero 0.10, DroidDetectCLS-Base 0.92 (Table 5).
- **Limitation:** Most training samples come from locally deployable models; reasoning models such as Claude 3.7 and DeepSeek R1 are left out for cost [author-acknowledged, §Limitations].
- **Relation:** Extends CoDet-M4 (§2.2) and scores GPTSniffer (2-class average 41.07) and Fast-DetectGPT as zero-shot baselines (§4.1, Table 3).

#### AICD Bench: A Challenging Benchmark for AI-Generated Code Detection
**Reference (APA 7):** Orel, D., Azizov, D., Paul, I., Wang, Y., Gurevych, I., & Nakov, P. (2026a). AICD Bench: A challenging benchmark for AI-generated code detection. In *Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)* (pp. 6913–6938). Association for Computational Linguistics. https://doi.org/10.18653/v1/2026.eacl-long.325
**Source note:** [orel-2026-aicd-bench-challenging-benchmark](../../machine-learning/llm-generated-code-detection/sources/orel-2026-aicd-bench-challenging-benchmark.md)
- **Setting:** general code on coding-problem data: Droid's algorithmic, general and research domains, extended with CodeNet, StarCoderData and The Vault generations (§4).
- **Method:** Benchmark with three tasks (robust binary, model-family attribution, four-way fine-grained), scored with classical, encoder, Fast-DetectGPT and zero-shot LLM baselines (§5).
- **Data:** 2.05M samples, 77 generators, 9 languages, 11 families (Table 2); adds 500K new generations, 50K human samples (The Heap) and 100K hybrid samples (SwallowCode) to Droid (§4).
- **Headline result:** Task 1 macro-F1: best trained model SVM with TF-IDF 43.05, below the random baseline 45.73 and Fast-DetectGPT 44.99; Task 3 best is ModernBERT 61.65 (Table 4). Averaged over detectors, 0.63 on a seen domain and language but 0.20 on an unseen domain (Table 5).
- **Limitation:** It inherits DroidCollection's distribution, so Droid generators cannot be evaluated on it [author-acknowledged, §Limitations].
- **Relation:** Builds on Droid (§4), says CoDet-M4 and Droid lack standardized tasks and splits (§2.2), and uses Fast-DetectGPT as a faster DetectGPT (§5.1).

#### An Empirical Study on Automatically Detecting AI-Generated Source Code: How Far Are We?
**Reference (APA 7):** Suh, H., Tafreshipour, M., Li, J., Bhattiprolu, A., & Ahmed, I. (2025). An empirical study on automatically detecting AI-generated source code: How far are we? In *2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)* (pp. 859–871). IEEE. https://doi.org/10.1109/ICSE55347.2025.00064
**Source note:** [suh-2024-empirical-study-automatically-detecting](../../machine-learning/llm-generated-code-detection/sources/suh-2024-empirical-study-automatically-detecting.md)
- **Setting:** general code on coding-problem data: MBPP and HumanEval-X problems, plus CodeSearchNet GitHub code (§III-A).
- **Method:** Tests five text detectors and GPTSniffer on AI code, then builds fine-tuned GPT-3.5, static-metric classifiers and CodeT5+ embedding classifiers (§III).
- **Data:** MBPP 974 problems; HumanEval-X 820 samples; CodeSearchNet 400 per language; Python, Java, C++. Generators: ChatGPT, Gemini Pro, GPT-4, Starcoder2-Instruct 15B (Tables I–II).
- **Headline result:** Text detectors have mean accuracy 47.83–50.83 (Table IV); GPTSniffer averages accuracy 57.24 and average F1 45.01 (Table V). The best model (AST embeddings) scores average F1 82.55 within dataset but 43.21 across datasets (Tables VI–VII).
- **Limitation:** Findings may hold only for the selected datasets and LLMs [author-acknowledged, §VI].
- **Relation:** Runs DetectGPT (accuracy 48.99, average F1 37.42) and GPTSniffer as baselines (Tables IV–V).
- Note: Venue, pages and DOI come from Crossref; the arXiv v1 text states none. §VI says three LLMs where four are used.

#### MultiAIGCD: A Comprehensive Dataset for AI Generated Code Detection Covering Multiple Languages, Models, Prompts, and Scenarios
**Reference (APA 7):** Demirok, B., Kutlu, M., & Mergen, S. (2026). MultiAIGCD: A comprehensive dataset for AI generated code detection covering multiple languages, models, prompts, and scenarios. *Neural Computing and Applications, 38*(16), Article 687. https://doi.org/10.1007/s00521-026-12336-0
**Source note:** [demirok-2025-multiaigcd-comprehensive-dataset-ai](../../machine-learning/llm-generated-code-detection/sources/demirok-2025-multiaigcd-comprehensive-dataset-ai.md)
- **Setting:** general code on coding-problem data: 800 CodeNet problems with human submissions (§3.1).
- **Method:** Builds a dataset where six LLMs write, fix or correct code, then tests SVMs on Ada and CodeT5+ embeddings and a fine-tuned CodeBERTa, including leave-one-LLM-out and cross-language runs (§5).
- **Data:** 32,148 human and 121,271 AI snippets (Table 2); Python, Java, Go; Llama-3.3-70B, Qwen2.5-Coder-32B, GPT-4o, o3-mini, Claude 3.5 Sonnet v2, DeepSeek-V3; three prompts (§3.2).
- **Headline result:** Java CodeBERTa F1 is 0.9815 on from-scratch code but 0.8071 on runtime fixes and 0.8048 on output corrections (Table 3). With Go held out, F1 is 0.3085 (SVM Ada), 0.1206 (SVM T5+) and 0.0712 (CodeBERTa) (Table 8).
- **Limitation:** Only three detectors and a limited prompt set were tested [author-acknowledged, §6].
- **Relation:** Extends AIGCodeSet, which it calls closest in scope but Python-only (§2), and lists Suh et al. in Table 1.
- Note: Numbers are from the arXiv v1 text; journal details come from the Springer record, and the published version may differ.

#### Code Detectors Have a Half-Life: Obsolescence and Metric Illusions in LLM-Generated Code Detection
**Reference (APA 7):** Djire, A. E. (2026). Code detectors have a half-life: Obsolescence and metric illusions in LLM-generated code detection. In *Proceedings of the 41st IEEE/ACM International Conference on Automated Software Engineering (ASE '26)*. ACM. https://doi.org/10.1145/3832783.3844566
**Source note:** [djire-2026-code-detectors-have-half](../../machine-learning/llm-generated-code-detection/sources/djire-2026-code-detectors-have-half.md)
- **Setting:** general code on coding-problem data: 18 problems from the AI-Human-Generated-Program-Code dataset (§3).
- **Method:** Compares eight LLM judges under four prompting strategies with three dedicated detectors, reporting accuracy and F1 per generator (§3–4).
- **Data:** 18 human and 126 AI snippets from seven generators (StarCoder, ChatGPT, Bing AI Chat, Code Llama, CodeWhisperer, GitHub Copilot, InstructCodeT5+); C++, Python, Java; judges at temperature 0.1 (§3).
- **Headline result:** DetectCodeGPT and GPT-Sniffer score accuracy 0.50 and F1 0.00 on every generator (Table 1, Finding 1). GPT-5-mini zero-shot reaches F1 0.75–0.95, but lexico-semantic prompting drops it to 0.25–0.40 (Table 1, Finding 2).
- **Limitation:** Only 18 problems and 18 human snippets, reused for every generator, with no confidence intervals [reader-inferred].
- **Relation:** Evaluates the anchors DetectCodeGPT and GPT-Sniffer (Table 1) and contrasts itself with the single-prompt LLM-judge study of Pan et al. (§2).
- Note: Reference [12] credits DetectCodeGPT to Xu and Sheng (2024); check this matches the anchor paper. Resolved: DetectCodeGPT is Shi et al.'s method ([Source note](../../machine-learning/llm-generated-code-detection/sources/shi-2024-between-lines-code-unraveling.md)); Xu and Sheng (2024) is a separate perplexity paper. In the review, cite Shi et al. for DetectCodeGPT and say this paper's reference list credits it to Xu and Sheng. The paper has 3 pages and no page range.

#### iJudge: A style-controlled educational dataset for evaluating human–LLM code authorship detection under distribution shift
**Reference (APA 7):** Chuon, C., Leechat, P., & Vittayakorn, S. (2026). iJudge: A style-controlled educational dataset for evaluating human–LLM code authorship detection under distribution shift. *Information and Software Technology*, Article 108364. https://doi.org/10.1016/j.infsof.2026.108364
**Source note:** [chuon-2026-ijudge-style-controlled-educational](../../machine-learning/llm-generated-code-detection/sources/chuon-2026-ijudge-style-controlled-educational.md)
- **Setting:** education: student Python submissions from KMITL's internal online judge (in use since 2014, about 250–260 students a year), problems from the 2014–2020 academic years; the specific courses are not named (§3.3, §4.2). Contest (CodeChef) and general code (CoDet-M4) are added as comparison pools.
- **Method:** Builds iJudge and CodeChef-extended, then trains SVM, XGBoost (140 hand-crafted features), UniXcoder, CodeBERT, Qwen2.5-Coder-1.5B and StarCoder2-3B (frozen probe or task-adapted) on four training mixtures and tests on five pools, with SHAP attribution (§5, §6).
- **Data:** iJudge: 338 problems, 1,352 human (4 per problem) and 1,352 LLM (676 GPT-4, 676 Gemini; Gemini version not stated) solutions. CodeChef-extended: 798 human, 1,596 LLM (GPT-4, Gemini 2.5). CoDet-M4 Python: 87,091 human, 80,387 LLM. Python only (§4.2.3, §4.3).
- **Headline result:** Macro-F1 (Overall-Mean): fine-tuned Qwen2.5-Coder-1.5B trained on ALL–PB-Balanced 0.984 (Table 7); fine-tuned UniXcoder trained on ALL also 0.984 (Table 6). XGBoost trained on iJudge only: 0.921 on iJudge, 0.532 on CodeChef-extended, 0.479 on CoDet-M4 (Table 5).
- **Limitation:** LLM code comes only from GPT-4 and Gemini under fixed prompts, and hybrid human–LLM editing is not modelled [author-acknowledged, §8].
- **Relation:** Uses the CoDet-M4 Python subset (and its UniXcoder checkpoint) as a pool and extends the CodeChef data and 140 features of Whodunit (Idialu et al., 2024) (§3.1, §3.2, §5.2).
- Note: The abstract says task-adapted decoder CodeLLMs are strongest overall; Tables 6 and 7 show a tie at 0.984 (Qwen2.5-Coder 0.984, UniXcoder 0.984, StarCoder2-3B 0.983), with no variance or confidence intervals reported. §6.2.2 says the Qwen versus StarCoder2 scores are not a controlled comparison.
- Note: The dataset is promised for release "upon acceptance" (Data Availability). The text is a journal pre-proof accepted 5 October 2026, so no volume, issue or pages exist yet.

### 3.2 Zero-shot and trained detectors

#### Distinguishing LLM-generated from Human-written Code by Contrastive Learning (CodeGPTSensor)
**Reference (APA 7):** Xu, X., Ni, C., Guo, X., Liu, S., Wang, X., Liu, K., & Yang, X. (2025). Distinguishing LLM-generated from human-written code by contrastive learning. *ACM Transactions on Software Engineering and Methodology, 34*(4), 1–31. https://doi.org/10.1145/3705300
**Source note:** [xu-2024-distinguishing-llm-generated-human](../../machine-learning/llm-generated-code-detection/sources/xu-2024-distinguishing-llm-generated-human.md)
- **Setting:** general code. Main data are GitHub functions from CodeSearchNet, not coding problems; the only problem-style data is Dα-C8, Java implementations of problems from a programming book (§6.3).
- **Method:** fine-tunes UniXcoder with a triplet contrastive loss (margin 1) to classify a function as human-written or ChatGPT-generated (§3).
- **Data:** HMCorp, 288K Python and 222K Java human/ChatGPT pairs; generator gpt-3.5-turbo, April 2023; 8:1:1 split (§4.1). Dα-C8: 1,484 Java snippets (§6.3).
- **Headline result:** On the HMCorp test set CodeGPTSensor reaches Python F1 0.992 / AUC 0.999 and Java F1 0.968 / AUC 0.995; DetectGPT accuracy is 0.499 (Python) and 0.477 (Java) (Table 6).
- **Limitation:** Only Java, Python, open-source functions and one ChatGPT version (gpt-3.5-turbo, April 2023) are covered [author-acknowledged, §7].
- **Relation:** Baselines include DetectGPT, DetectGPT4Code and GPTSniffer, which it beats in Table 6 and compares directly in §6.6.

Note: the Source note labels this "coding-problem data"; the paper's main corpus is CodeSearchNet GitHub functions. Volume, issue and pages (34(4), 1–31) come from the DOI record, not the arXiv text; the Source note's 2024 is the arXiv date.
- *Scope note:* narrow fit. The paper is evaluated mainly on CodeSearchNet GitHub functions; its one problem-style test is Java textbook exercises (§6.3). It is kept as a widely used trained-detector baseline.

#### Uncovering LLM-Generated Code: A Zero-Shot Synthetic Code Detector via Code Rewriting
**Reference (APA 7):** Ye, T., Du, Y., Ma, T., Wu, L., Zhang, X., Ji, S., & Wang, W. (2025). Uncovering LLM-generated code: A zero-shot synthetic code detector via code rewriting. *Proceedings of the AAAI Conference on Artificial Intelligence, 39*(1), 968–976. https://doi.org/10.1609/aaai.v39i1.32082
**Source note:** [ye-2024-uncovering-llm-generated-code](../../machine-learning/llm-generated-code-detection/sources/ye-2024-uncovering-llm-generated-code.md)
- **Setting:** general code on coding-problem data (APPS, MBPP; CodeContests for C++).
- **Method:** a generator LLM rewrites the code m times; cosine similarity between the original and each rewrite, scored by a SimCSE-tuned GraphCodeBERT, is the zero-shot score (Algorithm 1).
- **Data:** Python benchmarks from APPS test (770 human/770 synthetic per generator; GPT-4 100/100) and MBPP (233/233; GPT-4 100/100). Generators: CodeLlama-13B-Instruct, StarChat-Alpha, GPT-3.5-Turbo, GPT-4 (Tables 1–2).
- **Headline result:** With CodeLlama as detector LLM, m=8 gives average AUROC 80.16 (APPS) and 81.81 (MBPP) against 65.38 and 61.57 for the best baseline, LogRank; GPTZero scores 55.22 and 59.80 (Table 3).
- **Limitation:** After replacing 50% of identifiers, all zero-shot detectors, including this one, fall to random guessing [author-acknowledged, "Detecting Revised Synthetic Code", Fig. 9].
- **Relation:** Adapts DetectGPT to code (CodeT5-large perturber) as a baseline and reports log-probability methods degrading on code.

Note: the Source note gives 2024 (arXiv date); the AAAI-25 volume 39(1), 968–976 is from the DOI record, not the arXiv text.

#### Zero-Shot Detection of LLM-Generated Code via Approximated Task Conditioning
**Reference (APA 7):** Ashkenazi, M., Brenner, O., Furman Shohet, T., & Treister, E. (2025). Zero-shot detection of LLM-generated code via approximated task conditioning. In *Machine Learning and Knowledge Discovery in Databases. Research Track (ECML PKDD 2025)* (pp. 187–204). Springer. https://doi.org/10.1007/978-3-032-06078-5_11
**Source note:** [ashkenazi-2025-zero-shot-detection-llm](../../machine-learning/llm-generated-code-detection/sources/ashkenazi-2025-zero-shot-detection-llm.md)
- **Setting:** general code on coding-problem data (APPS, MBPP; CodeContests for C++ and Java).
- **Method:** ATC prompts a detector LLM to write a task description for the code, then scores mean code-token entropy conditioned on that task (Algorithm 1).
- **Data:** full APPS test set (3,765 instances after sanitisation), MBPP (500 test instances), CodeContests (152 C++, 129 Java; §4.7). Seven generators: GPT-3.5-Turbo, GPT-4o-mini, Claude3-haiku, StarChat-Alpha, CodeLlama-7B/13B, CodeGemma-7B (§4.1).
- **Headline result:** With CodeLlama-13B as detector and N=4 tasks, mean AUROC is 94.22 on MBPP and 93.82 on APPS (§4.2, Tables 1–2).
- **Limitation:** Results use public benchmarks only; task approximation in domain-specific repositories may be harder [author-acknowledged, §5].
- **Relation:** Takes Ye et al.'s rewriting detector as the SOTA to beat and reports its numbers as published; also compares DetectGPT, NPR and DetectCodeGPT (§4.1).

#### One Size Does Not Fit All: Investigating Efficacy of Perplexity in Detecting LLM-Generated Code
**Reference (APA 7):** Xu, J., Zhang, H., Yang, Y., Yang, L., Cheng, Z., Lyu, J., Liu, B., Zhou, X., Bacchelli, A., Chiam, Y. K., & Chiew, T. K. (2026). One size does not fit all: Investigating efficacy of perplexity in detecting LLM-generated code. *ACM Transactions on Software Engineering and Methodology, 35*(5), 1–34. https://doi.org/10.1145/3748506
**Source note:** [xu-2024-one-size-does-not](../../machine-learning/llm-generated-code-detection/sources/xu-2024-one-size-does-not.md)
- **Setting:** general code on coding-problem data (CodeNet puzzles).
- **Method:** compares eight perplexity-based detectors (incl. DetectGPT, NPR, DetectCodeGPT) with two feature-based and one pre-training-based (GPTSniffer) detector on accuracy by language, difficulty and solution size, speed, and generalisation across generators (§4–5).
- **Data:** 729 CodeNet puzzles, 8 languages, 16 human solutions per puzzle; 11,664 GPT-3.5 (gpt-3.5-turbo-0125) solutions plus 500 each from GPT-4o, Gemini-1.0, Llama-3.1; 500 pairs per evaluation cell (§4.2, §4.4).
- **Headline result:** On the CodeNet set, best perplexity AUC is 91% on C/C++ and 88% on large solutions; across the four generators perplexity gets 79.55–81.78% AUC against a 75.21–92.21% spread for the pre-training method (Introduction, §5.5, Tables 10–11).
- **Limitation:** Functions are self-contained puzzle solutions that may differ from real repositories [author-acknowledged, §7].
- **Relation:** Excludes Xu and Sheng's AIGCode Detector (batch paper 7) because its perturbation method is unspecified (§4.3.3); evaluates DetectCodeGPT and GPTSniffer.

Note: arXiv v2 carries a JACM template header; the TOSEM venue, year 2026 and 35(5), 1–34 come from the DOI record, and the Source note's 2024 is the arXiv date.

#### CodeVision: Detecting LLM-Generated Code Using 2D Token Probability Maps and Vision Models
**Reference (APA 7):** Xu, Z., & Sheng, V. S. (2025). CodeVision: Detecting LLM-generated code using 2D token probability maps and vision models. *arXiv preprint* arXiv:2501.03288. https://arxiv.org/abs/2501.03288
**Source note:** [xu-2025-codevision-detecting-llm-generated](../../machine-learning/llm-generated-code-detection/sources/xu-2025-codevision-detecting-llm-generated.md)
- **Setting:** general code on coding-problem data (CodeNet), motivated by academic integrity in programming education; no student submissions.
- **Method:** per-token log-probabilities from GPT-3.5-turbo-instruct are arranged into a line-by-token 2D matrix and classified by a ViT or ResNet trained on the maps.
- **Data:** 28,342 CodeNet samples (15,633 GPT-3.5/GPT-4, 12,709 human) in C, C++, Go, Java, Python, Ruby; 80/10/10 split; generator calls July 2024 to GPT-3.5-turbo-instruct and GPT-4-turbo (Datasets; Implementation Details). Table 2 Python set also uses SantaCoder-1.1B, CodeGeex2-6B, CodeLlama-7b, CodeQwen1.5-7B, StarCoder2-15B.
- **Headline result:** On its CodeNet-derived set, AUC is 0.96–0.99 for ResNet and 0.94–0.99 for ViT across six languages; DetectGPT gets 0.66–0.97 (Table 1). On Python from GPT-3.5-turbo, ResNet 0.98, ViT 0.96, DetectGPT 0.89 (Table 2).
- **Limitation:** Depends on the OpenAI API for probabilities (cost, availability) and offers little interpretability [author-acknowledged, Limitations].
- **Relation:** Runs DetectGPT and NPR as baselines (Table 1) and positions itself against GPTSniffer-style classifiers, SWEET-type watermarks and perturbation detectors (Related work).

#### Codetector: A Framework for Zero-Shot Detection of AI-Generated Code
**Reference (APA 7):** Adham, N., Duwe, H., & Hoos, H. H. (2026). Codetector: A framework for zero-shot detection of AI-generated code. In *Learning and Intelligent Optimization (LION 2025)* (LNCS Vol. 15745, pp. 157–173). Springer. https://doi.org/10.1007/978-3-032-09192-5_11
**Source note:** [adham-2025-codetector-framework-zero-shot](../../machine-learning/llm-generated-code-detection/sources/adham-2025-codetector-framework-zero-shot.md)
- **Setting:** general code on coding-problem and other data: LeetCode and APPS, plus CodeSearchNet and Stack Overflow.
- **Method:** a framework to generate AI code and run five existing zero-shot detectors (Fast-DetectGPT, Binoculars, rank, entropy and log-likelihood appear in Figs. 2–4), testing data leakage and sampling parameters (§1, §3).
- **Data:** 113,776 code samples from 17 LLMs over six datasets (the main text names only o1-mini and GPT-3.5-turbo, the latter as labeller); 12,294,388 detection samples. Human totals: LeetCode 1,000, APPS 561, CodeSearchNet 561, Stack Overflow 3,400. "Pre" data predate Nov 2022; "Post" data span Aug 2023–Apr 2024 (§4, Table 1).
- **Headline result:** On its generated LeetCode, APPS, CodeSearchNet and Stack Overflow data, newer detectors reach AUROC up to 97% (about 83% average); some detector–generator pairs show an absolute AUROC increase of over 40% on unseen data (§6).
- **Limitation:** Problem difficulty was not controlled when sampling [author-acknowledged, §4.2].
- **Relation:** Discusses DetectGPT, DetectGPT4Code and DetectCodeGPT as prior work (§2), and the education-oriented studies of Pan et al. and Hoq et al.

Note: the Source note gives 2025 (conference year); the paper's copyright line and volume page give 2026.

#### Detecting AI-Generated Code Assignments Using Perplexity of Large Language Models
**Reference (APA 7):** Xu, Z., & Sheng, V. S. (2024). Detecting AI-generated code assignments using perplexity of large language models. *Proceedings of the AAAI Conference on Artificial Intelligence, 38*(21), 23155–23162. https://doi.org/10.1609/aaai.v38i21.30361
**Source note:** [xu-2024-detecting-ai-generated-code](../../machine-learning/llm-generated-code-detection/sources/xu-2024-detecting-ai-generated-code.md)
- **Setting:** education (programming assignments); data are CodeNet problem solutions, built "to reflect the nature of student submissions", not real student work.
- **Method:** masks high-perplexity lines, fills them with fine-tuned CodeBERT, and ranks the original against perturbed copies on a score combining perplexity, line-perplexity deviation and burstiness (Algorithm 1).
- **Data:** about 400 CodeNet problems, 6 languages; 5,214 text-davinci-003 codes from text-to-code generation and code translation (temperature 0.6, top-p 0.1) and 5,214 human codes; 50 perturbed samples per input (Experiments Design, Hyper-Parameters).
- **Headline result:** On the AIGCode dataset, abstract: average AUC 0.87 against 0.56 for GPTZero. Per-language AUC 0.81–0.95 (GPTZero 0.28–0.90) (Table 1). Code blending bypasses it at 0.75 against 0.87 for GPTZero (Table 3).
- **Limitation:** Relies on one generator, text-davinci-003, and was not tested on other code LLMs [author-acknowledged, Discussion].
- **Relation:** Extends DetectGPT with targeted masking and 50 instead of 500 perturbed samples (Hyper-Parameters); compares DetectGPT, GPT2-Detector, RoBERTa-QA, GPTZero, Writer.

Note: the abstract gives GPTZero average AUC 0.56; the six GPTZero AUCs in Table 1 average 0.55.

#### Assessing AI Detectors in Identifying AI-Generated Code: Implications for Education
**Reference (APA 7):** Pan, W. H., Chok, M. J., Wong, J. L. S., Shin, Y. X., Poon, Y. S., Yang, Z., Chong, C. Y., Lo, D., & Lim, M. K. (2024). Assessing AI detectors in identifying AI-generated code: Implications for education. In *Proceedings of the 46th International Conference on Software Engineering: Software Engineering Education and Training* (pp. 1–11). ACM. https://doi.org/10.1145/3639474.3640068
**Source note:** [pan-2024-assessing-ai-detectors-identifying](../../machine-learning/llm-generated-code-detection/sources/pan-2024-assessing-ai-detectors-identifying.md)
- **Setting:** education (SE/CS programming); coding questions from Quescol, Kaggle and LeetCode, no student submissions.
- **Method:** tests five off-the-shelf detectors (GPTZero, Sapling, GPT-2 Detector, DetectGPT, GLTR) on ChatGPT code from 13 prompt or post-edit variants, threshold 0.5 (§3).
- **Data:** 5,069 Python problem/human-solution pairs (80 Quescol, 3,264 Kaggle, 1,725 LeetCode); ChatGPT via API, model version not reported (§3.2).
- **Headline result:** On its 5,069-sample Quescol/Kaggle/LeetCode set, Variant-1 accuracy is 0.4971 (GPTZero), 0.5043 (GPT-2 Detector), 0.4893 (DetectGPT), 0.5040 (GLTR), 0.6056 (Sapling); the maximum is 0.7693 (GLTR, Variant 7) (Table 3, §4.2).
- **Limitation:** Conclusions may be specific to the datasets analysed, and only Python is covered [author-acknowledged, §5.2.3].
- **Relation:** Uses the public DetectGPT implementation as one of the five detectors; evaluates no code-specific detector.

#### Is This You, LLM? Recognizing AI-written Programs with Multilingual Code Stylometry
**Reference (APA 7):** Gurioli, A., Gabbrielli, M., & Zacchiroli, S. (2025). Is this you, LLM? Recognizing AI-written programs with multilingual code stylometry. In *2025 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)* (pp. 394–405). IEEE. https://doi.org/10.1109/SANER64311.2025.00044
**Source note:** [gurioli-2024-this-you-llm-recognizing](../../machine-learning/llm-generated-code-detection/sources/gurioli-2024-this-you-llm-recognizing.md)
- **Setting:** general code; human snippets are Rosetta Code task solutions (1,127 tasks; §II-A3). No education or contest data.
- **Method:** fine-tunes a CodeT5plus-770M encoder with a classification head to label code human or AI; 90 monolingual models plus one multilingual model (§II-B).
- **Data:** H-AIRosettaMP, 121,247 snippets in 10 languages; AI snippets are StarCoder2-15B translations of human snippets from another language; Rosetta Code snapshot of 1 July 2022; 470 snippets per class per sub-dataset (§II-B2); 80/20 split (§II-B3).
- **Headline result:** On H-AIRosettaMP, the multilingual model averages 84.1% ± 3.8% accuracy (Table II). In-distribution monolingual models beat re-trained baselines by +7.2 (Java), +8.9 (C++), +1.5 (Python) points (Table IV).
- **Limitation:** AI code comes from code translation by one open model, so transfer to prompted generation and other LLMs is untested beyond one dataset [author-acknowledged, §VI].
- **Relation:** Contrasts itself with GPTSniffer, which is Java-only and ChatGPT-based, and re-trains Li et al. and Oedingen et al. baselines (§VII).

Note: the Source note gives 2024 (arXiv date); the paper is SANER 2025, pp. 394–405, per the DOI record.
- *Scope note:* uses Rosetta Code tasks, which this review counts as coding-problem data because each task pairs a problem statement with solutions.

### 3.3 Stylometry, AST features and programming-education studies

#### Whodunit: Classifying Code as Human Authored or GPT-4 Generated — A case study on CodeChef problems
**Reference (APA 7):** Idialu, O. J., Mathews, N. S., Maipradit, R., Atlee, J. M., & Nagappan, M. (2024). Whodunit: Classifying code as human authored or GPT-4 generated—A case study on CodeChef problems. In *Proceedings of the 21st International Conference on Mining Software Repositories* (pp. 394–406). ACM. https://doi.org/10.1145/3643991.3644926
**Source note:** [idialu-2024-whodunit-classifying-code-as](../../machine-learning/llm-generated-code-detection/sources/idialu-2024-whodunit-classifying-code-as.md)
- **Setting:** Competitive programming (CodeChef problems), motivated by educators' academic-integrity concerns (§1).
- **Method:** XGBoost classifier on 140 code-stylometry features (31 base features: layout, lexical, syntactic/AST, Halstead, complexity), evaluated with problem-grouped ten-fold cross-validation (§3.2–3.3).
- **Data:** 399 Python problems; 798 human solutions (submitted in 2020) and 798 GPT-4 (version 0613, temperature 0) solutions, 1596 in total; a correct-only subset of 161 problems (§3.1, §4 RQ3).
- **Headline result:** F1 and AUC-ROC of 0.91 with all features; 0.89 without the gameable features (empty-line density, whitespace ratio); the replicated n-gram baseline reaches F1 0.87 (n=2) and 0.88 (n=3) (T4).
- **Limitation:** Human solutions come from CodeChef users, not novices, and only GPT-4 is covered [author-acknowledged, §6.1].
- **Relation:** Its baseline is the n-gram XGBoost method of Bukhari et al., re-implemented in Python (T4); the paper does not discuss DetectGPT, GPTSniffer, DetectCodeGPT or SWEET.

#### Detection of LLM-Generated Java Code Using Discretized Nested Bigrams
**Reference (APA 7):** Paek, T., & Mohan, C. (2025). Detection of LLM-generated Java code using discretized nested bigrams. *arXiv preprint* arXiv:2502.15740. https://arxiv.org/abs/2502.15740
**Source note:** [paek-2025-detection-llm-generated-java](../../machine-learning/llm-generated-code-detection/sources/paek-2025-detection-llm-generated-java.md)
- **Setting:** General code; the larger dataset is competitive programming (2020 Google Code Jam), the smaller one is GitHub Java files (§3.1).
- **Method:** Binary classification of 10–70-line code groups using discretized AST nested-bigram frequencies (optionally CodeBERT-embedded) with tree ensembles (§3.2–3.3).
- **Data:** GPT Dataset: 976 files (666 human, 108 Bing GPT-4, 202 ChatGPT 3.5 rewrites); GPT GCJ: 76,089 files (58,524 human, 17,565 GPT-4o rewrites); plus a 40-author, 3,021-file dataset (§3.1, §4).
- **Headline result:** On the GPT Dataset EWD-NB-F averages 0.960 accuracy against 0.72 for the ZeroGPT API (§4.1); on GPT GCJ accuracy is 0.99 and AUC 0.998–0.999 at group sizes 40 and 70 (T5).
- **Limitation:** Detection is of LLM-rewritten human code, not solutions generated from problem statements, and robustness to unseen LLM styles is untested [author-acknowledged, §5].
- **Relation:** Cites Oedingen et al., Ye et al. and Xu and Sheng as related detectors (§2.1) but does not run them; DetectGPT, GPTSniffer, DetectCodeGPT and SWEET are not discussed.

Note: The Source note gives the venue as CSCI 2024 proceedings; the PDF names no venue (only the arXiv abstract page says it will appear there), so it is cited as a preprint. The paper is inconsistent on the human-author count (11 authors in §3.1, 15 in §5) and names the baseline both ZeroGPT (§4) and GPTZero (§5).

#### Whitespaces Don't Lie: Feature-Driven and Embedding-Based Approaches for Detecting Machine-Generated Code
**Reference (APA 7):** Nirob, S. M. H., Ehsan, S., Rahman, M., & Haque, S. (2026). Whitespaces don't lie: Feature-driven and embedding-based approaches for detecting machine-generated code. *arXiv preprint* arXiv:2601.19264. https://arxiv.org/abs/2601.19264
**Source note:** [nirob-2026-whitespaces-don-t-lie](../../machine-learning/llm-generated-code-detection/sources/nirob-2026-whitespaces-don-t-lie.md)
- **Setting:** General code; the benchmark of Orel et al. is not described as coding-problem data in this paper (§IV-A).
- **Method:** Compares handcrafted stylometric/structural features (surface, identifier, AST-depth proxies) against frozen CodeBERT embeddings, each fed to standard classifiers (§IV).
- **Data:** 500k training and 100k held-out test samples, mainly Python, 80/20 stratified train–validation split; generators and class ratio not reported (§IV-A, §V).
- **Headline result:** Test set (T2): features with Random Forest reach ROC-AUC 0.995, F1 0.971, accuracy 0.970, precision 0.961; CodeBERT with logistic regression reaches ROC-AUC 0.994, F1 0.965, accuracy 0.964, precision 0.969. Top features are leading spaces and tabs (§V-B).
- **Limitation:** No cross-generator, cross-language or adversarial experiment is reported, although the Discussion claims embeddings are more robust to distribution shift [reader-inferred].
- **Relation:** Names DetectCodeGPT as a zero-shot stylistic detector (§II-C) but does not compare against it.

Note: The Source note says the dataset is DroidCollection with an algorithmic domain; the paper cites it only as Orel et al. [3] ("Droid") and states no domain, so "coding-problem data" is not confirmed by this paper.
- *Scope note:* the paper does not state that its benchmark is coding-problem data, so its place in scope is unconfirmed.

#### Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming
**Reference (APA 7):** Ye, R., Fan, J., Zavaleta Bernuy, A., Karnalim, O., Denny, P., Leinonen, J., & Liut, M. (2026). Correctness, convergence, and AI-generated code detection: A longitudinal study of student and large language model code in introductory programming. In *Proceedings of the 26th Koli Calling International Conference on Computing Education Research (Koli Calling '26)*. ACM. https://doi.org/10.1145/3856208.3856226
**Source note:** [ye-2026-correctness-convergence-ai-generated](../../machine-learning/llm-generated-code-detection/sources/ye-2026-correctness-convergence-ai-generated.md)
- **Setting:** Education; ten weekly Python labs of one CS1 course at a research university (§3.1).
- **Method:** Evaluates "generated-reference matching": MOSS overlap between student files and LLM-generated solutions, plus exact AST-form counts for five functions, across the 2021, 2023 and 2025 cohorts (§3.4–3.5).
- **Data:** 29,970 student submissions (9,735, 10,987, 9,248) and 90,000 LLM attempts (1,000 per LLM, lab and year) from GPT-5.5, Gemini 3.1 Pro and Claude Opus 4.8 (§3.1–3.2).
- **Headline result:** 87.79–88.14% of cross-LLM pairs matched in MOSS (T3); student–LLM match incidence in 2025 was 1.76–2.12 times the 2021 rate (§4.2.2); 97.0–99.4% of cross-matches were under 30 lines (§4.3).
- **Limitation:** Without verified source labels the study cannot validate individual AI-use detection or explain why code changed [author-acknowledged, §6].
- **Relation:** Tests the pseudo-submission idea of Bashir and the sample matching of Karnalim et al. (§1, §2.3) and cites GPTSniffer as an in-distribution classifier and DetectGPT among curvature-based detectors (§1, §2.3).

#### Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies
**Reference (APA 7):** Wang, K., Akins, S., Mohammed, A., & Lawrence, R. (2023). Student mastery or AI deception? Analyzing ChatGPT's assessment proficiency and evaluating detection strategies. *arXiv preprint* arXiv:2311.16292. https://arxiv.org/abs/2311.16292
**Source note:** [wang-2023-student-mastery-or-ai](../../machine-learning/llm-generated-code-detection/sources/wang-2023-student-mastery-or-ai.md)
- **Setting:** Education; CS1 and CS2 (Java) assignments, plus a databases course, at one research university (§III-A).
- **Method:** Grades ChatGPT 3.5 on course assessments, then tests MOSS, JPlag, GPTZero and instructor/TA judgement at telling its code from student code (§III-B, §III-C).
- **Data:** 50 anonymized student submissions and 50 ChatGPT 3.5 answers; MOSS/JPlag runs on 100 submissions per question with 5%–50% AI share; GPTZero on 24 solutions (14 human, 10 AI); human survey of 32 solutions (14 AI), 10 responses (§III-C, §IV-B).
- **Headline result:** Instructors and TAs averaged recall 69.29%, precision 74.51%, F1 71.42%, accuracy 69% and false-positive rate 22% (§IV-C); GPTZero gave AI solutions very low AI probability, lower than human ones (§IV-B2, no figures).
- **Limitation:** Only ChatGPT 3.5 with a single prompt was used and no obfuscation was applied, so detection rates would likely fall in practice [author-acknowledged, §VI].
- **Relation:** Tests general-purpose tools (MOSS, JPlag, GPTZero) only; none of the anchor methods or other batch papers are discussed.

Note: MOSS and JPlag results appear only in Figures 6–9, with no numbers in the text. The Source note's venue (CSCI 2023) is not in the PDF; it comes from the arXiv comment, so the paper is cited as a preprint.

#### Sieving Coding Assignments Over Submissions Generated by AI and Novice Programmers
**Reference (APA 7):** Jégourel, C., Ong, J. Y., Kurniawan, O., Lim, M. S., & Chitluru, K. (2024). Sieving coding assignments over submissions generated by AI and novice programmers. In *24th Koli Calling International Conference on Computing Education Research (Koli Calling '24)*, November 12–17, 2024, Koli, Finland (11 pages). ACM. https://doi.org/10.1145/3699538.3699569
**Source note:** [jegourel-2024-sieving-coding-assignments-over](../../machine-learning/llm-generated-code-detection/sources/jegourel-2024-sieving-coding-assignments-over.md)
- **Setting:** education: Python submissions to one first-year undergraduate exam question (a 3×3 determinant function) and to a Tic-Tac-Toe home project from a first-programming-course for adult continuing-education learners (§4.1, §4.2).
- **Method:** Python code is tokenised, pairwise BLEU or Fahrenberg distances are computed, and Ward hierarchical clustering is run on a 70% training split. Each cluster gets a majority label (Human/AI), and a test file takes the label of its nearest medoid (§3.3, §4.3).
- **Data:** Exam: 50 human files (the 50 largest of 413) plus 50 AI files (25 ChatGPT 3.5, 25 GitHub Copilot); test set 14 human and 16 AI. Tic-Tac-Toe: 44 human (2021), 28 ChatGPT 3.5 and 21 Copilot files; 65 train, 28 test (15 human, 13 AI) (§4.1–4.3, §5).
- **Headline result:** Exam, BLEU: accuracy 97% (Table 4: TP 14, TN 15, FP 1, FN 0). Tic-Tac-Toe, Fahrenberg λ≤0.4: about 93%, 26 of 28 correct; BLEU 86% (Table 6, §5.2).
- **Limitation:** Only ChatGPT 3.5 and Copilot at default settings, about 100 programs per experiment, two prompting students, and two problems analysed separately, so accuracy may fall on a wider problem set [author-acknowledged, §6.1].
- **Relation:** The authors say their accuracy (greater than 86%) appears to surpass that of the AI-code detectors reported by Orenstrakh et al. (2023), but they did not compare against MOSS or any other tool (§6.1).
- Note: The abstract's "over 90%" is not a reported measurement. §7 says "exceeding 90% on average", but no average is computed; the figures are the best setting per assignment (97% and about 93%). The same tables give lower values: Fahrenberg on the exam 76% to 87% (§5.1.3), Tic-Tac-Toe BLEU 86%, λ=0.8 79% (§5.2). §6 itself says "exceeding 86%". §7's "true positive and negative rates greater than 93%" conflicts with Table 4 (true negative rates 68% to 82% for Fahrenberg).
- Note: §5 says simulations ran "over the training datasets", while §4.3 says test files are classified; the confusion matrices are described as test-set results. λ was recommended after viewing these results. The paper reports no confidence intervals or repeated runs.
- Note: The front page gives no article number or page range, only "11 pages"; "Lim Meng Shin" is printed given-name-first, so "Lim, M. S." assumes Lim is the family name.

#### Using pseudo-AI submissions for detecting AI-generated code
**Reference (APA 7):** Bashir, S. (2025). Using pseudo-AI submissions for detecting AI-generated code. *Frontiers in Computer Science, 7*, Article 1549761. https://doi.org/10.3389/fcomp.2025.1549761
**Source note:** [bashir-2025-pseudo-ai-submissions-detecting](../../machine-learning/llm-generated-code-detection/sources/bashir-2025-pseudo-ai-submissions-detecting.md)
- **Setting:** Education; an introductory C programming course (§4) and a public student-homework dataset (§3).
- **Method:** Instructors generate "pseudo-AI submissions" with ChatGPT, and a student submission is flagged by its Dolos (AST-fingerprint) similarity to them (§3.1).
- **Data:** 28 of 48 problems from the IEEE DataPort homework dataset (2016–2017 submissions); 14 prompts; user study with 43 students in 2 sections and 2 assignments; ChatGPT version not stated (§3, §4).
- **Headline result:** User-study median similarity to pseudo-submissions: student code 14% and 13%, AI-generated code 59% and 60% (T6, Assignments 1 and 2).
- **Limitation:** Effectiveness on long or advanced tasks is not explored, and short tasks give higher similarity [author-acknowledged, §5, §3.3].
- **Relation:** Contrasts itself with trained classifiers (Nguyen et al., Xu and Sheng, Hoq et al.) as vulnerable to prompt engineering (§1), and uses instructor-made references instead of training.

Note: The abstract claims "over 96% accuracy", but the body reports no accuracy, precision or recall; T6 ranges overlap (AI minimum 20–21%, student maximum 24–25%).

#### An Embedding-Based Approach for Identifying LLM-Generated Code in Student Assignments
**Reference (APA 7):** Gacek, P. (2025). An embedding-based approach for identifying LLM-generated code in student assignments. In *Proceedings of the Generative Code Intelligence Workshop (GeCoIn 2025) at ECAI 2025* (CEUR Workshop Proceedings, Vol. 4075). CEUR-WS.org. https://ceur-ws.org/Vol-4075/paper3.pdf
**Source note:** [gacek-2025-embedding-based-approach-identifying](../../machine-learning/llm-generated-code-detection/sources/gacek-2025-embedding-based-approach-identifying.md)
- **Setting:** Education; an Algorithms and Data Structures course at AGH University of Krakow (§3).
- **Method:** Generates k LLM solutions and rewrites per task, embeds comments-stripped code with Qodo-Embed-1, and flags students whose cosine similarity exceeds 0.94 (§2.2–2.3).
- **Data:** 509 student submissions; GPT-4o and Gemini 2.5 Flash, k=4 for the example task of 102 submissions; a survey of 50 students (§2.1, §3, §3.1). Language not stated (listings are Python).
- **Headline result:** Independently written code clustered at 0.79–0.85 cosine similarity, while suspected AI-assisted code scored 0.90–0.96 (§3.1, Figure 6); no accuracy, precision or recall is reported.
- **Limitation:** No ground-truth labels exist, so evaluation is unsupervised and the 0.94 cutoff is set empirically on the same data [author-acknowledged, §2.3, §3].
- **Relation:** Cites none of the other batch papers; it applies the reference-solution comparison idea with embeddings and positions itself against text-focused detectors (§1).

#### Detecting GenAI assistance in programming assessments with over-uniqueness and sample matching
**Reference (APA 7):** Karnalim, O., Toba, H., Wijanto, M. C., Setiawan, Y. D., Surantha, N., & Liut, M. (2026). Detecting GenAI assistance in programming assessments with over-uniqueness and sample matching. *Discover Computing, 29*, Article 5. https://doi.org/10.1007/s10791-025-09884-9
**Source note:** [karnalim-2026-detecting-genai-assistance-programming](../../machine-learning/llm-generated-code-detection/sources/karnalim-2026-detecting-genai-assistance-programming.md)
- **Setting:** Education; introductory programming courses with weekly assessments and an exam, at one institution (§4.1, §5).
- **Method:** Zero-shot, integrated into a plagiarism detector: flag submissions that are over-unique (threshold 90%) or similar to a GenAI sample (threshold 50%), using five similarity measures (§3).
- **Data:** Weekly (Python, 55 students, 26 assessments, six tutor-written GenAI submissions each, GPT-3.5); Weekly Alt (17 assessments); Weekly Align (Java, 46 students, 40 assessments); Exam (17 students, 2 exams, about half GenAI-assisted) (§4.1).
- **Headline result:** Average MAP 71% overall: over-uniqueness 63%, sample matching 77%, combined 72% (§4.6); on Weekly Align sample matching gives 64% and over-uniqueness 26% (§4.3–4.4).
- **Limitation:** The method assumes GenAI submissions are unique or similar to each other, which fails when students ask for a particular style [author-acknowledged, §5].
- **Relation:** Describes DetectGPT, GPTZero and GLTR as text detectors in its related work (§2.2) and does not compare against them.

#### Does AI Assistance Leave a Temporal Fingerprint? Detecting Overreliance in AI-Assisted Writing and Programming
**Reference (APA 7):** Davalos, E., & Zhang, Y. (2026). Does AI assistance leave a temporal fingerprint? Detecting overreliance in AI-assisted writing and programming. *arXiv preprint* arXiv:2609.17883. https://arxiv.org/abs/2609.17883
**Source note:** [davalos-2026-does-ai-assistance-leave](../../machine-learning/llm-generated-code-detection/sources/davalos-2026-does-ai-assistance-leave.md)
- **Setting:** Education-oriented programming telemetry (short lab-style tasks), not coding-problem code artifacts; also essay writing (Data).
- **Method:** Random forests on label-free temporal features (largest insertion delta, delta variability, deletion ratio) separate minimal-AI, collaborative and simulated wholesale-delegation sessions (Method).
- **Data:** RealHumanEval: 243 records, 219 traces (88 human-only, 131 collaborative); CoAuthor: 1,447 sessions (GPT-3); CS1 keystrokes: 5.1 million from 487 students; simulated delegation: 150 programming traces. Programming LLMs not reported (Data).
- **Headline result:** Programming delegation (simulated) F1 0.997, with 1 of 219 real traces (0.46%) misclassified as delegation; human-only vs collaborative F1 0.590 and 0.701, accuracy 0.794 (T2).
- **Limitation:** The delegation condition is simulated, so the features detect a specified behavior, not an observed one [author-acknowledged, Limitations].
- **Relation:** Says code detection has stayed artifact-based and that watermarks show only that a model was involved (Related Work); anchor methods are not discussed.

### 3.4 Robustness and watermarking

#### Evaluating Software Plagiarism Detection in the Age of AI: Automated Obfuscation and Lessons for Academic Integrity
**Reference (APA 7):** Sağlam, T., & Schmid, L. (2025). Evaluating software plagiarism detection in the age of AI: Automated obfuscation and lessons for academic integrity. *arXiv preprint* arXiv:2505.20158. https://arxiv.org/abs/2505.20158
**Source note:** [saglam-2025-evaluating-software-plagiarism-detection](../../machine-learning/llm-generated-code-detection/sources/saglam-2025-evaluating-software-plagiarism-detection.md)
- **Setting:** Education: programming assignments from university courses (Java, C/C++). Not a watermark paper.
- **Method:** Tests whether two defences added to the JPlag similarity detector (Token Sequence Normalization, Subsequence Match Merging, and both) resist algorithmic and GPT-4 obfuscation, and separate GPT-4-generated from human programs by mutual similarity (§4, §5.5).
- **Data:** Real student code: six datasets of 18 to 626 programs (Table 1); over 4.1 million pairwise comparisons (§4); GPT-4 (version not given), 15 obfuscation prompts (§4.4); 50 GPT-4 programs for each of PROGpedia-19, PROGpedia-56 and TicTacToe (Table 2).
- **Headline result:** Median similarity gap, GPT-4 pairs vs human pairs, JPlag baseline vs Subsequence Match Merging: 15.04 vs 23.58 (PROGpedia-19), 33.13 vs 34.47 (PROGpedia-56), 14.57 vs 21.10 points (TicTacToe) (Table 10).
- **Limitation:** The signal exists only if several students submit output from the same model, and full generation works only below 300 to 400 lines [author-acknowledged, §5.5, §7].
- **Relation:** Calls current AI-code detectors unreliable, citing Pan et al. (2024) and Suh et al. (2025, reported to beat GPTSniffer), and names watermarking as open research (§7.3.3, §8.4).
- **Note:** Text gives 787 plagiarised programs (§4.4); the Table 2 caption gives 851.

#### Disappearing Ink: Obfuscation Breaks N-gram Code Watermarks in Theory and Practice
**Reference (APA 7):** Zhang, G., Li, M., Bagdasarian, E., Ma, S., & Zhai, J. (2025). Disappearing ink: Obfuscation breaks N-gram code watermarks in theory and practice. *arXiv preprint* arXiv:2507.05512. https://arxiv.org/abs/2507.05512
**Source note:** [zhang-2025-disappearing-ink-obfuscation-breaks](../../machine-learning/llm-generated-code-detection/sources/zhang-2025-disappearing-ink-obfuscation-breaks.md)
- **Setting:** General code on coding-problem data: function-level benchmarks.
- **Method:** Models obfuscation as a Markov random walk and proves that, assuming "distribution consistency", an N-gram watermark detector fails with rate approaching 1 − ϵpos (Theorems 3.3, 3.4); tests it with off-the-shelf obfuscators.
- **Data:** SWEET, WLLM, SynthID; LLaMA-3.1-8B-Instruct, DeepSeek-Coder-33B-Base; HumanEval, MBPP+, HumanEval-X-JS, MBPP-JS; four obfuscators (§4.1); 50 SWE-bench Verified tasks (App. M). Per-benchmark counts not reported. Student/contest code: no, only HumanEval/MBPP-family.
- **Headline result:** Post-obfuscation AUROC clusters near 0.5; only 9 of 1,280 obfuscated data points fall outside (0.4, 0.6) (§4.2). Distribution consistency holds in 1,557 of 1,620 spaces, 96.11% (Table 1).
- **Limitation:** Covers only N-gram-based schemes, and scores code quality only by test passing [author-acknowledged, Limitations].
- **Relation:** SWEET is one of the three attacked schemes (§4.1); App. O reports the ACW-s variant of Guo and Cheng (2025) falling to AUROC 52.92% under Python-Minifier.
- **Note:** Read v2 (PDF; its HTML is unavailable), five authors. v1 has four authors and reports the consistency test as 98.10% on 158 segments (§1, §6.4).

#### Is The Watermarking Of LLM-Generated Code Robust?
**Reference (APA 7):** Suresh, T., Ugare, S., Singh, G., & Misailovic, S. (2024). Is the watermarking of LLM-generated code robust? *arXiv preprint* arXiv:2403.17983. https://arxiv.org/abs/2403.17983
**Source note:** [suresh-2024-watermarking-llm-generated-code](../../machine-learning/llm-generated-code-detection/sources/suresh-2024-watermarking-llm-generated-code.md)
- **Setting:** General code on coding-problem data: HumanEval completions.
- **Method:** An AST-walking algorithm applies d = 5 random semantics-preserving edits (AddDeadCode, InsertPrint, Rename, WrapTryCatch, Mixed) to watermarked Python and measures the drop in detection (§2.2, §3).
- **Data:** LLaMA-7B, CodeLlama-7B on HumanEval; UMD and Unigram watermarks (γ = 0.25); 3 completions pooled, z > 3; mean of 3 runs (§3.3, §4.1). Problem count not reported. Student/contest code: no, only HumanEval.
- **Headline result:** LLaMA-7B TPR falls from 0.79 to 0.22 (UMD, WrapTryCatch) and 0.76 to 0.01 (Unigram, AddDeadCode) (Table 2); CodeLlama-7B 0.82 to 0.28 and 0.72 to 0.03 (Table 3).
- **Limitation:** Python only, two 7B models, two text-derived watermarks; no code-specific scheme is tested [reader-inferred].
- **Relation:** Describes DetectGPT as needing white-box access and costly perturbations, and SWEET as needing regeneration at detection (§5); tests neither.
- **Note:** PDF header reads "ICLR 2024"; the text names no track, so the Source note's "Tiny Papers" is unverified.

#### Efficient and Universal Watermarking for LLM-Generated Code Detection
**Reference (APA 7):** Li, B., Fu, Z., Zhang, M., Zhang, P., Sun, J., & Wang, X. (2026). Efficient and universal watermarking for LLM-generated code detection. *IEEE Transactions on Software Engineering*. https://doi.org/10.1109/TSE.2026.3710556
**Source note:** [li-2024-efficient-universal-watermarking-llm](../../machine-learning/llm-generated-code-detection/sources/li-2024-efficient-universal-watermarking-llm.md)
- **Setting:** General code on coding-problem data: MBPP, APPS, HumanEval+ prompts and SRDD projects; students named as motivation (§I).
- **Method:** ACW post-processes LLM output with 46 idempotent semantics-preserving transformations (§IV-A); detection checks whether they were applied. No model access needed.
- **Data:** GPT-4, GPT-4o, Qwen2.5-Coder-14B-FP16; 974 MBPP, 3,035 APPS, 164 HumanEval+ outputs per LLM, 500 SRDD projects (7,465 functions) per GPT-4 and GPT-4o; human negatives are the benchmarks' own solutions and CodeSearchNet (§IV-A). Student code: no. APPS (listed in this review's scope as coding-problem data) is the only contest-style set in the batch; the paper does not describe its provenance.
- **Headline result:** ACC 97.25 to 100%, TPR 94.51 to 100%, FPR at most 0.17% on all sets; APPS-Qwen: ACW ACC 98.15, TPR 96.47, FPR 0.17 vs SWEET 71.20, 47.80, 5.40 (Table II).
- **Limitation:** The 46 transformations are shown only for Python [author-acknowledged, §VII].
- **Relation:** Table II compares against SWEET and STONE (Kim et al., this batch), WLLM and WaterMax; baselines run on Qwen only.
- **Note:** Venue and DOI come from the arXiv record (v5); volume and pages not reported.

#### Practical and Effective Code Watermarking for Large Language Models
**Reference (APA 7):** Guo, Z., & Cheng, M. (2025). Practical and effective code watermarking for large language models. In *Advances in Neural Information Processing Systems* (Vol. 38). https://doi.org/10.52202/085713-2485
**Source note:** [guo-2025-practical-effective-code-watermarking](../../machine-learning/llm-generated-code-detection/sources/guo-2025-practical-effective-code-watermarking.md)
- **Setting:** General code on coding-problem data: HumanEval, MBPP, HumanEvalPack.
- **Method:** ACW (AST-guided Code Watermarking) trains a Watermark Partitioning Network on AST-derived substitutable positions; detection needs only the code, not the LLM or prompt (§4).
- **Data:** OpenCoder-1.5B-Instruct (main), DeepSeek-Coder-1.3B-instruct (App. F.1), OpenCoder-8B-Instruct (Table 3); HumanEval, MBPP (Python); HumanEvalPack Java, C++, JavaScript (Table 2). Counts not reported. Student/contest code: no, only HumanEval/MBPP-family.
- **Headline result:** AUROC / TPR@5%FPR 84.43 / 45.12 (HumanEval) and 81.18 / 44.20 (MBPP) vs WLLM 70.17 / 20.73 and 76.44 / 27.80; DetectGPT 51.12 and 46.15 AUROC (Table 1).
- **Limitation:** Weaker for languages with complex type systems, and vulnerable to sophisticated code-transformation attacks [author-acknowledged, App. I].
- **Relation:** Runs SWEET as an oracle reference (AUROC 83.10, HumanEval) and DetectGPT as a post-hoc baseline (Table 1).
- **Note:** Not the "ACW" of Li et al. (above); Guo and Cheng cite that work only as a format-altering method (§2).

#### Marking Code Without Breaking It: Code Watermarking for Detecting LLM-Generated Code
**Reference (APA 7):** Kim, J., Park, S., & Han, Y.-S. (2026). Marking code without breaking it: Code watermarking for detecting LLM-generated code. In *Findings of the Association for Computational Linguistics: EACL 2026*. https://arxiv.org/abs/2502.18851
**Source note:** [kim-2025-marking-code-without-breaking](../../machine-learning/llm-generated-code-detection/sources/kim-2025-marking-code-without-breaking.md)
- **Setting:** General code on coding-problem data: MBPP+, HumanEval+, HumanEvalPack.
- **Method:** STONE watermarks only non-syntactic tokens, keeping keywords and delimiters intact; the STEM score merges correctness, detectability and imperceptibility (§3).
- **Data:** Qwen2.5-Coder-7B (Llama-3.1-8B in App. B); MBPP+ 399 problems, HumanEval+ 164, HumanEvalPack C++ 164 and Java 164 (Table 1); baselines KGW, EWD, SWEET (§4). Student/contest code: no, only HumanEval/MBPP-family.
- **Headline result:** STONE vs SWEET on MBPP+: pass@1 0.571 vs 0.502, AUROC 0.982 vs 0.867, STEM 0.848 vs 0.787; HumanEval+ AUROC 0.777 vs 0.710 (Table 2).
- **Limitation:** Capacity drops on code with few non-syntactic tokens (obfuscated scripts, code golf), and an algorithm-aware attacker could rename all variables and strip comments [author-acknowledged, Limitations].
- **Relation:** Extends SWEET and tests both against refactoring and GPT-4o paraphrase attacks on HumanEval+ (§6.2, Figure 4); criticises Li et al. (above) for unnatural code but does not run it (§7).
- **Note:** Venue taken from the arXiv comment ("Findings of EACL 2026"); pages not reported.

#### CODE ACROSTIC: Robust Watermarking for Code Generation
**Reference (APA 7):** Lin, L., Xin, S., Cao, Y., & Cao, X. (2025). Code Acrostic: Robust watermarking for code generation. *arXiv preprint* arXiv:2512.14753. https://arxiv.org/abs/2512.14753
**Source note:** [lin-2025-code-acrostic-robust-watermarking](../../machine-learning/llm-generated-code-detection/sources/lin-2025-code-acrostic-robust-watermarking.md)
- **Setting:** General code on coding-problem data: HumanEval (homework programming cited as motivation, §1).
- **Method:** Builds a secret Cue List from 1-gram statistics of a third-party corpus; watermark tokens are injected and detected only after cue tokens, to survive comment removal (§4).
- **Data:** HumanEval, 164 problems; DeepSeek-Coder-1.3b via MarkLLM; baselines KGW, SWEET, EWD (§5.1). Student/contest code: no, only HumanEval.
- **Headline result:** AUROC 0.772 vs KGW 0.685, SWEET 0.692, EWD 0.750; Pass@1 51.20 vs 53.05 unwatermarked (Table 1). Comments excluded from detection: TPR 34.76 vs EWD 20.73, KGW 17.07, SWEET 16.46 (Table 2a).
- **Limitation:** One benchmark and one 1.3B model; with comments included SWEET (87.20) and EWD (87.19) beat it (85.37) (Table 2a) [reader-inferred].
- **Relation:** Cites Suresh et al. (this batch) for the fragility of code watermarks (§2.2) and benchmarks against SWEET; lists Li et al. and Kim et al. only as related work.
- **Note:** The paper names no venue; the Source note's "WISE 2025" comes from OpenAlex and Semantic Scholar, so it is cited here as arXiv preprint.

#### Watermarking Low-entropy Generation for Large Language Models: An Unbiased and Low-risk Method
**Reference (APA 7):** Mao, M., Wei, D., Chen, Z., Fang, X., & Chau, M. (2024). Watermarking low-entropy generation for large language models: An unbiased and low-risk method. *arXiv preprint* arXiv:2405.14604. https://arxiv.org/abs/2405.14604
**Source note:** [mao-2024-watermarking-low-entropy-generation](../../machine-learning/llm-generated-code-detection/sources/mao-2024-watermarking-low-entropy-generation.md)
- **Setting:** General code on coding-problem data: HumanEval, used as the low-entropy test beside C4 text.
- **Method:** STA-1 (Sampling One Then Accepting) is an unbiased watermark with lower risk of bad output in low-entropy steps; STA-M samples more at high-entropy steps to add strength (§3).
- **Data:** HumanEval, 164 Python problems, CodeLLaMA-7B-Instruct; C4 with LLaMA-2-7B (at least 500 sequences); baselines KGW, RDW, Dipmark, γ-reweight; z thresholds 2 and 2.5; 10 runs (§4.1, App. F.1). Student/contest code: no, only HumanEval.
- **Headline result:** HumanEval, z = 2.0: STA-1 AUC 0.677, F1 0.526 (γ-reweight 0.671, 0.522; KGW δ=2 0.775, 0.737) (Table 3).
- **Limitation:** Attacks (copy-paste, GPT-3.5 paraphrase, DIPPER) are run on C4 only, and paraphrase robustness in low-entropy settings is left open [author-acknowledged, §7].
- **Relation:** Table 1 lists Lee et al. (2023, "Who wrote this code?", the SWEET paper) among earlier methods but does not run it.
- **Note:** The paper calls itself a "Preprint"; no venue is given.

### 3.5 Further included papers

These 53 papers meet the scope and are not annotated in full. A Source column reading *no-access* means the full text is not yet available.

| Paper | Year | Venue | Method | Source |
| --- | --- | --- | --- | --- |
| ChatGPT Code Detection: Techniques for Uncovering the Source of Code (Oedingen et al.) | 2024 | AI (MDPI), 2024, 5(3), 1066–1094; arXiv preprint 2405.15512 | trained classifier | [note](../../machine-learning/llm-generated-code-detection/sources/oedingen-2024-chatgpt-code-detection-techniques.md) |
| LLMSniffer: Detecting LLM-Generated Code via GraphCodeBERT and Supervised Contrastive Learning (Dihan & Muhtasim) | 2026 | arXiv preprint | trained classifier | [note](../../machine-learning/llm-generated-code-detection/sources/dihan-2026-llmsniffer-detecting-llm-generated.md) |
| DuoLens: A Framework for Robust Detection of Machine-Generated Multilingual Text and Code (Agrawal et al.) | 2025 | NeurIPS 2025 Workshop on Deep Learning for Code; arXiv preprint 2510.1 | trained classifier (fine-tuned | [note](../../machine-learning/llm-generated-code-detection/sources/agrawal-2025-duolens-framework-robust-detection.md) |
| Fine-Tuning Pre-Trained Code Models for AI-Generated Code Detection (Archaeology at SemEval-2026 Task 13) (Ispas & Nisioi) | 2026 | SemEval-2026 (DOI 10.18653/v1/2026.semeval-1.383); arXiv preprint 2605 | trained classifier (CodeBERT, | [note](../../machine-learning/llm-generated-code-detection/sources/ispas-2026-fine-tuning-pre-trained.md) |
| mcdok at SemEval-2026 Task 13: Finetuning LLMs for Detection of Machine-Generated Code (Skurla et al.) | 2026 | SemEval-2026; arXiv preprint 2604.21365 | trained classifier (fine-tuned | [note](../../machine-learning/llm-generated-code-detection/sources/skurla-2026-mcdok-at-semeval-2026.md) |
| FMI_SU_Yotkova_Kastreva at SemEval-2026 Task 13: Lightweight Detection of LLM-Generated Code via Stylometric Signals (Yotkova et al.) | 2026 | SemEval-2026 (DOI 10.18653/v1/2026.semeval-1.275); arXiv preprint 2605 | stylometry/AST + trained class | [note](../../machine-learning/llm-generated-code-detection/sources/yotkova-2026-fmi-su-yotkova-kastreva.md) |
| Dream at SemEval-2026 Task 13: SALSA for Single-Pass Machine-Generated Code Detection (Berdichevsky et al.) | 2026 | SemEval-2026 (DOI 10.18653/v1/2026.semeval-1.52); arXiv preprint 2606. | trained classifier (parameter- | [note](../../machine-learning/llm-generated-code-detection/sources/berdichevsky-2026-dream-at-semeval-2026.md) |
| CodeRipple: Wavelet-Based Detection of LLM-Generated Code (Yao et al.) | 2026 | ACL 2026 (Long Papers), pp. 38351–38364 | zero-shot | [note](../../machine-learning/llm-generated-code-detection/sources/yao-2026-coderipple-wavelet-based-detection.md) |
| MAGECODE: Machine-Generated Code Detection Method Using Large Language Models (Pham et al.) | 2024 | IEEE Access (DOI 10.1109/ACCESS.2024.3509987) | trained classifier (CodeT5+ fe | no-access |
| Detecting AI-Generated Text and Code: An Empirical Study of Cross-Generator and Cross-Domain Generalization (Alluri et al.) | 2026 | AI (MDPI), DOI 10.3390/ai7080319 | empirical study + trained clas | no-access |
| From Syntax Trees to Embeddings: A Comparative Study of AI-Generated Code Detection (Jakimoski et al.) | 2026 | MIPRO 2026 (IEEE), DOI 10.1109/MIPRO70003.2026.11591667 | stylometry/AST + trained class | no-access |
| Deep Learning Techniques for Differentiating Human-Written and AI-Generated Source Codes (Apsara et al.) | 2026 | ICARC 2026 (IEEE), DOI 10.1109/ICARC68737.2026.11453890 | trained classifier (ANN, CNN, | no-access |
| LevDetectCode: Zero-Shot Detection of AI-Generated Code Using Levenshtein Distance (Fu et al.) | 2025 | International Journal of Software Engineering and Knowledge Engineerin | zero-shot | no-access |
| UCSC-NLP at SemEval-2026 Task 13: Multi-View Generalization and Diagnostic Analysis of Machine-Generated Code Detection (Chauhan & Nur) | 2026 | SemEval-2026; arXiv preprint 2604.26990 | trained classifier (UniXcoder | [note](../../machine-learning/llm-generated-code-detection/sources/chauhan-2026-ucsc-nlp-at-semeval.md) |
| Comparative Analysis of Rewriting-Based Large Language Model-Generated Synthetic Code Detection (Alambana & Nurwidyantoro) | 2026 | IEEE ICAIIA 2026 (DOI 10.1109/ICAIIA70172.2026.11691940) | zero-shot (rewriting-similarit | no-access |
| CDUP: Detecting AI Generated Code Using Abstract Syntax Tree Analyst (Păuleț & Moruz) | 2025 | Procedia Computer Science (DOI 10.1016/j.procs.2025.09.329) | stylometry/AST (AST clone-dete | [note](../../machine-learning/llm-generated-code-detection/sources/paulet-2025-cdup-detecting-ai-generated.md) |
| Detecting ChatGPT-Generated Code Submissions in a CS1 Course Using Machine Learning Models (Hoq et al.) | 2024 | ACM SIGCSE Technical Symposium 2024 | trained classifier (traditiona | no-access |
| Detecting AI assisted submissions in introductory programming via code anomaly (Karnalim et al.) | 2024 | Education and Information Technologies, 29, 16841–16866 | stylometry/AST (34 code-anomal | no-access |
| Machine Learning Models to Detect AI-Assisted Code Anomaly in Introductory Programming Course (Toba & Karnalim) | 2024 | Advanced Technologies and the University of the Future, LNNS vol. 1140 | trained classifier (tree-based | no-access |
| Detecting AI-Generated Pseudocode in High School Online Programming Courses Using an Explainable Approach (Liu et al.) | 2025 | ACM SIGCSE Technical Symposium 2025 (DOI 10.1145/3641554.3701942) | trained classifier (explainabl | no-access |
| What are the differences between student and ChatGPT-generated pseudocode? Detecting AI-generated pseudocode in high school programming using explainable machine learning (Liu et al.) | 2025 | Education and Information Technologies, 30, 14853–14892 | trained classifier (ensemble c | no-access |
| Leveraging LLM for Detecting and Explaining LLM-generated Code in Python Programming Courses (Baek et al.) | 2025 | ACM SIGCSE Technical Symposium 2025, poster (DOI 10.1145/3641555.37052 | trained classifier (LLM-based | no-access |
| LLM-Based Explainable Detection of LLM-Generated Code in Python Programming Courses (Baek et al.) | 2026 | ACM SIGCSE Technical Symposium 2026 (DOI 10.1145/3770762.3772605) | trained classifier (fine-tuned | no-access |
| Detecting AI-Generated Code in Introductory Programming Courses (Ramachandra et al.) | 2026 | ACM SIGCSE Technical Symposium 2026 (DOI 10.1145/3770762.3772522) | trained classifier (Random For | no-access |
| AI-Generated Code Detection: An Examination of Current Tools in Education (Argotty & Manrique) | 2025 | ITS 2025, LNCS vol. 15723, pp. 192–201 | robustness study (seven detect | no-access |
| Detection of GenAI-produced and student-written C# code: A comparative study of classifier algorithms and code stylometry features (Adegbite & Kotzé) | 2025 | The African Journal of Information and Communication (AJIC), issue 35 | stylometry/AST (Roslyn code-me | [note](../../machine-learning/llm-generated-code-detection/sources/adegbite-2025-detection-genai-produced-student.md) |
| Machine learning approach to detect GAI-disguised academic programming plagiarism (Karnalim et al.) | 2026 | Applied Computer Science (DOI 10.35784/acs_8915) | trained classifier, also a rob | [note](../../machine-learning/llm-generated-code-detection/sources/karnalim-2026-machine-learning-approach-detect.md) |
| A Threshold Selection Method in Code Plagiarism Checking Function for Code Writing Problem in Java Programming Learning Assistant System Considering AI-Generated Codes (Permatasari et al.) | 2025 | Analytics (MDPI), 5(1), 2 (DOI 10.3390/analytics5010002) | zero-shot (Levenshtein similar | [note](../../machine-learning/llm-generated-code-detection/sources/permatasari-2025-threshold-selection-method-code.md) |
| Detection of AI-Generated Source Code in Programming Assignments (Vysocan et al.) | 2026 | IEEE International Conference on Intelligent Engineering Systems (INES | trained classifier (TF-IDF cha | no-access |
| Multi-Layer Feature Fusion for Detecting AI-Generated Code in Programming Education (Guo & Tang) | 2025 | IEEE International Conference on Big Data 2025 (DOI 10.1109/BigData669 | trained classifier (ShanghaiTe | no-access |
| Argus: Academic Integrity in the Era of Generative AI (Racovan et al.) | 2026 | arXiv preprint | stylometry/AST, combined with | [note](../../machine-learning/llm-generated-code-detection/sources/racovan-2026-argus-academic-integrity-era.md) |
| Towards Robust Plagiarism Detection in Programming Education: Introducing Tolerant Token Matching Techniques to Counter Novel Obfuscation Methods (Maisch et al.) | 2025 | European Conference on Software Engineering Education (ECSEE) 2025 (DO | robustness study (tolerant tok | no-access |
| NPC: Automated Tool for Detecting and Explaining ChatGPT-Generated Programs (Saeheng et al.) | 2026 | ICAART 2026, vol. 5, pp. 4714–4719 (DOI 10.5220/0014485500004052) | trained classifier (with local | [note](../../machine-learning/llm-generated-code-detection/sources/saeheng-2026-npc-automated-tool-detecting.md) |
| Attributing ChatGPT-generated Source Codes (Choi & Mohaisen) | 2025 | IEEE Transactions on Dependable and Secure Computing (DOI 10.1109/TDSC | stylometry/AST (code authorshi | [note](../../machine-learning/llm-generated-code-detection/sources/choi-2025-attributing-chatgpt-generated-source.md) |
| An Entropy-based Text Watermarking Detection Method (Lu et al.) | 2024 | ACL 2024 (main) | watermark (detection-side, ent | [note](../../machine-learning/llm-generated-code-detection/sources/lu-2024-entropy-based-text-watermarking.md) |
| Robust and Secure Code Watermarking for Large Language Models via ML/Crypto Codesign (Zhang et al.) | 2025 | ACM TAISAP (accepted, per arXiv comment) | watermark (learned insertion w | [note](../../machine-learning/llm-generated-code-detection/sources/zhang-2025-robust-secure-code-watermarking.md) |
| Invisible Entropy: Towards Safe and Efficient Low-Entropy LLM Watermarking (Gu et al.) | 2025 | EMNLP 2025 (main), per the OpenAlex record \| arXiv preprint | watermark (entropy-tagger repl | [note](../../machine-learning/llm-generated-code-detection/sources/gu-2025-invisible-entropy-safe-efficient.md) |
| Optimizing Token Choice for Code Watermarking: An RL Approach (Guo et al.) | 2025 | ICML 2026 (per arXiv comment); v1 title "...: A RL Approach" | watermark (RL-trained policy, | [note](../../machine-learning/llm-generated-code-detection/sources/guo-2025-optimizing-token-choice-code.md) |
| SWaRL: Safeguard Code Watermarking via Reinforcement Learning (Javidnia et al.) | 2026 | arXiv preprint | watermark (RL co-training with | [note](../../machine-learning/llm-generated-code-detection/sources/javidnia-2026-swarl-safeguard-code-watermarking.md) |
| Semantic Differentiation for Tackling Challenges in Watermarking Low-Entropy Constrained Generation Outputs (Le et al.) | 2026 | COLM 2026 (per arXiv comment) | watermark (sequence-level, Seq | [note](../../machine-learning/llm-generated-code-detection/sources/le-2026-semantic-differentiation-tackling-challenges.md) |
| MATRIX: Multi-Layer Code Watermarking via Dual-Channel Constrained Parity-Check Encoding (Nie et al.) | 2026 | arXiv preprint | watermark (post-hoc dual-chann | [note](../../machine-learning/llm-generated-code-detection/sources/nie-2026-matrix-multi-layer-code.md) |
| SSG: Logit-Balanced Vocabulary Partitioning for LLM Watermarking (Gu et al.) | 2026 | ACL 2026 (main), per arXiv comment | watermark (vocabulary partitio | [note](../../machine-learning/llm-generated-code-detection/sources/gu-2026-ssg-logit-balanced-vocabulary.md) |
| Signature filtering: a lightweight enhancement for statistical watermark detection in large language models (Hong et al.) | 2026 | arXiv preprint (OpenAlex links a journal version that was not opened) | watermark (detection-time filt | [note](../../machine-learning/llm-generated-code-detection/sources/hong-2026-signature-filtering-lightweight-enhancement.md) |
| PromptMark: A Prompt-Guided Iterative-Feedback Framework for Source Code Watermarking (Fahad et al.) | 2026 | ENASE 2026 (per arXiv comment) | watermark (black-box, prompt-g | [note](../../machine-learning/llm-generated-code-detection/sources/fahad-2026-promptmark-prompt-guided-iterative.md) |
| Multi-Channel Spread-Spectrum Code Watermarking (Choi et al.) | 2026 | arXiv preprint | watermark (post-hoc, 24-bit pa | [note](../../machine-learning/llm-generated-code-detection/sources/choi-2026-multi-channel-spread-spectrum.md) |
| Preserving Structure, Strengthening Signals: A Grammar-Driven Approach to Optimize the Trade-off Between Quality and Detectability in Code Watermarking (Yu et al.) | 2026 | arXiv preprint | watermark (grammar-driven thre | [note](../../machine-learning/llm-generated-code-detection/sources/yu-2026-preserving-structure-strengthening-signals.md) |
| SEW: Style-Encoded Watermarking of LLM-Generated Code (Lim et al.) | 2026 | arXiv preprint | watermark (post-hoc code-style | [note](../../machine-learning/llm-generated-code-detection/sources/lim-2026-sew-style-encoded-watermarking.md) |
| Grammar-Guided Code Watermarking with Green Temperature (Jin et al.) | 2026 | arXiv preprint | watermark (grammar-constrained | [note](../../machine-learning/llm-generated-code-detection/sources/jin-2026-grammar-guided-code-watermarking.md) |
| SynMark: Semantic-Coordinate Multi-Bit Watermarking during LLM Code Generation (Xu et al.) | 2026 | arXiv preprint | watermark (multi-bit, semantic | [note](../../machine-learning/llm-generated-code-detection/sources/xu-2026-synmark-semantic-coordinate-multi.md) |
| MALTO at SemEval-2026 Task 13: Detecting Human, AI, and Hybrid Code via Hard Negative Mining and Curriculum-Driven Ensembles (Arslan et al.) | 2026 | Proceedings of SemEval-2026 (ACL), pp. 2413–2420 | trained classifier | [note](../../machine-learning/llm-generated-code-detection/sources/arslan-2026-malto-at-semeval-2026.md) |
| MedHastra at SemEval-2026 Task 13: Stylometric Ensembles and Transformer Fine-Tuning for Robust AI Code Detection, Attribution, and Adversarial Analysis (Chandrasekar et al.) | 2026 | Proceedings of SemEval-2026 (ACL), pp. 2098–2103 | trained classifier | [note](../../machine-learning/llm-generated-code-detection/sources/chandrasekar-2026-medhastra-at-semeval-2026.md) |
| Hiding in Plain Sight: On the Robustness of AI-Generated Code Detection (Pordanesh et al.) | 2025 | DIMVA 2025, Springer LNCS 15748 | robustness study | [note](../../machine-learning/llm-generated-code-detection/sources/pordanesh-2025-hiding-plain-sight-robustness.md) |
| A dataset for human-written and AI-generated code source classification (Boukili et al.) | 2026 | Data in Brief | dataset/benchmark | [note](../../machine-learning/llm-generated-code-detection/sources/boukili-2026-dataset-human-written-ai.md) |

## 4. Synthesis

### 4.1 Detection methods

Four method families appear in the annotated papers.

**Text detectors transfer poorly to code.** Five off-the-shelf text detectors reach a mean accuracy of 47.83–50.83 on AI-generated code (Suh et al., 2025, Table IV), and DetectGPT scores 0.499 accuracy on Python and 0.477 on Java where a code-specific classifier reaches F1 0.992 and 0.968 (Xu et al., 2025, Table 6). In a classroom test, four of five detectors score between 0.4893 and 0.5043 accuracy on ChatGPT code, with Sapling at 0.6056 (Pan et al., 2024, Table 3), and GPTZero gave AI solutions a lower AI probability than human ones (Wang et al., 2023, §IV-B2).

**Zero-shot methods built for code do better.** Rewriting the code with a generator model and scoring the similarity of the rewrites gives an average AUROC of 80.16 on APPS and 81.81 on MBPP, against 65.38 and 61.57 for the best baseline (Ye et al., 2025, Table 3). Conditioning the score on a model-written task description reaches a mean AUROC of 94.22 on MBPP and 93.82 on APPS (Ashkenazi et al., 2025, §4.2). A perplexity-and-burstiness score for student-style assignments reaches an average AUC of 0.87 against 0.56 for GPTZero, but with one generator, text-davinci-003 (Xu & Sheng, 2024, Table 1 and Discussion). Perplexity detectors vary with the language and the solution: the best reaches AUC 91% on C/C++ and 88% on large solutions (Xu et al., 2026, Introduction). The papers use different datasets and metrics, so these figures do not form a ranking *(inference)*.

**Trained classifiers score highest in distribution.** UniXcoder reaches F1 98.65 on CoDet-M4 against 62.03 for the Fast-DetectGPT baseline (Orel, Azizov, et al., 2025, Table 2), and DroidDetectCLS-Large reaches an average weighted F1 of 97.00 in the two-class setting against 67.85 for Fast-DetectGPT (Orel, Paul, et al., 2025, Table 3). Handcrafted features with a random forest reach ROC-AUC 0.995, close to the 0.994 of CodeBERT embeddings with logistic regression (Nirob et al., 2026, Table 2); that paper does not say its benchmark is coding-problem data. On iJudge's mixed training pools, fine-tuned UniXcoder and fine-tuned Qwen2.5-Coder-1.5B tie at macro-F1 0.984, with no variance reported (Chuon et al., 2026, Tables 6–7).

**Stylometry and similarity methods suit small settings.** A classifier over 140 stylometric features reaches F1 and AUC of 0.91 on CodeChef solutions, and 0.89 once the easily gamed features are removed (Idialu et al., 2024, Table 4). Nested AST bigrams reach 0.960 accuracy against 0.72 for the ZeroGPT API (Paek & Mohan, 2025, §4.1). In courses, comparing a submission with instructor-generated AI solutions gives median similarities of 14% and 13% for students against 59% and 60% for AI code (Bashir, 2025, Table 6), and flagging over-unique or sample-matching submissions gives a mean average precision of 71% (Karnalim et al., 2026, §4.6). Clustering BLEU distances between submissions and labelling each cluster by majority classifies 97% of 30 test files for one exam question, and about 93% of 28 for a second assignment under the best Fahrenberg setting (Jégourel et al., 2024, Tables 4 and 6); the abstract's "over 90%" is the best setting per assignment, not a computed average (Jégourel et al., 2024, §7). A similarity cutoff set empirically on unlabelled data separates independent work at 0.79–0.85 from suspected AI-assisted work at 0.90–0.96 (Gacek, 2025, §3.1). Process data offers another signal: temporal features of editing sessions separate simulated wholesale delegation from other sessions with F1 0.997 (Davalos & Zhang, 2026, Table 2).

### 4.2 Datasets and benchmarks

**Benchmarks have grown fast and lean on online-judge code.** AIGCodeSet draws on 317 CodeNet problems and 4,755 human files (Demirok & Kutlu, 2025, §3.1), and MultiAIGCD on 800 CodeNet problems with six generators (Demirok et al., 2026, §3). CoDet-M4 holds 499,467 snippets (Orel, Azizov, et al., 2025, Table 1), Droid 1.06 million (Orel, Paul, et al., 2025, Table 1) and AICD Bench 2.05 million samples from 77 generators (Orel et al., 2026a, Table 2). SemEval-2026 Task 13 drew 81 teams to its binary subtask; the best macro-F1 was 0.99708 against 0.82409 for the runner-up, and 0.50819 on generator attribution (Orel et al., 2026b, Tables 4–5).

**Hard splits remove most of the apparent accuracy.** On AICD Bench the best trained model on the robust binary task, an SVM on TF-IDF, scores macro-F1 43.05, below a random baseline of 45.73 (Orel et al., 2026a, Table 4). Averaged over detectors, performance is 0.63 on a seen domain and language but 0.20 on an unseen domain (Orel et al., 2026a, Table 5). In the SemEval task, domain shift hurt more than language shift (Orel et al., 2026b, §6.1).

**Student code is the scarce resource.** Several detector studies built for education use no student submissions: CodeNet solutions stand in for coursework (Xu & Sheng, 2024; Xu & Sheng, 2025), and questions come from Quescol, Kaggle and LeetCode (Pan et al., 2024). Real course data appears mainly in smaller studies: course assignments at one institution (Wang et al., 2023), three student cohorts of a CS1 course (Ye et al., 2026), a public homework dataset and an introductory C course (Bashir, 2025), a data-structures course (Gacek, 2025), and an exam question and home project of a first-programming course (Jégourel et al., 2024, §4.1–4.2). iJudge adds 1,352 human solutions to 338 problems from one university's internal online judge, paired with 1,352 solutions from GPT-4 and Gemini (Chuon et al., 2026, §4.2.3); its authors promise the dataset for release upon acceptance (Chuon et al., 2026, Data Availability). The contrast between large benchmarks of judge code and small studies of real coursework is the review's own reading of these entries *(inference)*.

**Labels and sample sizes are often weak.** One course study has no ground-truth labels, so its evaluation is unsupervised (Gacek, 2025, §2.3). Another cannot validate individual AI-use detection without verified source labels (Ye et al., 2026, §6). A comparison of eight LLM judges with three detectors uses 18 human snippets (Djire, 2026, §3), and a clustering study tests about 100 programs per experiment (Jégourel et al., 2024, §6.1).

### 4.3 Robustness and evasion

**Distribution shift.** On CoDet-M4, the best F1 on unseen domains is 58.22 (Orel, Azizov, et al., 2025, Table 9) and UniXcoder reaches F1 39.36 on hybrid code (Orel, Azizov, et al., 2025, Table 13). The best model of an empirical study scores an average F1 of 82.55 within a dataset and 43.21 across datasets (Suh et al., 2025, Tables VI–VII). With Go held out, MultiAIGCD detectors fall to F1 0.3085 (SVM on Ada embeddings), 0.1206 (SVM on CodeT5+ embeddings) and 0.0712 (CodeBERTa) (Demirok et al., 2026, Table 8). DetectCodeGPT and GPT-Sniffer score accuracy 0.50 and F1 0.00 on every generator in a small test of 18 problems (Djire, 2026, Table 1). XGBoost trained on iJudge alone scores macro-F1 0.921 on iJudge but 0.532 on CodeChef-extended and 0.479 on CoDet-M4 (Chuon et al., 2026, Table 5).

**Code that is edited rather than written.** Recall on AIGCodeSet is 0.985 for code written from scratch but 0.677 for code with runtime errors fixed and 0.769 for corrected outputs (Demirok & Kutlu, 2025, Table 5). A Java CodeBERTa detector falls from F1 0.9815 to 0.8071 and 0.8048 on the same two tasks (Demirok et al., 2026, Table 3).

**Evasion.** Replacing half of the identifiers drives every zero-shot detector, including the rewriting detector, to random guessing (Ye et al., 2025, Fig. 9). Code blending lowers one perplexity detector to an AUC of 0.75, against 0.87 for GPTZero (Xu & Sheng, 2024, Table 3). Adversarially humanised code is caught with recall 0.92 by a detector trained on it, against 0.10 for GPT-Zero (Orel, Paul, et al., 2025, Table 5). For plagiarism tools, defences added to JPlag keep GPT-4-generated programs more similar to one another than human ones, but the signal exists only when several students submit output from the same model (Sağlam & Schmid, 2025, §5.5).

**Watermarks.** Semantics-preserving edits cut the true-positive rate of text watermarks on code from 0.76 to 0.01 (Suresh et al., 2024, Table 2), and obfuscation drives N-gram watermark detection to an AUROC near 0.5, with only 9 of 1,280 obfuscated points outside 0.4–0.6 (Zhang et al., 2025, §4.2). Code-specific schemes report strong detection: post-hoc transformations give accuracy of 97.25–100% with a false-positive rate of at most 0.17% (Li et al., 2026, Table II), AST-guided partitioning gives AUROC 84.43 on HumanEval against 70.17 for a text baseline (Guo & Cheng, 2025, Table 1), and marking only non-syntactic tokens gives AUROC 0.982 on MBPP+ against 0.867 for SWEET (Kim et al., 2026, Table 2). Their authors state limits: vulnerability to sophisticated code-transformation attacks (Guo & Cheng, 2025, App. I), and low capacity on code with few non-syntactic tokens (Kim et al., 2026, Limitations). With comments included, SWEET and EWD beat CODE ACROSTIC (Lin et al., 2025, Table 2a). Across the seven watermark papers annotated in section 3.4, none evaluates on student code: six use only HumanEval- or MBPP-family data, and Li et al. (2026) adds APPS, whose provenance the paper does not state.

### 4.4 Gaps and open problems

The gaps below follow from the evidence in section 3. Each is an inference unless a cited paper states it.

1. **Real coursework is under-tested.** Large benchmarks use judge or repository code, and the studies with real student code are small (see 4.2) *(inference)*. iJudge narrows the gap for one institution's Python submissions, but it does not model hybrid human–LLM editing (Chuon et al., 2026, §8).
2. **Mixed authorship is weak.** Hybrid code gives F1 39.36 on CoDet-M4 (Orel, Azizov, et al., 2025, Table 13), recall falls on fixed or corrected code (Demirok & Kutlu, 2025, Table 5), and the one process-based detector is tested on simulated delegation (Davalos & Zhang, 2026, Limitations).
3. **Generalisation has no settled protocol.** Reported accuracy drops sharply across domains, languages and datasets (Orel et al., 2026a, Table 5; Demirok et al., 2026, Table 8; Suh et al., 2025, Tables VI–VII). AICD Bench was built because earlier benchmarks lack standardised tasks and splits (Orel et al., 2026a, §2.2), and how well it and SemEval-2026 Task 13 predict performance on real classroom code is untested *(inference)*.
4. **Evasion is rarely tested against education detectors.** Only code blending (Xu & Sheng, 2024) and plagiarism-tool obfuscation (Sağlam & Schmid, 2025) are tried on them in the annotated set, and one course study applied no obfuscation at all (Wang et al., 2023, §VI).
5. **False accusations are barely measured.** In the annotated entries, instructors and teaching assistants had a false-positive rate of 22% (Wang et al., 2023, §IV-C). No annotated paper reports a false-positive rate for detectors on novice or non-native-English writers' code *(inference; to check against the 53 table papers)*. The fairness of flagging real students stays open.
6. **Watermarks need a cooperating provider.** A watermark can only be verified when the model that wrote the code applied it *(inference)*, and no watermark paper tests on student code (see 4.3). A student using an unwatermarked model gives a watermark detector nothing to find *(inference)*.
7. **Results are hard to compare.** Studies report accuracy, F1, AUROC and mean average precision on different data, and some use thresholds set on the test data (Gacek, 2025, §2.3) *(inference)*.

**Coverage.** The review leaves out about 21 SemEval-2026 Task 13 system papers, 11 provisionally excluded papers whose full text could not be read, and 17 leads the search could not open (section 2). Findings that rest on these would change only if the missing papers disagree with the annotated ones.

## 5. Conclusion

Detecting LLM-generated code in coding problems is no longer a one-detector question. Text detectors fail on code (Suh et al., 2025; Pan et al., 2024), code-specific zero-shot and trained detectors score well in distribution (Ye et al., 2025; Orel, Paul, et al., 2025), and the same detectors lose most of that accuracy on unseen domains, languages, edited code and obfuscation (Orel et al., 2026a; Demirok et al., 2026; Ye et al., 2025). Evidence from real student coursework is thin and small-scale next to the benchmarks *(inference)*, and watermarking has not been tested on it. The open work is evaluation on authentic student and contest data, robust handling of mixed authorship, and an honest measure of false accusations.

## References

- Adham, N., Duwe, H., & Hoos, H. H. (2026). Codetector: A framework for zero-shot detection of AI-generated code. In *Learning and Intelligent Optimization (LION 2025)* (LNCS Vol. 15745, pp. 157–173). Springer. https://doi.org/10.1007/978-3-032-09192-5_11 [adham-2025-codetector-framework-zero-shot](../../machine-learning/llm-generated-code-detection/sources/adham-2025-codetector-framework-zero-shot.md)
- Ashkenazi, M., Brenner, O., Furman Shohet, T., & Treister, E. (2025). Zero-shot detection of LLM-generated code via approximated task conditioning. In *Machine Learning and Knowledge Discovery in Databases. Research Track (ECML PKDD 2025)* (pp. 187–204). Springer. https://doi.org/10.1007/978-3-032-06078-5_11 [ashkenazi-2025-zero-shot-detection-llm](../../machine-learning/llm-generated-code-detection/sources/ashkenazi-2025-zero-shot-detection-llm.md)
- Bashir, S. (2025). Using pseudo-AI submissions for detecting AI-generated code. *Frontiers in Computer Science, 7*, Article 1549761. https://doi.org/10.3389/fcomp.2025.1549761 [bashir-2025-pseudo-ai-submissions-detecting](../../machine-learning/llm-generated-code-detection/sources/bashir-2025-pseudo-ai-submissions-detecting.md)
- Chuon, C., Leechat, P., & Vittayakorn, S. (2026). iJudge: A style-controlled educational dataset for evaluating human–LLM code authorship detection under distribution shift. *Information and Software Technology*, Article 108364. https://doi.org/10.1016/j.infsof.2026.108364 [chuon-2026-ijudge-style-controlled-educational](../../machine-learning/llm-generated-code-detection/sources/chuon-2026-ijudge-style-controlled-educational.md)
- Davalos, E., & Zhang, Y. (2026). Does AI assistance leave a temporal fingerprint? Detecting overreliance in AI-assisted writing and programming. *arXiv preprint* arXiv:2609.17883. https://arxiv.org/abs/2609.17883 [davalos-2026-does-ai-assistance-leave](../../machine-learning/llm-generated-code-detection/sources/davalos-2026-does-ai-assistance-leave.md)
- Demirok, B., & Kutlu, M. (2025). AIGCodeSet: A new annotated dataset for AI generated code detection. In *2025 33rd Signal Processing and Communications Applications Conference (SIU)* (pp. 1–4). IEEE. https://doi.org/10.1109/SIU66497.2025.11112334 [demirok-2024-aigcodeset-new-annotated-dataset](../../machine-learning/llm-generated-code-detection/sources/demirok-2024-aigcodeset-new-annotated-dataset.md)
- Demirok, B., Kutlu, M., & Mergen, S. (2026). MultiAIGCD: A comprehensive dataset for AI generated code detection covering multiple languages, models, prompts, and scenarios. *Neural Computing and Applications, 38*(16), Article 687. https://doi.org/10.1007/s00521-026-12336-0 [demirok-2025-multiaigcd-comprehensive-dataset-ai](../../machine-learning/llm-generated-code-detection/sources/demirok-2025-multiaigcd-comprehensive-dataset-ai.md)
- Djire, A. E. (2026). Code detectors have a half-life: Obsolescence and metric illusions in LLM-generated code detection. In *Proceedings of the 41st IEEE/ACM International Conference on Automated Software Engineering (ASE '26)*. ACM. https://doi.org/10.1145/3832783.3844566 [djire-2026-code-detectors-have-half](../../machine-learning/llm-generated-code-detection/sources/djire-2026-code-detectors-have-half.md)
- Gacek, P. (2025). An embedding-based approach for identifying LLM-generated code in student assignments. In *Proceedings of the Generative Code Intelligence Workshop (GeCoIn 2025) at ECAI 2025* (CEUR Workshop Proceedings, Vol. 4075). CEUR-WS.org. https://ceur-ws.org/Vol-4075/paper3.pdf [gacek-2025-embedding-based-approach-identifying](../../machine-learning/llm-generated-code-detection/sources/gacek-2025-embedding-based-approach-identifying.md)
- Guo, Z., & Cheng, M. (2025). Practical and effective code watermarking for large language models. In *Advances in Neural Information Processing Systems* (Vol. 38). https://doi.org/10.52202/085713-2485 [guo-2025-practical-effective-code-watermarking](../../machine-learning/llm-generated-code-detection/sources/guo-2025-practical-effective-code-watermarking.md)
- Gurioli, A., Gabbrielli, M., & Zacchiroli, S. (2025). Is this you, LLM? Recognizing AI-written programs with multilingual code stylometry. In *2025 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)* (pp. 394–405). IEEE. https://doi.org/10.1109/SANER64311.2025.00044 [gurioli-2024-this-you-llm-recognizing](../../machine-learning/llm-generated-code-detection/sources/gurioli-2024-this-you-llm-recognizing.md)
- Idialu, O. J., Mathews, N. S., Maipradit, R., Atlee, J. M., & Nagappan, M. (2024). Whodunit: Classifying code as human authored or GPT-4 generated—A case study on CodeChef problems. In *Proceedings of the 21st International Conference on Mining Software Repositories* (pp. 394–406). ACM. https://doi.org/10.1145/3643991.3644926 [idialu-2024-whodunit-classifying-code-as](../../machine-learning/llm-generated-code-detection/sources/idialu-2024-whodunit-classifying-code-as.md)
- Jégourel, C., Ong, J. Y., Kurniawan, O., Lim, M. S., & Chitluru, K. (2024). Sieving coding assignments over submissions generated by AI and novice programmers. In *24th Koli Calling International Conference on Computing Education Research (Koli Calling '24)*, November 12–17, 2024, Koli, Finland (11 pages). ACM. https://doi.org/10.1145/3699538.3699569 [jegourel-2024-sieving-coding-assignments-over](../../machine-learning/llm-generated-code-detection/sources/jegourel-2024-sieving-coding-assignments-over.md)
- Karnalim, O., Toba, H., Wijanto, M. C., Setiawan, Y. D., Surantha, N., & Liut, M. (2026). Detecting GenAI assistance in programming assessments with over-uniqueness and sample matching. *Discover Computing, 29*, Article 5. https://doi.org/10.1007/s10791-025-09884-9 [karnalim-2026-detecting-genai-assistance-programming](../../machine-learning/llm-generated-code-detection/sources/karnalim-2026-detecting-genai-assistance-programming.md)
- Kim, J., Park, S., & Han, Y.-S. (2026). Marking code without breaking it: Code watermarking for detecting LLM-generated code. In *Findings of the Association for Computational Linguistics: EACL 2026*. https://arxiv.org/abs/2502.18851 [kim-2025-marking-code-without-breaking](../../machine-learning/llm-generated-code-detection/sources/kim-2025-marking-code-without-breaking.md)
- Li, B., Fu, Z., Zhang, M., Zhang, P., Sun, J., & Wang, X. (2026). Efficient and universal watermarking for LLM-generated code detection. *IEEE Transactions on Software Engineering*. https://doi.org/10.1109/TSE.2026.3710556 [li-2024-efficient-universal-watermarking-llm](../../machine-learning/llm-generated-code-detection/sources/li-2024-efficient-universal-watermarking-llm.md)
- Lin, L., Xin, S., Cao, Y., & Cao, X. (2025). Code Acrostic: Robust watermarking for code generation. *arXiv preprint* arXiv:2512.14753. https://arxiv.org/abs/2512.14753 [lin-2025-code-acrostic-robust-watermarking](../../machine-learning/llm-generated-code-detection/sources/lin-2025-code-acrostic-robust-watermarking.md)
- Mao, M., Wei, D., Chen, Z., Fang, X., & Chau, M. (2024). Watermarking low-entropy generation for large language models: An unbiased and low-risk method. *arXiv preprint* arXiv:2405.14604. https://arxiv.org/abs/2405.14604 [mao-2024-watermarking-low-entropy-generation](../../machine-learning/llm-generated-code-detection/sources/mao-2024-watermarking-low-entropy-generation.md)
- Nirob, S. M. H., Ehsan, S., Rahman, M., & Haque, S. (2026). Whitespaces don't lie: Feature-driven and embedding-based approaches for detecting machine-generated code. *arXiv preprint* arXiv:2601.19264. https://arxiv.org/abs/2601.19264 [nirob-2026-whitespaces-don-t-lie](../../machine-learning/llm-generated-code-detection/sources/nirob-2026-whitespaces-don-t-lie.md)
- Orel, D., Azizov, D., & Nakov, P. (2025). CoDet-M4: Detecting machine-generated code in multi-lingual, multi-generator and multi-domain settings. In *Findings of the Association for Computational Linguistics: ACL 2025* (pp. 10570–10593). Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.findings-acl.550 [orel-2025-codet-m4-detecting-machine](../../machine-learning/llm-generated-code-detection/sources/orel-2025-codet-m4-detecting-machine.md)
- Orel, D., Azizov, D., Paul, I., Wang, Y., Gurevych, I., & Nakov, P. (2026a). AICD Bench: A challenging benchmark for AI-generated code detection. In *Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)* (pp. 6913–6938). Association for Computational Linguistics. https://doi.org/10.18653/v1/2026.eacl-long.325 [orel-2026-aicd-bench-challenging-benchmark](../../machine-learning/llm-generated-code-detection/sources/orel-2026-aicd-bench-challenging-benchmark.md)
- Orel, D., Azizov, D., Paul, I., Wang, Y., Gurevych, I., & Nakov, P. (2026b). SemEval-2026 task 13: Detecting machine-generated code with multiple programming languages, generators, and application scenarios. In *Proceedings of the 20th International Workshop on Semantic Evaluation (SemEval-2026)* (pp. 3640–3658). Association for Computational Linguistics. https://doi.org/10.18653/v1/2026.semeval-1.445 [orel-2026-semeval-2026-task-13](../../machine-learning/llm-generated-code-detection/sources/orel-2026-semeval-2026-task-13.md)
- Orel, D., Paul, I., Gurevych, I., & Nakov, P. (2025). Droid: A resource suite for AI-generated code detection. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing* (pp. 31263–31289). Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.emnlp-main.1593 [orel-2025-droid-resource-suite-ai](../../machine-learning/llm-generated-code-detection/sources/orel-2025-droid-resource-suite-ai.md)
- Paek, T., & Mohan, C. (2025). Detection of LLM-generated Java code using discretized nested bigrams. *arXiv preprint* arXiv:2502.15740. https://arxiv.org/abs/2502.15740 [paek-2025-detection-llm-generated-java](../../machine-learning/llm-generated-code-detection/sources/paek-2025-detection-llm-generated-java.md)
- Pan, W. H., Chok, M. J., Wong, J. L. S., Shin, Y. X., Poon, Y. S., Yang, Z., Chong, C. Y., Lo, D., & Lim, M. K. (2024). Assessing AI detectors in identifying AI-generated code: Implications for education. In *Proceedings of the 46th International Conference on Software Engineering: Software Engineering Education and Training* (pp. 1–11). ACM. https://doi.org/10.1145/3639474.3640068 [pan-2024-assessing-ai-detectors-identifying](../../machine-learning/llm-generated-code-detection/sources/pan-2024-assessing-ai-detectors-identifying.md)
- Sağlam, T., & Schmid, L. (2025). Evaluating software plagiarism detection in the age of AI: Automated obfuscation and lessons for academic integrity. *arXiv preprint* arXiv:2505.20158. https://arxiv.org/abs/2505.20158 [saglam-2025-evaluating-software-plagiarism-detection](../../machine-learning/llm-generated-code-detection/sources/saglam-2025-evaluating-software-plagiarism-detection.md)
- Suh, H., Tafreshipour, M., Li, J., Bhattiprolu, A., & Ahmed, I. (2025). An empirical study on automatically detecting AI-generated source code: How far are we? In *2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)* (pp. 859–871). IEEE. https://doi.org/10.1109/ICSE55347.2025.00064 [suh-2024-empirical-study-automatically-detecting](../../machine-learning/llm-generated-code-detection/sources/suh-2024-empirical-study-automatically-detecting.md)
- Suresh, T., Ugare, S., Singh, G., & Misailovic, S. (2024). Is the watermarking of LLM-generated code robust? *arXiv preprint* arXiv:2403.17983. https://arxiv.org/abs/2403.17983 [suresh-2024-watermarking-llm-generated-code](../../machine-learning/llm-generated-code-detection/sources/suresh-2024-watermarking-llm-generated-code.md)
- Wang, K., Akins, S., Mohammed, A., & Lawrence, R. (2023). Student mastery or AI deception? Analyzing ChatGPT's assessment proficiency and evaluating detection strategies. *arXiv preprint* arXiv:2311.16292. https://arxiv.org/abs/2311.16292 [wang-2023-student-mastery-or-ai](../../machine-learning/llm-generated-code-detection/sources/wang-2023-student-mastery-or-ai.md)
- Xu, J., Zhang, H., Yang, Y., Yang, L., Cheng, Z., Lyu, J., Liu, B., Zhou, X., Bacchelli, A., Chiam, Y. K., & Chiew, T. K. (2026). One size does not fit all: Investigating efficacy of perplexity in detecting LLM-generated code. *ACM Transactions on Software Engineering and Methodology, 35*(5), 1–34. https://doi.org/10.1145/3748506 [xu-2024-one-size-does-not](../../machine-learning/llm-generated-code-detection/sources/xu-2024-one-size-does-not.md)
- Xu, X., Ni, C., Guo, X., Liu, S., Wang, X., Liu, K., & Yang, X. (2025). Distinguishing LLM-generated from human-written code by contrastive learning. *ACM Transactions on Software Engineering and Methodology, 34*(4), 1–31. https://doi.org/10.1145/3705300 [xu-2024-distinguishing-llm-generated-human](../../machine-learning/llm-generated-code-detection/sources/xu-2024-distinguishing-llm-generated-human.md)
- Xu, Z., & Sheng, V. S. (2025). CodeVision: Detecting LLM-generated code using 2D token probability maps and vision models. *arXiv preprint* arXiv:2501.03288. https://arxiv.org/abs/2501.03288 [xu-2025-codevision-detecting-llm-generated](../../machine-learning/llm-generated-code-detection/sources/xu-2025-codevision-detecting-llm-generated.md)
- Xu, Z., & Sheng, V. S. (2024). Detecting AI-generated code assignments using perplexity of large language models. *Proceedings of the AAAI Conference on Artificial Intelligence, 38*(21), 23155–23162. https://doi.org/10.1609/aaai.v38i21.30361 [xu-2024-detecting-ai-generated-code](../../machine-learning/llm-generated-code-detection/sources/xu-2024-detecting-ai-generated-code.md)
- Ye, R., Fan, J., Zavaleta Bernuy, A., Karnalim, O., Denny, P., Leinonen, J., & Liut, M. (2026). Correctness, convergence, and AI-generated code detection: A longitudinal study of student and large language model code in introductory programming. In *Proceedings of the 26th Koli Calling International Conference on Computing Education Research (Koli Calling '26)*. ACM. https://doi.org/10.1145/3856208.3856226 [ye-2026-correctness-convergence-ai-generated](../../machine-learning/llm-generated-code-detection/sources/ye-2026-correctness-convergence-ai-generated.md)
- Ye, T., Du, Y., Ma, T., Wu, L., Zhang, X., Ji, S., & Wang, W. (2025). Uncovering LLM-generated code: A zero-shot synthetic code detector via code rewriting. *Proceedings of the AAAI Conference on Artificial Intelligence, 39*(1), 968–976. https://doi.org/10.1609/aaai.v39i1.32082 [ye-2024-uncovering-llm-generated-code](../../machine-learning/llm-generated-code-detection/sources/ye-2024-uncovering-llm-generated-code.md)
- Zhang, G., Li, M., Bagdasarian, E., Ma, S., & Zhai, J. (2025). Disappearing ink: Obfuscation breaks N-gram code watermarks in theory and practice. *arXiv preprint* arXiv:2507.05512. https://arxiv.org/abs/2507.05512 [zhang-2025-disappearing-ink-obfuscation-breaks](../../machine-learning/llm-generated-code-detection/sources/zhang-2025-disappearing-ink-obfuscation-breaks.md)
