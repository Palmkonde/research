---
question: What do the confusion matrix, precision, recall, specificity and F1 measure, and how is each computed from the matrix?
date: 2026-10-28
status: answered
---

## TL;DR
The confusion matrix counts a binary classifier's true positives, false positives, true negatives and false negatives[^fawcett]. Precision $TP/(TP+FP)$ asks how many predicted positives are real, recall $TP/(TP+FN)$ asks how many real positives were found, and specificity $TN/(TN+FP)$ asks how many real negatives were correctly rejected[^skguide][^fawcett]. F1 is the harmonic mean of precision and recall, equal to $2TP/(2TP+FP+FN)$[^fawcett][^skguide]. Each one ignores some cells of the matrix, so which one to report depends on which error costs more *(inference)*.

## Explanation
A classifier that outputs labels can be wrong in two different ways: it can raise a false alarm or it can miss a real case *(inference)*. One number such as accuracy mixes the two, while the confusion matrix keeps all four outcomes apart *(inference)*. Every metric on this page is a ratio of cells of that matrix, and the cells it leaves out decide what it is blind to *(inference)*. This page defines the matrix, then each metric, then works all of them on one toy dataset that later Findings in this Topic reuse *(inference)*.

### The confusion matrix
- **Four outcomes.** A positive instance classified as positive is a true positive, and classified as negative it is a false negative[^fawcett]. A negative instance classified as negative is a true negative, and classified as positive it is a false positive[^fawcett]. "Positive" and "negative" describe the prediction, and "true" and "false" say whether the prediction matches the actual label[^skguide].
- **The matrix.** Counting these four outcomes over a test set gives a two-by-two confusion matrix, also called a contingency table[^fawcett]. Its main diagonal holds the correct decisions and the other cells hold the errors[^fawcett].
- **Orientation differs between sources.** scikit-learn defines $C_{i,j}$ as the number of observations known to be in group $i$ and predicted to be in group $j$, so rows are actual classes and columns are predicted classes[^skcm]. Its user guide warns that other references may use a different convention for the axes[^skguide]. Fawcett's figure puts the true class on the columns and the predicted ("hypothesized") class on the rows[^fawcett], and van Rijsbergen's table also puts relevant and non-relevant on the columns and retrieved and not retrieved on the rows[^vr]. So before reading a matrix from a paper, check which axis is which *(inference)*.
- **The convention used here.** This Finding, and the rest of this Topic, uses scikit-learn's layout: rows are the actual class, columns the predicted class, negative class (label 0) first *(inference)*. In that layout true negatives are $C_{0,0}$, false positives $C_{0,1}$, false negatives $C_{1,0}$ and true positives $C_{1,1}$[^skcm].
- **Totals.** Fawcett writes $P$ for the total number of positives and $N$ for the total number of negatives[^fawcett]. In this layout they are row sums, $P = TP + FN$ and $N = TN + FP$, and the column sum $TP + FP$ is the number of predicted positives *(inference)*.

|  | predicted negative ($\hat y = 0$) | predicted positive ($\hat y = 1$) | row total |
|---|---|---|---|
| **actual negative** ($y = 0$) | TN | FP | $N = TN + FP$ |
| **actual positive** ($y = 1$) | FN | TP | $P = FN + TP$ |
| **column total** | $TN + FN$ | $TP + FP$ | $n$ |

*Figure: the binary confusion matrix in the layout this Topic uses, with rows for the actual class and columns for the predicted class, as in scikit-learn's `confusion_matrix`[^skcm]. Fawcett draws the same four cells transposed, with the true class on the columns[^fawcett]. The totals row and column are added here (inference).*

### Precision (positive predictive value)
**Question it answers:** of the samples the classifier predicted positive, how many are actually positive? *(inference: paraphrase of the definition below)*

$$\text{precision} = \frac{TP}{TP + FP}$$

- **Source and names.** Precision is $tp/(tp+fp)$[^skprfs][^fawcett]. It is also called the positive predictive value (PPV)[^fawcett]. scikit-learn describes it as "the ability of the classifier not to label a negative sample as positive"[^skprfs].
- **Where it lives.** Both of its cells sit in the predicted-positive column, so precision only looks at what the classifier flagged *(inference)*.
- **Range.** It is a count divided by a count at least as large, so it lies in $[0, 1]$ *(inference)*. It is undefined when the classifier predicts no positives, and scikit-learn's `zero_division` parameter sets the value returned in that case[^skprfs].
- **High and low.** Precision near 1 means almost every flagged sample is real; precision near 0 means most flags are false alarms *(inference)*.
- **When you care.** Precision matters when false positives are expensive, for example when every flag triggers a costly manual review, or when a spam filter hides a genuine email *(inference)*. It ignores false negatives, so a classifier that flags only its single most confident sample can reach precision 1 while missing nearly every positive *(inference)*.

