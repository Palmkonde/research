---
question: How is a decision threshold chosen and computed, and how does it link threshold-free metrics (AUC) to threshold metrics (F1)?
date: 2026-10-28
status: answered
---

## TL;DR
A scoring classifier plus a threshold $t$ gives a discrete classifier, and each threshold is one point in ROC space[^fawcett]. The same confusion matrix is also one point on the PR curve[^dg], and F1 and every other threshold metric are read from that matrix *(inference)*. The cut-off of 0.5 is only scikit-learn's hard-coded default for probabilities, which its guide says is "most certainly not ideal for most use cases"[^skthr]. Choose $t$ on validation data, never on the test set[^skthr][^skpit]. There are four common rules *(inference: the grouping)*:
- maximize F1 or $F_\beta$ over the sweep *(inference)*;
- maximize Youden's $J = \text{TPR} - \text{FPR}$[^skguide][^powers];
- meet a target such as recall $\ge 0.9$ at the best precision[^skthr] *(inference: the rule as written)*;
- minimize expected cost: for probabilities this means predicting positive when $p \ge c_{FP}/(c_{FP}+c_{FN})$[^elkan], which on the ROC curve is the most northwest iso-cost line[^fawcett].

For calibrated probabilities, the F1-optimal threshold is half the best F1[^lipton]. On a fixed score scale, the F1-optimal and cost-optimal thresholds move with prevalence while Youden's does not *(inference)*. ROC AUC summarizes all thresholds at once, while F1 is read at one of them, so two models can rank differently on the two[^fawcett].

## Explanation
The [ROC/PR Finding](roc-auc-vs-pr-auc.md) showed that one set of scores gives a whole family of confusion matrices, one per threshold *(inference)*. A deployed classifier must commit to one of them, and every number on its report card (precision, recall, F1) depends on which one *(inference)*. This page shows how that threshold is computed from the sweep and which rule fits which goal *(inference)*. It then explains why a threshold chosen on one dataset does not carry over to another with a different prevalence *(inference)*. It keeps the Topic's notation and layout: rows of the confusion matrix are the actual class, $P$ and $N$ count actual positives and negatives, $\pi = P/(P+N)$, $\text{TPR} = TP/P$ and $\text{FPR} = FP/N$ *(inference)*.

### Scores, probabilities, and why 0.5 is only a default
- **Two kinds of output.** A scoring classifier's output can be a strict probability, or an uncalibrated score for which "a higher score indicates a higher probability" is the only property that holds[^fawcett]. In scikit-learn, `predict_proba` returns conditional probability estimates $P(y \mid X)$, and `decision_function` returns a decision score[^skthr].
- **The default cut-off.** scikit-learn's `predict` uses hard-coded rules: positive when $P(y \mid X)$ is greater than 0.5, or when the decision score is greater than 0[^skthr]. This Topic instead predicts positive when $\text{score} \ge t$, as `roc_curve` does[^skroc]. No toy score equals 0.5, so the two conventions agree there *(inference)*.
- **Why 0.5 is not special.** Elkan notes that standard learners built to maximize accuracy implicitly decide at probability threshold 0.5[^elkan]. His cost formula below gives 0.5 only when the two errors cost the same *(inference: setting $c_{FP} = c_{FN}$ in eq. (2))*. Fawcett adds that accuracy at a 0.5 threshold would be appropriate only if the scores were proper probabilities[^fawcett]. His Fig. 4 shows a classifier with a perfect ROC curve that is only 80% accurate at 0.5[^fawcett].
- **Scores are not comparable across models.** Comparing models of different classes at a common threshold is meaningless, since one may score in $[0, 1]$ and another in $[-1, +1]$[^fawcett].
- **Calibration matters for two rules below.** The cost rule and the half-F1 rule assume calibrated probabilities[^elkan][^lipton]. How calibration is measured is a separate open Question in the [Topic README](README.md) *(inference)*.

### One threshold is one point on each curve
$$TP(t) = \#\{i : y_i = 1,\ s_i \ge t\}, \qquad FP(t) = \#\{i : y_i = 0,\ s_i \ge t\}, \qquad FN(t) = P - TP(t)$$

- **From scores to a matrix.** Each threshold value gives a different point in ROC space[^fawcett]. For a fixed dataset, each ROC point with recall above 0 matches exactly one PR point with the same confusion matrix[^dg]. So the threshold is the single parameter that ties together one ROC point, one PR point and one confusion matrix *(inference)*.
- **Every threshold metric is a function of $t$.** Precision, recall, F1, $F_\beta$, $J$ and cost all come from the same four counts at $t$ *(inference)*:
  $$F_\beta(t) = \frac{(1+\beta^2)\,TP(t)}{(1+\beta^2)\,TP(t) + FP(t) + \beta^2 FN(t)}, \qquad J(t) = \text{TPR}(t) - \text{FPR}(t).$$
