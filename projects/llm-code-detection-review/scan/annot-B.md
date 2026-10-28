# Annotations — batch B

### Distinguishing LLM-generated from Human-written Code by Contrastive Learning (CodeGPTSensor)
**Reference (APA 7):** Xu, X., Ni, C., Guo, X., Liu, S., Wang, X., Liu, K., & Yang, X. (2025). Distinguishing LLM-generated from human-written code by contrastive learning. *ACM Transactions on Software Engineering and Methodology, 34*(4), 1–31. https://doi.org/10.1145/3705300
**Source note:** [xu-2024-distinguishing-llm-generated-human](../../../machine-learning/llm-generated-code-detection/sources/xu-2024-distinguishing-llm-generated-human.md)
- **Setting:** general code. Main data are GitHub functions from CodeSearchNet, not coding problems; the only problem-style data is Dα-C8, Java implementations of problems from a programming book (§6.3).
- **Method:** fine-tunes UniXcoder with a triplet contrastive loss (margin 1) to classify a function as human-written or ChatGPT-generated (§3).
- **Data:** HMCorp, 288K Python and 222K Java human/ChatGPT pairs; generator gpt-3.5-turbo, April 2023; 8:1:1 split (§4.1). Dα-C8: 1,484 Java snippets (§6.3).
- **Headline result:** On the HMCorp test set CodeGPTSensor reaches Python F1 0.992 / AUC 0.999 and Java F1 0.968 / AUC 0.995; DetectGPT accuracy is 0.499 (Python) and 0.477 (Java) (Table 6).
- **Limitation:** Only Java, Python, open-source functions and one ChatGPT version (gpt-3.5-turbo, April 2023) are covered [author-acknowledged, §7].
- **Relation:** Baselines include DetectGPT, DetectGPT4Code and GPTSniffer, which it beats in Table 6 and compares directly in §6.6.

Note: the Source note labels this "coding-problem data"; the paper's main corpus is CodeSearchNet GitHub functions. Volume, issue and pages (34(4), 1–31) come from the DOI record, not the arXiv text; the Source note's 2024 is the arXiv date.

### Uncovering LLM-Generated Code: A Zero-Shot Synthetic Code Detector via Code Rewriting
**Reference (APA 7):** Ye, T., Du, Y., Ma, T., Wu, L., Zhang, X., Ji, S., & Wang, W. (2025). Uncovering LLM-generated code: A zero-shot synthetic code detector via code rewriting. *Proceedings of the AAAI Conference on Artificial Intelligence, 39*(1), 968–976. https://doi.org/10.1609/aaai.v39i1.32082
**Source note:** [ye-2024-uncovering-llm-generated-code](../../../machine-learning/llm-generated-code-detection/sources/ye-2024-uncovering-llm-generated-code.md)
- **Setting:** general code on coding-problem data (APPS, MBPP; CodeContests for C++).
- **Method:** a generator LLM rewrites the code m times; cosine similarity between the original and each rewrite, scored by a SimCSE-tuned GraphCodeBERT, is the zero-shot score (Algorithm 1).
- **Data:** Python benchmarks from APPS test (770 human/770 synthetic per generator; GPT-4 100/100) and MBPP (233/233; GPT-4 100/100). Generators: CodeLlama-13B-Instruct, StarChat-Alpha, GPT-3.5-Turbo, GPT-4 (Tables 1–2).
- **Headline result:** With CodeLlama as detector LLM, m=8 gives average AUROC 80.16 (APPS) and 81.81 (MBPP) against 65.38 and 61.57 for the best baseline, LogRank; GPTZero scores 55.22 and 59.80 (Table 3).
- **Limitation:** After replacing 50% of identifiers, all zero-shot detectors, including this one, fall to random guessing [author-acknowledged, "Detecting Revised Synthetic Code", Fig. 9].
- **Relation:** Adapts DetectGPT to code (CodeT5-large perturber) as a baseline and reports log-probability methods degrading on code.

Note: the Source note gives 2024 (arXiv date); the AAAI-25 volume 39(1), 968–976 is from the DOI record, not the arXiv text.