### Recall (sensitivity, true positive rate)
**Question it answers:** of the samples that are actually positive, how many did the classifier find? *(inference: paraphrase of the definition below)*

$$\text{recall} = \frac{TP}{TP + FN}$$

- **Source and names.** Recall is $tp/(tp+fn)$, "intuitively the ability of the classifier to find all the positive samples"[^skprfs]. Fawcett defines the true positive rate as positives correctly classified over total positives, $TP/P$, and gives "hit rate" and "recall" as its other names[^fawcett]. Recall is also called sensitivity and the true positive rate (TPR)[^skguide][^fawcett].
- **Where it lives.** Both of its cells sit in the actual-positive row *(inference)*.
- **Range.** It lies in $[0, 1]$ *(inference)*. It is undefined when the data has no actual positives, and `zero_division` again sets the returned value[^skprfs].
- **High and low.** Recall near 1 means almost no positive is missed; recall near 0 means most positives slip through *(inference)*.
- **When you care.** Recall matters when false negatives are expensive, for example a disease screen that must not miss a sick patient, or a fraud check that must not miss a fraud *(inference)*. It ignores false positives: unconditionally predicting positive is the ROC point $(1, 1)$, which has a true positive rate of 1[^fawcett].

### Specificity (true negative rate)
**Question it answers:** of the samples that are actually negative, how many did the classifier correctly call negative? *(inference: paraphrase of the definition below)*

$$\text{specificity} = \frac{TN}{TN + FP} = 1 - \text{FPR}, \qquad \text{FPR} = \frac{FP}{N}$$

- **Source and names.** Fawcett defines specificity as $TN/(FP + TN)$ and shows it equals $1 - \text{FPR}$, where the false positive rate (also called the false alarm rate) is negatives incorrectly classified over total negatives[^fawcett]. Specificity is also called the true negative rate (TNR)[^skguide].
- **Where it lives.** Both of its cells sit in the actual-negative row, so specificity is recall computed for the negative class *(inference)*.
- **Range.** It lies in $[0, 1]$, and is undefined only when there are no actual negatives *(inference)*.
- **High and low.** Specificity near 1 means almost every negative is correctly let through; near 0 means most negatives get flagged *(inference)*.
- **When you care.** Specificity is usually read together with sensitivity, for example in a medical test, where low specificity means healthy people are told they are ill *(inference)*. An ROC graph plots the true positive rate against the false positive rate, which is $1 - \text{specificity}$[^fawcett][^skguide].
- **Specificity is not precision.** Both are hurt by false positives, but specificity divides them by the number of actual negatives and precision by the number of predicted positives *(inference)*. When negatives far outnumber positives, a classifier can have high specificity and low precision at once, because a small fraction of many negatives is still many false alarms *(inference)*.

### F1 and F-beta
**Question it answers:** how good is the classifier at both finding the positives and keeping its flags clean, in one number? *(inference)*

Fawcett gives the F-measure as[^fawcett]

$$F_1 = \frac{2}{\dfrac{1}{\text{precision}} + \dfrac{1}{\text{recall}}},$$

which is the harmonic mean of precision and recall *(inference)*. Clearing the fractions gives the two common forms *(inference)*:

$$F_1 = \frac{2 \cdot \text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}} = \frac{2\,TP}{2\,TP + FP + FN}.$$

- **The count form.** scikit-learn computes $F_\beta$ as $(1+\beta^2)\,tp \,/\, \big((1+\beta^2)\,tp + fp + \beta^2 fn\big)$, an otherwise equivalent formula that avoids division by zero when precision and recall are both zero[^skguide]. Setting $\beta = 1$ gives $2TP/(2TP + FP + FN)$ *(inference)*.
- **Range.** $F_\beta$ reaches its best value at 1 and its worst at 0[^skprfs].
- **Why the harmonic mean.** The harmonic mean is pulled toward the smaller of its two inputs, so F1 is high only when precision and recall are both high *(inference)*. With precision 1 and recall 0.01, F1 is about 0.02 while the arithmetic mean is about 0.505 *(inference)*.
- **What it ignores.** $TN$ does not appear in the count form, so F1 is blind to how many negatives were correctly rejected *(inference)*. As a result, F1 changes if you swap which class is called positive *(inference)*.

**F-beta** weights the two inputs unequally[^skguide]:

$$F_\beta = (1 + \beta^2)\,\frac{\text{precision} \cdot \text{recall}}{\beta^2\,\text{precision} + \text{recall}} = \frac{(1 + \beta^2)\,TP}{(1 + \beta^2)\,TP + FP + \beta^2\,FN}.$$

