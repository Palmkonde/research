---
question: How does class imbalance change which metric and which graph to report?
date: 2026-10-28
status: answered
---

## TL;DR
A metric that mixes counts from both actual classes moves with the prevalence $\pi$, even when the classifier does not change[^fawcett]. That covers accuracy, precision, F1, MCC, Cohen's kappa, the PR curve and AP *(inference: from the sections below)*. TPR, FPR and specificity are each a ratio within one class, and balanced accuracy, the ROC curve and ROC AUC combine only those within-class rates, so none of them moves with $\pi$[^fawcett][^saito] *(inference: for balanced accuracy and specificity)*. By Bayes' rule, $\text{precision} = \pi\,\text{TPR} / \big(\pi\,\text{TPR} + (1-\pi)\,\text{FPR}\big)$, which falls toward 0 as positives get rarer[^brabec][^williams]. Over the same shift, the all-negative classifier's accuracy rises to $1-\pi$ *(inference)*. Saito and Rehmsmeier argue that the PR plot is more informative than the ROC plot on imbalanced data[^saito]. McDermott et al. argue that AUPRC is not generally the better summary under imbalance, and that AUROC should be the default for comparing models, with AUPRC kept for settings where the costly errors are false positives among the top-scored instances[^mcd]. At low prevalence, report the prevalence itself, draw both curves with their baselines, and never compare AP across test sets whose prevalence differs[^brabec][^saito][^mcd].

## Explanation
Imbalance is the usual case, not the exception: Fawcett notes that class skews of $10^1$ and $10^2$ are very common and that skews up to $10^6$ have been observed[^fawcett]. A number reported on a test set mixes the classifier's behavior with that set's class mix, and the two Findings before this one showed both effects on the shared toy dataset: accuracy that barely beats predicting all negatives, and AP that falls when negatives are added *(inference)*. This page separates the metrics that measure only the classifier from those that also measure the class mix, derives how much the second group moves, and turns that into reporting rules *(inference)*. It keeps the earlier notation: $P$ and $N$ are the numbers of actual positives and negatives, $n = P + N$, $\text{TPR} = TP/P$ and $\text{FPR} = FP/N$, and the confusion matrix has rows for the actual class *(inference)*. The prevalence is $\pi = P/n$ *(inference)*. Where $P(\cdot)$ is followed by an event, as in $P(y = 1)$, it means a probability, not the count of positives *(inference)*.

### Why accuracy misleads: the majority-class baseline
- **Accuracy as a mix of two rates.** Dividing each cell of the confusion matrix by $n$ gives $TP/n = \pi\,\text{TPR}$, $FN/n = \pi\,(1-\text{TPR})$, $FP/n = (1-\pi)\,\text{FPR}$ and $TN/n = (1-\pi)(1-\text{FPR})$ *(inference)*. Williams makes the same observation: the normalized table is fully determined by TPR, FPR and the class ratio[^williams]. So
  $$\text{accuracy} = \frac{TP + TN}{n} = \pi\,\text{TPR} + (1-\pi)\,(1 - \text{FPR}),$$
  a weighted mean of sensitivity and specificity whose weights are the class proportions *(inference)*. As $\pi \to 0$, accuracy tends to specificity, and the positives stop counting *(inference)*.