### Zero-Shot Detection of LLM-Generated Code via Approximated Task Conditioning
**Reference (APA 7):** Ashkenazi, M., Brenner, O., Furman Shohet, T., & Treister, E. (2025). Zero-shot detection of LLM-generated code via approximated task conditioning. In *Machine Learning and Knowledge Discovery in Databases. Research Track (ECML PKDD 2025)* (pp. 187–204). Springer. https://doi.org/10.1007/978-3-032-06078-5_11
**Source note:** [ashkenazi-2025-zero-shot-detection-llm](../../../machine-learning/llm-generated-code-detection/sources/ashkenazi-2025-zero-shot-detection-llm.md)
- **Setting:** general code on coding-problem data (APPS, MBPP; CodeContests for C++ and Java).
- **Method:** ATC prompts a detector LLM to write a task description for the code, then scores mean code-token entropy conditioned on that task (Algorithm 1).
- **Data:** full APPS test set (3,765 instances after sanitisation), MBPP (500 test instances), CodeContests (152 C++, 129 Java; §4.7). Seven generators: GPT-3.5-Turbo, GPT-4o-mini, Claude3-haiku, StarChat-Alpha, CodeLlama-7B/13B, CodeGemma-7B (§4.1).
- **Headline result:** With CodeLlama-13B as detector and N=4 tasks, mean AUROC is 94.22 on MBPP and 93.82 on APPS (§4.2, Tables 1–2).
- **Limitation:** Results use public benchmarks only; task approximation in domain-specific repositories may be harder [author-acknowledged, §5].
- **Relation:** Takes Ye et al.'s rewriting detector as the SOTA to beat and reports its numbers as published; also compares DetectGPT, NPR and DetectCodeGPT (§4.1).

### One Size Does Not Fit All: Investigating Efficacy of Perplexity in Detecting LLM-Generated Code
**Reference (APA 7):** Xu, J., Zhang, H., Yang, Y., Yang, L., Cheng, Z., Lyu, J., Liu, B., Zhou, X., Bacchelli, A., Chiam, Y. K., & Chiew, T. K. (2026). One size does not fit all: Investigating efficacy of perplexity in detecting LLM-generated code. *ACM Transactions on Software Engineering and Methodology, 35*(5), 1–34. https://doi.org/10.1145/3748506
**Source note:** [xu-2024-one-size-does-not](../../../machine-learning/llm-generated-code-detection/sources/xu-2024-one-size-does-not.md)
- **Setting:** general code on coding-problem data (CodeNet puzzles).
- **Method:** compares eight perplexity-based detectors (incl. DetectGPT, NPR, DetectCodeGPT) with two feature-based and one pre-training-based (GPTSniffer) detector on accuracy by language, difficulty and solution size, speed, and generalisation across generators (§4–5).
- **Data:** 729 CodeNet puzzles, 8 languages, 16 human solutions per puzzle; 11,664 GPT-3.5 (gpt-3.5-turbo-0125) solutions plus 500 each from GPT-4o, Gemini-1.0, Llama-3.1; 500 pairs per evaluation cell (§4.2, §4.4).
- **Headline result:** On the CodeNet set, best perplexity AUC is 91% on C/C++ and 88% on large solutions; across the four generators perplexity gets 79.55–81.78% AUC against a 75.21–92.21% spread for the pre-training method (Introduction, §5.5, Tables 10–11).
- **Limitation:** Functions are self-contained puzzle solutions that may differ from real repositories [author-acknowledged, §7].
- **Relation:** Excludes Xu and Sheng's AIGCode Detector (batch paper 7) because its perturbation method is unspecified (§4.3.3); evaluates DetectCodeGPT and GPTSniffer.

Note: arXiv v2 carries a JACM template header; the TOSEM venue, year 2026 and 35(5), 1–34 come from the DOI record, and the Source note's 2024 is the arXiv date.

