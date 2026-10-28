# Citation check: llm-generated-code-detection sources

Run 2026-10-28. Scope: 89 Source notes (no-access.md excluded). Verdict rule: title (same words, ignoring case and punctuation) and first author match the named record.

verified: 89 | minor: 0 | mismatch: 0 | not found: 0

Method: every title and first author was compared by script against the arXiv API (69 notes), Crossref (23 DOIs), and ACL Anthology bib files (7). Nine notes with no arXiv or DOI record (four ACL Anthology pages, two CEUR-WS proceedings pages, a NeurIPS page, a zyBooks page, an AAAI/mlanthology page) were checked on those pages. Venue claims were compared with arXiv comments, journal_ref, Crossref container titles and OpenAlex. Year differences between arXiv v1 and the venue or print year are recorded in the notes column, not counted as errors.

Open items for the caller (none changes a verdict): the DOI in `ye-2026-correctness-convergence-ai-generated.md` does not resolve yet; `adham-2025-codetector-framework-zero-shot.md` is 2025 (conference) vs 2026 (Crossref print year).

| Note | Verdict | Record differs / remark | Confirmed by |
|---|---|---|---|
| adegbite-2025-detection-genai-produced-student.md | verified | Crossref title carries an added French subtitle; English title matches. | Crossref 10.23962/ajic.i35.21309 |
| adham-2025-codetector-framework-zero-shot.md | verified | Record year differs: Crossref issued 2026 (LNCS volume); note 2025 = LION conference year (Leiden PDF is AdhEtAl25). Venue-year vs print-year, not an error. | Crossref 10.1007/978-3-032-09192-5_11 |
| agrawal-2025-duolens-framework-robust-detection.md | verified | — | arXiv API 2510.18904 |
| aiersilan-2026-seeding-watermarks-detect-verbatim.md | verified | — | arXiv API 2605.16336 |
| arslan-2026-malto-at-semeval-2026.md | verified | — | ACL Anthology bib 2026.semeval-1.304 (title, first author Arslan, 2026, pp. 2413-2420 match) |
| ashkenazi-2025-zero-shot-detection-llm.md | verified | — | arXiv API 2506.06069 |
| bashir-2025-pseudo-ai-submissions-detecting.md | verified | — | Crossref 10.3389/fcomp.2025.1549761 |
| berdichevsky-2026-dream-at-semeval-2026.md | verified | — | arXiv API 2606.25102; Crossref 10.18653/v1/2026.semeval-1.52 |
| chandrasekar-2026-medhastra-at-semeval-2026.md | verified | — | ACL Anthology bib 2026.semeval-1.264 (title, Chandrasekar, 2026, pp. 2098-2103 match) |
| chauhan-2026-ucsc-nlp-at-semeval.md | verified | Venue SemEval-2026 confirmed by Crossref search (DOI 10.18653/v1/2026.semeval-1.311). | arXiv API 2604.26990 |
| choi-2025-attributing-chatgpt-generated-source.md | verified | — | Crossref 10.1109/TDSC.2025.3535218 |
| choi-2026-multi-channel-spread-spectrum.md | verified | — | arXiv API 2607.06009 |
| davalos-2026-does-ai-assistance-leave.md | verified | — | arXiv API 2609.17883 |
| delphino-2025-assessing-prevalence-ai-assisted.md | verified | — | arXiv API 2507.06438 |
| demirok-2024-aigcodeset-new-annotated-dataset.md | verified | — | arXiv API 2412.16594 |
| demirok-2025-multiaigcd-comprehensive-dataset-ai.md | verified | Crossref issued 2026 (journal); note year 2025 = arXiv v1. Both recorded. | arXiv API 2507.21693; Crossref 10.1007/s00521-026-12336-0 |
| dickey-2025-failure-plagiarism-detection-competitive.md | verified | — | arXiv API 2505.08244 |
| dihan-2026-llmsniffer-detecting-llm-generated.md | verified | — | arXiv API 2604.16058 |
| djire-2026-code-detectors-have-half.md | verified | — | arXiv API 2610.01664; Crossref 10.1145/3832783.3844566 |
| fahad-2026-promptmark-prompt-guided-iterative.md | verified | — | arXiv API 2606.20835 |
| gacek-2025-embedding-based-approach-identifying.md | verified | — | CEUR-WS Vol-4075 table of contents (paper3, single author Paulina Gacek, GeCoIn 2025) |
| gacek-2026-investigating-code-similarity-patterns.md | verified | — | Crossref 10.5220/0014949400004021 |
| gu-2025-invisible-entropy-safe-efficient.md | verified | Venue EMNLP 2025 confirmed in OpenAlex (DOI 10.18653/v1/2025.emnlp-main.341); arXiv has no venue field. | arXiv API 2505.14112 |
| gu-2026-ssg-logit-balanced-vocabulary.md | verified | — | arXiv API 2604.22438 |
| guo-2025-optimizing-token-choice-code.md | verified | arXiv v1 title "...: A RL Approach" confirmed; current title matches note. | arXiv API 2508.11925 |
| guo-2025-practical-effective-code-watermarking.md | verified | — | NeurIPS 2025 proceedings page (citation_title, Guo & Cheng) + Crossref search (DOI 10.52202/085713-2485) |
| gurioli-2024-this-you-llm-recognizing.md | verified | — | arXiv API 2412.14611 |
| hong-2026-signature-filtering-lightweight-enhancement.md | verified | arXiv lists DOI 10.1016/j.ipm.2026.104998 (Information Processing & Management 2026), confirmed in OpenAlex; note says arXiv preprint, which is also true. | arXiv API 2606.18430 |
| hoq-2023-detecting-chatgpt-generated-code.md | verified | — | CEUR-WS Vol-3487 table of contents (paper2, Hoq first author, LLM@AIED 2023) |
| idialu-2024-whodunit-classifying-code-as.md | verified | — | arXiv API 2403.04013; Crossref 10.1145/3643991.3644926 |
| ispas-2026-fine-tuning-pre-trained.md | verified | ACL/Crossref title is "Archaeology at SemEval-2026 Task 13: Fine-Tuning Pre-Trained Code Models..."; note uses the arXiv title with the team name in parentheses. Same paper. | arXiv API 2605.01596; Crossref 10.18653/v1/2026.semeval-1.383 |
| javidnia-2026-swarl-safeguard-code-watermarking.md | verified | — | arXiv API 2601.02602 |
| jin-2026-grammar-guided-code-watermarking.md | verified | — | arXiv API 2610.05323 |
| karnalim-2026-detecting-genai-assistance-programming.md | verified | — | Crossref 10.1007/s10791-025-09884-9 |
| karnalim-2026-machine-learning-approach-detect.md | verified | — | Crossref 10.35784/acs_8915 |
| ke-2023-discriminating-human-authored-chatgpt.md | verified | — | arXiv API 2306.14397 |
| kim-2025-marking-code-without-breaking.md | verified | — | arXiv API 2502.18851 |
| krishna-2023-paraphrasing-evades-detectors-ai.md | verified | — | arXiv API 2303.13408 |
| le-2026-semantic-differentiation-tackling-challenges.md | verified | — | arXiv API 2601.11629 |
| lee-2023-who-wrote-this-code.md | verified | — | arXiv API 2305.15060 |
| li-2023-tracing-code-provenance-code.md | verified | — | arXiv API 2305.12461 |
| li-2024-efficient-universal-watermarking-llm.md | verified | arXiv v1 title "Resilient Watermarking for LLM-Generated Codes" confirmed; TSE DOI 10.1109/TSE.2026.3710556 in arXiv record. | arXiv API 2402.07518 |
| lim-2026-sew-style-encoded-watermarking.md | verified | — | arXiv API 2609.39414 |
| lin-2025-code-acrostic-robust-watermarking.md | verified | Venue WISE 2025 confirmed in Crossref (DOI 10.1007/978-981-95-7251-9_35). | arXiv API 2512.14753 |
| lu-2024-entropy-based-text-watermarking.md | verified | — | arXiv API 2403.13485 |
| ma-2023-code-ethics-holistic-audit.md | verified | — | arXiv API 2305.12747 |
| mao-2024-watermarking-low-entropy-generation.md | verified | — | arXiv API 2405.14604 |
| nguyen-2023-this-snippet-written-chatgpt.md | verified | Matches arXiv title; journal version (JSS 2024, DOI 10.1016/j.jss.2024.112059) confirmed in Crossref. | arXiv API 2307.09381; Crossref 10.1016/j.jss.2024.112059 |
| nie-2026-matrix-multi-layer-code.md | verified | — | arXiv API 2604.16001 |
| nirob-2026-whitespaces-don-t-lie.md | verified | — | arXiv API 2601.19264 |
| oedingen-2024-chatgpt-code-detection-techniques.md | verified | — | arXiv API 2405.15512 |
| orel-2025-codet-m4-detecting-machine.md | verified | — | arXiv API 2503.13733; ACL Anthology bib 2025.findings-acl.550 |
| orel-2025-droid-resource-suite-ai.md | verified | Record title is "$\texttt{Droid}$: A Resource Suite..." (LaTeX markup only); same words. | arXiv API 2507.10583; ACL Anthology bib 2025.emnlp-main.1593 |
| orel-2026-aicd-bench-challenging-benchmark.md | verified | — | arXiv API 2602.02079; ACL Anthology bib 2026.eacl-long.325 |
| orel-2026-semeval-2026-task-13.md | verified | — | ACL Anthology bib 2026.semeval-1.445 (title, first author Orel, 2026 match) |
| orenstrakh-2023-detecting-llm-generated-text.md | verified | COMPSAC 2024 DOI confirmed in Crossref (title omits "A"). | arXiv API 2307.07411; Crossref 10.1109/COMPSAC61105.2024.00027 |
| paek-2025-detection-llm-generated-java.md | verified | OpenAlex: Springer CCIS DOI 10.1007/978-3-031-94937-1_10 (2025); note says CSCI 2024 proceedings. Same paper, venue-year vs print-year. | arXiv API 2502.15740 |
| pan-2024-assessing-ai-detectors-identifying.md | verified | — | arXiv API 2401.03676; Crossref 10.1145/3639474.3640068 |
| paulet-2025-cdup-detecting-ai-generated.md | verified | — | Crossref 10.1016/j.procs.2025.09.329 |
| permatasari-2025-threshold-selection-method-code.md | verified | — | Crossref 10.3390/analytics5010002 |
| racovan-2026-argus-academic-integrity-era.md | verified | — | arXiv API 2609.36073 |
| sadasivan-2023-can-ai-generated-text.md | verified | — | arXiv API 2303.11156 |
| saeheng-2026-npc-automated-tool-detecting.md | verified | — | Crossref 10.5220/0014485500004052 |
| saglam-2025-evaluating-software-plagiarism-detection.md | verified | — | arXiv API 2505.20158 |
| shi-2024-between-lines-code-unraveling.md | verified | — | arXiv API 2401.06461 |
| skurla-2026-mcdok-at-semeval-2026.md | verified | Venue SemEval-2026 confirmed by Crossref search (DOI 10.18653/v1/2026.semeval-1.47). | arXiv API 2604.21365 |
| suh-2024-empirical-study-automatically-detecting.md | verified | — | arXiv API 2411.04299 |
| sun-2023-codemark-imperceptible-watermarking-code.md | verified | — | arXiv API 2308.14401 |
| suresh-2024-watermarking-llm-generated-code.md | verified | — | arXiv API 2403.17983 |
| toba-2023-inappropriate-benefits-identification-chatgpt.md | verified | — | arXiv API 2309.16697 |
| vahid-2023-chatgpt-cheat-detection-cs1.md | verified | — | zyBooks research-library page (title, Vahid first author, published 17 Feb 2023); ITiCSE 2024 follow-up not checked |
| wang-2023-evaluating-aigc-detectors-code.md | verified | — | arXiv API 2304.05193 |
| wang-2023-student-mastery-or-ai.md | verified | — | arXiv API 2311.16292 |
| xu-2024-chatgpt-generated-code-assignment.md | verified | Crossref: Student Abstract, Xu, Xu, Sheng, pp. 23688-23689; note says "Xu et al.", consistent. | Crossref 10.1609/aaai.v38i21.30527 |
| xu-2024-detecting-ai-generated-code.md | verified | Crossref 10.1609/aaai.v38i21.30361: title, Xu & Sheng, pp. 23155-23162, 2024 all match. Distinct from the Student Abstract note. | Crossref 10.1609/aaai.v38i21.30361 + mlanthology page |
| xu-2024-distinguishing-llm-generated-human.md | verified | Crossref issued 2025 (TOSEM issue); note year 2024 = arXiv v1. | arXiv API 2411.04704; Crossref 10.1145/3705300 |
| xu-2024-one-size-does-not.md | verified | Crossref issued 2026 (TOSEM issue); note year 2024 = arXiv v1. | arXiv API 2412.16525; Crossref 10.1145/3748506 |
| xu-2025-codevision-detecting-llm-generated.md | verified | — | arXiv API 2501.03288 |
| xu-2026-synmark-semantic-coordinate-multi.md | verified | — | arXiv API 2610.32017 |
| yang-2023-code-watermarking-dual-channel.md | verified | — | arXiv API 2309.00860 |
| yang-2023-zero-shot-detection-machine.md | verified | — | arXiv API 2310.05103 |
| yao-2026-coderipple-wavelet-based-detection.md | verified | — | ACL Anthology bib 2026.acl-long.1777 (title, Yao, 2026, pp. 38351-38364 match) |
| ye-2024-uncovering-llm-generated-code.md | verified | — | arXiv API 2405.16133 |
| ye-2026-correctness-convergence-ai-generated.md | verified | Title/author match arXiv; arXiv lists the same DOI, but Crossref and doi.org return 404 for 10.1145/3856208.3856226 (not yet registered). Re-check the DOI later. | arXiv API 2610.00863 |
| yemets-2026-source-code-authorship-attribution.md | verified | — | arXiv API 2608.00227 |
| yotkova-2026-fmi-su-yotkova-kastreva.md | verified | Crossref title spells the team name "FMISUYotkovaKastreva"; same paper. DOI and year confirmed. | arXiv API 2605.04157; Crossref 10.18653/v1/2026.semeval-1.275 |
| yu-2026-preserving-structure-strengthening-signals.md | verified | — | arXiv API 2607.10210 |
| zhang-2025-disappearing-ink-obfuscation-breaks.md | verified | — | arXiv API 2507.05512 |
| zhang-2025-robust-secure-code-watermarking.md | verified | — | arXiv API 2502.02068 |
