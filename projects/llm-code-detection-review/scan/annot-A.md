# Annotations — batch A

### SemEval-2026 Task 13: Detecting Machine-Generated Code with Multiple Programming Languages, Generators, and Application Scenarios
**Reference (APA 7):** Orel, D., Azizov, D., Paul, I., Wang, Y., Gurevych, I., & Nakov, P. (2026). SemEval-2026 task 13: Detecting machine-generated code with multiple programming languages, generators, and application scenarios. In *Proceedings of the 20th International Workshop on Semantic Evaluation (SemEval-2026)* (pp. 3640–3658). Association for Computational Linguistics. https://doi.org/10.18653/v1/2026.semeval-1.445
**Source note:** [orel-2026-semeval-2026-task-13](../../../machine-learning/llm-generated-code-detection/sources/orel-2026-semeval-2026-task-13.md)
- **Setting:** general code on coding-problem data. Training is algorithmic code (CodeNet, TACO, LeetCode, CodeForces); the test adds research and generic deployed code (§2–3).
- **Method:** Shared-task overview with three subtasks: A binary human vs machine, B generator-family attribution, C human / AI / hybrid / adversarial (§2).
- **Data:** Subtask A: train 238,475 human + 261,525 AI (Python, Java, C++); test 390,054 human + 109,946 AI (Table 1). B: 45 generators (§2). C: 78 AI generators (Table 3). Teams: 81, 34 and 32 (§4).
- **Headline result:** Top macro-F1 was 0.99708 in A (runner-up 0.82409, baseline 0.30530; Table 4), 0.50819 in B (Table 5) and 0.78546 in C (Table 6). Domain shift hurt more than language shift (§6.1).
- **Limitation:** AST-depth, line-length and size filters remove verbose, complex or very short code common in real repositories [author-acknowledged, §8].
- **Relation:** Builds on Droid for data and on CoDet-M4 for Subtask B (§2–3); releases an enlarged version of the data as AICD Bench (§9).

### AIGCodeSet: A New Annotated Dataset for AI Generated Code Detection
**Reference (APA 7):** Demirok, B., & Kutlu, M. (2025). AIGCodeSet: A new annotated dataset for AI generated code detection. In *2025 33rd Signal Processing and Communications Applications Conference (SIU)* (pp. 1–4). IEEE. https://doi.org/10.1109/SIU66497.2025.11112334
**Source note:** [demirok-2024-aigcodeset-new-annotated-dataset](../../../machine-learning/llm-generated-code-detection/sources/demirok-2024-aigcodeset-new-annotated-dataset.md)
- **Setting:** general code on coding-problem data: 317 problems from CodeNet's 800-problem "Python Benchmark" (§3.1).
- **Method:** Builds a Python dataset in which LLMs write code from scratch, fix runtime errors or correct wrong answers, then tests Ada-embedding, TF-IDF and Bayes baselines (§3.2, §4.1).
- **Data:** 4,755 human files; 2,853 generated, 2,828 after filtering; CodeLlama 34B, Codestral 22B, Gemini 1.5 Flash; random 80/20 split (§3.1–3.3, §4.1).
- **Headline result:** Bayes classifier: F1 0.63, accuracy 0.63, precision 0.52, recall 0.81 (Table 3). Its recall is 0.985 on from-scratch code but 0.677 on fixed runtime errors and 0.769 on corrected outputs (Table 5).
- **Limitation:** Python only, three mid-size generators, and a random sample split not stated to keep a problem's files on one side [reader-inferred].
- **Relation:** Cites Suh et al. (2024) as prior Java work (§2) and reuses the Bayes classifier of Oedingen et al. (§4.1).
- Note: The arXiv text (v3) states no venue; SIU 2025 and the DOI come from Crossref. MultiAIGCD §2 gives this paper's generated count as 2,282; the paper itself says 2,828 (§3.3).