- **The majority-class baseline.** A classifier that predicts negative for every sample has $\text{TPR} = \text{FPR} = 0$, so its accuracy is $1 - \pi$ *(inference)*. On the toy dataset that is $14/20 = 0.70$, which the [first Finding](confusion-matrix-basic-metrics.md#example-the-shared-toy-dataset) showed is only 0.05 below the real classifier's 0.75 *(inference)*. At $\pi = 0.01$ the useless classifier scores 0.99 *(inference)*.
- **When a classifier beats the baseline.** Subtracting gives $\text{accuracy} - (1 - \pi) = \big((TP + TN) - (TN + FP)\big)/n = (TP - FP)/n$ *(inference)*. So a classifier beats the all-negative baseline on accuracy exactly when it has more true than false positives, which is exactly when its precision is above $1/2$ *(inference)*. At low prevalence that is a high bar even for a classifier with good TPR and FPR, as the examples below show *(inference)*.
- **What the sources say.** Fawcett names accuracy as a metric that uses both classes and so changes with the class distribution while the classifier does not[^fawcett]. scikit-learn warns about accuracy that is above chance only because the classifier takes advantage of an imbalanced test set[^skguide]. In Saito and Rehmsmeier's example, accuracy is 0.6 on both a balanced and an imbalanced dataset, while precision falls from 0.6 to 0.33, a drop that accuracy leaves unnoticed[^saito].

### Which metrics move with prevalence
Fawcett's argument is that any metric using values from both actual classes is sensitive to class skew, while the ROC axes, TPR and FPR, are each a ratio within one class and do not depend on the class distribution[^fawcett]. In this Topic's layout that means "both rows" against "one row" *(inference)*. The rule is about mixing counts from the two rows in one ratio or in a $\pi$-weighted sum; balanced accuracy escapes it, because it averages two within-row rates with fixed weights *(inference)*. Williams adds a caveat: this invariance holds exactly for the population ROC curve, while empirical ROC curves vary somewhat as the ratio changes, as they do across any two samples[^williams].

| Metric | Moves with $\pi$? | Why |
|---|---|---|
| TPR (recall, sensitivity) | no | ratio within the actual-positive row |
| FPR, specificity | no | ratio within the actual-negative row |
| balanced accuracy | no | mean of TPR and specificity |
| ROC curve, ROC AUC | no | built from TPR and FPR only |
| precision | yes | predicted-positive column spans both rows |
| F1, $F_\beta$ | yes | contains precision |
| accuracy | yes | weights the two rows by $\pi$ and $1-\pi$ |
| MCC, Cohen's kappa | yes | use all four cells and the class totals |
| PR curve, AP | yes | built from precision |

*Figure: which metrics depend on the prevalence, and why (inference: the Why column applies each formula). Fawcett classes accuracy, precision and F score as skew-sensitive and the TPR and FPR of the ROC graph as skew-free[^fawcett]. In Saito and Rehmsmeier's example only precision, MCC and the three $F_\beta$ scores change between the balanced and imbalanced datasets, and among the plots they compare only the PR plot changes[^saito]. The rows for specificity, balanced accuracy and Cohen's kappa follow from their formulas (inference).*

### Precision as a function of prevalence
The mechanism behind the table is Bayes' rule (see the [probability basics](../../fundamentals/probability-basics/README.md) Prerequisite) *(inference)*. Brabec et al. write the rates as conditional probabilities: $\text{TPR} = P(\hat y = 1 \mid y = 1)$, $\text{FPR} = P(\hat y = 1 \mid y = 0)$ and precision $= P(y = 1 \mid \hat y = 1)$[^brabec]. They label the negative class $-1$; this Topic labels it $0$ *(inference)*. With the positive prevalence $\pi$ as the prior, Bayes' rule gives[^brabec]

$$\text{precision}(\pi) = \frac{\pi\,\text{TPR}}{\pi\,\text{TPR} + (1-\pi)\,\text{FPR}}.$$

- **Who says so.** Brabec et al. derive this formula with Bayes' theorem and stress that TPR and FPR are not affected by the positive prevalence while precision is[^brabec]. Williams writes the same formula with the ratio $r = P/N = \pi/(1-\pi)$ as $\text{precision} = \text{TPR} / (\text{TPR} + \text{FPR}/r)$[^williams]. Multiplying its numerator and denominator by $\pi$ gives the form above *(inference)*. The same result also follows from the normalized cells: $TP/(TP+FP) = \pi\,\text{TPR} / \big(\pi\,\text{TPR} + (1-\pi)\,\text{FPR}\big)$ *(inference)*.
- **Limits.** Precision tends to 1 as $\pi \to 1$, and to 0 as $\pi \to 0$ whenever $\text{FPR} > 0$[^williams]. Lowering $\pi$ at fixed recall lowers precision, because the denominator grows[^williams].
- **Odds form.** Dividing precision by $1 - \text{precision}$ gives
  $$\frac{\text{precision}}{1 - \text{precision}} = \frac{\pi}{1 - \pi} \cdot \frac{\text{TPR}}{\text{FPR}},$$
  so the odds that a flagged sample is positive are the prior odds of a positive times the likelihood ratio $\text{TPR}/\text{FPR}$ *(inference)*. The classifier fixes the likelihood ratio and the data fix the prior odds, so a tenfold drop in the prior odds is a tenfold drop in the posterior odds *(inference)*.
- **F1 and $F_\beta$.** Williams substitutes the precision formula into $F_\beta$ and gets $F_\beta = (1+\beta^2)\,\text{TPR} / (\text{TPR} + \text{FPR}/r + \beta^2)$, which shows its explicit dependence on $r$[^williams]. At $\beta = 1$, multiplying through by $\pi$ gives *(inference)*
  $$F_1(\pi) = \frac{2\,\pi\,\text{TPR}}{\pi\,(1 + \text{TPR}) + (1-\pi)\,\text{FPR}}.$$
- **The PR baseline moves with $\pi$.** A random classifier lies on the ROC diagonal[^fawcett], so it has $\text{TPR} = \text{FPR}$, and the formula then gives precision $= \pi$ at every threshold *(inference)*. That is Saito and Rehmsmeier's random baseline $y = P/(P+N)$, whose area is also $P/(P+N)$[^saito]. scikit-learn likewise states that random predictions give an AP equal to the fraction of positives[^skguide]. The ROC baseline, the diagonal with area 0.5, does not move[^saito].

### The PR curve and AP under a prevalence shift
- **The whole curve moves.** A shift in $\pi$ leaves each threshold's TPR and FPR, and so its recall, unchanged, and moves its precision by the formula above[^williams]. Williams uses this to predict a PR curve at one class ratio from the curve at another, and finds close agreement with the curve measured directly[^williams]. Fawcett shows two classifiers whose ROC curves are identical at 1:1 and 1:10 class ratios while their PR curves differ substantially[^fawcett].
- **The ranking of classifiers can flip.** Fawcett notes that in some cases the conclusion of which classifier is better can change with a shifted distribution[^fawcett]. Brabec et al. show that PR-AUC and F1 can swap the order of two classifiers as the imbalance changes, and warn that this invites cherry-picking the imbalance rate that favors one method[^brabec]. ROC AUC cannot flip this way, because it does not depend on $\pi$[^fawcett] *(inference: the conclusion)*.
- **So AP values from different prevalences are not comparable.** Brabec et al. argue that a PR curve has little value without the imbalance ratio it was computed at[^brabec]. An AP of 0.44 at $\pi = 0.04$ and an AP of 0.76 at $\pi = 0.30$ can come from the same classifier, as the example below shows *(inference)*. Hoiem et al.'s "normalized precision" and Siblini et al.'s fixed reference ratio $r_0$ make such comparisons possible by fixing one class ratio for every dataset[^williams].
- **The test prevalence may not be the deployment prevalence.** Brabec et al. note that test sets are often less imbalanced than the data seen in deployment, which makes PR-based results too optimistic[^brabec]. Their remedy is not to subsample the test set to the deployment ratio: keep all the samples, so TPR and FPR are estimated with low variance, and compute precision at the ratio of interest with the formula above[^brabec].

### Balanced accuracy, MCC and Cohen's kappa
**Balanced accuracy** is

$$\text{balanced accuracy} = \frac{1}{2}\left( \frac{TP}{TP + FN} + \frac{TN}{TN + FP} \right) = \frac{\text{TPR} + (1 - \text{FPR})}{2}.$$

- scikit-learn describes it as avoiding inflated performance estimates on imbalanced datasets[^skguide]. In the binary case it is the mean of sensitivity and specificity, which is also the area under the ROC curve for binary predictions rather than scores[^skguide]. It equals plain accuracy on a balanced dataset, and its adjusted version (rescaled so random scores 0) is Youden's J statistic, also called informedness[^skguide].
- It averages two one-row rates with fixed weights of $1/2$, so unlike accuracy it does not move with $\pi$ *(inference)*. The all-negative classifier scores $(0 + 1)/2 = 1/2$ at any prevalence *(inference)*. scikit-learn says balanced accuracy drops to $1/n_\text{classes}$ for a classifier that beats chance only through the imbalance[^skguide].

**Matthews correlation coefficient (MCC).** scikit-learn gives[^skguide]

$$\text{MCC} = \frac{TP \cdot TN - FP \cdot FN}{\sqrt{(TP + FP)(TP + FN)(TN + FP)(TN + FN)}}.$$

It is in essence a correlation coefficient from $-1$ (inverse) through $0$ (random) to $+1$ (perfect)[^skguide], and it still moves with prevalence, falling from 0.2 to 0.17 in Saito and Rehmsmeier's example while TPR and specificity stay fixed[^saito].

**Cohen's kappa**[^skkappa]:

$$\kappa = \frac{p_o - p_e}{1 - p_e},$$

the observed agreement $p_o$ corrected for the agreement $p_e$ expected by chance from each labeling's class frequencies[^skkappa]; since $p_e$ uses the class totals, kappa also moves with $\pi$ *(inference)*.

What MCC and kappa measure, and when they beat F1, is a separate open Question in the [Topic README](README.md) *(inference)*.

### The debate: is PR more informative than ROC under imbalance?
**The case for PR (Saito and Rehmsmeier 2015).**
- They argue that the visual interpretability of ROC plots on imbalanced data "can be deceptive", owing to "an intuitive but wrong interpretation of specificity"[^saito]. PR plots, in contrast, can give an accurate prediction of future classification performance, because they evaluate the fraction of true positives among positive predictions[^saito].
- In their simulation, one ROC point stands for 160 false positives and 500 true positives on the balanced data, and for 1600 false positives and the same 500 true positives on the imbalanced data[^saito]. The ROC curves fail to show this difference[^saito].
- They also show two classifiers that differ clearly in the early-retrieval region but have the same ROC AUC, 0.8[^saito]. They conclude that ROC AUC is inadequate for judging early retrieval there, and that ROC plots on imbalanced data need the early-retrieval area checked[^saito].
- Their conclusion "strongly recommend[s] PRC plots as the most informative visual analysis tool"[^saito]. Davis and Goadrich likewise note that ROC curves can give an overly optimistic view under a large class skew[^dg].

**The case for ROC AUC (McDermott et al. 2024).**
- They target the claim that, for a binary task with many more negatives than positives, AUPRC gives a "better", "more accurate" or "fairer" evaluation than AUROC, and they argue that this claim is wrong[^mcd].
- Their Theorem 1 writes both areas as expectations over the scores $t$ of the positive samples[^mcd]:
  $$\text{AUROC}(f) = 1 - \mathbb{E}_{t \sim f(x) \mid y=1}\big[\text{FPR}(f, t)\big], \qquad \text{AUPRC}(f) = 1 - P(y = 0)\, \mathbb{E}_{t \sim f(x) \mid y=1}\!\left[\frac{\text{FPR}(f, t)}{P_x(f(x) > t)}\right].$$
  Its key step is Bayes' rule in the form $\text{precision}(f, \tau) = 1 - P(y = 0)\,\text{FPR}(f, \tau)/P_x(f(x) > \tau)$[^mcd]. This is the same formula as above, since $P_x(f(x) > \tau) = \pi\,\text{TPR} + (1-\pi)\,\text{FPR}$ *(inference)*.
- Apart from the fixed prevalence, AUROC weighs every false positive equally, while AUPRC divides each one by the model's firing rate, the chance of scoring above that threshold[^mcd]. So AUROC improves by the same amount whichever misordered adjacent pair is fixed, and AUPRC improves more when the fixed mistake sits at a higher score (Theorem 2)[^mcd]. On this reading, the deciding factor is not class imbalance but the model's use case[^mcd].
- Their Theorem 3 assumes a model calibrated on the low-prevalence subgroup, and shows that as that subgroup's prevalence goes to 0, the single fix that most raises AUPRC lies in the higher-prevalence subgroup[^mcd]. In their synthetic experiments, optimizing AUPRC favors the higher-prevalence subgroup, while optimizing AUROC treats the subgroups about equally[^mcd]. On real fairness datasets the effect is milder, and it grows with the prevalence gap between the groups[^mcd].
- Their guidance:
  - use AUROC for context-independent model comparison, for deployments where false negatives are costly, and for fair allocation across subpopulations[^mcd];
  - use AUPRC to cut high-score false positives in a single-group setting, such as screening molecules or information retrieval, when false positives cost far more than false negatives[^mcd].
- Their review of the literature found 424 papers making the AUPRC-is-better claim, 167 of them with no citation[^mcd]. The paper most often cited for it is Davis and Goadrich, which argues that the PR curve may be more informative under imbalance but never says its area should be preferred over ROC AUC[^mcd].

**Where the two sides agree.**
- McDermott et al. distinguish curves, which communicate many operating points to someone deploying the model, from areas, which are single-number summaries for model comparison that ignores the deployment[^mcd].
- They mark as valid the claim that PR curves can better reflect deployment objectives, citing Saito and Rehmsmeier among others, and reject only its stretch into "AUPRC is better whenever classes are imbalanced"[^mcd]. They call the claim that AUPRC's dependence on prevalence is desirable too vague to evaluate[^mcd].
- They also say their guidance is not a reason to stop reporting both metrics or the ROC and PR curves[^mcd].
- So the two papers mostly answer different questions *(inference)*. Saito and Rehmsmeier ask which plot shows a reader how a classifier will perform on imbalanced data, and McDermott et al. ask which area should pick between models *(inference)*. Fawcett's case for ROC graphs fits the second question: they separate classifier performance from class skew and error costs[^fawcett].

### What to report at low prevalence
- **State the prevalence.** Give the test-set $\pi$, and the deployment $\pi$ if it is known and different[^brabec]. It is the PR baseline, so a reader cannot judge an AP without it[^saito].
- **Never let accuracy stand alone.** Put the majority-class accuracy $1 - \pi$ next to it, or report balanced accuracy, or recall and specificity, instead *(inference)*. Balanced accuracy avoids the inflated estimates that plain accuracy gives on imbalanced data[^skguide].
- **Graphs: draw both, with baselines.**
  - The ROC curve shows ranking quality independent of the class mix[^fawcett]. Draw its diagonal baseline[^fawcett].
  - The PR curve shows what fraction of the flagged samples are real[^saito]. Draw its horizontal baseline at $\pi$[^saito].
  - At low prevalence, the PR curve is the one that shows the false-positive load, as in Saito and Rehmsmeier's 1600-false-positive point[^saito]. The ROC curve stays the same if the prevalence changes later[^fawcett].
  - McDermott et al. do not argue against reporting both curves[^mcd].
- **Pick the headline area by use case, not by imbalance alone.**
  - Use ROC AUC to compare models when the threshold and costs are not known, when missed positives are the costly error, or when subgroups must be treated evenly[^mcd].
  - Use AUPRC (AP is one estimator of it) when the cost lies in false positives among the top-ranked instances, such as a fixed review budget or a retrieval list[^mcd].
  - Whichever area you use, name the PR-area estimator, as the [ROC/PR Finding](roc-auc-vs-pr-auc.md) explains *(inference)*.
- **Do not compare PR-AUC, AP or F1 across datasets with different prevalence.**
  - Both the values and the order of the classifiers can change with the imbalance[^brabec][^fawcett].
  - To compare, recompute precision at one common $\pi$ from each classifier's TPR and FPR[^brabec][^williams]. Alternatively, compare a prevalence-free metric such as ROC AUC *(inference)*.
- **Do not subsample the test set to reach a target prevalence.** Keep every negative, and compute precision at the target $\pi$ from the formula[^brabec].
- **Give the operating point.** If the model will be used at a threshold, report precision, recall and specificity there, together with the $\pi$ they were measured at *(inference)*. How to choose that threshold is a separate open Question in the [Topic README](README.md) *(inference)*.

### Example: one classifier at two prevalences
Start from the shared toy dataset of the [first Finding](confusion-matrix-basic-metrics.md#example-the-shared-toy-dataset), unchanged: 20 samples, 6 positives, $\pi = 0.30$, and at threshold 0.5 the counts $TN = 11$, $FP = 3$, $FN = 2$, $TP = 4$ *(inference)*. Make a skewed copy by repeating every negative 10 times with the same score, so $P = 6$, $N = 140$, $n = 146$ and $\pi = 6/146 = 3/73 \approx 0.041$ *(inference)*. Each copy of a negative lands on the same side of every threshold as its original, so at 0.5 the copy has $TN = 110$, $FP = 30$, $FN = 2$, $TP = 4$ *(inference)*. The classifier, and so its TPR $= 2/3$ and FPR $= 3/14$, has not changed; only the class mix has *(inference)*.

$$
C_{\pi = 0.30} =
\begin{array}{r|cc}
 & \hat y = 0 & \hat y = 1 \\ \hline
y = 0 & 11 & 3 \\
y = 1 & 2 & 4
\end{array}
\qquad
C_{\pi = 6/146} =
\begin{array}{r|cc}
 & \hat y = 0 & \hat y = 1 \\ \hline
y = 0 & 110 & 30 \\
y = 1 & 2 & 4
\end{array}
$$

*Figure: the toy confusion matrix at threshold 0.5 and its skewed copy, in the rows-are-actual layout of scikit-learn's `confusion_matrix`[^skcm]. The negative row is multiplied by 10 and the positive row is unchanged (inference).*

**Precision from the formula.** At $\pi = 0.30$: $\pi\,\text{TPR} = 0.3 \cdot \tfrac23 = 0.2$ and $(1-\pi)\,\text{FPR} = 0.7 \cdot \tfrac{3}{14} = 0.15$, so precision $= 0.2/0.35 = 4/7 \approx 0.571$, the same as $TP/(TP+FP)$ *(inference)*. At $\pi = 6/146$: $\pi\,\text{TPR} = \tfrac{6}{146} \cdot \tfrac23 = \tfrac{4}{146}$ and $(1-\pi)\,\text{FPR} = \tfrac{140}{146} \cdot \tfrac{3}{14} = \tfrac{30}{146}$, so precision $= 4/34 = 2/17 \approx 0.118$, matching $4/(4+30)$ *(inference)*.

**F1 and accuracy.** $F_1 = 2TP/(2TP + FP + FN)$ goes from $8/13 \approx 0.615$ to $8/(8 + 30 + 2) = 1/5 = 0.2$ *(inference)*. Accuracy goes from $15/20 = 0.75$ to $(4 + 110)/146 = 57/73 \approx 0.781$, so it rises while precision falls to about a fifth of its value *(inference)*.

| metric | $\pi = 0.30$ ($n = 20$) | $\pi = 6/146$ ($n = 146$) | moved? |
|---|---|---|---|
| TPR (recall) | $2/3 \approx 0.667$ | $2/3 \approx 0.667$ | no |
| FPR | $3/14 \approx 0.214$ | $3/14 \approx 0.214$ | no |
| specificity | $11/14 \approx 0.786$ | $11/14 \approx 0.786$ | no |
| balanced accuracy | $61/84 \approx 0.726$ | $61/84 \approx 0.726$ | no |
| ROC AUC | $73/84 \approx 0.869$ | $73/84 \approx 0.869$ | no |
| precision | $4/7 \approx 0.571$ | $2/17 \approx 0.118$ | yes |
| F1 | $8/13 \approx 0.615$ | $1/5 = 0.200$ | yes |
| accuracy | $3/4 = 0.750$ | $57/73 \approx 0.781$ | yes |
| all-negative accuracy $1 - \pi$ | $7/10 = 0.700$ | $70/73 \approx 0.959$ | yes |
| MCC | $\approx 0.435$ | $\approx 0.212$ | yes |
| Cohen's kappa | $19/44 \approx 0.432$ | $95/679 \approx 0.140$ | yes |
| AP | $1211/1584 \approx 0.765$ | $413/936 \approx 0.441$ | yes |
| AP baseline $\pi$ | $0.300$ | $3/73 \approx 0.041$ | yes |

*Figure: the threshold-0.5 metrics and the two areas for the same classifier at two prevalences (inference). Every value was computed with exact fractions and checked against scikit-learn 1.9.1 (inference: throwaway script, not shown). The split into moved and unmoved rows matches the table of prevalence-dependent metrics above (inference).*

Reading the table:
- On the toy data the classifier beats the all-negative baseline on accuracy, 0.75 against 0.70, because $TP = 4 > FP = 3$ *(inference)*. On the skewed copy it loses, 0.781 against 0.959, because $TP = 4 < FP = 30$, even though nothing about the classifier changed *(inference)*.
- Balanced accuracy shows the same value at both prevalences, and the all-negative classifier scores 0.5 on it at both *(inference)*.
- MCC halves and kappa falls to about a third, so neither is a prevalence-free summary *(inference)*. Both stay above 0, which is the kappa of the all-negative classifier at any prevalence, since its $p_o$ and $p_e$ both equal $1 - \pi$ *(inference)*.

### Example: ROC AUC and AP on the skewed copy
**ROC AUC is unchanged.** There are now $P \cdot N = 6 \cdot 140 = 840$ (positive, negative) pairs, and each original pair appears 10 times with the same outcome *(inference)*. The 73 winning pairs of the [ROC/PR Finding](roc-auc-vs-pr-auc.md#example-roc-auc-by-hand) become 730, so $W = 730/840 = 73/84 \approx 0.869$ *(inference)*. The copies tie only with other negatives, never with a positive, so the pair-counting formula needs no $1/2$ terms *(inference)*.

**AP falls.** Recall still rises only at the six positives, each time by $1/6$, so AP is again the mean of the precisions at those steps *(inference)*. The count of negatives above each positive is now ten times larger *(inference)*:

| positive reached | s01 | s02 | s04 | s06 | s08 | s11 |
|---|---|---|---|---|---|---|
| TP | 1 | 2 | 3 | 4 | 5 | 6 |
| FP above it (toy, then copy) | 0, 0 | 0, 0 | 1, 10 | 2, 20 | 3, 30 | 5, 50 |
| precision on the copy | $1$ | $1$ | $3/13$ | $1/6$ | $1/7$ | $3/28$ |

$$\text{AP}_{\pi = 6/146} = \frac{1}{6}\left( 1 + 1 + \frac{3}{13} + \frac{1}{6} + \frac{1}{7} + \frac{3}{28} \right) = \frac{1}{6} \cdot \frac{2891}{1092} = \frac{413}{936} \approx 0.441$$

*(inference: arithmetic; scikit-learn 1.9.1's `average_precision_score` also gives 0.441239)*

This confirms the 0.441 stated in the [ROC/PR Finding](roc-auc-vs-pr-auc.md#example-average-precision-and-the-trapezoidal-pr-area-by-hand) *(inference)*. The first two positives keep precision 1, because no negative scores above them; every later positive loses precision, because the negatives above it are now ten times as many *(inference)*. AP falls from 0.765 to 0.441 while its baseline falls from 0.30 to 0.041, so relative to its baseline AP actually rises, from about 2.5 times to about 10.7 times *(inference)*. This is why an AP is meaningless without its prevalence *(inference)*.

### Example: precision against prevalence
Hold $\text{TPR} = 2/3$ and $\text{FPR} = 3/14$ fixed and vary $\pi$ in the formulas above *(inference)*. The likelihood ratio is $\text{TPR}/\text{FPR} = (2/3)/(3/14) = 28/9 \approx 3.1$, so a flagged sample's odds of being positive are about 3.1 times the prior odds at every $\pi$ *(inference)*. For example, at $\pi = 0.01$: $\pi\,\text{TPR} = 1/150$ and $(1-\pi)\,\text{FPR} = 0.99 \cdot 3/14 = 297/1400$, so precision $= (1/150)/(1/150 + 297/1400) = 28/919 \approx 0.030$ *(inference)*.

| $\pi$ | precision | $F_1$ | accuracy | all-negative accuracy $1 - \pi$ | balanced accuracy |
|---|---|---|---|---|---|
| $0.5$ | $28/37 \approx 0.757$ | $56/79 \approx 0.709$ | $61/84 \approx 0.726$ | $0.500$ | $61/84 \approx 0.726$ |
| $0.3$ | $4/7 \approx 0.571$ | $8/13 \approx 0.615$ | $3/4 = 0.750$ | $0.700$ | $61/84 \approx 0.726$ |
| $0.1$ | $28/109 \approx 0.257$ | $56/151 \approx 0.371$ | $65/84 \approx 0.774$ | $0.900$ | $61/84 \approx 0.726$ |
| $6/146 \approx 0.041$ | $2/17 \approx 0.118$ | $1/5 = 0.200$ | $57/73 \approx 0.781$ | $\approx 0.959$ | $61/84 \approx 0.726$ |
| $0.01$ | $28/919 \approx 0.030$ | $56/961 \approx 0.058$ | $659/840 \approx 0.785$ | $0.990$ | $61/84 \approx 0.726$ |

*Figure: precision, F1 and accuracy of one fixed classifier as the prevalence drops, from the formulas $\text{precision}(\pi)$ and $F_1(\pi)$ derived from Brabec et al.[^brabec] and Williams[^williams]. Every entry is exact arithmetic, checked with a throwaway script (inference). At $\pi = 0.5$ accuracy equals balanced accuracy, as scikit-learn notes for balanced data[^skguide].*

- Precision falls by about a factor of 25 from $\pi = 0.5$ to $\pi = 0.01$, while recall stays at $2/3$ *(inference)*. Accuracy instead creeps up toward the specificity $11/14 \approx 0.786$, as the accuracy formula predicts *(inference)*.
- Precision equals $1/2$ where $\pi\,\text{TPR} = (1-\pi)\,\text{FPR}$, that is at $\pi = \text{FPR}/(\text{TPR} + \text{FPR}) = 9/37 \approx 0.243$ *(inference)*. Below that prevalence this classifier's accuracy is lower than the all-negative classifier's, by the identity $\text{accuracy} - (1-\pi) = (TP - FP)/n$ *(inference)*.

![Line plot against prevalence on a log axis from 0.001 to 1: precision and F1 fall toward 0 as prevalence drops, accuracy stays near 0.78, balanced accuracy is flat at 0.726, the all-negative accuracy 1 minus prevalence rises toward 1, and a dotted random baseline equals prevalence](assets/class-imbalance-metric-choice/precision-vs-prevalence.svg)
*Figure: metrics of the toy classifier at TPR 2/3 and FPR 3/14 as the prevalence π varies on a log axis, drawn from the precision formula of Brabec et al.[^brabec] and the F1 formula of Williams[^williams]. Dots mark the precision values in the table above and squares mark F1 at π = 0.30 and π = 6/146, the two vertical dotted lines (inference). The finely dotted rising curve is the random-classifier precision π, the PR baseline[^saito]. Balanced accuracy is flat at 61/84 and accuracy rises toward the specificity 11/14, while the all-negative accuracy 1 − π overtakes accuracy at π = 9/37, where precision is 1/2; the two rings mark that crossing (inference). The curves were generated from the same exact fractions as the tables (inference).*

## Follow-ups
- How do you recompute a PR curve, AP and F1 for a target deployment prevalence from test-set TPR and FPR, and how many test negatives are needed for precision to be reliable at low prevalence?
- Does rebalancing the training set (resampling or class weights) change a classifier's test ROC and PR curves, or only shift its threshold?
- How does AUPRC's preference for high-prevalence subgroups affect fairness evaluation, and how should metrics be reported per subgroup?

[^fawcett]: [Fawcett, An introduction to ROC analysis](sources/fawcett-2006-roc-analysis.md)
[^saito]: [Saito and Rehmsmeier, The precision-recall plot is more informative than the ROC plot on imbalanced datasets](sources/saito-rehmsmeier-2015-prc-imbalanced.md)
[^dg]: [Davis and Goadrich, The relationship between precision-recall and ROC curves](sources/davis-goadrich-2006-pr-roc.md)
[^mcd]: [McDermott et al., A closer look at AUROC and AUPRC under class imbalance](sources/mcdermott-2024-auroc-auprc-imbalance.md)
[^williams]: [Williams, The effect of class imbalance on precision-recall curves](sources/williams-2021-imbalance-pr-curves.md)
[^brabec]: [Brabec et al., On model evaluation under non-constant class imbalance](sources/brabec-2020-non-constant-imbalance.md)
[^skguide]: [scikit-learn User Guide: Metrics and scoring (1.9.1)](sources/sklearn-model-evaluation.md)
[^skcm]: [scikit-learn API: confusion_matrix (1.9.1)](sources/sklearn-confusion-matrix.md)
[^skkappa]: [scikit-learn API: cohen_kappa_score (1.9.1)](sources/sklearn-cohen-kappa-score.md)