### CodeVision: Detecting LLM-Generated Code Using 2D Token Probability Maps and Vision Models
**Reference (APA 7):** Xu, Z., & Sheng, V. S. (2025). CodeVision: Detecting LLM-generated code using 2D token probability maps and vision models. *arXiv preprint* arXiv:2501.03288. https://arxiv.org/abs/2501.03288
**Source note:** [xu-2025-codevision-detecting-llm-generated](../../../machine-learning/llm-generated-code-detection/sources/xu-2025-codevision-detecting-llm-generated.md)
- **Setting:** general code on coding-problem data (CodeNet), motivated by academic integrity in programming education; no student submissions.
- **Method:** per-token log-probabilities from GPT-3.5-turbo-instruct are arranged into a line-by-token 2D matrix and classified by a ViT or ResNet trained on the maps.
- **Data:** 28,342 CodeNet samples (15,633 GPT-3.5/GPT-4, 12,709 human) in C, C++, Go, Java, Python, Ruby; 80/10/10 split; generator calls July 2024 to GPT-3.5-turbo-instruct and GPT-4-turbo (Datasets; Implementation Details). Table 2 Python set also uses SantaCoder-1.1B, CodeGeex2-6B, CodeLlama-7b, CodeQwen1.5-7B, StarCoder2-15B.
- **Headline result:** On its CodeNet-derived set, AUC is 0.96–0.99 for ResNet and 0.94–0.99 for ViT across six languages; DetectGPT gets 0.66–0.97 (Table 1). On Python from GPT-3.5-turbo, ResNet 0.98, ViT 0.96, DetectGPT 0.89 (Table 2).
- **Limitation:** Depends on the OpenAI API for probabilities (cost, availability) and offers little interpretability [author-acknowledged, Limitations].
- **Relation:** Runs DetectGPT and NPR as baselines (Table 1) and positions itself against GPTSniffer-style classifiers, SWEET-type watermarks and perturbation detectors (Related work).

### Codetector: A Framework for Zero-Shot Detection of AI-Generated Code
**Reference (APA 7):** Adham, N., Duwe, H., & Hoos, H. H. (2026). Codetector: A framework for zero-shot detection of AI-generated code. In *Learning and Intelligent Optimization (LION 2025)* (LNCS Vol. 15745, pp. 157–173). Springer. https://doi.org/10.1007/978-3-032-09192-5_11
**Source note:** [adham-2025-codetector-framework-zero-shot](../../../machine-learning/llm-generated-code-detection/sources/adham-2025-codetector-framework-zero-shot.md)
- **Setting:** general code on coding-problem and other data: LeetCode and APPS, plus CodeSearchNet and Stack Overflow.
- **Method:** a framework to generate AI code and run five existing zero-shot detectors (Fast-DetectGPT, Binoculars, rank, entropy and log-likelihood appear in Figs. 2–4), testing data leakage and sampling parameters (§1, §3).
- **Data:** 113,776 code samples from 17 LLMs over six datasets (the main text names only o1-mini and GPT-3.5-turbo, the latter as labeller); 12,294,388 detection samples. Human totals: LeetCode 1,000, APPS 561, CodeSearchNet 561, Stack Overflow 3,400. "Pre" data predate Nov 2022; "Post" data span Aug 2023–Apr 2024 (§4, Table 1).
- **Headline result:** On its generated LeetCode, APPS, CodeSearchNet and Stack Overflow data, newer detectors reach AUROC up to 97% (about 83% average); some detector–generator pairs show an absolute AUROC increase of over 40% on unseen data (§6).
- **Limitation:** Problem difficulty was not controlled when sampling [author-acknowledged, §4.2].
- **Relation:** Discusses DetectGPT, DetectGPT4Code and DetectCodeGPT as prior work (§2), and the education-oriented studies of Pan et al. and Hoq et al.

Note: the Source note gives 2025 (conference year); the paper's copyright line and volume page give 2026.

### Detecting AI-Generated Code Assignments Using Perplexity of Large Language Models
**Reference (APA 7):** Xu, Z., & Sheng, V. S. (2024). Detecting AI-generated code assignments using perplexity of large language models. *Proceedings of the AAAI Conference on Artificial Intelligence, 38*(21), 23155–23162. https://doi.org/10.1609/aaai.v38i21.30361
**Source note:** [xu-2024-detecting-ai-generated-code](../../../machine-learning/llm-generated-code-detection/sources/xu-2024-detecting-ai-generated-code.md)
- **Setting:** education (programming assignments); data are CodeNet problem solutions, built "to reflect the nature of student submissions", not real student work.
- **Method:** masks high-perplexity lines, fills them with fine-tuned CodeBERT, and ranks the original against perturbed copies on a score combining perplexity, line-perplexity deviation and burstiness (Algorithm 1).
- **Data:** about 400 CodeNet problems, 6 languages; 5,214 text-davinci-003 codes from text-to-code generation and code translation (temperature 0.6, top-p 0.1) and 5,214 human codes; 50 perturbed samples per input (Experiments Design, Hyper-Parameters).
- **Headline result:** On the AIGCode dataset, abstract: average AUC 0.87 against 0.56 for GPTZero. Per-language AUC 0.81–0.95 (GPTZero 0.28–0.90) (Table 1). Code blending bypasses it at 0.75 against 0.87 for GPTZero (Table 3).
- **Limitation:** Relies on one generator, text-davinci-003, and was not tested on other code LLMs [author-acknowledged, Discussion].
- **Relation:** Extends DetectGPT with targeted masking and 50 instead of 500 perturbed samples (Hyper-Parameters); compares DetectGPT, GPT2-Detector, RoBERTa-QA, GPTZero, Writer.

