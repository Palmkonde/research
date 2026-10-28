# Slice B: education and contests

Bibliography for slice B of the [search protocol](search-protocol.md). Slice B covers studies in programming courses and exams, academic integrity, plagiarism tools facing LLM code, competitive programming and online judges, and stylometry / AST / authorship attribution. The inclusion criteria are the Scope section of the [review README](../README.md). All searches ran on 2026-10-28.

A **candidate** is a record that passed the title screen for slice B. Some hits were clearly off-topic for this slice: vulnerability detection, test generation, code-generation benchmarks, prose-only detection, and clone detection. Others were general-code detectors with no education, contest or stylometry angle, which slice A owns. None of these get an entry. The logged counts cover them. Semantic Scholar's `total` is a loose relevance count, so each S2 row also says how many top results were screened.

A candidate gets an entry only if I opened its URL and the title, authors and date on that page matched. Some publisher pages blocked automated access: ACM DL (Cloudflare 403), IEEE Xplore (empty render) and MDPI (403). For those papers the URL is the Semantic Scholar or conference-program page I opened, and the entry says so. Six title-screen leads could not be opened on any page that shows their content, so they have no entry (listed at the end of the Queries section).

## Queries

### Database searches

| # | Source | Query | Hits | Screened |
| --- | --- | --- | --- | --- |
| b1a | Semantic Scholar (2023–2026) | detecting ChatGPT generated code programming course | 2003 | top 100 |
| b1b | Semantic Scholar | AI-generated code detection programming assignments students | failed (HTTP 429 after 7 retries) | 0 |
| b1c | Semantic Scholar | LLM-generated code introductory programming CS1 detection | 364 | top 100 |
| b2a | Semantic Scholar | academic integrity ChatGPT programming assignments detection | 935 | top 100 |
| b2b | Semantic Scholar | plagiarism detection LLM generated code | 1347 | top 100 |
| b3a | Semantic Scholar | MOSS JPlag AI-generated code plagiarism | failed (429) | 0 |
| b3b | Semantic Scholar | Dolos plagiarism ChatGPT code | 102 | top 100 |
| b4a | Semantic Scholar | competitive programming AI-generated code detection | 4531 | top 100 |
| b4b | Semantic Scholar | online judge LLM generated solutions detection Codeforces | 61 | 61 |
| b5a | Semantic Scholar | stylometry LLM generated code authorship | 78 | 78 |
| b5b | Semantic Scholar | code authorship attribution large language models | failed (429) | 0 |
| b6a | Semantic Scholar | AST features distinguishing human and AI-written code | 14 | 14 |
| b7a | Semantic Scholar | AI detectors AI-generated code education | failed (429) | 0 |
| b7b | Semantic Scholar | machine-generated code detection student submissions | failed (429) | 0 |
| b8a | Semantic Scholar | GPT-4 generated code stylometric Whodunit | failed (429) | 0 |
| b8b | Semantic Scholar | ChatGPT code detection introductory programming exam | 248 | top 100 |
| b9a | Semantic Scholar | human vs AI generated code competitive programming Codeforces LeetCode | failed (429) | 0 |
| o1 | OpenAlex (from 2023-06-01) | ChatGPT generated code detection students | 23295 | top 200 |
| o2 | OpenAlex | AI-generated code detection programming education | 70598 | top 200 |
| o3 | OpenAlex | LLM-generated code plagiarism detection | 3823 | top 200 |
| o4 | OpenAlex | academic integrity generative AI programming assignments | 15521 | top 200 |
| o5 | OpenAlex | MOSS JPlag Dolos ChatGPT | 7 | 7 |
| o6 | OpenAlex | competitive programming AI-generated code detection | 45873 | top 200 |
| o7 | OpenAlex | code stylometry GPT authorship | 334 | top 200 |
| o8 | OpenAlex | AI-generated code detector | 51949 | top 200 |
| o9 | OpenAlex | distinguishing human-written and ChatGPT-generated code | 23202 | top 200 |
| o10 | OpenAlex | online judge ChatGPT cheating | 2361 | top 200 |
| o11 | OpenAlex | AST features AI-generated code classification | 5921 | top 200 |
| o12 | OpenAlex | contract cheating programming large language models detection | 1760 | top 200 |
| x1 | arXiv advanced search (abstract field, first submitted 2023-11-01 to 2026-10-31) | "generated code" detection students | 3 | 3 |
| x2 | arXiv | ChatGPT code plagiarism | 9 | 9 |
| x3 | arXiv | LLM code "academic integrity" | 26 | 26 |
| x4 | arXiv | MOSS JPlag LLM | 0 | 0 |
| x5 | arXiv | "competitive programming" AI-generated detection | 2 | 2 |
| x6 | arXiv | Codeforces LLM cheating | 0 | 0 |
| x7 | arXiv | stylometry code LLM | 4 | 4 |
| x8 | arXiv | authorship attribution code LLM-generated | 16 | 16 |
| x9 | arXiv | "AI-generated code" education | 12 | 12 |
| x10 | arXiv | "LLM-generated code" detection | 44 | 44 |
| x11 | arXiv | "AI-generated code" detection | 36 | 36 |
| x12 | arXiv | "machine-generated code" detection | 7 | 7 |
| x13 | arXiv | programming assignments generative AI detection | 7 | 7 |
| x14 | arXiv | "online judge" LLM | 10 | 10 |
| a1–a8 | arXiv export API (`export.arxiv.org/api/query`), 8 Boolean queries | e.g. `abs:"competitive programming" AND abs:"AI-generated" AND abs:detect` | failed ("Rate exceeded" / 503 over 5 retries each); replaced by x1–x14 | 0 |
| d1–d12 | DBLP publication search API (`dblp.org`, `dblp.uni-trier.de`, `dblp.dagstuhl.de`), 12 queries | e.g. "ChatGPT code detect", "AI-generated code students", "stylometry code LLM" | failed (anti-bot challenge page on all three mirrors); venue sweep moved to OpenAlex/S2 venue fields | 0 |
| acm | ACM Digital Library | landing pages | blocked (Cloudflare HTTP 403 to curl and WebFetch); ACM papers verified via SIGCSE/researchr program pages or Semantic Scholar | n/a |

### Google Scholar substitute (WebSearch)

There was no direct Google Scholar access. The queries below ran through the WebSearch tool, and each returned about 10 links.

| # | Query | Leads it added |
| --- | --- | --- |
| w1 | Hoq detecting ChatGPT-generated code CS1 course | Hoq et al. 2024; Hoq et al. 2023 (CEUR); Vahid et al. 2023 whitepaper |
| w2 | Idialu Whodunit classifying code as human authored or GPT-4 generated stylometry | Idialu et al. 2024 |
| w3 | Pan "Assessing AI detectors in identifying AI-generated code" implications for education | Pan et al. 2024 |
| w4 | detecting LLM-generated solutions Codeforces competitive programming contest cheating detection paper | none new; only Codeforces blog posts (not citable) |
| w5 | JPlag OR Dolos OR MOSS plagiarism detection AI-generated code obfuscation ChatGPT study 2024 2025 | Sağlam & Schmid 2025; Maertens et al. 2024 (Dolos) |
| w6 | ITiCSE OR "Koli Calling" OR ICER detecting AI-generated code student submissions 2024 2025 | Jegourel et al. 2024 (Koli); Gacek 2025 (GeCoIn) |
| w7 | "AI-generated" code detection CS1 students "false positives" instructors study arXiv 2025 2026 | SIGCSE 2026 program pages (Ramachandra et al.; Baek et al.) |
| w8 | keystroke OR "typing behavior" OR "editing history" detect ChatGPT pasted code programming students | 2507.22956, 2511.12468 (both writing, not code) |
| w9 | Computers & Education OR "ACM Transactions on Computing Education" detecting generative AI code programming assignments | none new |
| w10–w15 | exact-title lookups to find an openable page for already-known candidates (SIGCSE 2025 Liu et al.; SIGCSE 2025 Baek et al.; Koli 2024 "Sieving"; ITiCSE 2024 Pang & Vahid; Choi & Mohaisen TDSC; Bukhari et al. SCORED) | 2608.00227 (Yemets & Horváth) |

### Venue sweep

DBLP and ACM DL were blocked, so the venue sweep reads the venue field of every S2, OpenAlex and snowball record:

| Venue | Slice-B records found |
| --- | --- |
| ACM SIGCSE TS | 5 (Hoq 2024; Liu 2025; Baek 2025; Baek 2026; Ramachandra 2026) |
| ITiCSE | 1 (Pang & Vahid 2024, a later version of a 2023 whitepaper) |
| ICER | 0 |
| Koli Calling | 2 (Jegourel 2024; Ye 2026) |
| ACE | 0 |
| CompEd | 0 |
| Computers & Education | 0 |
| ACM TOCE | 0 |
| Education and Information Technologies | 2 (Karnalim 2024; Liu 2025) |
| ICSE-SEET | 2 (Pan 2024; Sağlam 2024, which is excluded) |
| arXiv cs.CY / cs.SE | covered by x1–x14 |

### Snowballing

The Semantic Scholar citations and references endpoints returned HTTP 429 throughout, so I snowballed with OpenAlex instead: `filter=cites:<id>` for forward citations and `referenced_works` for backward references. The same title screen was applied.