### CoDet-M4: Detecting Machine-Generated Code in Multi-Lingual, Multi-Generator and Multi-Domain Settings
**Reference (APA 7):** Orel, D., Azizov, D., & Nakov, P. (2025). CoDet-M4: Detecting machine-generated code in multi-lingual, multi-generator and multi-domain settings. In *Findings of the Association for Computational Linguistics: ACL 2025* (pp. 10570–10593). Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.findings-acl.550
**Source note:** [orel-2025-codet-m4-detecting-machine](../../../machine-learning/llm-generated-code-detection/sources/orel-2025-codet-m4-detecting-machine.md)
- **Setting:** general code on coding-problem data: LeetCode and CodeForces solutions, plus GitHub code (§3.1).
- **Method:** Builds a large human/LLM corpus, trains SVM, CatBoost and CodeBERT / CodeT5 / UniXcoder detectors, and tests unseen generators, domains, languages and hybrid code (§4).
- **Data:** 499,467 snippets (252,886 human, 246,581 LLM), Python, Java, C++ (Table 1). Generators: CodeLlama 7B, Llama3.1 8B, CodeQwen 1.5 7B, Nxcode-orpo 7B, GPT-4o (§3.2).
- **Headline result:** In distribution, UniXcoder reaches F1 98.65 against 62.03 for the Fast-DetectGPT baseline (Table 2). On unseen domains the best F1 is 58.22 (CodeT5, Table 9); on hybrid code UniXcoder gets F1 39.36 (Table 13).
- **Limitation:** Only three languages, mostly function- and class-level code, and a narrow set of prompts [author-acknowledged, §Limitations].
- **Relation:** Uses Fast-DetectGPT as its zero-shot baseline (§4.1) and reviews GPTSniffer as limited to function-level Python and Java detection (§2).

### Droid: A Resource Suite for AI-Generated Code Detection
**Reference (APA 7):** Orel, D., Paul, I., Gurevych, I., & Nakov, P. (2025). Droid: A resource suite for AI-generated code detection. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing* (pp. 31263–31289). Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.emnlp-main.1593
**Source note:** [orel-2025-droid-resource-suite-ai](../../../machine-learning/llm-generated-code-detection/sources/orel-2025-droid-resource-suite-ai.md)
- **Setting:** general code on coding-problem data: algorithmic solutions from TACO, CodeNet (AtCoder, AIZU), LeetCode and CodeForces, plus GitHub and research code (§3.1).
- **Method:** Builds DroidCollection (human, AI, machine-refined and adversarially humanised code) and trains DroidDetect, ModernBERT encoders of 149M and 396M parameters (§1, §5).
- **Data:** 1.06M samples (Table 1); 43 models, 11 families, 7 languages, 3 domains (§1); 157K preference pairs for adversarial data (§3.4).
- **Headline result:** Average weighted F1: DroidDetectCLS-Large 97.00 (2-class) and 88.78 (3-class), against 67.85 and 64.54 for Fast-DetectGPT (Table 3). Adversarial recall: GPT-Zero 0.10, DroidDetectCLS-Base 0.92 (Table 5).
- **Limitation:** Most training samples come from locally deployable models; reasoning models such as Claude 3.7 and DeepSeek R1 are left out for cost [author-acknowledged, §Limitations].
- **Relation:** Extends CoDet-M4 (§2.2) and scores GPTSniffer (2-class average 41.07) and Fast-DetectGPT as zero-shot baselines (§4.1, Table 3).

### AICD Bench: A Challenging Benchmark for AI-Generated Code Detection
**Reference (APA 7):** Orel, D., Azizov, D., Paul, I., Wang, Y., Gurevych, I., & Nakov, P. (2026). AICD Bench: A challenging benchmark for AI-generated code detection. In *Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)* (pp. 6913–6938). Association for Computational Linguistics. https://doi.org/10.18653/v1/2026.eacl-long.325
**Source note:** [orel-2026-aicd-bench-challenging-benchmark](../../../machine-learning/llm-generated-code-detection/sources/orel-2026-aicd-bench-challenging-benchmark.md)
- **Setting:** general code on coding-problem data: Droid's algorithmic, general and research domains, extended with CodeNet, StarCoderData and The Vault generations (§4).
- **Method:** Benchmark with three tasks (robust binary, model-family attribution, four-way fine-grained), scored with classical, encoder, Fast-DetectGPT and zero-shot LLM baselines (§5).
- **Data:** 2.05M samples, 77 generators, 9 languages, 11 families (Table 2); adds 500K new generations, 50K human samples (The Heap) and 100K hybrid samples (SwallowCode) to Droid (§4).
- **Headline result:** Task 1 macro-F1: best trained model SVM with TF-IDF 43.05, below the random baseline 45.73 and Fast-DetectGPT 44.99; Task 3 best is ModernBERT 61.65 (Table 4). Averaged over detectors, 0.63 on a seen domain and language but 0.20 on an unseen domain (Table 5).
- **Limitation:** It inherits DroidCollection's distribution, so Droid generators cannot be evaluated on it [author-acknowledged, §Limitations].
- **Relation:** Builds on Droid (§4), says CoDet-M4 and Droid lack standardized tasks and splits (§2.2), and uses Fast-DetectGPT as a faster DetectGPT (§5.1).

