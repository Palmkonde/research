# Annotations — batch C

Read from the full text of each paper (arXiv PDFs, CEUR PDF, Frontiers and Springer article pages), except the Sieving paper (abstract-level only). Locators: § = section, T = table.

### Whodunit: Classifying Code as Human Authored or GPT-4 Generated — A case study on CodeChef problems
**Reference (APA 7):** Idialu, O. J., Mathews, N. S., Maipradit, R., Atlee, J. M., & Nagappan, M. (2024). Whodunit: Classifying code as human authored or GPT-4 generated—A case study on CodeChef problems. In *Proceedings of the 21st International Conference on Mining Software Repositories* (pp. 394–406). ACM. https://doi.org/10.1145/3643991.3644926
**Source note:** [idialu-2024-whodunit-classifying-code-as](../../../machine-learning/llm-generated-code-detection/sources/idialu-2024-whodunit-classifying-code-as.md)
- **Setting:** Competitive programming (CodeChef problems), motivated by educators' academic-integrity concerns (§1).
- **Method:** XGBoost classifier on 140 code-stylometry features (31 base features: layout, lexical, syntactic/AST, Halstead, complexity), evaluated with problem-grouped ten-fold cross-validation (§3.2–3.3).
- **Data:** 399 Python problems; 798 human solutions (submitted in 2020) and 798 GPT-4 (version 0613, temperature 0) solutions, 1596 in total; a correct-only subset of 161 problems (§3.1, §4 RQ3).
- **Headline result:** F1 and AUC-ROC of 0.91 with all features; 0.89 without the gameable features (empty-line density, whitespace ratio); the replicated n-gram baseline reaches F1 0.87 (n=2) and 0.88 (n=3) (T4).
- **Limitation:** Human solutions come from CodeChef users, not novices, and only GPT-4 is covered [author-acknowledged, §6.1].
- **Relation:** Its baseline is the n-gram XGBoost method of Bukhari et al., re-implemented in Python (T4); the paper does not discuss DetectGPT, GPTSniffer, DetectCodeGPT or SWEET.

### Detection of LLM-Generated Java Code Using Discretized Nested Bigrams
**Reference (APA 7):** Paek, T., & Mohan, C. (2025). Detection of LLM-generated Java code using discretized nested bigrams. *arXiv preprint* arXiv:2502.15740. https://arxiv.org/abs/2502.15740
**Source note:** [paek-2025-detection-llm-generated-java](../../../machine-learning/llm-generated-code-detection/sources/paek-2025-detection-llm-generated-java.md)
- **Setting:** General code; the larger dataset is competitive programming (2020 Google Code Jam), the smaller one is GitHub Java files (§3.1).
- **Method:** Binary classification of 10–70-line code groups using discretized AST nested-bigram frequencies (optionally CodeBERT-embedded) with tree ensembles (§3.2–3.3).
- **Data:** GPT Dataset: 976 files (666 human, 108 Bing GPT-4, 202 ChatGPT 3.5 rewrites); GPT GCJ: 76,089 files (58,524 human, 17,565 GPT-4o rewrites); plus a 40-author, 3,021-file dataset (§3.1, §4).
- **Headline result:** On the GPT Dataset EWD-NB-F averages 0.960 accuracy against 0.72 for the ZeroGPT API (§4.1); on GPT GCJ accuracy is 0.99 and AUC 0.998–0.999 at group sizes 40 and 70 (T5).
- **Limitation:** Detection is of LLM-rewritten human code, not solutions generated from problem statements, and robustness to unseen LLM styles is untested [author-acknowledged, §5].
- **Relation:** Cites Oedingen et al., Ye et al. and Xu and Sheng as related detectors (§2.1) but does not run them; DetectGPT, GPTSniffer, DetectCodeGPT and SWEET are not discussed.

Note: The Source note gives the venue as CSCI 2024 proceedings; the PDF names no venue (only the arXiv abstract page says it will appear there), so it is cited as a preprint. The paper is inconsistent on the human-author count (11 authors in §3.1, 15 in §5) and names the baseline both ZeroGPT (§4) and GPTZero (§5).