| Round | Seeds | Forward citations (unique) | Backward references (unique) | New candidates |
| --- | --- | --- | --- | --- |
| 1 | 13 seed records (Hoq 2024; Whodunit, both the MSR DOI and the arXiv record; Pan 2024; Wang 2023; Xu & Sheng 2024; Oedingen 2024; Karnalim 2026 Discover Computing; Gurioli 2025; Liu 2025 SIGCSE; Bashir 2025; Sağlam & Schmid 2025, which had no OpenAlex links) | 172 | 264 | Karnalim et al. 2024 (EAIT); Liu et al. 2025 (EAIT); Pang & Vahid 2024; Maisch et al. 2025; Baek et al. 2025; Cuellar Argotty & Manrique 2025; Adegbite & Kotzé 2025/2026; Permatasari et al. 2025; Vysocan et al. 2026; Guo & Tang 2025; Păuleț & Moruz 2025; Sağlam et al. 2024 (ICSE-SEET); Ortín et al. 2025; Lu & Wai 2026; Nitika & Narwal 2025; Chandra et al. 2026; Raghunandan et al. 2025; Choi et al. 2025 (ICDCS); Maertens et al. 2024; Bukhari et al. 2023; Irudayaraja et al. 2026 |
| 2 | 21 includes added after round 1 (Baek 2026; Ramachandra 2026; Vysocan 2026; Guo & Tang 2025; Gacek 2026; Jegourel 2024; Maisch 2025; Karnalim 2026 ACS; Permatasari 2025; Cuellar Argotty 2025; Liu 2025 EAIT; Karnalim 2024 EAIT; Paek 2025; Choi 2025 TDSC; Păuleț 2025; Baek 2025; Adegbite 2025; Ye 2026; Racovan 2026; Davalos 2026; Oedingen arXiv record) | 72 | 347 | Toba & Karnalim 2024; Maisch et al. 2026 (FSE); Sağlam et al. 2024 (ICSE, two papers) |

Ye 2026, Racovan 2026 and Davalos 2026 are 2026 arXiv preprints with no citation links yet in OpenAlex.

The last two includes were seeded separately:
- Saeheng et al. 2026 (NPC): OpenAlex has no citation links for it (0 forward, 0 backward).
- Gacek 2025 (GeCoIn): not indexed in OpenAlex. On Semantic Scholar (paper `a2cb4b31…`) it has 2 forward citations: Gacek et al. 2026 (CSEDU, already included) and "Comparative Analysis of Non-Commercial Plagiarism Detectors for Computer Science Education", which has no LLM angle in its title and failed the screen. S2 lists 0 references for it.

Round 2 and the final seeds found 4 new candidates, all background or exclude. Snowballing had saturated.

### Leads not entered (no page with matching content could be opened)

- AVERT (Vintila, ITHET 2024). IEEE only, page empty.
- Simmons et al., "AI Generated Code Plagiarism Detection in Computer Science Courses: A Literature Mapping" (FIE 2024). IEEE only. A secondary study, so background at most.
- Ha, "Programming Education Using Generative AI: Focusing on Evaluation of Code Generation Accuracy and Plagiarism Detection" (J. Digital Contents Society 2026). Both S2 and OpenAlex have no abstract.
- Karnalim, "Similarities of Human and AI Assistance in Programming Plagiarism: Student Perspective" (LNNS 2025). Not opened.
- Saeheng et al., "AI Literacy in Code: Identifying and Explaining ChatGPT-Generated Programs in Educational Settings". Mahidol repository returned 403.
- Utrecht MSc thesis on detecting AI-generated APPS solutions (studenttheses.uu.nl). Not opened.

## Included

### Detecting ChatGPT-Generated Code Submissions in a CS1 Course Using Machine Learning Models
- **Authors**: Muntasir Hoq, Yang Shi, Juho Leinonen, Damilola Babalola, Collin F. Lynch, Thomas Price, Bita Akram
- **Year / first public**: 2024-03 (SIGCSE TS 2024). An earlier workshop paper by the same group, "Detecting ChatGPT-Generated Code in a CS1 Course" (CEUR Vol-3487, 2023), is entered under Background. The SIGCSE paper adds the novice-impersonation experiment and the pattern analysis.
- **Venue**: ACM SIGCSE Technical Symposium 2024
- **URL**: https://sigcse2024.sigcse.org/details/sigcse-ts-2024-Papers-1/169/Detecting-ChatGPT-Generated-Code-Submissions-in-a-CS1-Course-Using-Machine-Learning-M (DOI 10.1145/3626252.3630826; the ACM page returned 403)
- **Access**: paywalled
- **Setting**: education
- **Method family**: trained classifier (traditional ML and AST-based deep models)
- **Dataset**: openly available dataset of CS1 student programs, plus ChatGPT solutions to the same assignments (size not on the page opened)
- **Headline result**: Both traditional ML and AST-based deep learning models identify ChatGPT-generated code with "accuracy above 90%".
- **Limitation**: Deploying the models needs ML knowledge and resources that instructors often lack [author-acknowledged].
- **Decision**: include. A CS1 setting with trained classifiers, first published 2024-03, inside the window. Flag for the synthesis that this is the extended version of a July 2023 workshop paper.

### Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies
- **Authors**: Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence
- **Year / first public**: 2023-11 (arXiv v1, 27 Nov 2023)
- **Venue**: arXiv preprint. The arXiv comment says it was published at CSCI 2023 (IEEE CPS), Research Track on Education.
- **URL**: https://arxiv.org/abs/2311.16292
- **Access**: open
- **Setting**: education
- **Method family**: robustness study (MOSS, JPlag, GPTZero and instructor/TA judgement evaluated on AI solutions)
- **Dataset**: assessments from CS1, CS2 and a databases course; GPTZero test on 24 solutions (14 human, 10 AI)
- **Headline result**: not reported as a single figure. Precision, recall and F1 for MOSS and JPlag appear only in figures, and the text reports that GPTZero gave AI solutions "very low probability of AI scores".
- **Limitation**: Similarity-based detection is weak when only a small share of submissions (5%) are AI-generated [author-acknowledged, Section on detection results].
- **Decision**: include. A course-based evaluation of plagiarism tools and an AI detector on LLM code, first public 2023-11, inside the window.

### Assessing AI Detectors in Identifying AI-Generated Code: Implications for Education
- **Authors**: Wei Hung Pan, Ming Jie Chok, Jonathan Leong Shan Wong, Yung Xin Shin, Yeong Shian Poon, Zhou Yang, Chun Yong Chong, David Lo, Mei Kuan Lim
- **Year / first public**: 2024-01 (arXiv v1, 8 Jan 2024)
- **Venue**: ICSE-SEET 2024 (DOI 10.1145/3639474.3640068)
- **URL**: https://arxiv.org/abs/2401.03676
- **Access**: open
- **Setting**: education
- **Method family**: robustness study (five AIGC detectors against 13 prompt variants)
- **Dataset**: 5,069 Python problem–solution samples (80 Quescol, 3,264 Kaggle, 1,725 LeetCode), plus ChatGPT outputs
- **Headline result**: Existing AIGC detectors perform poorly. GLTR's accuracy ranges from 0.4841 to 0.7693 across code variants (Conclusion).
- **Limitation**: The conclusions "might be specific to the dataset" used [author-acknowledged, Section 5.2.3 External Validity].
- **Decision**: include. Education framing, coding-problem data (LeetCode), detector robustness.

### Detecting AI-Generated Code Assignments Using Perplexity of Large Language Models
- **Authors**: Zhenyu Xu, Victor S. Sheng
- **Year / first public**: 2024-03 (AAAI-24 proceedings)
- **Venue**: AAAI Conference on Artificial Intelligence 2024, pp. 23155–23162
- **URL**: https://mlanthology.org/aaai/2024/xu2024aaai-detecting (DOI 10.1609/aaai.v38i21.30361; ojs.aaai.org reset the connection)
- **Access**: open
- **Setting**: education
- **Method family**: zero-shot (targeted masking perturbation with a perplexity and burstiness score)
- **Dataset**: student code assignments with text-davinci-003 outputs (size not on the page opened)
- **Headline result**: Average AUC rises from 0.56 (GPTZero baseline) to 0.87 on code generated by text-davinci-003.
- **Limitation**: The headline is reported for a single, now-retired generator (text-davinci-003) [reader-inferred].
- **Decision**: include. A zero-shot detector built for programming assignments.

### ChatGPT Code Detection: Techniques for Uncovering the Source of Code
- **Authors**: Marc Oedingen, Raphael C. Engelhardt, Robin Denz, Maximilian Hammer, Wolfgang Konen
- **Year / first public**: 2024-05 (arXiv v1, 24 May 2024)
- **Venue**: AI (MDPI), 5(3), 2024 (DOI 10.3390/ai5030053)
- **URL**: https://arxiv.org/abs/2405.15512
- **Access**: open
- **Setting**: general code on coding-problem data. The paper is framed around higher education and competitive programming.
- **Method family**: trained classifier (embedding features with DNN, RF and XGBoost) plus white-box features with a Bayes classifier
- **Dataset**: 31,400 Python samples (3.14×10⁴), with human solutions from APPS, CodeChef and others (Table 1) and paired ChatGPT solutions
- **Headline result**: 98% accuracy with embedding features and supervised learners. White-box features reach 85–88%, and untrained humans do no better than random guessing.
- **Limitation**: Only one generator family (ChatGPT) is tested, so the result may not transfer to other LLMs [reader-inferred].
- **Decision**: include. Trained classifier on coding-problem data with an education framing.

### Detecting AI assisted submissions in introductory programming via code anomaly
- **Authors**: Oscar Karnalim, Hapnes Toba, Meliana Christianti Johan
- **Year / first public**: 2024-02 (online 16 Feb 2024)
- **Venue**: Education and Information Technologies, 29, 16841–16866
- **URL**: https://link.springer.com/article/10.1007/s10639-024-12520-6
- **Access**: paywalled
- **Setting**: education
- **Method family**: stylometry/AST (34 code-anomaly features, needs no other submissions)
- **Dataset**: three introductory-programming datasets, not public
- **Headline result**: "the detector and its normalized variation are effective with 89% top-K precision" on three datasets.
- **Limitation**: Student discussion or internet access reduces effectiveness by about 25%, and so does using AI on only some tasks [author-acknowledged, abstract].
- **Decision**: include. A CS1 detector built on code-anomaly features.