- $F_\beta$ weights recall more than precision by a factor of $\beta$, and $\beta = 1$ makes them equally important[^skprfs]. So $\beta = 2$ leans toward recall and $\beta = 0.5$ toward precision *(inference)*.
- **Origin.** van Rijsbergen derived an effectiveness measure $E = 1 - 1\big/\big(\alpha \tfrac{1}{P} + (1 - \alpha)\tfrac{1}{R}\big)$, with $\alpha = 1/(\beta^2 + 1)$, for a user who "attaches $\beta$ times as much importance to recall as precision"[^vr]. With $\alpha = 1/2$, that is $\beta = 1$, he notes it corresponds to a user who attaches equal importance to precision and recall[^vr]. Substituting $\alpha$ into $1 - E$ gives exactly the $F_\beta$ formula above, so $F_\beta = 1 - E$ *(inference)*.

### Accuracy, briefly
**Question it answers:** of all samples, how many did the classifier get right? *(inference)*

$$\text{accuracy} = \frac{TP + TN}{TP + TN + FP + FN} = \frac{TP + TN}{P + N}$$

- Fawcett gives accuracy as $(TP + TN)/(P + N)$[^fawcett], and scikit-learn as the fraction of correct predictions[^skguide].
- **Why it misleads under imbalance.** Fawcett argues that any metric using values from both classes is sensitive to the class distribution, and names accuracy, precision, lift and F score; the tp rate and fp rate are each a ratio within one class and do not depend on it[^fawcett]. He states this for columns, since his matrix puts the true class on the columns; in this Finding's layout the same split is between metrics that use both rows and metrics that stay within one row *(inference)*. Specificity is $1 - \text{FPR}$, so it is also unaffected by the class distribution *(inference)*.
- scikit-learn notes that if accuracy is above chance only because the classifier exploits an imbalanced test set, balanced accuracy, the mean of sensitivity and specificity, drops to $1/n_\text{classes}$[^skguide].
- How imbalance changes which metric to report is a separate open Question in the [Topic README](README.md) *(inference)*.

### Summary

| Metric | Other names | Formula | Question it answers | Cells used (this layout) |
|---|---|---|---|---|
| precision | PPV | $\frac{TP}{TP+FP}$ | of predicted positives, how many are real? | predicted-positive column |
| recall | sensitivity, TPR, hit rate | $\frac{TP}{TP+FN}$ | of real positives, how many were found? | actual-positive row |
| specificity | TNR, $1 - \text{FPR}$ | $\frac{TN}{TN+FP}$ | of real negatives, how many were rejected? | actual-negative row |
| F1 | F-measure | $\frac{2TP}{2TP+FP+FN}$ | are precision and recall both high? | every cell except TN |
| accuracy | none | $\frac{TP+TN}{n}$ | of all samples, how many are right? | diagonal over all cells |

*Figure: the five metrics side by side, whose formulas and other names come from Fawcett[^fawcett] and the scikit-learn guide[^skguide]. The questions and the cells-used column are read off this Finding's layout (inference).*

### Example: the shared toy dataset
This dataset is reused by the later Findings in this Topic (ROC and PR curves, imbalance, thresholds, reporting), so its labels and scores should not be changed *(inference)*. It has 20 samples, 6 actual positives and 14 negatives, a prevalence of $6/20 = 0.30$ *(inference)*. Each sample has a true label $y$ and a classifier score in $[0, 1]$; no two scores are tied and no score equals 0.5 *(inference)*. The rows are sorted by score, highest first, so a threshold is a cut between two rows *(inference)*.

The decision rule at threshold 0.5 is: predict positive ($\hat y = 1$) if and only if the score is at least 0.5 *(inference: a choice made for this example)*.

| id | true label $y$ | score | $\hat y$ at 0.5 | outcome |
|---|---|---|---|---|
| s01 | 1 | 0.95 | 1 | TP |
| s02 | 1 | 0.88 | 1 | TP |
| s03 | 0 | 0.83 | 1 | FP |
| s04 | 1 | 0.76 | 1 | TP |
| s05 | 0 | 0.71 | 1 | FP |
| s06 | 1 | 0.64 | 1 | TP |
| s07 | 0 | 0.58 | 1 | FP |
| s08 | 1 | 0.47 | 0 | FN |
| s09 | 0 | 0.42 | 0 | TN |
| s10 | 0 | 0.37 | 0 | TN |
| s11 | 1 | 0.33 | 0 | FN |
| s12 | 0 | 0.29 | 0 | TN |
| s13 | 0 | 0.24 | 0 | TN |
| s14 | 0 | 0.19 | 0 | TN |
| s15 | 0 | 0.15 | 0 | TN |
| s16 | 0 | 0.12 | 0 | TN |
| s17 | 0 | 0.09 | 0 | TN |
| s18 | 0 | 0.06 | 0 | TN |
| s19 | 0 | 0.04 | 0 | TN |
| s20 | 0 | 0.02 | 0 | TN |