### Whitespaces Don't Lie: Feature-Driven and Embedding-Based Approaches for Detecting Machine-Generated Code
**Reference (APA 7):** Nirob, S. M. H., Ehsan, S., Rahman, M., & Haque, S. (2026). Whitespaces don't lie: Feature-driven and embedding-based approaches for detecting machine-generated code. *arXiv preprint* arXiv:2601.19264. https://arxiv.org/abs/2601.19264
**Source note:** [nirob-2026-whitespaces-don-t-lie](../../../machine-learning/llm-generated-code-detection/sources/nirob-2026-whitespaces-don-t-lie.md)
- **Setting:** General code; the benchmark of Orel et al. is not described as coding-problem data in this paper (§IV-A).
- **Method:** Compares handcrafted stylometric/structural features (surface, identifier, AST-depth proxies) against frozen CodeBERT embeddings, each fed to standard classifiers (§IV).
- **Data:** 500k training and 100k held-out test samples, mainly Python, 80/20 stratified train–validation split; generators and class ratio not reported (§IV-A, §V).
- **Headline result:** Test set (T2): features with Random Forest reach ROC-AUC 0.995, F1 0.971, accuracy 0.970, precision 0.961; CodeBERT with logistic regression reaches ROC-AUC 0.994, F1 0.965, accuracy 0.964, precision 0.969. Top features are leading spaces and tabs (§V-B).
- **Limitation:** No cross-generator, cross-language or adversarial experiment is reported, although the Discussion claims embeddings are more robust to distribution shift [reader-inferred].
- **Relation:** Names DetectCodeGPT as a zero-shot stylistic detector (§II-C) but does not compare against it.

Note: The Source note says the dataset is DroidCollection with an algorithmic domain; the paper cites it only as Orel et al. [3] ("Droid") and states no domain, so "coding-problem data" is not confirmed by this paper.

### Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming
**Reference (APA 7):** Ye, R., Fan, J., Zavaleta Bernuy, A., Karnalim, O., Denny, P., Leinonen, J., & Liut, M. (2026). Correctness, convergence, and AI-generated code detection: A longitudinal study of student and large language model code in introductory programming. In *Proceedings of the 26th Koli Calling International Conference on Computing Education Research (Koli Calling '26)*. ACM. https://doi.org/10.1145/3856208.3856226
**Source note:** [ye-2026-correctness-convergence-ai-generated](../../../machine-learning/llm-generated-code-detection/sources/ye-2026-correctness-convergence-ai-generated.md)
- **Setting:** Education; ten weekly Python labs of one CS1 course at a research university (§3.1).
- **Method:** Evaluates "generated-reference matching": MOSS overlap between student files and LLM-generated solutions, plus exact AST-form counts for five functions, across the 2021, 2023 and 2025 cohorts (§3.4–3.5).
- **Data:** 29,970 student submissions (9,735, 10,987, 9,248) and 90,000 LLM attempts (1,000 per LLM, lab and year) from GPT-5.5, Gemini 3.1 Pro and Claude Opus 4.8 (§3.1–3.2).
- **Headline result:** 87.79–88.14% of cross-LLM pairs matched in MOSS (T3); student–LLM match incidence in 2025 was 1.76–2.12 times the 2021 rate (§4.2.2); 97.0–99.4% of cross-matches were under 30 lines (§4.3).
- **Limitation:** Without verified source labels the study cannot validate individual AI-use detection or explain why code changed [author-acknowledged, §6].
- **Relation:** Tests the pseudo-submission idea of Bashir and the sample matching of Karnalim et al. (§1, §2.3) and cites GPTSniffer as an in-distribution classifier and DetectGPT among curvature-based detectors (§1, §2.3).

### Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies
**Reference (APA 7):** Wang, K., Akins, S., Mohammed, A., & Lawrence, R. (2023). Student mastery or AI deception? Analyzing ChatGPT's assessment proficiency and evaluating detection strategies. *arXiv preprint* arXiv:2311.16292. https://arxiv.org/abs/2311.16292
**Source note:** [wang-2023-student-mastery-or-ai](../../../machine-learning/llm-generated-code-detection/sources/wang-2023-student-mastery-or-ai.md)
- **Setting:** Education; CS1 and CS2 (Java) assignments, plus a databases course, at one research university (§III-A).
- **Method:** Grades ChatGPT 3.5 on course assessments, then tests MOSS, JPlag, GPTZero and instructor/TA judgement at telling its code from student code (§III-B, §III-C).
- **Data:** 50 anonymized student submissions and 50 ChatGPT 3.5 answers; MOSS/JPlag runs on 100 submissions per question with 5%–50% AI share; GPTZero on 24 solutions (14 human, 10 AI); human survey of 32 solutions (14 AI), 10 responses (§III-C, §IV-B).
- **Headline result:** Instructors and TAs averaged recall 69.29%, precision 74.51%, F1 71.42%, accuracy 69% and false-positive rate 22% (§IV-C); GPTZero gave AI solutions very low AI probability, lower than human ones (§IV-B2, no figures).
- **Limitation:** Only ChatGPT 3.5 with a single prompt was used and no obfuscation was applied, so detection rates would likely fall in practice [author-acknowledged, §VI].
- **Relation:** Tests general-purpose tools (MOSS, JPlag, GPTZero) only; none of the anchor methods or other batch papers are discussed.

Note: MOSS and JPlag results appear only in Figures 6–9, with no numbers in the text. The Source note's venue (CSCI 2023) is not in the PDF; it comes from the arXiv comment, so the paper is cited as a preprint.

### Sieving Coding Assignments Over Submissions Generated by AI and Novice Programmers
**Reference (APA 7):** Jégourel, C., Ong, J. Y., Kurniawan, O., Shin, L. M., & Chitluru, K. (2024). Sieving coding assignments over submissions generated by AI and novice programmers. In *Proceedings of the 24th Koli Calling International Conference on Computing Education Research* (Article 12). ACM. https://doi.org/10.1145/3699538.3699569
**Source note:** NONE YET (full text unavailable; listed in [no-access.md](../../../machine-learning/llm-generated-code-detection/sources/no-access.md))
- **Setting:** *(pending source)* The abstract points to Python code from AI tools and novice programmers (education).
- **Method:** *(pending source)* The abstract mentions text-distance measures with hierarchical clustering.
- **Data:** *(pending source)*
- **Headline result:** *(pending source)* The abstract reportedly claims over 90% accuracy from distance to cluster representatives; metric, dataset and table not verified.
- **Limitation:** *(pending source)*
- **Relation:** *(pending source)* Ye et al. cite it among prior pseudo-submission and task-specific clustering studies (Ye et al., §1, §2.3).

Note: Bibliographic details come from the SUTD repository page and the reference list of Ye et al.; the abstract was reached through a page-fetch summary, not read verbatim.

### Using pseudo-AI submissions for detecting AI-generated code
**Reference (APA 7):** Bashir, S. (2025). Using pseudo-AI submissions for detecting AI-generated code. *Frontiers in Computer Science, 7*, Article 1549761. https://doi.org/10.3389/fcomp.2025.1549761
**Source note:** [bashir-2025-pseudo-ai-submissions-detecting](../../../machine-learning/llm-generated-code-detection/sources/bashir-2025-pseudo-ai-submissions-detecting.md)
- **Setting:** Education; an introductory C programming course (§4) and a public student-homework dataset (§3).
- **Method:** Instructors generate "pseudo-AI submissions" with ChatGPT, and a student submission is flagged by its Dolos (AST-fingerprint) similarity to them (§3.1).
- **Data:** 28 of 48 problems from the IEEE DataPort homework dataset (2016–2017 submissions); 14 prompts; user study with 43 students in 2 sections and 2 assignments; ChatGPT version not stated (§3, §4).
- **Headline result:** User-study median similarity to pseudo-submissions: student code 14% and 13%, AI-generated code 59% and 60% (T6, Assignments 1 and 2).
- **Limitation:** Effectiveness on long or advanced tasks is not explored, and short tasks give higher similarity [author-acknowledged, §5, §3.3].
- **Relation:** Contrasts itself with trained classifiers (Nguyen et al., Xu and Sheng, Hoq et al.) as vulnerable to prompt engineering (§1), and uses instructor-made references instead of training.

Note: The abstract claims "over 96% accuracy", but the body reports no accuracy, precision or recall; T6 ranges overlap (AI minimum 20–21%, student maximum 24–25%).

### An Embedding-Based Approach for Identifying LLM-Generated Code in Student Assignments
**Reference (APA 7):** Gacek, P. (2025). An embedding-based approach for identifying LLM-generated code in student assignments. In *Proceedings of the Generative Code Intelligence Workshop (GeCoIn 2025) at ECAI 2025* (CEUR Workshop Proceedings, Vol. 4075). CEUR-WS.org. https://ceur-ws.org/Vol-4075/paper3.pdf
**Source note:** [gacek-2025-embedding-based-approach-identifying](../../../machine-learning/llm-generated-code-detection/sources/gacek-2025-embedding-based-approach-identifying.md)
- **Setting:** Education; an Algorithms and Data Structures course at AGH University of Krakow (§3).
- **Method:** Generates k LLM solutions and rewrites per task, embeds comments-stripped code with Qodo-Embed-1, and flags students whose cosine similarity exceeds 0.94 (§2.2–2.3).
- **Data:** 509 student submissions; GPT-4o and Gemini 2.5 Flash, k=4 for the example task of 102 submissions; a survey of 50 students (§2.1, §3, §3.1). Language not stated (listings are Python).
- **Headline result:** Independently written code clustered at 0.79–0.85 cosine similarity, while suspected AI-assisted code scored 0.90–0.96 (§3.1, Figure 6); no accuracy, precision or recall is reported.
- **Limitation:** No ground-truth labels exist, so evaluation is unsupervised and the 0.94 cutoff is set empirically on the same data [author-acknowledged, §2.3, §3].
- **Relation:** Cites none of the other batch papers; it applies the reference-solution comparison idea with embeddings and positions itself against text-focused detectors (§1).

### Detecting GenAI assistance in programming assessments with over-uniqueness and sample matching
**Reference (APA 7):** Karnalim, O., Toba, H., Wijanto, M. C., Setiawan, Y. D., Surantha, N., & Liut, M. (2026). Detecting GenAI assistance in programming assessments with over-uniqueness and sample matching. *Discover Computing, 29*, Article 5. https://doi.org/10.1007/s10791-025-09884-9
**Source note:** [karnalim-2026-detecting-genai-assistance-programming](../../../machine-learning/llm-generated-code-detection/sources/karnalim-2026-detecting-genai-assistance-programming.md)
- **Setting:** Education; introductory programming courses with weekly assessments and an exam, at one institution (§4.1, §5).
- **Method:** Zero-shot, integrated into a plagiarism detector: flag submissions that are over-unique (threshold 90%) or similar to a GenAI sample (threshold 50%), using five similarity measures (§3).
- **Data:** Weekly (Python, 55 students, 26 assessments, six tutor-written GenAI submissions each, GPT-3.5); Weekly Alt (17 assessments); Weekly Align (Java, 46 students, 40 assessments); Exam (17 students, 2 exams, about half GenAI-assisted) (§4.1).
- **Headline result:** Average MAP 71% overall: over-uniqueness 63%, sample matching 77%, combined 72% (§4.6); on Weekly Align sample matching gives 64% and over-uniqueness 26% (§4.3–4.4).
- **Limitation:** The method assumes GenAI submissions are unique or similar to each other, which fails when students ask for a particular style [author-acknowledged, §5].
- **Relation:** Describes DetectGPT, GPTZero and GLTR as text detectors in its related work (§2.2) and does not compare against them.

### Does AI Assistance Leave a Temporal Fingerprint? Detecting Overreliance in AI-Assisted Writing and Programming
**Reference (APA 7):** Davalos, E., & Zhang, Y. (2026). Does AI assistance leave a temporal fingerprint? Detecting overreliance in AI-assisted writing and programming. *arXiv preprint* arXiv:2609.17883. https://arxiv.org/abs/2609.17883
**Source note:** [davalos-2026-does-ai-assistance-leave](../../../machine-learning/llm-generated-code-detection/sources/davalos-2026-does-ai-assistance-leave.md)
- **Setting:** Education-oriented programming telemetry (short lab-style tasks), not coding-problem code artifacts; also essay writing (Data).
- **Method:** Random forests on label-free temporal features (largest insertion delta, delta variability, deletion ratio) separate minimal-AI, collaborative and simulated wholesale-delegation sessions (Method).
- **Data:** RealHumanEval: 243 records, 219 traces (88 human-only, 131 collaborative); CoAuthor: 1,447 sessions (GPT-3); CS1 keystrokes: 5.1 million from 487 students; simulated delegation: 150 programming traces. Programming LLMs not reported (Data).
- **Headline result:** Programming delegation (simulated) F1 0.997, with 1 of 219 real traces (0.46%) misclassified as delegation; human-only vs collaborative F1 0.590 and 0.701, accuracy 0.794 (T2).
- **Limitation:** The delegation condition is simulated, so the features detect a specified behavior, not an observed one [author-acknowledged, Limitations].
- **Relation:** Says code detection has stayed artifact-based and that watermarks show only that a model was involved (Related Work); anchor methods are not discussed.