Note: the abstract gives GPTZero average AUC 0.56; the six GPTZero AUCs in Table 1 average 0.55.

### Assessing AI Detectors in Identifying AI-Generated Code: Implications for Education
**Reference (APA 7):** Pan, W. H., Chok, M. J., Wong, J. L. S., Shin, Y. X., Poon, Y. S., Yang, Z., Chong, C. Y., Lo, D., & Lim, M. K. (2024). Assessing AI detectors in identifying AI-generated code: Implications for education. In *Proceedings of the 46th International Conference on Software Engineering: Software Engineering Education and Training* (pp. 1–11). ACM. https://doi.org/10.1145/3639474.3640068
**Source note:** [pan-2024-assessing-ai-detectors-identifying](../../../machine-learning/llm-generated-code-detection/sources/pan-2024-assessing-ai-detectors-identifying.md)
- **Setting:** education (SE/CS programming); coding questions from Quescol, Kaggle and LeetCode, no student submissions.
- **Method:** tests five off-the-shelf detectors (GPTZero, Sapling, GPT-2 Detector, DetectGPT, GLTR) on ChatGPT code from 13 prompt or post-edit variants, threshold 0.5 (§3).
- **Data:** 5,069 Python problem/human-solution pairs (80 Quescol, 3,264 Kaggle, 1,725 LeetCode); ChatGPT via API, model version not reported (§3.2).
- **Headline result:** On its 5,069-sample Quescol/Kaggle/LeetCode set, Variant-1 accuracy is 0.4971 (GPTZero), 0.5043 (GPT-2 Detector), 0.4893 (DetectGPT), 0.5040 (GLTR), 0.6056 (Sapling); the maximum is 0.7693 (GLTR, Variant 7) (Table 3, §4.2).
- **Limitation:** Conclusions may be specific to the datasets analysed, and only Python is covered [author-acknowledged, §5.2.3].
- **Relation:** Uses the public DetectGPT implementation as one of the five detectors; evaluates no code-specific detector.

### Is This You, LLM? Recognizing AI-written Programs with Multilingual Code Stylometry
**Reference (APA 7):** Gurioli, A., Gabbrielli, M., & Zacchiroli, S. (2025). Is this you, LLM? Recognizing AI-written programs with multilingual code stylometry. In *2025 IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)* (pp. 394–405). IEEE. https://doi.org/10.1109/SANER64311.2025.00044
**Source note:** [gurioli-2024-this-you-llm-recognizing](../../../machine-learning/llm-generated-code-detection/sources/gurioli-2024-this-you-llm-recognizing.md)
- **Setting:** general code; human snippets are Rosetta Code task solutions (1,127 tasks; §II-A3). No education or contest data.
- **Method:** fine-tunes a CodeT5plus-770M encoder with a classification head to label code human or AI; 90 monolingual models plus one multilingual model (§II-B).
- **Data:** H-AIRosettaMP, 121,247 snippets in 10 languages; AI snippets are StarCoder2-15B translations of human snippets from another language; Rosetta Code snapshot of 1 July 2022; 470 snippets per class per sub-dataset (§II-B2); 80/20 split (§II-B3).
- **Headline result:** On H-AIRosettaMP, the multilingual model averages 84.1% ± 3.8% accuracy (Table II). In-distribution monolingual models beat re-trained baselines by +7.2 (Java), +8.9 (C++), +1.5 (Python) points (Table IV).
- **Limitation:** AI code comes from code translation by one open model, so transfer to prompted generation and other LLMs is untested beyond one dataset [author-acknowledged, §VI].
- **Relation:** Contrasts itself with GPTSniffer, which is Java-only and ChatGPT-based, and re-trains Li et al. and Oedingen et al. baselines (§VII).

Note: the Source note gives 2024 (arXiv date); the paper is SANER 2025, pp. 394–405, per the DOI record.