### An Empirical Study on Automatically Detecting AI-Generated Source Code: How Far Are We?
**Reference (APA 7):** Suh, H., Tafreshipour, M., Li, J., Bhattiprolu, A., & Ahmed, I. (2025). An empirical study on automatically detecting AI-generated source code: How far are we? In *2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)* (pp. 859–871). IEEE. https://doi.org/10.1109/ICSE55347.2025.00064
**Source note:** [suh-2024-empirical-study-automatically-detecting](../../../machine-learning/llm-generated-code-detection/sources/suh-2024-empirical-study-automatically-detecting.md)
- **Setting:** general code on coding-problem data: MBPP and HumanEval-X problems, plus CodeSearchNet GitHub code (§III-A).
- **Method:** Tests five text detectors and GPTSniffer on AI code, then builds fine-tuned GPT-3.5, static-metric classifiers and CodeT5+ embedding classifiers (§III).
- **Data:** MBPP 974 problems; HumanEval-X 820 samples; CodeSearchNet 400 per language; Python, Java, C++. Generators: ChatGPT, Gemini Pro, GPT-4, Starcoder2-Instruct 15B (Tables I–II).
- **Headline result:** Text detectors have mean accuracy 47.83–50.83 (Table IV); GPTSniffer averages accuracy 57.24 and average F1 45.01 (Table V). The best model (AST embeddings) scores average F1 82.55 within dataset but 43.21 across datasets (Tables VI–VII).
- **Limitation:** Findings may hold only for the selected datasets and LLMs [author-acknowledged, §VI].
- **Relation:** Runs DetectGPT (accuracy 48.99, average F1 37.42) and GPTSniffer as baselines (Tables IV–V).
- Note: Venue, pages and DOI come from Crossref; the arXiv v1 text states none. §VI says three LLMs where four are used.

### MultiAIGCD: A Comprehensive Dataset for AI Generated Code Detection Covering Multiple Languages, Models, Prompts, and Scenarios
**Reference (APA 7):** Demirok, B., Kutlu, M., & Mergen, S. (2026). MultiAIGCD: A comprehensive dataset for AI generated code detection covering multiple languages, models, prompts, and scenarios. *Neural Computing and Applications, 38*(16), Article 687. https://doi.org/10.1007/s00521-026-12336-0
**Source note:** [demirok-2025-multiaigcd-comprehensive-dataset-ai](../../../machine-learning/llm-generated-code-detection/sources/demirok-2025-multiaigcd-comprehensive-dataset-ai.md)
- **Setting:** general code on coding-problem data: 800 CodeNet problems with human submissions (§3.1).
- **Method:** Builds a dataset where six LLMs write, fix or correct code, then tests SVMs on Ada and CodeT5+ embeddings and a fine-tuned CodeBERTa, including leave-one-LLM-out and cross-language runs (§5).
- **Data:** 32,148 human and 121,271 AI snippets (Table 2); Python, Java, Go; Llama-3.3-70B, Qwen2.5-Coder-32B, GPT-4o, o3-mini, Claude 3.5 Sonnet v2, DeepSeek-V3; three prompts (§3.2).
- **Headline result:** Java CodeBERTa F1 is 0.9815 on from-scratch code but 0.8071 on runtime fixes and 0.8048 on output corrections (Table 3). With Go held out, F1 is 0.3085 (SVM Ada), 0.1206 (SVM T5+) and 0.0712 (CodeBERTa) (Table 8).
- **Limitation:** Only three detectors and a limited prompt set were tested [author-acknowledged, §6].
- **Relation:** Extends AIGCodeSet, which it calls closest in scope but Python-only (§2), and lists Suh et al. in Table 1.
- Note: Numbers are from the arXiv v1 text; journal details come from the Springer record, and the published version may differ.