The seven samples above the cut (s01 to s07) hold 4 positives and 3 negatives, and the thirteen below it hold 2 positives and 11 negatives *(inference)*. That gives $TP = 4$, $FP = 3$, $FN = 2$, $TN = 11$ *(inference)*:

$$
C \;=\;
\begin{array}{r|cc}
 & \hat y = 0 & \hat y = 1 \\ \hline
y = 0 & TN = 11 & FP = 3 \\
y = 1 & FN = 2 & TP = 4
\end{array}
\qquad
P = 6,\; N = 14,\; n = 20
$$

*Figure: the confusion matrix of the toy dataset at threshold 0.5, in the rows-are-actual layout of scikit-learn's `confusion_matrix`[^skcm]. The counts are tallied from the table above (inference: also checked with a throwaway script, not shown).*

Working each metric by hand *(inference: all values below were also checked with exact fractions and with scikit-learn 1.9.1, not shown)*:

- **Precision** $= \dfrac{TP}{TP + FP} = \dfrac{4}{4 + 3} = \dfrac{4}{7} \approx 0.571$ *(inference)*. Of the 7 flagged samples, 4 are real positives *(inference)*.
- **Recall** $= \dfrac{TP}{TP + FN} = \dfrac{4}{4 + 2} = \dfrac{2}{3} \approx 0.667$ *(inference)*. The classifier found 4 of the 6 positives and missed s08 and s11 *(inference)*.
- **Specificity** $= \dfrac{TN}{TN + FP} = \dfrac{11}{11 + 3} = \dfrac{11}{14} \approx 0.786$, so $\text{FPR} = \dfrac{3}{14} \approx 0.214$ *(inference)*.
- **F1 as a harmonic mean** $= \dfrac{2 \cdot \frac{4}{7} \cdot \frac{2}{3}}{\frac{4}{7} + \frac{2}{3}} = \dfrac{16/21}{26/21} = \dfrac{16}{26} = \dfrac{8}{13} \approx 0.615$ *(inference)*.
- **F1 from counts** $= \dfrac{2 \cdot 4}{2 \cdot 4 + 3 + 2} = \dfrac{8}{13} \approx 0.615$, the same value *(inference)*.
- **$F_2$** $= \dfrac{5 \cdot 4}{5 \cdot 4 + 3 + 4 \cdot 2} = \dfrac{20}{31} \approx 0.645$, and **$F_{0.5}$** $= \dfrac{1.25 \cdot 4}{1.25 \cdot 4 + 3 + 0.25 \cdot 2} = \dfrac{5}{8.5} = \dfrac{10}{17} \approx 0.588$ *(inference)*.
- **Accuracy** $= \dfrac{TP + TN}{n} = \dfrac{4 + 11}{20} = \dfrac{15}{20} = 0.75$ *(inference)*.

Reading the numbers:
- $F_2 > F_1 > F_{0.5}$ here because recall (0.667) is higher than precision (0.571), and a larger $\beta$ leans the mean toward recall *(inference)*.
- Specificity (0.786) is higher than precision (0.571) although both are hurt by the same 3 false positives: those 3 are $3/14$ of the actual negatives but $3/7$ of the predicted positives *(inference)*.
- A useless classifier that predicts negative for every sample gets accuracy $14/20 = 0.70$, only 0.05 below this classifier, while its recall is $0/6 = 0$ and its precision is undefined *(inference)*. scikit-learn warns about exactly this: accuracy that is above chance only because the classifier takes advantage of an imbalanced test set[^skguide].

## Follow-ups
- How should precision, recall and F1 be reported when a denominator is zero (no predicted positives, or no actual positives), and how does the `zero_division` choice change an average over classes or folds?
- How does F1 change when the other class is called positive, and how should the positive class be chosen?
- Why is the harmonic mean, rather than the arithmetic or geometric mean, the right way to combine precision and recall (van Rijsbergen's measurement-theory argument)?

[^skguide]: [scikit-learn User Guide: Metrics and scoring (1.9.1)](sources/sklearn-model-evaluation.md)
[^skcm]: [scikit-learn API: confusion_matrix (1.9.1)](sources/sklearn-confusion-matrix.md)
[^skprfs]: [scikit-learn API: precision_recall_fscore_support (1.9.1)](sources/sklearn-precision-recall-fscore-support.md)
[^fawcett]: [Fawcett, An introduction to ROC analysis](sources/fawcett-2006-roc-analysis.md)
[^vr]: [van Rijsbergen, Information Retrieval, Chapter 7](sources/van-rijsbergen-1979-information-retrieval.md)