### Machine Learning Models to Detect AI-Assisted Code Anomaly in Introductory Programming Course
- **Authors**: Hapnes Toba, Oscar Karnalim
- **Year / first public**: 2024-12 (online 17 Dec 2024)
- **Venue**: Advanced Technologies and the University of the Future, LNNS vol. 1140, pp. 163–181
- **URL**: https://link.springer.com/chapter/10.1007/978-3-031-71530-3_11
- **Access**: paywalled
- **Setting**: education
- **Method family**: trained classifier (tree-based, parametric and neural models on code-anomaly features)
- **Dataset**: weekly Python submissions from an introductory course, 2023–2024 first semester (size not on the page)
- **Headline result**: Random committee with all features reaches 96.7% accuracy and 62.9% recall. Meta-learning models exceed 95% accuracy on real student submissions.
- **Limitation**: A recall of 62.9% means about a third of AI-assisted submissions go undetected by the best single model [reader-inferred].
- **Decision**: include. A follow-up to the code-anomaly detector, with trained classifiers in CS1.

### Sieving Coding Assignments Over Submissions Generated by AI and Novice Programmers
- **Authors**: Cyrille Jégourel, Jung Yi Ong, Oka Kurniawan, Lim Meng Shin, Kushat Chitluru
- **Year / first public**: 2024-11 (12 Nov 2024)
- **Venue**: Koli Calling '24 (DOI 10.1145/3699538.3699569)
- **URL**: https://repository.sutd.edu.sg/esploro/outputs/conferenceProceeding/Sieving-Coding-Assignments-Over-Submissions-Generated/9911329909846
- **Access**: open (S2 lists an ACM open PDF; the ACM page itself returned 403)
- **Setting**: education
- **Method family**: zero-shot (text-distance measures with hierarchical clustering)
- **Dataset**: Python submissions from novice programmers and from AI tools (size not on the page opened)
- **Headline result**: Distances to cluster representatives predict AI versus novice origin with "an accuracy of over 90%".
- **Limitation**: Dataset size and course context are not given on the repository page, so external validity cannot be judged from the abstract [reader-inferred].
- **Decision**: include. A Koli Calling education study of a training-free detector.

### Detecting AI-Generated Pseudocode in High School Online Programming Courses Using an Explainable Approach
- **Authors**: Zifeng Liu, Xinyue Jiao, Wanli Xing, Wangda Zhu
- **Year / first public**: 2025-02 (SIGCSE TS 2025)
- **Venue**: ACM SIGCSE Technical Symposium 2025 (DOI 10.1145/3641554.3701942)
- **URL**: https://sigcse2025.sigcse.org/details/sigcse-ts-2025-Papers/70/Detecting-AI-Generated-Pseudocode-in-High-School-Online-Programming-Courses-Using-an-
- **Access**: paywalled
- **Setting**: education (K-12)
- **Method family**: trained classifier (explainable ML with SHAP)
- **Dataset**: 7,838 pseudocode submissions from 2,578 high-school students, plus 6,300 samples from three ChatGPT versions
- **Headline result**: not reported on the page opened. The journal version below reports 98.97%.
- **Limitation**: The target is pseudocode, not executable code, so the features may not carry over to program source [reader-inferred].
- **Decision**: include. An education setting with a trained classifier. It overlaps the EAIT journal version, which the synthesis should treat as the same study.