### Code Detectors Have a Half-Life: Obsolescence and Metric Illusions in LLM-Generated Code Detection
**Reference (APA 7):** Djire, A. E. (2026). Code detectors have a half-life: Obsolescence and metric illusions in LLM-generated code detection. In *Proceedings of the 41st IEEE/ACM International Conference on Automated Software Engineering (ASE '26)*. ACM. https://doi.org/10.1145/3832783.3844566
**Source note:** [djire-2026-code-detectors-have-half](../../../machine-learning/llm-generated-code-detection/sources/djire-2026-code-detectors-have-half.md)
- **Setting:** general code on coding-problem data: 18 problems from the AI-Human-Generated-Program-Code dataset (§3).
- **Method:** Compares eight LLM judges under four prompting strategies with three dedicated detectors, reporting accuracy and F1 per generator (§3–4).
- **Data:** 18 human and 126 AI snippets from seven generators (StarCoder, ChatGPT, Bing AI Chat, Code Llama, CodeWhisperer, GitHub Copilot, InstructCodeT5+); C++, Python, Java; judges at temperature 0.1 (§3).
- **Headline result:** DetectCodeGPT and GPT-Sniffer score accuracy 0.50 and F1 0.00 on every generator (Table 1, Finding 1). GPT-5-mini zero-shot reaches F1 0.75–0.95, but lexico-semantic prompting drops it to 0.25–0.40 (Table 1, Finding 2).
- **Limitation:** Only 18 problems and 18 human snippets, reused for every generator, with no confidence intervals [reader-inferred].
- **Relation:** Evaluates the anchors DetectCodeGPT and GPT-Sniffer (Table 1) and contrasts itself with the single-prompt LLM-judge study of Pan et al. (§2).
- Note: Reference [12] credits DetectCodeGPT to Xu and Sheng (2024); check this matches the anchor paper. Resolved: DetectCodeGPT is Shi et al.'s method ([Source note](../../../machine-learning/llm-generated-code-detection/sources/shi-2024-between-lines-code-unraveling.md)); Xu and Sheng (2024) is a separate perplexity paper. In the review, cite Shi et al. for DetectCodeGPT and say this paper's reference list credits it to Xu and Sheng. The paper has 3 pages and no page range.

### iJudge: A style-controlled educational dataset for evaluating human–LLM code authorship detection under distribution shift
**Reference (APA 7):** Chuon, C., Leechat, P., & Vittayakorn, S. (2026). iJudge: A style-controlled educational dataset for evaluating human–LLM code authorship detection under distribution shift. *Information and Software Technology*, Article 108364. https://doi.org/10.1016/j.infsof.2026.108364
**Source note:** none yet; listed in [no-access](../../../machine-learning/llm-generated-code-detection/sources/no-access.md)
- **Setting:** education: authentic student Python submissions from an institutional online judge; the course is not named in the abstract *(pending source)*.
- **Method:** Introduces iJudge and a train x test protocol across iJudge, CodeChef-extended and CoDet-M4, testing SVM, XGBoost, UniXcoder, CodeBERT, Qwen2.5-Coder-1.5B and StarCoder2-3B, with attribution analysis *(pending source)*.
- **Data:** Sample sizes, generators and languages beyond Python are not in the abstract *(pending source)*.
- **Headline result:** Task-adapted decoder CodeLLMs perform best overall but stay sensitive to source coverage and mixture balance; the abstract gives no numbers *(pending source)*.
- **Limitation:** Single-source training transfers poorly across pools, so use is advised as assessment support, not standalone evidence of misconduct [author-acknowledged, abstract] *(pending source)*.
- **Relation:** Uses CoDet-M4 as one of its three data pools *(pending source)*.
- Note: Annotated from the abstract only. Semantic Scholar flags the DOI as open access (hybrid, CC BY-NC), so the full text may be downloadable.
