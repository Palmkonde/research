# Classification metrics
How to measure and report a classifier's quality, for binary and multiclass problems. Every threshold metric (precision, recall, specificity, F1) is computed from the confusion matrix, which counts predictions against true labels. Threshold-free summaries (ROC-AUC, PR-AUC) sweep the decision threshold over the classifier's scores. Class imbalance decides which of these stay informative, and multiclass problems add a choice of averaging (macro, micro, weighted) that a paper must name.

Every Finding here gives the formula for each metric in LaTeX and a hand-worked `### Example:` on one shared toy dataset, introduced in the first Finding, so the numbers agree across Findings. Findings cover math and usage only, with no code for now.

## Prerequisites
- [Probability basics](../../fundamentals/probability-basics/README.md)
- [Statistical inference](../../fundamentals/statistical-inference/README.md)

## Questions
- [x] [What do the confusion matrix, precision, recall, specificity and F1 measure, and how is each computed from the matrix?](confusion-matrix-basic-metrics.md)
- [x] [When should I use ROC-AUC vs PR-AUC, and how is each curve and area computed?](roc-auc-vs-pr-auc.md)
- [x] [How does class imbalance change which metric and which graph to report?](class-imbalance-metric-choice.md)
- [x] [How are macro, micro and weighted F1 (and precision/recall) computed in multiclass, and when do I use each?](multiclass-averaging.md)
- [x] [How is a decision threshold chosen and computed, and how does it link threshold-free metrics (AUC) to threshold metrics (F1)?](decision-threshold.md)
- [x] [How should I report classification results in a paper or report: which tables and figures, which averaging to name, confidence intervals or std over seeds, and which baselines?](reporting-classification-results.md)
- [ ] How are classification metrics computed for multilabel problems?
- [ ] What is probability calibration, and how is it measured (reliability diagram, Brier score, ECE)?
- [ ] What do the Matthews correlation coefficient (MCC) and Cohen's kappa measure, and when do they beat F1?
- [ ] How should precision, recall and F1 be reported when a denominator is zero (no predicted positives, or no actual positives), and how does the `zero_division` choice change an average over classes or folds?
- [ ] How does F1 change when the other class is called positive, and how should the positive class be chosen?
- [ ] Why is the harmonic mean, rather than the arithmetic or geometric mean, the right way to combine precision and recall (van Rijsbergen's measurement-theory argument)?
- [ ] How are tied scores handled in ROC and PR curves, and how do ties change ROC AUC, AP and the trapezoidal PR area?
- [ ] How are the interpolated AP variants (11-point and PASCAL VOC all-point interpolation) computed, and how do they differ from scikit-learn's non-interpolated AP?
- [ ] What is partial ROC AUC (scikit-learn's `max_fpr`), and when should it replace the full AUC?
- [ ] What are precision-recall-gain curves (Flach and Kull 2015), and do they fix the baseline and interpolation problems of PR-AUC?
- [ ] How is the standard error of an ROC AUC estimated (Hanley-McNeil, DeLong), and how are two classifiers' AUCs compared on the same test set?
- [ ] How do you recompute a PR curve, AP and F1 for a target deployment prevalence from test-set TPR and FPR, and how many test negatives are needed for precision to be reliable at low prevalence?
- [ ] Does rebalancing the training set (resampling or class weights) change a classifier's test ROC and PR curves, or only shift its threshold?
- [ ] How does AUPRC's preference for high-prevalence subgroups affect fairness evaluation, and how should metrics be reported per subgroup?
- [ ] When does one-vs-one (Hand and Till) multiclass ROC AUC disagree with one-vs-rest macro AUC, and which should be reported under class imbalance?
- [ ] When should a majority or background class be left out of micro averaging through `labels` (for example the "O" tag in named-entity recognition), and how should the resulting micro-precision and micro-recall be reported?
- [ ] How much does choosing the threshold on the same data that reports the score inflate F1, and how large must a validation set be for the chosen threshold to be stable?
- [ ] How are thresholds chosen per class in multiclass and multilabel problems, and why do micro- and macro-F1 lead to different optimal thresholds (Lipton et al.'s batch observation)?
- [ ] How are example-dependent costs, such as Elkan's credit-card transaction amounts, turned into a decision rule?
- [ ] How does interpolating between two classifiers on the ROC convex hull reach an operating point that no single threshold gives?
- [ ] Do BCa or bootstrap-t intervals fix the under-coverage of the percentile bootstrap for test-set metrics such as F1, AP and ROC AUC on small test sets?
- [ ] How does Nadeau and Bengio's corrected resampled t-test carry over to repeated $k$-fold cross-validation, and how does it compare with Dietterich's 5x2cv test in size and power?
- [ ] How are several classifiers compared over many datasets with the Friedman test, its post-hoc tests and critical-difference diagrams (Demšar 2006)?
- [ ] How is the probability of outperforming, $P(A > B)$, estimated over randomized runs, and when should it replace comparing mean scores (Bouthillier et al.)?