### What are the differences between student and ChatGPT-generated pseudocode? Detecting AI-generated pseudocode in high school programming using explainable machine learning
- **Authors**: Zifeng Liu, Wanli Xing, Xinyue Jiao, Chenglu Li, Wangda Zhu
- **Year / first public**: 2025-02 (published 1 Feb 2025)
- **Venue**: Education and Information Technologies, 30, 14853–14892
- **URL**: https://link.springer.com/article/10.1007/s10639-025-13385-z
- **Access**: paywalled
- **Setting**: education (K-12)
- **Method family**: trained classifier (ensemble compared against six baselines, explained with SHAP)
- **Dataset**: 7,838 student pseudocode submissions (2020–2023) and 6,300 ChatGPT samples. Hugging Face dataset `Zifeng01code/Pseudocodes`.
- **Headline result**: The ensemble model reaches 98.97% accuracy.
- **Limitation**: Student submissions resemble GPT-3 output more than other GPT versions, so accuracy may depend on which generator the student used [reader-inferred from the abstract's similarity finding].
- **Decision**: include. This is the journal extension of the SIGCSE 2025 paper, so dedupe them as one study in the synthesis.

### Leveraging LLM for Detecting and Explaining LLM-generated Code in Python Programming Courses
- **Authors**: Jeonghun Baek, Tetsuro Yamazaki, Akimasa Morihata, Junichiro Mori, Yoko Yamakata, Kenjiro Taura, Shigeru Chiba
- **Year / first public**: 2025-02 (SIGCSE TS 2025, posters track)
- **Venue**: ACM SIGCSE Technical Symposium 2025, poster (DOI 10.1145/3641555.3705212)
- **URL**: https://www.semanticscholar.org/paper/238a5f79b27883776ef21703529cf5ef559e5862 (the ACM page returned 403)
- **Access**: paywalled
- **Setting**: education
- **Method family**: trained classifier (LLM-based detector with explanations)
- **Dataset**: submissions from an introductory Python course (size not on the page)
- **Headline result**: Over 99% accuracy. Instructors judged 64.7% of the "LLM-generated" reasons appropriate.
- **Limitation**: This is a poster abstract, and the evaluation details are not on the page [reader-inferred].
- **Decision**: include. It is the precursor of the SIGCSE 2026 paper below, so dedupe the two in the synthesis.

### LLM-Based Explainable Detection of LLM-Generated Code in Python Programming Courses
- **Authors**: Jeonghun Baek, Tetsuro Yamazaki, Akimasa Morihata, Junichiro Mori, Yoko Yamakata, Kenjiro Taura, Shigeru Chiba
- **Year / first public**: 2026-02 (SIGCSE TS 2026)
- **Venue**: ACM SIGCSE Technical Symposium 2026 (DOI 10.1145/3770762.3772605)
- **URL**: https://sigcse2026.sigcse.org/details/sigcse-ts-2026-Papers/44/LLM-Based-Explainable-Detection-of-LLM-Generated-Code-in-Python-Programming-Courses
- **Access**: open (OpenAlex marks it OA)
- **Setting**: education
- **Method family**: trained classifier (fine-tuned code LLMs on labels plus GPT-4o explanations)
- **Dataset**: student-written and LLM-generated Python code from the authors' course, with explanations
- **Headline result**: Over 99% accuracy. Applied to past course data, it estimates that LLM-generated submissions rose from nearly 0% (2022A) to over 40% (2024A).
- **Limitation**: The authors devote a discussion to false positives and responsible deployment [author-acknowledged, abstract].
- **Decision**: include. First public 2026-02. CS1 Python course data. Trained classifier.

### Detecting AI-Generated Code in Introductory Programming Courses
- **Authors**: Aryan Ramachandra, Suhani Chaudhary, Justin Tran, Riti Desai, Ashley Pang, Mariam Salloum
- **Year / first public**: 2026-02 (SIGCSE TS 2026)
- **Venue**: ACM SIGCSE Technical Symposium 2026 (DOI 10.1145/3770762.3772522)
- **URL**: https://sigcse2026.sigcse.org/details/sigcse-ts-2026-Papers/73/Detecting-AI-Generated-Code-in-Introductory-Programming-Courses
- **Access**: open (OpenAlex marks it OA)
- **Setting**: education
- **Method family**: trained classifier (Random Forest, XGBoost and others)
- **Dataset**: thousands of C++ CS1 submissions plus an equal number of AI-generated solutions to the same prompts
- **Headline result**: not reported as a number on the page ("high precision and recall"). Context: 10–15% of about 350 CS1 students were cited for LLM plagiarism.
- **Limitation**: Models stayed robust when trained on noisy labels that included AI samples. The page does not quantify this [author-acknowledged, abstract].
- **Decision**: include. First public 2026-02. CS1 C++ submissions. Trained classifier.

### Using pseudo-AI submissions for detecting AI-generated code
- **Authors**: Shariq Bashir
- **Year / first public**: 2025-05 (23 May 2025)
- **Venue**: Frontiers in Computer Science (DOI 10.3389/fcomp.2025.1549761)
- **URL**: https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1549761/full
- **Access**: open
- **Setting**: education
- **Method family**: zero-shot (similarity to instructor-generated "pseudo-AI" reference submissions)
- **Dataset**: user study with programming assignments (size not in the abstract)
- **Headline result**: The method detects AI-generated code with over 96% accuracy in a user study.
- **Limitation**: Detection relies on students' AI output resembling the published pseudo-AI examples, and different prompting can make AI code harder to identify [author-acknowledged, abstract Introduction].
- **Decision**: include. First public 2025-05. Programming-assignment setting. Zero-shot reference matching against instructor-generated AI samples.

### AI-Generated Code Detection: An Examination of Current Tools in Education
- **Authors**: Juan Esteban Cuellar Argotty, Rubén Manrique
- **Year / first public**: 2025-07 (online 29 Jul 2025)
- **Venue**: ITS 2025, LNCS vol. 15723, pp. 192–201
- **URL**: https://link.springer.com/chapter/10.1007/978-3-031-98281-1_15
- **Access**: paywalled
- **Setting**: education
- **Method family**: robustness study (seven detection tools, with obfuscation)
- **Dataset**: 822 human-written and 822 AI-generated Python solutions from the Senecode platform, with AI samples varied by six prompt variants. The dataset is public on GitHub.
- **Headline result**: not reported as a number on the page opened. The abstract reports "substantial performance drops under minor obfuscation".
- **Limitation**: The tools tested are commercial text detectors (e.g. GPTZero, ZeroGPT, Originality.ai), whose versions change over time [reader-inferred].
- **Decision**: include. First public 2025-07. Introductory-programming platform data. Robustness study of detectors under obfuscation.

### Detection of GenAI-produced and student-written C# code: A comparative study of classifier algorithms and code stylometry features
- **Authors**: Adewuyi Adetayo Adegbite, Eduan Kotzé
- **Year / first public**: 2025-07 (15 Jul 2025)
- **Venue**: The African Journal of Information and Communication (AJIC), issue 35 (DOI 10.23962/ajic.i35.21309)
- **URL**: https://ajic.wits.ac.za/article/view/21309
- **Access**: open
- **Setting**: education
- **Method family**: stylometry/AST (Roslyn code-metric features with six classifiers)
- **Dataset**: verified first-year student C# code from the University of the Free State, plus Blackbox.AI, ChatGPT and Copilot code (four balanced sets)
- **Headline result**: not reported as a number in the abstract. XGBoost was strongest on GenAI code and random forest on student code.
- **Limitation**: The data come from a single institution and a single language (C#) [reader-inferred].
- **Decision**: include. First public 2025-07. First-year student C# code. Stylometry features with trained classifiers.

### Detecting GenAI assistance in programming assessments with over-uniqueness and sample matching
- **Authors**: Oscar Karnalim, Hapnes Toba, Maresha Caroline Wijanto, Yehezkiel David Setiawan, Nico Surantha, Michael Liut
- **Year / first public**: 2026-01 (online 5 Jan 2026)
- **Venue**: Discover Computing, 29, article 5
- **URL**: https://link.springer.com/article/10.1007/s10791-025-09884-9
- **Access**: open
- **Setting**: education
- **Method family**: zero-shot (no training data; over-uniqueness plus similarity to a GenAI sample)
- **Dataset**: four datasets: Weekly (Python), Weekly Alt (Python, 17 assessments), Weekly Align (Java, 40 assessments) and a 17-student simulated exam. Eight languages are supported.
- **Headline result**: 71% MAP.
- **Limitation**: Effectiveness depends on submission length and on students aligning GenAI code with their own style [author-acknowledged, abstract].
- **Decision**: include. First public 2026-01. Course assessments and exams. Zero-shot (training-free) detector.

### Machine learning approach to detect GAI-disguised academic programming plagiarism
- **Authors**: Oscar Karnalim, Yehezkiel David Setiawan, Maresha Caroline Wijanto, Rossevine Artha Nathasya
- **Year / first public**: 2026-06 (30 Jun 2026)
- **Venue**: Applied Computer Science (DOI 10.35784/acs_8915)
- **URL**: https://ph.pollub.pl/index.php/acs/article/view/8915
- **Access**: open
- **Setting**: education
- **Method family**: trained classifier, also a robustness study (23 features combining program similarity and GAI-style traits such as list comprehension, recursion and unparenthesised conditions)
- **Dataset**: 6,344 instances from a machine-intelligence course
- **Headline result**: The stacking classifier reaches 89.17% accuracy and 88.77% F-score, about twice the similarity-only baselines on most metrics.
- **Limitation**: Data come from one course, and GAI-style features may shift as models change [reader-inferred].
- **Decision**: include. Plagiarism disguised by an LLM, in an education setting. This is slice B's "plagiarism tools facing LLM code" remit.

### A Threshold Selection Method in Code Plagiarism Checking Function for Code Writing Problem in Java Programming Learning Assistant System Considering AI-Generated Codes
- **Authors**: Perwira Annissa Dyah Permatasari, Mustika Mentari, Safira Adine Kinari, Soe Thandar Aung, Nobuo Funabiki, Htoo Htoo Sandi Kyaw, Khaing Hsu Wai
- **Year / first public**: 2025-12 (26 Dec 2025)
- **Venue**: Analytics (MDPI), 5(1), 2 (DOI 10.3390/analytics5010002)
- **URL**: https://www.semanticscholar.org/paper/9cd5e9e9b336945d3b85ebb80b8024179fe1853c (mdpi.com returned 403)
- **Access**: open
- **Setting**: education
- **Method family**: zero-shot (Levenshtein similarity with an IQR-fence threshold, applied to student and AI code)
- **Dataset**: 745 Java codes: 420 from 35 first-year students (POLINEMA, 12 problems) and 325 from 65 third-year students (Okayama, 5 problems), plus code from four AI models
- **Headline result**: not reported as a number in the abstract. It says some student codes exceed the threshold against AI-generated codes, indicating GenAI use.
- **Limitation**: The method flags similarity to AI samples, not AI authorship as such [reader-inferred].
- **Decision**: include. A plagiarism checker evaluated against AI-generated code in a course.

### Detection of AI-Generated Source Code in Programming Assignments
- **Authors**: Jakub Vysocan, Lenka Bubeňková, Emília Pietriková
- **Year / first public**: 2026-07 (INES 2026)
- **Venue**: IEEE International Conference on Intelligent Engineering Systems (INES) 2026 (DOI 10.1109/INES69513.2026.11661214)
- **URL**: https://www.semanticscholar.org/paper/634dae2bdbc0cab9e565bd850ee4ee136315bc9c (the IEEE page rendered empty)
- **Access**: paywalled
- **Setting**: education
- **Method family**: trained classifier (TF-IDF character n-grams)
- **Dataset**: 16,271 C samples: 8,782 AI-generated across five LLM families, and 7,489 student solutions from 2021 (pre-ChatGPT) and 2022 cohorts
- **Headline result**: Macro-F1 0.998 on a by-student split, with significant degradation on unseen assignment types.
- **Limitation**: AI-like classification rates rise on newer cohorts whose true authorship is uncertain, so the authors recommend risk-ranking with human review [author-acknowledged, abstract].
- **Decision**: include. First public 2026-07. Student C assignments. Trained classifier with out-of-distribution robustness analysis.

### Multi-Layer Feature Fusion for Detecting AI-Generated Code in Programming Education
- **Authors**: Siqi Guo, Zhihao Tang
- **Year / first public**: 2025-12 (IEEE BigData 2025, 8 Dec 2025)
- **Venue**: IEEE International Conference on Big Data 2025 (DOI 10.1109/BigData66926.2025.11400936)
- **URL**: https://www.semanticscholar.org/paper/9d2386499be1665b15dd4503585bf0778131853c (the IEEE page rendered empty)
- **Access**: paywalled
- **Setting**: education, on algorithmic code
- **Method family**: trained classifier (ShanghaiTect: watermark check, perplexity and burstiness, AST and TF-IDF, CodeBERT embeddings)
- **Dataset**: 18,393 Python and C++ algorithmic code snippets
- **Headline result**: Average accuracy of about 98% across evaluations.
- **Limitation**: The abstract does not say where the human algorithmic code came from [reader-inferred].
- **Decision**: include. First public 2025-12. Programming-education framing on algorithmic code. Trained classifier.

### An Embedding-Based Approach for Identifying LLM-Generated Code in Student Assignments
- **Authors**: Paulina Gacek
- **Year / first public**: 2025-10 (GeCoIn 2025, 26 Oct 2025)
- **Venue**: GeCoIn 2025: Generative Code Intelligence Workshop at ECAI 2025, CEUR-WS Vol-4075
- **URL**: https://ceur-ws.org/Vol-4075/paper3.pdf
- **Access**: open
- **Setting**: education
- **Method family**: zero-shot (code-embedding similarity to LLM reference solutions)
- **Dataset**: real student assignments from a university Algorithms and Data Structures course, plus a 50-student survey
- **Headline result**: Original work clusters at cosine similarity 0.79–0.85 and likely AI-generated work at 0.90–0.96. The cutoff was set at 0.94.
- **Limitation**: No fixed threshold can separate cases perfectly, because narrow solution spaces produce similar honest code [author-acknowledged, Discussion].
- **Decision**: include. First public 2025-10. University algorithms-course assignments. Zero-shot embedding-similarity detector.

### Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming
- **Authors**: Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, Michael Liut
- **Year / first public**: 2026-10 (arXiv v1, 1 Oct 2026)
- **Venue**: arXiv preprint. Accepted at Koli Calling '26.
- **URL**: https://arxiv.org/abs/2610.00863
- **Access**: open
- **Setting**: education
- **Method family**: zero-shot (MOSS matching against a generated-reference bank, plus exact-AST-form analysis)
- **Dataset**: 29,970 student submissions from ten Python labs (2021, 2023, 2025) and 90,000 attempts from three frontier LLMs
- **Headline result**: not reported as a detection metric. Student submissions matched generated references more often in later cohorts.
- **Limitation**: Attributing AI use to an individual submission would need additional evidence beyond a match [author-acknowledged, abstract].
- **Decision**: include. First public 2026-10. Ten CS1 Python labs. Zero-shot reference-bank matching (MOSS and AST forms) evaluated as a detector.

### Argus: Academic Integrity in the Era of Generative AI
- **Authors**: David Racovan, Ajay Rawat, Christopher K. May, Jeffrey A. Turkstra
- **Year / first public**: 2026-09 (arXiv v1, 28 Sep 2026)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2609.36073
- **Access**: open
- **Setting**: education
- **Method family**: stylometry/AST, combined with behavioural indicators
- **Dataset**: six years of Spring offerings of a large-enrolment C-programming CS2 course at Purdue
- **Headline result**: 45% of enrolled students showed patterns consistent with LLM-assisted development in Spring 2026, and flagged use correlates negatively with proctored-exam scores.
- **Limitation**: The authors stress that false positives carry serious consequences and require a structured human-review process [author-acknowledged, abstract].
- **Decision**: include. First public 2026-09. CS2 course over six years. Stylometric plus behavioural indicators.

### Does AI Assistance Leave a Temporal Fingerprint? Detecting Overreliance in AI-Assisted Writing and Programming
- **Authors**: Eduardo Davalos, Yike Zhang
- **Year / first public**: 2026-09 (arXiv v1, 15 Sep 2026)
- **Venue**: arXiv preprint (submitted to AHFE 2026)
- **URL**: https://arxiv.org/abs/2609.17883
- **Access**: open
- **Setting**: education (pre-LLM CS1 keystroke corpus as baseline) and programming telemetry
- **Method family**: trained classifier (temporal process features)
- **Dataset**: RealHumanEval editor telemetry (243 programmer records), a pre-LLM CS1 corpus (5.1 M keystrokes), and CoAuthor (writing)
- **Headline result**: Temporal-feature classifiers separate simulated delegation from authentic work with F1 ≥ 0.997, and at most 0.5% of real work is misclassified.
- **Limitation**: Delegation is simulated, and ordinary collaboration stays hard to tell apart from unassisted work, pending validation in authentic coursework [author-acknowledged, abstract].
- **Decision**: include. It is borderline: process data rather than code text. Keep it as the only process-based programming entry.

### Evaluating Software Plagiarism Detection in the Age of AI: Automated Obfuscation and Lessons for Academic Integrity
- **Authors**: Timur Sağlam, Larissa Schmid
- **Year / first public**: 2025-05 (arXiv v1, 26 May 2025)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2505.20158
- **Access**: open
- **Setting**: education
- **Method family**: robustness study (JPlag defences against algorithmic and AI-based obfuscation)
- **Dataset**: several real-world programming-assignment datasets, over four million pairwise comparisons
- **Headline result**: not reported as a number in the abstract. The defences significantly improve detection of obfuscated plagiarism and also improve detection of AI-generated programs.
- **Limitation**: The defences were not designed for AI-generated programs [author-acknowledged, abstract].
- **Decision**: include. First public 2025-05. Programming-assignment datasets. Robustness study of JPlag against AI-based obfuscation and AI-generated programs.

### Towards Robust Plagiarism Detection in Programming Education: Introducing Tolerant Token Matching Techniques to Counter Novel Obfuscation Methods
- **Authors**: Robin Maisch, Nathan Hagel, Alexander Bartel
- **Year / first public**: 2025-05 (ECSEE 2025)
- **Venue**: European Conference on Software Engineering Education (ECSEE) 2025 (DOI 10.1145/3723010.3723019)
- **URL**: https://www.semanticscholar.org/paper/89d712019493db3ce7ad930b4206fa15a51c59ee (the ACM page returned 403)
- **Access**: open (OpenAlex marks it OA)
- **Setting**: education
- **Method family**: robustness study (tolerant token matching against AI-obfuscated plagiarism)
- **Dataset**: a real-life dataset with AI-obfuscated plagiarism (size not in the abstract)
- **Headline result**: The median similarity gap between originals and plagiarisms grows by 1 to 6 percentage points.
- **Limitation**: The target is plagiarism disguised by an LLM, not code written from scratch by an LLM [reader-inferred].
- **Decision**: include. This is slice B's plagiarism-tool remit.

### CDUP: Detecting AI Generated Code Using Abstract Syntax Tree Analyst
- **Authors**: Ștefan Păuleț, Alex Moruz
- **Year / first public**: 2025 (KES 2025, Procedia Computer Science)
- **Venue**: Procedia Computer Science (DOI 10.1016/j.procs.2025.09.329)
- **URL**: https://api.openalex.org/works/doi:10.1016/j.procs.2025.09.329 (sciencedirect.com returned 403; Semantic Scholar record https://www.semanticscholar.org/paper/95f856c0a240e7b5b91dd5a40a4508dc1b693bf9 matches title and authors)
- **Access**: open
- **Setting**: education (framed on student submissions)
- **Method family**: stylometry/AST (AST clone-detection techniques)
- **Dataset**: small samples of C programs (size not in the abstract)
- **Headline result**: not reported
- **Limitation**: The authors evaluate only small samples and present the work as a first step [author-acknowledged, abstract].
- **Decision**: include. It meets the scope but the evidence is weak, so give it low weight.

### NPC: Automated Tool for Detecting and Explaining ChatGPT-Generated Programs
- **Authors**: Pachanitha Saeheng, Napat Boongaree, Chutweeraya Sriwilailak, Chaiyong Ragkhitwetsagul, Teeradaj Racharak, Ekapol Chuangsuwanich
- **Year / first public**: 2026 (ICAART 2026)
- **Venue**: ICAART 2026, vol. 5, pp. 4714–4719 (DOI 10.5220/0014485500004052)
- **URL**: https://www.scitepress.org/Link.aspx?doi=10.5220/0014485500004052
- **Access**: open
- **Setting**: education
- **Method family**: trained classifier (with local neighbourhood sampling for post-hoc explanations)
- **Dataset**: not reported on the page opened
- **Headline result**: not reported. The abstract reports only that users found the explanations clear and helpful.
- **Limitation**: This is a tool paper, and no detection accuracy is reported in the abstract [reader-inferred].
- **Decision**: include. It is a tool paper in scope, so give it low weight.

### Whodunit: Classifying Code as Human Authored or GPT-4 Generated -- A case study on CodeChef problems
- **Authors**: Oseremen Joy Idialu, Noble Saji Mathews, Rungroj Maipradit, Joanne M. Atlee, Meiyappan Nagappan
- **Year / first public**: 2024-03 (arXiv v1, 6 Mar 2024)
- **Venue**: MSR 2024 (DOI 10.1145/3643991.3644926)
- **URL**: https://arxiv.org/abs/2403.04013
- **Access**: open
- **Setting**: competitive programming
- **Method family**: stylometry/AST
- **Dataset**: human CodeChef solutions and GPT-4 solutions to the same problems
- **Headline result**: F1 and AUC-ROC of 0.91. A variant without gameable features (whitespace, empty lines) reaches 0.89.
- **Limitation**: The classifier performs slightly worse on harder problems [author-acknowledged, abstract].
- **Decision**: include. First public 2024-03. Competitive programming (CodeChef). Stylometry.

### Is This You, LLM? Recognizing AI-written Programs with Multilingual Code Stylometry
- **Authors**: Andrea Gurioli, Maurizio Gabbrielli, Stefano Zacchiroli
- **Year / first public**: 2024-12 (arXiv v1, 19 Dec 2024)
- **Venue**: SANER 2025 (DOI 10.1109/SANER64311.2025.00044)
- **URL**: https://arxiv.org/abs/2412.14611
- **Access**: open
- **Setting**: general code on coding-problem data (H-AIRosettaMP, built from Rosetta Code programming tasks)
- **Method family**: stylometry/AST (transformer-encoder stylometry classifier)
- **Dataset**: H-AIRosettaMP, 121,247 snippets in 10 languages, with open LLMs only
- **Headline result**: Average accuracy of 84.1% ± 3.8% across 10 languages with one model.
- **Limitation**: Only open LLMs are used, with no proprietary models such as ChatGPT [author-acknowledged, abstract].
- **Decision**: include. First public 2024-12. Coding-problem data (Rosetta Code tasks). Stylometry classifier.

### Detection of LLM-Generated Java Code Using Discretized Nested Bigrams
- **Authors**: Timothy Paek, Chilukuri Mohan
- **Year / first public**: 2025-02 (arXiv v1, 7 Feb 2025). The arXiv comment says it precedes the CSCI 2024 proceedings version.
- **Venue**: arXiv preprint (CSCI 2024, Springer)
- **URL**: https://arxiv.org/abs/2502.15740
- **Access**: open
- **Setting**: general code on coding-problem data (GPT GCJ dataset built from Google Code Jam)
- **Method family**: stylometry/AST (discretized nested bigram frequency features)
- **Dataset**: GPT Dataset (976 Java files, GitHub authors rewritten by GPT-3.5/GPT-4), and GPT GCJ Dataset (76,089 files, more than 1,000 authors, GPT-4o)
- **Headline result**: 99% accuracy and 0.999 AUC on 76,089 GCJ files with GPT-4o. On the smaller GPT-rewrite set it exceeds 96%, against 72% for a GPT-detection API.
- **Limitation**: The AI samples are GPT rewrites of human code, not solutions generated from the problem statement [reader-inferred, Section 3.1].
- **Decision**: include. First public 2025-02. Coding-problem data (Google Code Jam). Stylometry features.

### Attributing ChatGPT-generated Source Codes
- **Authors**: Soohyeon Choi, David Mohaisen
- **Year / first public**: 2025-01 (IEEE TDSC, online 27 Jan 2025)
- **Venue**: IEEE Transactions on Dependable and Secure Computing (DOI 10.1109/TDSC.2025.3535218)
- **URL**: https://www.cs.ucf.edu/~mohaisen/p/tdsc25chatgpt
- **Access**: open (author copy)
- **Setting**: competitive programming (Google Code Jam 2017–2019, Table 1)
- **Method family**: stylometry/AST (code authorship attribution)
- **Dataset**: GCJ human solutions with ChatGPT-generated codes (about 6K samples for the binary task)
- **Headline result**: The binary ChatGPT-vs-human model reaches 87% accuracy on 6K samples. The proposed attribution reaches 81.3–91.7%, against 8.3–29.2% for the naive approach.
- **Limitation**: Off-the-shelf authorship attribution fails on ChatGPT code without the proposed regrouping step [author-acknowledged, abstract].
- **Decision**: include. First public 2025-01. Competitive-programming data (Google Code Jam). Authorship-attribution stylometry.

## Background

### Investigating Code Similarity Patterns in LLM-Generated and Human-Written Programming Solutions
- **Authors**: Paulina Gacek, Bartosz Gdowski, Konrad Szymański, Wojciech Żmuda
- **Year / first public**: 2026 (CSEDU 2026)
- **Venue**: CSEDU 2026, vol. 1, pp. 478–485 (DOI 10.5220/0014949400004021)
- **URL**: https://www.scitepress.org/Link.aspx?doi=10.5220/0014949400004021
- **Access**: open
- **Setting**: education, on algorithmic tasks
- **Method family**: empirical study (structural and lexical similarity analysis)
- **Dataset**: 9,000 solutions to constrained algorithmic tasks: human submissions from before 2023, plus GPT-5.2 and Gemini 3.0 Flash outputs
- **Headline result**: AI solutions cluster tightly, with structural similarity above 75%, against 28% for human solutions (abstract: "(>75% similarity compared to 28% for humans)").
- **Limitation**: The authors warn of model-specific masking and false positives before deployment [author-acknowledged, abstract].
- **Decision**: background. First public 2026 and in an education setting, but it characterises similarity patterns without evaluating a detector, so no Scope method family applies.

### Detecting LLM-Generated Text in Computing Education: A Comparative Study for ChatGPT Cases
- **Authors**: Michael Sheinman Orenstrakh, Oscar Karnalim, Carlos Anibal Suarez, Michael Liut
- **Year / first public**: 2023-07 (arXiv v1, 10 Jul 2023)
- **Venue**: arXiv preprint (later COMPSAC 2024, DOI 10.1109/COMPSAC61105.2024.00027)
- **URL**: https://arxiv.org/abs/2307.07411
- **Access**: open
- **Setting**: education
- **Method family**: empirical study (eight LLM-text detectors)
- **Dataset**: 124 pre-ChatGPT CS student submissions and 40 ChatGPT submissions
- **Headline result**: GPTZero produced 52 false positives out of 114 human submissions, and all detectors were less accurate on code.
- **Limitation**: The submissions are mainly prose; code is a minor part [reader-inferred from abstract].
- **Decision**: background. First public in July 2023, before the window. It is a known anchor.

### Detecting ChatGPT-Generated Code in a CS1 Course
- **Authors**: Muntasir Hoq, Yang Shi, Juho Leinonen, Damilola Babalola, Collin Lynch, Bita Akram
- **Year / first public**: 2023 (LLM@AIED 2023 workshop, CEUR-WS Vol-3487)
- **Venue**: Workshop on Empowering Education with LLMs (LLM@AIED) 2023
- **URL**: https://ceur-ws.org/Vol-3487/paper2.pdf
- **Access**: open
- **Setting**: education
- **Method family**: trained classifier (SVM, XGBoost, code2vec, ASTNN)
- **Dataset**: open CS1 student solutions plus ChatGPT code for the same assignments
- **Headline result**: Accuracies higher than 90%.
- **Limitation**: This is the workshop precursor of the SIGCSE 2024 paper [reader-inferred].
- **Decision**: background. Published in 2023 (AIED was in July), before the window. It is superseded by Hoq et al. 2024.

### ChatGPT and Cheat Detection in CS1 Using a Program Autograding System
- **Authors**: Frank Vahid, Lizbeth Areizaga, Ashley Pang. The ITiCSE 2024 version (DOI 10.1145/3649217.3653558) lists Ashley Pang and Frank Vahid.
- **Year / first public**: 2023-02 (zyBooks whitepaper, 17 Feb 2023)
- **Venue**: zyBooks white paper. Later ITiCSE 2024.
- **URL**: https://www.zybooks.com/research-items/chatgpt-and-cheat-detection-in-cs1-using-a-program-autograding-system/
- **Access**: open
- **Setting**: education
- **Method family**: empirical study (autograder style-anomaly, similarity and time flags)
- **Dataset**: 10 CS1 assignments with ChatGPT acting as 20 students
- **Headline result**: not reported as a number. Style anomalies were flagged automatically, and with 5 or more ChatGPT users in a class the similarity checker would likely flag them.
- **Limitation**: The study is simulated, with no real students [reader-inferred].
- **Decision**: background. First public in February 2023, before the window. The ITiCSE 2024 paper is a later version of the same study.

### Inappropriate Benefits and Identification of ChatGPT Misuse in Programming Tests: A Controlled Experiment
- **Authors**: Hapnes Toba, Oscar Karnalim, Meliana Christianti Johan, Terutoshi Tada, Yenni Merlin Djajalaksana, Tristan Vivaldy
- **Year / first public**: 2023-08 (arXiv v1, 11 Aug 2023)
- **Venue**: ICL 2023 (LNNS)
- **URL**: https://arxiv.org/abs/2309.16697
- **Access**: open
- **Setting**: education
- **Method family**: empirical study (controlled experiment and manual identification)
- **Dataset**: 17 students, two programming tests
- **Headline result**: Students using ChatGPT finish tests about twice as fast with comparable performance. Detection is manual and not quantified.
- **Limitation**: n = 17 [reader-inferred].
- **Decision**: background. August 2023, before the window.

### Discriminating Human-authored from ChatGPT-Generated Code Via Discernable Feature Analysis
- **Authors**: Li Ke, Hong Sheng, Fu Cai, Zhang Yunhe, Liu Ming
- **Year / first public**: 2023-06 (arXiv v1, 26 Jun 2023)
- **Venue**: ISSREW 2023
- **URL**: https://arxiv.org/abs/2306.14397
- **Access**: open
- **Setting**: general code (open-source repositories)
- **Method family**: stylometry/AST
- **Dataset**: about 10,000 lines of ChatGPT code plus cleaned open-source human code
- **Headline result**: not reported as a number in the abstract ("high accuracy").
- **Limitation**: Repository code, not coding problems [reader-inferred].
- **Decision**: background. June 2023, a foundational stylometry paper.

### Is this Snippet Written by ChatGPT? An Empirical Study with a CodeBERT-Based Classifier
- **Authors**: Phuong T. Nguyen, Juri Di Rocco, Claudio Di Sipio, Riccardo Rubei, Davide Di Ruscio, Massimiliano Di Penta
- **Year / first public**: 2023-07 (arXiv v1, 18 Jul 2023)
- **Venue**: arXiv preprint (later JSS 2024 as GPTSniffer)
- **URL**: https://arxiv.org/abs/2307.09381
- **Access**: open
- **Setting**: general code
- **Method family**: trained classifier (CodeBERT)
- **Dataset**: paired human and ChatGPT snippets
- **Headline result**: not reported as a number in the abstract. It outperforms GPTZero and the OpenAI Text Classifier.
- **Limitation**: The dataset composition was not checked; it is cited only as a pre-window baseline [reader-inferred].
- **Decision**: background. GPTSniffer, named in the README as a foundational paper, dated July 2023.

### ChatGPT-Generated Code Assignment Detection Using Perplexity of Large Language Models (Student Abstract)
- **Authors**: Zhenyu Xu, Ruoyu Xu, Victor S. Sheng
- **Year / first public**: 2024-03 (AAAI-24)
- **Venue**: AAAI 2024 Student Abstract (DOI 10.1609/aaai.v38i21.30527)
- **URL**: https://api.openalex.org/works/doi:10.1609/aaai.v38i21.30527 (ojs.aaai.org reset the connection)
- **Access**: open
- **Setting**: education
- **Method family**: zero-shot
- **Dataset**: as in Xu & Sheng 2024
- **Headline result**: Average AUC rises from 0.56 (GPTZero) to 0.87.
- **Limitation**: This is a two-page companion to the main AAAI paper [reader-inferred].
- **Decision**: background. It duplicates Xu & Sheng 2024, so cite the main paper.

### The Failure of Plagiarism Detection in Competitive Programming
- **Authors**: Ethan Dickey
- **Year / first public**: 2025-05 (arXiv v1, 13 May 2025)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2505.08244
- **Access**: open
- **Setting**: competitive programming (course)
- **Method family**: empirical study (experience report and literature review of Moss, Kattis and oral interviews)
- **Dataset**: seven semesters of a Purdue CP1 course (about 100 students each)
- **Headline result**: not reported
- **Limitation**: Experience-based observations, not a controlled evaluation [author-acknowledged, abstract].
- **Decision**: background. In the window and setting, but no detection method is evaluated. Useful for the synthesis of contest settings.

### Assessing the Prevalence of AI-assisted Cheating in Programming Courses: A Pilot Study
- **Authors**: Kaléu Delphino
- **Year / first public**: 2025-07 (arXiv v1, 8 Jul 2025)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2507.06438
- **Access**: open
- **Setting**: education
- **Method family**: empirical study (anonymous survey and interviews)
- **Dataset**: one CS class, n = 120
- **Headline result**: More than 25% of survey respondents admitted AI plagiarism.
- **Limitation**: Only one student agreed to be interviewed [author-acknowledged, abstract].
- **Decision**: background. It measures prevalence, not detection.

### Evaluating AI-Generated C# Code in Computing Education: Implications for Academic Integrity
- **Authors**: Adewuyi Adetayo Adegbite, Eduan Kotzé
- **Year / first public**: 2026-01 (online 2 Jan 2026)
- **Venue**: ICT Education (SACLA 2025), CCIS vol. 2770, pp. 119–136
- **URL**: https://link.springer.com/chapter/10.1007/978-3-032-12457-9_8
- **Access**: paywalled
- **Setting**: education
- **Method family**: empirical study (questionnaire, code examination, grade comparison)
- **Dataset**: 368 questionnaire responses plus code samples
- **Headline result**: not reported as a detection metric. AI code showed detectable patterns and outscored human code in grading.
- **Limitation**: No detector is evaluated [reader-inferred].
- **Decision**: background. First public 2026-01 and in an education setting, but a questionnaire and grading study with no detector evaluated.

### Source Code Authorship Attribution Does Not Generalize from Competitions to Classrooms
- **Authors**: Serhii Yemets, Marek Horváth
- **Year / first public**: 2026-07 (arXiv v1, 31 Jul 2026)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2608.00227
- **Access**: open
- **Setting**: competitive programming and education (human authors only)
- **Method family**: stylometry/AST (CodeBERT authorship attribution)
- **Dataset**: GCJ (Kaggle and a curated archive), plus coursework datasets of 690 and 812 authors
- **Headline result**: 92.6% Top-1 on GCJ with 10 authors, against 0.2% and 0.06% Top-1 on coursework (at or below chance).
- **Limitation**: Human-vs-human attribution only, with no LLM code [reader-inferred].
- **Decision**: background. It does not detect LLM code, but it directly tests whether GCJ-trained stylometry transfers to classrooms. That matters for Whodunit, Paek and Choi.

### Distinguishing AI- and Human-Generated Code: A Case Study
- **Authors**: Sufiyan Bukhari, Benjamin Tan, Lorenzo De Carli
- **Year / first public**: 2023-11 (SCORED '23 at CCS, 26 Nov 2023)
- **Venue**: SCORED@CCS 2023 (DOI 10.1145/3605770.3625215)
- **URL**: https://www.semanticscholar.org/paper/914a3d8c8f96aa4ea7139cf1a370e648d2aa40bd (the ACM page returned 403)
- **Access**: open (OpenAlex lists an ACM PDF)
- **Setting**: out of scope as framed. The paper is about software supply-chain provenance, and the dataset is described only as "a standardized task".
- **Method family**: stylometry/AST (lexical and syntactic features)
- **Dataset**: not named on the page opened
- **Headline result**: Accuracy up to 92%.
- **Limitation**: The setting could not be confirmed from the abstract [reader-inferred].
- **Decision**: background. In the date window with a stylometry method, but neither an education setting nor coding-problem data could be confirmed. Upgrade it to include if the full text shows coding-problem data.

### Attributing ChatGPT-Transformed Synthetic Code
- **Authors**: Soohyeon Choi, Ali Alkinoon, Ahod Alghuried, Abdulaziz Alghamdi, David Mohaisen
- **Year / first public**: 2025-07 (ICDCS 2025)
- **Venue**: IEEE ICDCS 2025 (DOI 10.1109/ICDCS63083.2025.00018)
- **URL**: https://www.semanticscholar.org/paper/3ccecf475d1fe276e0d155f47747d3e24324e5c2 (the IEEE page rendered empty)
- **Access**: paywalled
- **Setting**: unconfirmed. This is probably the GCJ line of work from the TDSC paper, but the dataset is not stated on the page opened.
- **Method family**: robustness study (authorship attribution on ChatGPT-transformed code)
- **Dataset**: not stated on the page opened
- **Headline result**: A binary authorship model reaches up to 93% accuracy on ChatGPT-transformed code.
- **Limitation**: ChatGPT produced at most 12 distinct styles when transforming code [author-acknowledged, abstract].
- **Decision**: background. Relevant to robustness, but the coding-problem setting is unconfirmed. Slice C may also hold it.

### Criminal Minds: How First-Year CS Students Plagiarize Code
- **Authors**: Robin Maisch, Larissa Schmid, Richard J. Glassey, Dominik Fuchß, Nils Niehues, Haoyu Liu, Anne Koziolek
- **Year / first public**: 2026-07 (ESEC/FSE 2026)
- **Venue**: ESEC/FSE 2026 (DOI 10.1145/3803437.3805789)
- **URL**: https://www.semanticscholar.org/paper/d4b9df749ee23d159ff9510cb96016f98c364e17 (the ACM page returned 403)
- **Access**: open (OpenAlex marks it OA)
- **Setting**: education
- **Method family**: empirical study (students asked to plagiarise and evade detectors)
- **Dataset**: plagiarism attempts from students at two universities
- **Headline result**: not reported as a number. Only a few submissions plagiarise successfully, and the strategies include LLM-based obfuscation.
- **Limitation**: LLM use is one strategy among many, and detecting LLM code is not the target [reader-inferred].
- **Decision**: background. First public 2026-07 and in an education setting. LLM-based obfuscation is one plagiarism strategy among many, and LLM-code detection is not evaluated.

### On Seeding Watermarks to Detect Verbatim LLM Copy-Paste Responses
- **Authors**: Aizierjiang Aiersilan, Artin Yousefi, Robert Pless
- **Year / first public**: 2026-05 (arXiv v1, 7 May 2026)
- **Venue**: arXiv preprint (accepted at AIES 2026)
- **URL**: https://arxiv.org/abs/2605.16336
- **Access**: open
- **Setting**: education (all assignment types, not programming-specific)
- **Method family**: watermark (input-side, a hidden instruction in the assignment prompt)
- **Dataset**: compliance across eight LLM families and educational content channels
- **Headline result**: not reported as a number in the abstract.
- **Limitation**: The evaluation is not specific to code [reader-inferred from abstract].
- **Decision**: background. It is an educator-controlled watermark relevant to slice C, but not evaluated on programming assignments.

## Excluded

### I Know Which LLM Wrote Your Code Last Summer: LLM generated Code Stylometry for Authorship Attribution
- **Authors**: Tamas Bisztray, Bilel Cherif, Richard A. Dubniczky, et al.
- **Year / first public**: 2025-06 (arXiv v1, 18 Jun 2025)
- **Venue**: AISec@CCS 2025
- **URL**: https://arxiv.org/abs/2506.17323
- **Access**: open
- **Setting**: out of scope
- **Method family**: stylometry/AST
- **Dataset**: LLM-AuthorBench, 32,000 C programs from eight LLMs
- **Headline result**: 97.56% binary accuracy (GPT-4.1 vs GPT-4o) and 95.40% five-class attribution.
- **Limitation**: No human-written code [reader-inferred].
- **Decision**: exclude. It attributes code between LLMs, not human versus LLM.

### The Hidden DNA of LLM-Generated JavaScript: Structural Patterns Enable High-Accuracy Authorship Attribution
- **Authors**: Norbert Tihanyi, Bilel Cherif, Richard A. Dubniczky, Mohamed Amine Ferrag, Tamás Bisztray
- **Year / first public**: 2025-10 (arXiv v1, 12 Oct 2025)
- **Venue**: LLM4Code@ICSE 2026
- **URL**: https://arxiv.org/abs/2510.10493
- **Access**: open
- **Setting**: out of scope
- **Method family**: stylometry/AST
- **Dataset**: LLM-NodeJS, 50,000 Node.js back-ends from 20 LLMs
- **Headline result**: 95.8% five-class attribution accuracy.
- **Limitation**: LLM-only data [reader-inferred].
- **Decision**: exclude. Model-to-model attribution on back-end code, with no human code or coding problems.

### Code Fingerprints: Disentangled Attribution of LLM-Generated Code
- **Authors**: Jiaxun Guo, Ziyuan Yang, Mengyu Sun, et al.
- **Year / first public**: 2026-03 (arXiv v1, 4 Mar 2026)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2603.04212
- **Access**: open
- **Setting**: out of scope
- **Method family**: trained classifier
- **Dataset**: code from DeepSeek, Claude, Qwen and ChatGPT
- **Headline result**: not reported in the abstract excerpt.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. Model-level attribution between LLMs.

### GoCoMA: Hyperbolic Multimodal Representation Fusion for Large Language Model-Generated Code Attribution
- **Authors**: Nitin Choudhury, Bikrant Bikram Pratap Maurya, Bhavinkumar Vinodbhai Kuwar, Arun Balaji Buduru
- **Year / first public**: 2026-03 (arXiv v1, 24 Mar 2026)
- **Venue**: ICME 2026
- **URL**: https://arxiv.org/abs/2604.16377
- **Access**: open
- **Setting**: out of scope
- **Method family**: stylometry/AST, with binary-image features
- **Dataset**: CoDET-M4 and LLMAuthorBench
- **Headline result**: not reported as a number in the abstract.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. LLM-source attribution, not human versus LLM.

### Style, Not Self: Surface Cues Explain Zero-Shot Code Attribution by Large Language Models
- **Authors**: Ehsan Barkhordar, Surendrabikram Thapa
- **Year / first public**: 2026-09 (arXiv v1, 24 Sep 2026)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2609.30048
- **Access**: open
- **Setting**: out of scope
- **Method family**: empirical study
- **Dataset**: MBPP, HumanEval and DS-1000 solutions from 5–12 LLMs
- **Headline result**: Single-solution self-recognition balanced accuracy of 49–58%.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. LLM self-recognition, not detecting LLM versus human code.

### Leveraging Large Language Models to Obscure Code Stylometry: A Comparative Study of GPT-3.5 and GPT-4
- **Authors**: Saman Pordanesh, Benjamin Tan
- **Year / first public**: 2026-06 (arXiv v1, 21 Jun 2026)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2606.22306
- **Access**: open
- **Setting**: out of scope
- **Method family**: robustness study
- **Dataset**: human-authorship attribution data (not named in the abstract)
- **Headline result**: not reported as a number in the abstract.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. It uses LLMs to evade human authorship attribution, and the detection target is not LLM origin.

### I Can Find You in Seconds! Leveraging Large Language Models for Code Authorship Attribution
- **Authors**: Soohyeon Choi, Yong Kiam Tan, Mark Huasong Meng, et al.
- **Year / first public**: 2025-01 (arXiv v1, 14 Jan 2025)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2501.08165
- **Access**: open
- **Setting**: out of scope
- **Method family**: zero-shot (LLM as attributor)
- **Dataset**: GitHub C++ (500 authors) and Java (686 authors)
- **Headline result**: MCC 0.78 for zero-shot same-author verification.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. Human authorship attribution using LLMs.

### Detection of LLM-Paraphrased Code and Identification of the Responsible LLM Using Coding Style Features
- **Authors**: Shinwoo Park, Hyundong Jin, Jeong-won Cha, Yo-Sub Han
- **Year / first public**: 2025-02 (arXiv v1, 25 Feb 2025)
- **Venue**: Engineering Applications of Artificial Intelligence, vol. 162 (2025)
- **URL**: https://arxiv.org/abs/2502.17749
- **Access**: open
- **Setting**: out of scope (GitHub repositories from 2019)
- **Method family**: stylometry/AST
- **Dataset**: LPcode, human GitHub code with paraphrases from four LLMs (21,355 samples)
- **Headline result**: F1 improves by 2.64% and 15.17% over the best baselines on the two tasks.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. Repository code, not coding problems or education. Slice C (paraphrase robustness) may hold it.

### Whitespaces Don't Lie: Feature-Driven and Embedding-Based Approaches for Detecting Machine-Generated Code
- **Authors**: Syed Mehedi Hasan Nirob, Shamim Ehsan, Moqsadur Rahman, Summit Haque
- **Year / first public**: 2026-01 (arXiv v1, 27 Jan 2026)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2601.19264
- **Access**: open
- **Setting**: out of scope for slice B (general code, the Droid benchmark)
- **Method family**: stylometry/AST and trained classifier
- **Dataset**: Droid, 600k samples
- **Headline result**: Feature-based ROC-AUC 0.995 and F1 0.971.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude from B. A general detector on a general benchmark, which slice A owns.

### Automatic Detection of LLM-Generated Code: A Comparative Case Study of Contemporary Models Across Function and Class Granularities
- **Authors**: Musfiqur Rahman, SayedHassan Khatoonabadi, Ahmad Abdellatif, Emad Shihab
- **Year / first public**: 2024-09 (arXiv v1, 2 Sep 2024)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2409.01382
- **Access**: open
- **Setting**: out of scope (CodeSearchNet)
- **Method family**: trained classifier
- **Dataset**: 14,485 Python functions and 11,913 classes from CodeSearchNet
- **Headline result**: GPT-3.5 AUC-ROC 0.96, against about 0.68–0.80 for newer models.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. Repository code, which slice A owns.

### A Structural and Behavioral Hybrid Framework for Detecting AI-Generated Code in Programming Education
- **Authors**: Arockia Irudayaraja M., Rexton George R., Nishanth K., Sakthivel P.
- **Year / first public**: 2026-10 (17 Oct 2026)
- **Venue**: Journal of Information Technology and Digital World, 8(4), 394–409
- **URL**: https://irojournals.com/itdw/article/view/2456
- **Access**: open
- **Setting**: out of scope as evidenced. "Programming education" appears in the title, but the source of the 6,800 samples is not stated.
- **Method family**: stylometry/AST, with runtime sandboxing
- **Dataset**: 6,800 Python, Java, C and C++ samples (source not stated)
- **Headline result**: 93.8% accuracy and 92.9% F1, falling to 89.4% F1 under obfuscation.
- **Limitation**: Data provenance is not stated [reader-inferred].
- **Decision**: exclude. Neither education data nor coding-problem data can be confirmed.

### Understanding AI Code Detection: A Feature-Level Analysis of Human, AI-Generated, and Hybrid Python Code
- **Authors**: Alexander Chandra, Benediktus Albert Chandra, Michelle Divine Winata, Meiliana, Fiqri Ramadhan Tambunan
- **Year / first public**: 2026-08 (ICISS 2026)
- **Venue**: International Conference on ICT for Smart Society 2026 (DOI 10.1109/ICISS71466.2026.11715288)
- **URL**: https://www.semanticscholar.org/paper/5182c21e87a44e675d545b3e34d769a7fad01e44
- **Access**: paywalled
- **Setting**: out of scope as evidenced (data source not in the abstract)
- **Method family**: stylometry/AST
- **Dataset**: human, AI and hybrid Python code (source not stated)
- **Headline result**: The fused SVM reaches 0.79 accuracy and F1 on three classes.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. No education or coding-problem setting could be confirmed. Slice C may want it for hybrid code.

### Who Wrote This Code? Investigating Human and AI Programming Patterns
- **Authors**: Nitika, Ramesh Narwal
- **Year / first public**: 2025-11 (ICIIP 2025)
- **Venue**: International Conference on Image Information Processing 2025 (DOI 10.1109/ICIIP68302.2025.11346257)
- **URL**: https://www.semanticscholar.org/paper/456afef2d24df477898a1c177fd6fbd0313f5e52
- **Access**: paywalled
- **Setting**: out of scope as evidenced
- **Method family**: empirical study
- **Dataset**: not stated in the abstract
- **Headline result**: not reported
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. The abstract gives no setting, data or results.

### AI Guarded Code Editor: Verifying Authentic Human Input
- **Authors**: Aditi Raghunandan, A. G. Aishwarya, Mohammad Adnan Khan, Nishant S, K. Panimozhi
- **Year / first public**: 2025-03 (COMP-SIF 2025)
- **Venue**: COMP-SIF 2025 (DOI 10.1109/COMP-SIF65618.2025.10969913)
- **URL**: https://www.semanticscholar.org/paper/1c8d603c48b2898afd0102700c7409d204db0a40
- **Access**: paywalled
- **Setting**: competitive programming and coding tests
- **Method family**: stylometry/AST (proposed)
- **Dataset**: not stated
- **Headline result**: not reported
- **Limitation**: The abstract describes a planned design ("We will design").
- **Decision**: exclude. No evaluation is reported.

### A machine learning assistant for detecting fraudulent activities in synchronous online programming exams
- **Authors**: Francisco Ortín, Álvaro Díaz Gago, Jose Quiroga, Miguel García
- **Year / first public**: 2025-09 (9 Sep 2025)
- **Venue**: PeerJ Computer Science (DOI 10.7717/peerj-cs.3159)
- **URL**: https://api.openalex.org/works/doi:10.7717/peerj-cs.3159
- **Access**: open
- **Setting**: education
- **Method family**: trained classifier (CNN+RNN on screen-capture frames)
- **Dataset**: screenshot sequences from online programming exams
- **Headline result**: 95.18% accuracy and 94.2% F2.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. It detects on-screen cheating behaviour, not the authorship of code.

### Automated Detection of AI-Obfuscated Plagiarism in Modeling Assignments
- **Authors**: Timur Sağlam, Sebastian Hahner, Larissa Schmid, Erik Burger
- **Year / first public**: 2024-04 (ICSE-SEET 2024)
- **Venue**: ICSE-SEET 2024 (DOI 10.1145/3639474.3640084)
- **URL**: https://api.openalex.org/works/doi:10.1145/3639474.3640084
- **Access**: open
- **Setting**: out of scope (modeling assignments, not code)
- **Method family**: robustness study
- **Dataset**: real modeling assignments with ChatGPT-obfuscated plagiarism
- **Headline result**: not reported as a number in the abstract.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. The artifacts are UML-style models, not programs.

### Detecting Automatic Software Plagiarism via Token Sequence Normalization
- **Authors**: Timur Sağlam, Moritz Brödel, Larissa Schmid, Sebastian Hahner
- **Year / first public**: 2024-04 (ICSE 2024)
- **Venue**: ICSE 2024 (DOI 10.1145/3597503.3639192)
- **URL**: https://www.semanticscholar.org/paper/510c0061fabb019d114b9d8455c03d259be083e8
- **Access**: open
- **Setting**: education
- **Method family**: robustness study
- **Dataset**: multiple real-world datasets
- **Headline result**: not reported as a number in the abstract.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. The attacks are algorithmic plagiarism generators, not LLMs. Its LLM follow-up (Sağlam & Schmid 2025) is included.

### Obfuscation-Resilient Software Plagiarism Detection with JPlag
- **Authors**: Timur Sağlam, Sebastian Hahner, Larissa Schmid, Erik Burger
- **Year / first public**: 2024-04 (ICSE-Companion 2024)
- **Venue**: ICSE 2024 Companion (DOI 10.1145/3639478.3643074)
- **URL**: https://www.semanticscholar.org/paper/3547abcf02e88e5e268819e128751dd97b20156c
- **Access**: open
- **Setting**: education
- **Method family**: robustness study
- **Dataset**: not stated in the abstract
- **Headline result**: not reported
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. A summary of JPlag defences against automated (non-LLM) obfuscation.

### An Interpretable Dual-Reference Framework for Learning Trajectory Anomaly Detection Using Code and Submission Behavior in C Programming Courses
- **Authors**: Xiqin Lu, Khaing Hsu Wai
- **Year / first public**: 2026 (IEEE Access)
- **Venue**: IEEE Access (DOI 10.1109/ACCESS.2026.3737282)
- **URL**: https://api.openalex.org/works/doi:10.1109/access.2026.3737282
- **Access**: open
- **Setting**: education
- **Method family**: empirical study (anomaly scoring)
- **Dataset**: 950 student–assignment records
- **Headline result**: not reported as a detection metric.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. It flags atypical learning trajectories and does not target LLM-generated code.

### Discovering and exploring cases of educational source code plagiarism with Dolos
- **Authors**: Rien Maertens, Maarten Van Neyghem, Maxiem Geldhof, Charlotte Van Petegem, Niko Strijbol, Peter Dawyndt, Bart Mesuere
- **Year / first public**: 2024-05 (SoftwareX)
- **Venue**: SoftwareX (DOI 10.1016/j.softx.2024.101755)
- **URL**: https://api.openalex.org/works/doi:10.1016/j.softx.2024.101755
- **Access**: open
- **Setting**: education
- **Method family**: dataset/benchmark (tool paper)
- **Dataset**: n/a
- **Headline result**: not reported
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. A Dolos tool paper with no evaluation on LLM code.

### LLM-Assisted Cheating Detection in Korean Language via Keystrokes
- **Authors**: Dong Hyun Roh, Rajesh Kumar, An Ngo
- **Year / first public**: 2025-07 (arXiv v1, 29 Jul 2025)
- **Venue**: IJCB 2025
- **URL**: https://arxiv.org/abs/2507.22956
- **Access**: open
- **Setting**: out of scope (Korean writing)
- **Method family**: trained classifier (keystrokes)
- **Dataset**: 69 participants writing tasks
- **Headline result**: not reported as a single number in the abstract.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. Prose, not code.

### Detecting LLM-Assisted Academic Dishonesty using Keystroke Dynamics
- **Authors**: Atharva Mehta, Rajesh Kumar, Aman Singla, Kartik Bisht, Yaman Kumar Singla, Rajiv Ratn Shah
- **Year / first public**: 2025-11 (arXiv v1, 16 Nov 2025)
- **Venue**: IEEE TBIOM 2026
- **URL**: https://arxiv.org/abs/2511.12468
- **Access**: open
- **Setting**: out of scope (writing)
- **Method family**: trained classifier (keystrokes)
- **Dataset**: 130 participants
- **Headline result**: not reported as a number in the abstract.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. Prose, not code.

### Beyond Representational Similarity: Source-Conditioned Description-Length Gain for Generative Plagiarism Detection and Candidate Source Reranking
- **Authors**: Peijia Guo, Wenxuan Xie, ZiGuang Li, Ming Li
- **Year / first public**: 2026-08 (arXiv v1, 4 Aug 2026)
- **Venue**: arXiv preprint
- **URL**: https://arxiv.org/abs/2608.03859
- **Access**: open
- **Setting**: out of scope (PAN text plagiarism)
- **Method family**: zero-shot
- **Dataset**: PAN 2025/2026
- **Headline result**: F1 0.94 on the PAN 2025-derived pairwise set.
- **Limitation**: Not assessed beyond the abstract, because the paper fails the Scope setting or target test [reader-inferred].
- **Decision**: exclude. Prose, not code.