- **Thresholds are intervals.** The counts change only when $t$ passes a sample's score, so on a finite set every metric is a step function of $t$ *(inference)*. With the scores sorted as $s_{(1)} > s_{(2)} > \dots$, every $t$ in $(s_{(k+1)}, s_{(k)}]$ gives the same matrix *(inference)*. So "the best threshold" is really a best interval, and any value in it, such as the score $s_{(k)}$ itself, represents it *(inference)*.
- **F1 is the ROC point plus the prevalence.** Substituting precision $= \pi\,\text{TPR}/\big(\pi\,\text{TPR} + (1-\pi)\,\text{FPR}\big)$ into $F_1$ gives the form derived in the [class-imbalance Finding](class-imbalance-metric-choice.md#precision-as-a-function-of-prevalence) from Williams' $F_\beta$ equation[^williams]:
  $$F_1(t) = \frac{2\,\pi\,\text{TPR}(t)}{\pi\,\big(1 + \text{TPR}(t)\big) + (1-\pi)\,\text{FPR}(t)}.$$
  So F1 at a threshold is fixed by that threshold's ROC point and by $\pi$, while $J(t)$ needs only the ROC point *(inference)*.

### Rule 1: maximize F1 or $F_\beta$ over the sweep
$$t_{F_\beta} = \arg\max_t F_\beta(t)$$

- **How to compute it.** Sort the scores, sweep the threshold down as in the [ROC/PR Finding](roc-auc-vs-pr-auc.md#from-scores-to-curves-the-threshold-sweep), evaluate $F_\beta$ at each of the $n + 1$ distinct matrices, and keep the best *(inference)*.
- **Choosing $\beta$.** $F_\beta$ weights recall $\beta$ times as much as precision, so $\beta = 2$ moves the optimum toward lower thresholds and higher recall *(inference: from the [first Finding](confusion-matrix-basic-metrics.md#f1-and-f-beta))*.
- **What the optimum looks like for probabilities.** Lipton, Elkan and Naryanaswamy show that, for calibrated probabilities, an instance with probability $s$ is predicted positive by the F1-maximizing rule if and only if $s \ge F^*/2$, where $F^*$ is the F1 that rule achieves[^lipton]:
  $$t_{F_1} = \frac{F^*}{2}.$$
  Because F1 cannot exceed 1, this threshold never exceeds 0.5[^lipton].

### Rule 2: maximize Youden's J
$$J(t) = \text{TPR}(t) - \text{FPR}(t) = \text{sensitivity}(t) + \text{specificity}(t) - 1$$

- **Definition.** Powers defines informedness as recall plus inverse recall minus 1, which equals $\text{tpr} - \text{fpr}$[^powers]. scikit-learn's adjusted balanced accuracy is, in the binary case, "also known as Youden's J statistic, or informedness"[^skguide]. Its rescaling of balanced accuracy from chance (1/2) to 1 gives $J = 2\,\text{BA} - 1 = \text{TPR} + \text{TNR} - 1$ *(inference)*.
- **Geometry.** $J$ is the vertical distance from the ROC point to the diagonal *(inference)*. Powers notes that, with equal costs and no skew ($c = 1$), isocost lines have the form $\text{tpr} - \text{fpr} = k$, and the highest one maximizes $\text{tpr} - \text{fpr}$[^powers]. So the Youden point is where a line of slope 1 touches the ROC curve from the northwest *(inference)*.
- **No prevalence in it.** $J$ uses only TPR and FPR, which are ratios within one class and do not depend on the class distribution[^fawcett]. So the Youden threshold does not move when $\pi$ changes and the score distributions stay fixed *(inference)*.
- **Default in scikit-learn.** `TunedThresholdClassifierCV` maximizes balanced accuracy by default[^sktuned]. Balanced accuracy is $(1 + J)/2$, so the default tuned threshold is the Youden point *(inference)*.

### Rule 3: a target recall or precision
$$t_{\text{rec} \ge r} = \arg\max_{t\,:\ \text{TPR}(t) \ge r} \text{precision}(t)$$

- **When to use it.** In scikit-learn's tumor-detection example, physicians prioritize a high recall because a missed cancer costs far more than further tests[^skthr]. A requirement like "recall $\ge 0.9$" is then a constraint, and among the thresholds that meet it you keep the one with the best precision *(inference)*. The precision-floor version swaps the two roles *(inference)*.
- **How to compute it.** Recall never falls as $t$ is lowered, so the feasible thresholds are all those at or below the highest one that meets the target *(inference)*. Precision is not monotone along the sweep (the [ROC/PR Finding](roc-auc-vs-pr-auc.md#the-pr-curve-precision-against-recall) calls it a sawtooth), so scan all of them rather than taking the first *(inference)*.
- **In scikit-learn.** `TunedThresholdClassifierCV` optimizes a binary metric, "potentially constrained by another metric"[^sktuned].

### Rule 4: minimum expected cost, and Elkan's threshold
Let $p = P(y = 1 \mid x)$ be a calibrated probability, using the conditional probability of the [probability basics](../../fundamentals/probability-basics/README.md) Prerequisite *(inference)*. The best prediction is the class with the lowest expected cost, computed with the conditional probability of each class[^elkan]. Elkan writes $c_{ij}$ for the cost of predicting class $i$ when the truth is $j$, with rows for the prediction, so a false positive costs $c_{10}$ and a false negative $c_{01}$[^elkan]. In this Topic's layout, with rows for the actual class, the same costs read *(inference: Elkan's matrix transposed)*:

$$
\begin{array}{r|cc}
 & \hat y = 0 & \hat y = 1 \\ \hline
y = 0 & c_{00} & c_{FP} = c_{10} \\
y = 1 & c_{FN} = c_{01} & c_{11}
\end{array}
$$

- **The rule.** Predict 1 if and only if $(1-p)\,c_{10} + p\,c_{11} \le (1-p)\,c_{00} + p\,c_{01}$, which holds exactly when $p \ge p^*$ with[^elkan]
  $$p^* = \frac{c_{10} - c_{00}}{c_{10} - c_{00} + c_{01} - c_{11}}.$$
- **Zero cost for correct decisions.** With $c_{00} = c_{11} = 0$ this becomes *(inference)*
  $$t^* = \frac{c_{FP}}{c_{FP} + c_{FN}}.$$
  Equal costs give $t^* = 1/2$, and a false negative four times as costly gives $t^* = 1/5$ *(inference)*. "Bayes-optimal" is a common name for this rule, not Elkan's own term *(inference)*.
- **One degree of freedom.** Scaling or shifting the cost matrix leaves the optimal decisions unchanged[^elkan], so only the ratio $c_{FN}/c_{FP}$ matters once the diagonal is zero *(inference)*.
- **Elkan's recommendation.** Learn the classifier from the training set as given, then compute the optimal decisions explicitly from its probability estimates[^elkan]. That is the threshold rule above *(inference)*. It is only as good as the probabilities, so on uncalibrated scores it is a rough guide, not an optimum *(inference)*.
- **The empirical version.** On a validation set, minimize the total cost $C(t) = c_{FP}\,FP(t) + c_{FN}\,FN(t)$ over the sweep *(inference)*. This needs no calibration, because it only counts errors *(inference)*.

### Iso-cost lines on the ROC curve
- **Fawcett's slope.** Two ROC points have the same expected cost when the line joining them has slope[^fawcett]
  $$m = \frac{c(Y, n)\,p(n)}{c(N, p)\,p(p)} = \frac{c_{FP}\,N}{c_{FN}\,P},$$
  where $c(Y, n)$ is the cost of a false positive, $c(N, p)$ that of a false negative, and $p(n)$, $p(p)$ the class proportions *(inference: Fawcett's symbols mapped to this Topic's)*.
- **Why.** The total cost is $C = c_{FP}\,N\,\text{FPR} + c_{FN}\,P\,(1 - \text{TPR})$ *(inference)*. Dividing by $c_{FN}\,P$ gives
  $$\text{TPR} - m\,\text{FPR} = 1 - \frac{C}{c_{FN}\,P},$$
  so minimizing cost is the same as maximizing the intercept of a line of slope $m$ through the ROC point *(inference)*.
- **The picture.** Lines more to the northwest (with a larger TP-intercept) have lower expected cost, and the best operating point is where the most northwest line of slope $m$ touches the curve[^fawcett]. Only points on the ROC convex hull can be optimal for any costs[^fawcett].
- **Youden is a special case.** Youden's $J$, which is informedness[^skguide], is the case $m = 1$[^powers], that is $c_{FN}/c_{FP} = N/P$ *(inference)*.
- **Prevalence moves the line.** In Fawcett's examples, 10 negatives per positive with equal costs gives $m = 10$, and balanced classes with false negatives ten times as costly give $m = 1/10$[^fawcett]. A shift in $\pi$ therefore changes $m$, and with it the best point and threshold, even though the curve itself does not change[^fawcett] *(inference: the threshold part)*.

### Why the best-F1 threshold depends on prevalence
- **The formula already says so.** $F_1(t)$ above contains $\pi$, so the threshold that maximizes it depends on $\pi$, while $\arg\max_t J(t)$ does not *(inference)*.
- **Lipton et al.'s theorem.** For known score distributions $p(s \mid y)$ and base rate $b = \pi$, a score is predicted positive by the F1-maximizing rule if and only if[^lipton]
  $$\frac{\pi\,p(s \mid y = 1)}{(1-\pi)\,p(s \mid y = 0)} \ \ge\ \mathcal{J}^*,$$
  where $\mathcal{J}^* = tp/(tp + fp + fn)$ is the Jaccard index of the optimal classifier, and its counts are fractions of the data, not raw counts[^lipton]. The prior odds $\pi/(1-\pi)$ multiply the left side, so the cut-off on the score moves with prevalence *(inference)*. They contrast this with cost-sensitive decisions, where the right side is a constant set by the costs alone[^lipton]. The prior odds still multiply the left side there, so a cost rule's cut-off on the score also moves with $\pi$ *(inference)*.
- **Which scale is fixed.** Two views need to be kept apart *(inference)*:
  - *Fixed scores.* The same model is applied to data with a different $\pi$, so each threshold keeps its TPR and FPR *(inference)*. The Youden threshold stays, while the F1 and cost thresholds move, as the example below shows *(inference)*.
  - *Recalibrated probabilities.* The probabilities are re-estimated for the new $\pi$ *(inference)*. Elkan's $t^* = c_{FP}/(c_{FP}+c_{FN})$ then stays fixed in probability space, because it contains no $\pi$[^elkan] *(inference: the reading)*. The score that maps to $t^*$ moves instead *(inference)*. Lipton et al.'s $F^*/2$ moves with $F^*$ *(inference)*.
- **The uninformative extreme.** If the classifier gives every example the same score, F1-optimal thresholding predicts every example positive, and the F1 this gets depends strongly on the base rate[^lipton].
- **Rankings can flip too.** Brabec et al. show that F1 can swap the order of two classifiers as the imbalance changes[^brabec].
- **What to do.** Tune the threshold on validation data whose prevalence matches deployment, and re-tune if the prevalence shifts *(inference)*. Alternatively, choose by $J$ or a cost rule whose $m$ uses the deployment $\pi$ *(inference)*.

### Choose on validation data, not the test set
- **The rule.** scikit-learn warns "You should never use the same data for training the classifier and tuning the decision threshold due to the risk of overfitting"[^skthr]. Its pitfalls page states that test data should never be used to make choices about the model, because leakage gives overly optimistic performance estimates[^skpit].
- **What it means here.** Picking $t$ is fitting one more parameter, so it needs its own data: fit the model on training data, choose $t$ on a validation split or by cross-validation, then report the test metrics at that fixed $t$ *(inference)*. The maximum F1 over a test-set sweep is the best of many tries on the test data, so it is biased upward *(inference)*.
- **How scikit-learn does it.** `TunedThresholdClassifierCV` uses an internal 5-fold stratified cross-validation by default[^skthr][^sktuned]. Its `cv="prefit"` option is meant only for a classifier that is already trained, with a new validation set used to tune the threshold[^skthr].

### Threshold-free and threshold metrics: how they connect
- **AUC sees every threshold; F1 sees one.** ROC AUC is the probability that a random positive outscores a random negative, a property of the whole ranking[^fawcett]. F1 is computed from the single matrix at the chosen $t$ *(inference)*.
- **Moving $t$ does not move AUC.** In scikit-learn, a tuned and an untuned classifier have the same `predict_proba` outputs, and so the same ROC and PR curves, while their class predictions differ[^skthr]. So threshold tuning can change F1 a lot while ROC AUC and AP stay fixed *(inference)*.
- **Rankings can disagree.** A high-AUC classifier can perform worse in a specific region of ROC space than a low-AUC one[^fawcett]. A model with the higher AUC can therefore have the lower best F1, as the example below shows *(inference)*.
- **What to report.** Report the area for ranking quality, and also the operating point: the threshold, the rule and data used to choose it, and the threshold metrics at that point *(inference)*.

### In scikit-learn (usage only)
- **Tuned threshold.** `TunedThresholdClassifierCV` post-tunes the threshold on `predict_proba` or `decision_function` output by optimizing a binary metric[^sktuned]. Set `scoring` to the metric you mean, since the default, balanced accuracy, may not suit the use case, and set the right `pos_label`[^skthr]. After fitting, `best_threshold_` holds the chosen threshold and `best_score_` the metric there[^sktuned].
- **Grid, not exact scores.** By default it tries 100 thresholds that discretize the classifier output, or an explicit array of thresholds you pass[^sktuned]. So its optimum can fall at a grid value inside the best interval rather than exactly at a score *(inference)*.
- **Fixed threshold.** `FixedThresholdClassifier` sets the threshold by hand, for example to Elkan's $t^*$ or a threshold chosen elsewhere[^skthr] *(inference: the use)*.
- **Plotting.** A plot of metric values against the threshold helps when more than one metric matters, and `metric_at_thresholds` computes one metric at each unique score threshold for such a plot[^skthr].

### Example: every threshold metric on the sweep
This is the shared toy dataset of the [first Finding](confusion-matrix-basic-metrics.md#example-the-shared-toy-dataset), unchanged: 20 samples, $P = 6$, $N = 14$, $\pi = 0.30$ *(inference)*. The table extends the sweep table of the [ROC/PR Finding](roc-auc-vs-pr-auc.md#example-the-threshold-sweep) with $F_1$, $F_2$, $J$ and a cost with $c_{FP} = 1$, $c_{FN} = 4$, so $C = FP + 4\,FN$ *(inference)*. Row $k$ holds for every $t$ in $(s_{(k+1)}, s_{(k)}]$, and the "threshold" column shows $s_{(k)}$ *(inference)*. Every value was computed with exact fractions in a throwaway script and spot-checked with scikit-learn 1.9.1 *(inference: not shown)*.

| step | threshold $t$ | TP | FP | FN | precision | recall (TPR) | $F_1$ | $F_2$ | $J$ | cost $C$ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | $+\infty$ | 0 | 0 | 6 | undefined | $0$ | $0$ | $0$ | $0$ | 24 |
| 1 | 0.95 | 1 | 0 | 5 | $1$ | $1/6$ (0.167) | $2/7$ (0.286) | $1/5$ (0.200) | $1/6$ (0.167) | 20 |
| 2 | 0.88 | 2 | 0 | 4 | $1$ | $1/3$ (0.333) | $1/2$ (0.500) | $5/13$ (0.385) | $1/3$ (0.333) | 16 |
| 3 | 0.83 | 2 | 1 | 4 | $2/3$ (0.667) | $1/3$ (0.333) | $4/9$ (0.444) | $10/27$ (0.370) | $11/42$ (0.262) | 17 |
| 4 | 0.76 | 3 | 1 | 3 | $3/4$ (0.750) | $1/2$ (0.500) | $3/5$ (0.600) | $15/28$ (0.536) | $3/7$ (0.429) | 13 |
| 5 | 0.71 | 3 | 2 | 3 | $3/5$ (0.600) | $1/2$ (0.500) | $6/11$ (0.545) | $15/29$ (0.517) | $5/14$ (0.357) | 14 |
| 6 | 0.64 | 4 | 2 | 2 | $2/3$ (0.667) | $2/3$ (0.667) | $2/3$ (0.667) | $2/3$ (0.667) | $11/21$ (0.524) | 10 |
| 7 | 0.58 | 4 | 3 | 2 | $4/7$ (0.571) | $2/3$ (0.667) | $8/13$ (0.615) | $20/31$ (0.645) | $19/42$ (0.452) | 11 |
| 8 | 0.47 | 5 | 3 | 1 | $5/8$ (0.625) | $5/6$ (0.833) | $5/7$ (0.714) | $25/32$ (0.781) | $13/21$ (0.619) | 7 |
| 9 | 0.42 | 5 | 4 | 1 | $5/9$ (0.556) | $5/6$ (0.833) | $2/3$ (0.667) | $25/33$ (0.758) | $23/42$ (0.548) | 8 |
| 10 | 0.37 | 5 | 5 | 1 | $1/2$ (0.500) | $5/6$ (0.833) | $5/8$ (0.625) | $25/34$ (0.735) | $10/21$ (0.476) | 9 |
| 11 | 0.33 | 6 | 5 | 0 | $6/11$ (0.545) | $1$ | $12/17$ (0.706) | $6/7$ (0.857) | $9/14$ (0.643) | 5 |
| 12 | 0.29 | 6 | 6 | 0 | $1/2$ (0.500) | $1$ | $2/3$ (0.667) | $5/6$ (0.833) | $4/7$ (0.571) | 6 |
| 13 | 0.24 | 6 | 7 | 0 | $6/13$ (0.462) | $1$ | $12/19$ (0.632) | $30/37$ (0.811) | $1/2$ (0.500) | 7 |
| 14 | 0.19 | 6 | 8 | 0 | $3/7$ (0.429) | $1$ | $3/5$ (0.600) | $15/19$ (0.789) | $3/7$ (0.429) | 8 |
| 15 | 0.15 | 6 | 9 | 0 | $2/5$ (0.400) | $1$ | $4/7$ (0.571) | $10/13$ (0.769) | $5/14$ (0.357) | 9 |
| 16 | 0.12 | 6 | 10 | 0 | $3/8$ (0.375) | $1$ | $6/11$ (0.545) | $3/4$ (0.750) | $2/7$ (0.286) | 10 |
| 17 | 0.09 | 6 | 11 | 0 | $6/17$ (0.353) | $1$ | $12/23$ (0.522) | $30/41$ (0.732) | $3/14$ (0.214) | 11 |
| 18 | 0.06 | 6 | 12 | 0 | $1/3$ (0.333) | $1$ | $1/2$ (0.500) | $5/7$ (0.714) | $1/7$ (0.143) | 12 |
| 19 | 0.04 | 6 | 13 | 0 | $6/19$ (0.316) | $1$ | $12/25$ (0.480) | $30/43$ (0.698) | $1/14$ (0.071) | 13 |
| 20 | 0.02 | 6 | 14 | 0 | $3/10$ (0.300) | $1$ | $6/13$ (0.462) | $15/22$ (0.682) | $0$ | 14 |

Reading the table:
- Step 7 is the default threshold 0.5: $TN = 11$, $FP = 3$, $FN = 2$, $TP = 4$ and $F_1 = 8/13$, as in the first Finding *(inference)*.
- Step 8 covers every $t \in (0.42, 0.47]$, so any threshold in it, such as 0.45, gives $F_1 = 5/7$ *(inference)*.
- At step 0, F1 is $0$ by the count form $2TP/(2TP + FP + FN)$, while precision is $0/0$ *(inference)*.

### Example: the selection rules on the toy data
Treat the 20 samples as if they were the validation set *(inference: a stand-in, since the toy has no separate split)*.

| rule | best step | threshold interval | value there | confusion matrix (TN, FP, FN, TP) |
|---|---|---|---|---|
| default $t = 0.5$ | 7 | $(0.47, 0.58]$ | $F_1 = 8/13 \approx 0.615$ | 11, 3, 2, 4 |
| max $F_1$ | 8 | $(0.42, 0.47]$ | $F_1 = 5/7 \approx 0.714$ | 11, 3, 1, 5 |
| recall $\ge 0.8$, best precision | 8 | $(0.42, 0.47]$ | precision $5/8 = 0.625$ | 11, 3, 1, 5 |
| max $F_2$ | 11 | $(0.29, 0.33]$ | $F_2 = 6/7 \approx 0.857$ | 9, 5, 0, 6 |
| max $J$ (Youden) | 11 | $(0.29, 0.33]$ | $J = 9/14 \approx 0.643$ | 9, 5, 0, 6 |
| recall $\ge 0.9$, best precision | 11 | $(0.29, 0.33]$ | precision $6/11 \approx 0.545$ | 9, 5, 0, 6 |
| min cost, $c_{FN} = 4\,c_{FP}$ | 11 | $(0.29, 0.33]$ | $C = 5$ | 9, 5, 0, 6 |

*Figure: the threshold each rule picks on the toy sweep, read off the table above (inference). Every rule lands on a whole interval of thresholds between two consecutive scores (inference).*

- **Max F1.** $F_1$ peaks at step 8 with $5/7$, at $t = 0.47$ *(inference)*. That is better than the default's $8/13$, because lowering the threshold past s08 turns a false negative into a true positive and adds no false positive *(inference)*.
- **Max J.** $J$ peaks at step 11: $\text{TPR} = 1$, $\text{FPR} = 5/14$, $J = 9/14$ *(inference)*. Youden's rule goes lower than F1's, to catch s11, at the price of two more false positives (s09, s10) *(inference)*.
- **Recall targets.** Recall first reaches $0.8$ at step 8 ($5/6$), where precision is $5/8$; the later steps that also qualify have lower precision *(inference)*. "Recall $\ge 0.9$" needs all six positives, so step 11 *(inference)*.
- **F1 vs F2.** $F_2$ peaks at step 11 with $6/7$, the same step as $J$, because it weights the missed positive s11 four times as much as a false alarm *(inference)*.
- **Fragile on 20 samples.** The F1 optimum at step 8 ($5/7 \approx 0.714$) beats step 11 ($12/17 \approx 0.706$) by only $1/119$ *(inference)*. Relabeling s09 as positive would make step 11 the winner *(inference: then step 8 has F1 $10/15$ and step 11 has $14/18$)*. Picking the best of 21 thresholds on the same data that reports the score is exactly the optimism that a separate validation set avoids[^skpit] *(inference: applied to this example)*.

![Two panels. Left: step plots of F1, Youden's J, recall and precision against the threshold from 0 to 1, with ticks a to d above the plot at thresholds 0.5, 0.47, 0.33 and 0.2, and rings at the F1 peak and the J peak. Right: the toy ROC curve with the points a to d marked, a thin solid iso-cost line of slope 7/12 and a dashed Youden line of slope 1 both touching point c, and a dotted diagonal](assets/decision-threshold/threshold-sweep.svg)
*Figure: left, the threshold metrics of the toy sweep as step functions of t, each constant on the interval between two consecutive scores; right, the same thresholds as points on the toy ROC curve (inference). Each threshold value gives one ROC point[^fawcett]. The ring on F1 marks its peak 5/7 at t = 0.47 (b), and the ring on J marks its peak 9/14 at t = 0.33 (c) (inference). Point a is the default threshold 0.5 at (3/14, 2/3), and d is Elkan's threshold 0.2 for a false negative four times as costly as a false positive, which lands at (1/2, 1) (inference). The thin solid line of slope 7/12 is the most northwest iso-cost line for those costs[^fawcett]. The dashed line of slope 1, drawn in the same pattern as J on the left, is the highest isocost line for J[^powers]; both lines touch the curve at c (inference). The coordinates were generated from the same exact fractions as the table (inference).*

### Example: a cost-based threshold
Take $c_{FP} = 1$ and $c_{FN} = 4$: a missed positive costs four false alarms *(inference: a choice for this example)*.

- **Empirical minimum.** $C = FP + 4\,FN$ is smallest at step 11, with $C = 5 + 4 \cdot 0 = 5$, against $C = 3 + 4 \cdot 2 = 11$ at the default 0.5 *(inference)*.
- **Iso-cost line.** The slope is $m = c_{FP} N/(c_{FN} P) = (1 \cdot 14)/(4 \cdot 6) = 7/12$ *(inference)*. By the identity $\text{TPR} - m\,\text{FPR} = 1 - C/(c_{FN} P) = 1 - C/24$, the minimum cost 5 gives the largest intercept, $1 - 5/24 = 19/24 \approx 0.792$, at the ROC point $(5/14, 1)$ *(inference)*. That is the thin solid line in the figure *(inference)*.
- **Youden as a cost rule.** On this dataset, $J$ is the cost rule with $c_{FN}/c_{FP} = N/P = 7/3$ *(inference)*. The ratio 7/3 differs from 4, yet both rules happen to pick step 11 here *(inference)*.
- **Elkan's threshold, as an illustration only.** For calibrated probabilities the rule is $t^* = 1/(1 + 4) = 0.2$ *(inference)*. On the toy scores, $t = 0.2$ predicts s01 to s13 positive, which is step 13, with cost $C = 7$, not the minimum 5 *(inference)*.
- **Why the rule misses.** The toy scores are not calibrated: the seven samples scored at least 0.5 have a mean score of $107/140 \approx 0.764$, but only $4/7 \approx 0.571$ of them are positive *(inference)*. Elkan's rule assumes the scores are the probabilities $P(y = 1 \mid x)$[^elkan], which these are not *(inference)*.
- **Lipton's rule, same caveat.** The half-F1 rule would set $t = F^*/2 = 5/14 \approx 0.357$, which on these scores is step 10 with $F_1 = 5/8$, not the optimum $5/7$ *(inference)*. The rule holds for calibrated probabilities[^lipton], so the gap again reflects the toy scores, not the theorem *(inference)*.

### Example: the same rules at a lower prevalence
Reuse the skewed copy of the [class-imbalance Finding](class-imbalance-metric-choice.md#example-one-classifier-at-two-prevalences): every negative repeated 10 times with the same score, so $P = 6$, $N = 140$, $\pi = 3/73 \approx 0.041$ *(inference)*. Each row of the sweep keeps its TP and FN, and its FP is multiplied by 10 *(inference)*.

| rule | best step on the toy ($\pi = 0.30$) | best step on the copy ($\pi \approx 0.041$) |
|---|---|---|
| max $F_1$ | 8, $t = 0.47$, $F_1 = 5/7$ | 2, $t = 0.88$, $F_1 = 1/2$ |
| max $J$ | 11, $t = 0.33$, $J = 9/14$ | 11, $t = 0.33$, $J = 9/14$ |
| min cost, $c_{FN} = 4\,c_{FP}$ | 11, $t = 0.33$, $C = 5$ | 2, $t = 0.88$, $C = 16$ |

*Figure: the best step for three rules at two prevalences, using the same scores (inference). The copy's values come from the toy table with every FP multiplied by 10, computed in the same throwaway script (inference).*

- **F1 moves.** On the copy, step 8 has $F_1 = 10/(10 + 30 + 1) = 10/41 \approx 0.244$, while step 2 has $4/(4 + 0 + 4) = 1/2$ *(inference)*. With ten times as many negatives above each positive, the only matrices with few false positives are the first two steps *(inference)*. That matches Lipton et al.'s rule, where lower prior odds raise the score needed to predict positive[^lipton] *(inference: applied to this example)*.
- **J stays.** TPR and FPR at each step are unchanged by the copy, so $J$ and its optimum stay the same[^fawcett] *(inference: the optimum)*.
- **Cost moves.** The iso-cost slope becomes $m = (1 \cdot 140)/(4 \cdot 6) = 35/6$, ten times steeper, so the most northwest line touches the ROC curve at step 2, $(0, 1/3)$, where $C = 0 + 4 \cdot 4 = 16$ *(inference)*. The ROC curve is the same; only the line changed[^fawcett] *(inference: on this example)*.

### Example: AUC and F1 can rank two models differently
Take a hypothetical second model B on the same 20 labels, not a change to the shared dataset: B ranks five positives first, then all 14 negatives, then the last positive *(inference: a ranking made up for this example)*.

- **AUC.** Each of B's first five positives beats all 14 negatives, and its last positive beats none, so $\text{AUC}_B = (5 \cdot 14)/84 = 5/6 \approx 0.833$ *(inference)*. That is below the toy model's $73/84 \approx 0.869$ from the [ROC/PR Finding](roc-auc-vs-pr-auc.md#example-roc-auc-by-hand) *(inference)*.
- **Best F1.** Cutting B after its fifth sample gives $TP = 5$, $FP = 0$, $FN = 1$, so $F_1 = 10/11 \approx 0.909$, above the toy model's best $5/7 \approx 0.714$ *(inference)*.
- **Reading it.** B is better in the low-FPR corner and worse at the far end, where its last positive sits below every negative *(inference)*. This is Fawcett's point that a higher-AUC classifier can do worse in a specific region of ROC space[^fawcett]. If the model will run at a single threshold, compare the models at that operating point, not only by AUC *(inference)*.

## Follow-ups
- How much does choosing the threshold on the same data that reports the score inflate F1, and how large must a validation set be for the chosen threshold to be stable?
- How are thresholds chosen per class in multiclass and multilabel problems, and why do micro- and macro-F1 lead to different optimal thresholds (Lipton et al.'s batch observation)?
- How are example-dependent costs, such as Elkan's credit-card transaction amounts, turned into a decision rule?
- How does interpolating between two classifiers on the ROC convex hull reach an operating point that no single threshold gives?

[^fawcett]: [Fawcett, An introduction to ROC analysis](sources/fawcett-2006-roc-analysis.md)
[^dg]: [Davis and Goadrich, The relationship between precision-recall and ROC curves](sources/davis-goadrich-2006-pr-roc.md)
[^skroc]: [scikit-learn API: roc_curve (1.9.1)](sources/sklearn-roc-curve.md)
[^skguide]: [scikit-learn User Guide: Metrics and scoring (1.9.1)](sources/sklearn-model-evaluation.md)
[^skthr]: [scikit-learn User Guide: Tuning the decision threshold for class prediction (1.9.1)](sources/sklearn-classification-threshold.md)
[^sktuned]: [scikit-learn API: TunedThresholdClassifierCV (1.9.1)](sources/sklearn-tuned-threshold-classifier-cv.md)
[^skpit]: [scikit-learn User Guide: Common pitfalls and recommended practices (1.9.1)](sources/sklearn-common-pitfalls.md)
[^elkan]: [Elkan, The foundations of cost-sensitive learning](sources/elkan-2001-cost-sensitive-learning.md)
[^lipton]: [Lipton, Elkan and Naryanaswamy, Thresholding classifiers to maximize F1 score](sources/lipton-2014-thresholding-f1.md)
[^powers]: [Powers, Evaluation: from precision, recall and F-measure to ROC, informedness, markedness and correlation](sources/powers-2011-evaluation-informedness.md)
[^williams]: [Williams, The effect of class imbalance on precision-recall curves](sources/williams-2021-imbalance-pr-curves.md)
[^brabec]: [Brabec et al., On model evaluation under non-constant class imbalance](sources/brabec-2020-non-constant-imbalance.md)
