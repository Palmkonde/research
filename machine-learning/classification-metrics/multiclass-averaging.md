---
question: How are macro, micro and weighted F1 (and precision/recall) computed in multiclass, and when do I use each?
date: 2026-10-28
status: answered
---

## TL;DR
A multiclass metric is built by treating the $K$-class problem as $K$ one-vs-rest binary problems, one per class, then averaging the $K$ binary scores[^skguide]. Macro takes the unweighted mean over classes, weighted weights each class by its support, and micro pools the counts before dividing[^skprfs]. For single-label multiclass with all labels included, micro-precision, micro-recall and micro-F1 all equal accuracy[^skguide]. Macro gives a rare class the same say as a common one[^skguide], while micro and weighted weight each class by its size, so the large classes dominate *(inference)*. "Macro F1" has two definitions in the literature, the mean of per-class F1 and the F1 of macro-precision and macro-recall, and scikit-learn computes the first[^ob][^skguide]. So a paper must name the averaging, and for macro F1 the formula too[^ob].

## Explanation
Precision, recall and F1 are defined for one positive class, so a problem with three or more classes has no single precision until you choose how to combine one per class *(inference)*. The choice is not cosmetic: on the toy matrix below, the same predictions score 0.653 under macro F1 and 0.800 under micro F1 *(inference)*. A reader who does not know which average was used cannot compare the number with anything else *(inference)*. This page derives each average from the $K \times K$ confusion matrix, proves which ones collapse to accuracy, and works all of them on one shared multiclass toy that later Findings reuse *(inference)*. It keeps the notation of the [first Finding](confusion-matrix-basic-metrics.md): $C_{ij}$ counts samples of actual class $i$ predicted as class $j$, so rows are actual and columns predicted[^skcm], and $n$ is the number of samples *(inference)*.

### One-vs-rest: each class gets its own TP, FP and FN
- **The reduction.** scikit-learn extends a binary metric to multiclass by treating the data as a collection of binary problems, one for each class, and then averaging the binary results across classes[^skguide]. Precision, recall and F-measures are applied to each label independently[^skguide].
- **Per-class counts.** For class $k$, call class $k$ "positive" and every other class "negative" *(inference)*. In the rows-are-actual layout this reads off the matrix as *(inference)*
  $$TP_k = C_{kk}, \qquad FP_k = \sum_{i \ne k} C_{ik}, \qquad FN_k = \sum_{j \ne k} C_{kj}, \qquad TN_k = n - TP_k - FP_k - FN_k.$$
  $FP_k$ is column $k$ without its diagonal cell (others predicted as $k$), and $FN_k$ is row $k$ without its diagonal cell ($k$ predicted as something else) *(inference)*.
- **Support.** The support $s_k$ is the number of occurrences of class $k$ in the true labels[^skprfs], which is the row sum $s_k = TP_k + FN_k$ *(inference)*.
- **Per-class metrics.** Each class then gets the binary formulas of the first Finding *(inference)*:
  $$P_k = \frac{TP_k}{TP_k + FP_k}, \qquad R_k = \frac{TP_k}{TP_k + FN_k} = \frac{TP_k}{s_k}, \qquad F_{1,k} = \frac{2\,TP_k}{2\,TP_k + FP_k + FN_k}.$$
  scikit-learn's `average=None` returns these $K$ values without averaging[^skguide].
- **Every error counts twice.** A sample of class $i$ predicted as class $j \ne i$ is a false negative for class $i$ and a false positive for class $j$ *(inference)*. This double role drives the micro-averaging proof below *(inference)*.

### Macro averaging: the unweighted mean over classes
$$\text{macro-}P = \frac{1}{K}\sum_{k} P_k, \qquad \text{macro-}R = \frac{1}{K}\sum_{k} R_k, \qquad \text{macro-}F_1 = \frac{1}{K}\sum_{k} F_{1,k}$$

- scikit-learn's `'macro'` calculates the metric for each label and takes their unweighted mean, which does not take label imbalance into account[^skprfs]. The user guide puts it as giving equal weight to each class[^skguide], and its table defines macro-$F_\beta$ as the mean of the per-label $F_\beta$[^skguide].
- **Macro recall is balanced accuracy.** scikit-learn defines balanced accuracy as the macro-average of the per-class recall scores[^skguide], which links this page to the [class-imbalance Finding](class-imbalance-metric-choice.md#balanced-accuracy-mcc-and-cohens-kappa) *(inference)*.
- **Absent classes.** Labels not present in the data can be included in a macro average through the `labels` argument, and they are "assigned" 0 samples[^skprfs]. Each such label then adds a 0 (or whatever `zero_division` sets) to the mean, which is why the `zero_division` choice matters most for macro averages *(inference)*. That choice is its own open Question in the [Topic README](README.md) *(inference)*.

### Micro averaging: pool the counts, then divide
$$\text{micro-}P = \frac{\sum_k TP_k}{\sum_k (TP_k + FP_k)}, \qquad \text{micro-}R = \frac{\sum_k TP_k}{\sum_k (TP_k + FN_k)}, \qquad \text{micro-}F_1 = \frac{2\sum_k TP_k}{2\sum_k TP_k + \sum_k FP_k + \sum_k FN_k}$$

- scikit-learn's `'micro'` calculates metrics globally by counting the total true positives, false negatives and false positives[^skprfs]. Rather than averaging the per-class metric, it sums the numerators and denominators of the per-class metrics and divides once, which gives each sample-class pair an equal contribution[^skguide].
- **The guide's caveat.** It says micro-averaging may be preferred in multilabel settings, including multiclass classification where a majority class is to be ignored[^skguide]. Ignoring a class means leaving it out of the `labels` argument, as its own example does with a "negative class"[^skguide].

**Claim: for single-label multiclass with all $K$ labels included, micro-precision = micro-recall = micro-F1 = accuracy.** The user guide states this result[^skguide]; the proof below is *(inference)*.

1. Each sample has exactly one true class $i$ and one predicted class $j$, so it adds 1 to exactly one cell $C_{ij}$, and $\sum_{i,j} C_{ij} = n$ *(inference)*.
2. Summing false positives over all classes adds up every off-diagonal cell once, by columns *(inference)*:
   $$\sum_k FP_k = \sum_k \sum_{i \ne k} C_{ik} = \sum_{i \ne j} C_{ij}.$$
3. Summing false negatives over all classes adds up the same off-diagonal cells, by rows *(inference)*:
   $$\sum_k FN_k = \sum_k \sum_{j \ne k} C_{kj} = \sum_{i \ne j} C_{ij}.$$
4. So $\sum_k FP_k = \sum_k FN_k = n - \sum_k C_{kk}$, the number of misclassified samples, and therefore *(inference)*
   $$\text{micro-}P = \frac{\sum_k C_{kk}}{\sum_k C_{kk} + \big(n - \sum_k C_{kk}\big)} = \frac{\sum_k C_{kk}}{n} = \text{micro-}R.$$
5. The right-hand side is accuracy, the fraction of correct predictions[^skguide]. Micro-$F_1$ is the harmonic mean of two equal numbers, so it equals them too; the count form gives the same, $2T/(2T + 2(n - T)) = T/n$ with $T = \sum_k C_{kk}$ *(inference)*.

Where the proof breaks:
- **A subset of labels.** If the sum runs over a subset $L$ of the classes, $\sum_{k \in L} FP_k$ counts errors predicted *into* $L$ and $\sum_{k \in L} FN_k$ counts errors coming *from* $L$, and these differ in general, so micro-precision and micro-recall separate *(inference)*. The user guide states the identity only "if all labels are included"[^skguide]. Leaving a class out does two things: its true positives drop out of the numerator, and the false positives into $L$ stop matching the false negatives from $L$ *(inference)*. In the guide's own `labels=[1, 2]` example, micro-recall is 0[^skguide], while the accuracy of the same arrays is $2/6$ *(inference: from its arrays)*.
- **Multilabel.** A sample may have zero or several true labels, so step 1 fails, and micro-precision and micro-recall again differ *(inference)*. Multilabel metrics are their own open Question in the [Topic README](README.md) *(inference)*.

### Weighted averaging: weight each class by its support
$$\text{weighted-}M = \sum_k \frac{s_k}{n}\, M_k, \qquad M \in \{P, R, F_1\}, \qquad n = \sum_k s_k$$

- scikit-learn's `'weighted'` calculates the metric for each label and averages them weighted by support, the number of true instances for each label[^skprfs]. It alters macro to account for label imbalance[^skprfs], and the guide's table writes it as $\frac{1}{\sum_l \lvert y_l\rvert}\sum_l \lvert y_l\rvert\, M(y_l, \hat y_l)$, where $\lvert y_l\rvert$ is the number of true instances of label $l$[^skguide].
- **Weighted recall is accuracy.** Substituting $R_k = TP_k/s_k$ cancels the weights *(inference)*:
  $$\text{weighted-}R = \sum_k \frac{s_k}{n} \cdot \frac{TP_k}{s_k} = \frac{\sum_k TP_k}{n} = \text{accuracy}.$$
  So in single-label multiclass, weighted recall, micro-precision, micro-recall and micro-F1 are four names for one number *(inference)*.

**Weighted F1 can fall outside the range between weighted precision and weighted recall.** scikit-learn's documentation of `average` says weighted averaging "can result in an F-score that is not between precision and recall"[^skprfs][^skf1], and the user guide repeats it[^skguide]. Why, and in which direction *(inference)*:
1. For each class, the harmonic mean is at most the arithmetic mean, $F_{1,k} \le \tfrac12 (P_k + R_k)$, with equality only when $P_k = R_k$ *(inference)*.
2. Averaging with weights $s_k/n$ keeps the inequality: $\text{weighted-}F_1 \le \tfrac12(\text{weighted-}P + \text{weighted-}R) \le \max(\text{weighted-}P, \text{weighted-}R)$ *(inference)*.
3. So weighted F1 can never sit above both, but it can sit below both *(inference)*. That happens when weighted precision and weighted recall are close while individual classes have $P_k \ne R_k$, since then the weighted harmonic-mean loss $\tfrac12(\text{weighted-}P + \text{weighted-}R) - \text{weighted-}F_1$ exceeds half the gap between the two averages *(inference)*.
4. Step 2 applies to any fixed weights, so the same holds for macro F1 against macro-precision and macro-recall *(inference)*.

The toy below shows it: weighted precision 0.791, weighted recall 0.800, weighted F1 0.780 *(inference)*.

### Samples averaging, briefly
scikit-learn's `'samples'` applies only to multilabel problems: it computes the metric over the true and predicted label sets of each sample and averages over samples, with no per-class step[^skguide]. Its documentation says it is only meaningful for multilabel classification, where it differs from accuracy[^skprfs]. For single-label data each sample has one true and one predicted label, so its per-sample precision, recall and F1 are each 1 or 0, and their mean would just be accuracy *(inference)*. scikit-learn 1.9.1 refuses it on multiclass input with the message "Samplewise metrics are not available outside of multilabel classification" *(inference: observed in the throwaway check)*. The multilabel case is its own open Question in the [Topic README](README.md) *(inference)*.

### Two definitions of "macro F1"
Opitz and Burst find two formulas in use under the same name[^ob]. In this Topic's notation, with $\bar P$ and $\bar R$ the macro-precision and macro-recall *(inference: notation)*:

$$\text{averaged } F_1 = \frac{1}{K}\sum_k \frac{2 P_k R_k}{P_k + R_k}, \qquad\qquad F_1 \text{ of averages} = \frac{2\,\bar P\,\bar R}{\bar P + \bar R}, \quad \bar P = \frac{1}{K}\sum_k P_k,\ \ \bar R = \frac{1}{K}\sum_k R_k.$$

- **Names and structure.** The first is the arithmetic mean over per-class harmonic means, and the second is the harmonic mean over arithmetic means[^ob]. In the second, the precision of each class gets multiplied with the recall of every other class, while in the first each precision meets only its own class's recall[^ob].
- **Orientation warning.** Their confusion matrix counts $m_{ij} = \lvert\{s : f(s_1) = i,\ s_2 = j\}\rvert$, predicted class $i$ against true class $j$, so their rows are the predicted class[^ob]. That is the transpose of this Topic's layout *(inference)*. They also write $n$ for the number of classes, which this page calls $K$ *(inference)*.
- **Their theorem.** For every confusion matrix[^ob]:
  1. $F_1$ of averages $\ge$ averaged $F_1$[^ob];
  2. the inequality is strict exactly when some class has $P_i \ne R_i$, which is exactly when some class has $P_i < R_i$ and another has $P_j > R_j$[^ob];
  3. the largest possible gap is $0.5$ when the number of classes is even, and $0.5 - 1/(2K^2)$ when it is odd[^ob].
- **What the gap rewards.** The gap is large when a classifier has a strong bias toward certain types of error, with high recall on some classes and high precision on others[^ob]. They say the F1 of averages "rewards" such classifiers, and that it is insensitive to which classes carry which bias[^ob].
- **Rankings can flip.** The two formulas can rank two classifiers differently[^ob]. In their binary Table 1 the F1 of averages is 0.50 and the averaged F1 is 0.49; in Table 2, which adds a bias toward one class, they are 0.55 and 0.48[^ob]. So the bias raises one score and lowers the other *(inference: recomputed from their tables, which give 0.500 and 0.486, then 0.555 and 0.479)*.
- **Their recommendation.** They recommend the averaged F1, the arithmetic mean over per-class F1, as much more robust to the error-type distribution, and they ask authors to at least say which formula they use[^ob]. Among their examples of papers using the F1 of averages is Sokolova and Lapalme (2009)[^ob].
- **Which one scikit-learn computes.** scikit-learn's macro F-measure is the arithmetic mean over per-class F-measures, "not the harmonic mean over the arithmetic precision and recall means", and the guide cites Opitz and Burst for the difference[^skguide]. So `f1_score(average='macro')` is the averaged $F_1$, and computing $2\bar P\bar R/(\bar P + \bar R)$ from `precision_score` and `recall_score` gives the other one *(inference)*.

### How each average treats rare classes
The three averages differ only in the weight each class gets *(inference)*:

| average | weight of class $k$ in P, R, F1 | weight of the rare class in the toy |
|---|---|---|
| macro | $1/K$ | $1/3 \approx 0.333$ |
| weighted | $s_k/n$ | $10/90 \approx 0.111$ |
| micro | pools counts; equals $\sum_k (s_k/n)\,R_k$ | $10/90 \approx 0.111$, through recall |

*Figure: the weight each averaging gives a class (inference: read off the formulas above). The micro row uses the identity micro-F1 = accuracy = weighted recall proved above (inference).*

- **Macro: every class has an equal say.** The user guide says macro averaging may be a means of highlighting the performance of infrequent classes that are nonetheless important[^skguide]. It also warns that the assumption that all classes are equally important is often untrue, so macro averaging can over-emphasize the typically low performance on an infrequent class[^skguide].
- **Weighted: large classes dominate.** A class's share of the average is its share of the samples, so a class with 1% of the samples moves weighted F1 by at most 0.01 however badly it is handled *(inference)*.
- **Micro: large classes dominate, by construction.** Micro gives each sample-class pair the same weight[^skguide], so classes count in proportion to their size, and in single-label multiclass it equals accuracy[^skguide]. The [class-imbalance Finding](class-imbalance-metric-choice.md#why-accuracy-misleads-the-majority-class-baseline) shows how accuracy can hide a class the classifier ignores *(inference)*.
- **So the gap is diagnostic.** When macro F1 is well below micro or weighted F1, the small classes are handled worse than the large ones *(inference)*. On the toy below the gap is $0.800 - 0.653 \approx 0.15$, almost all of it from class 2 *(inference)*.

### Multiclass ROC AUC and average precision
Threshold-free scores need one score per class per sample, not just labels *(inference)*. For multiclass input, scikit-learn's `roc_auc_score` expects `y_score` of shape $(n, K)$ holding probability estimates that sum to 1 across classes[^skrocauc]. Its `multi_class` argument defaults to `'raise'`, so you must pass `'ovr'` or `'ovo'` explicitly[^skrocauc].

- **One-vs-rest (`'ovr'`).** It computes the AUC of each class against all the others, treating the multiclass case like the multilabel case[^skrocauc]. `average='macro'` takes the unweighted mean of the $K$ AUCs, and `'weighted'` weights them by support[^skrocauc].
  - It is sensitive to class imbalance even with `average='macro'`, because the imbalance changes the composition of each "rest" group[^skrocauc]. One way to see this: the "rest" for class $k$ mixes the other classes in proportion to their sizes, so its score distribution, and hence each FPR, depends on that mix *(inference)*.
  - Only OvR supports `average='micro'` and `average=None`[^skrocauc]. Micro treats each element of the $n \times K$ label indicator matrix as one binary instance[^skrocauc], so it pools the $nK$ (indicator, score) pairs, $n$ of them positive, into one ROC curve *(inference)*.
- **One-vs-one (`'ovo'`).** It averages the AUC of every pair of classes[^skrocauc]. The user guide gives Hand and Till's uniformly weighted form[^skguide]
  $$\text{AUC}_\text{ovo} = \frac{1}{K(K-1)} \sum_{j=1}^{K} \sum_{k > j} \big( \text{AUC}(j \mid k) + \text{AUC}(k \mid j) \big),$$
  where $\text{AUC}(j \mid k)$ uses class $j$ as positive and class $k$ as negative, and in general $\text{AUC}(j \mid k) \ne \text{AUC}(k \mid j)$[^skguide]. `average='weighted'` multiplies each pair's term by the prevalence $p(j \cup k)$ of the two classes[^skguide]. With `average='macro'`, OvO is insensitive to class imbalance[^skrocauc].
- **Average precision.** `average_precision_score` accepts multiclass labels, with `average='macro'` as its default and `'micro'` again treating each element of the label indicator matrix as a label[^skap]. Each class's AP is then a one-vs-rest AP, so its random baseline is that class's prevalence $s_k/n$, by the result of the [ROC/PR Finding](roc-auc-vs-pr-auc.md) *(inference)*. A macro AP therefore mixes classes with different baselines *(inference)*.

The toy matrix below has labels only, no scores, so these areas are not computed for it *(inference)*.

### Which average to use, and what to write in a paper
- **Every class matters equally, including rare ones** (rare diseases, minority intents): report macro F1, alongside the per-class table *(inference)*. This is the case the guide names for macro: infrequent classes that are nonetheless important[^skguide].
- **Every sample matters equally** (overall throughput, where a rare class is rare in deployment too): micro F1, but in single-label multiclass that is accuracy, so report it as accuracy *(inference)*.
- **A support-weighted summary.** Weighted averaging alters macro to account for label imbalance[^skprfs]. It therefore tracks the large classes much like micro, so report it with weighted precision and recall, knowing its F1 can fall below both *(inference)*.
- **A majority "background" class to ignore** (such as an "other" or "O" class): micro over the remaining labels, set through `labels`, is the case the guide names[^skguide]. Micro-precision and micro-recall then differ and should both be reported *(inference)*.
- **Always report the per-class table.** Give $P_k$, $R_k$, $F_{1,k}$ and $s_k$ for every class, since no single average shows which class is failing *(inference)*. scikit-learn returns them with `average=None`[^skguide].
- **Name the averaging in the text.** Write "macro-F1", "micro-F1" or "weighted-F1", never a bare "F1", for any problem with more than two classes *(inference)*. For macro F1, also say whether it is the mean of per-class F1 or the F1 of macro-precision and macro-recall, as Opitz and Burst ask[^ob]. scikit-learn's `f1_score` requires the `average` argument for multiclass targets[^skf1], so code always makes this choice even when the paper hides it *(inference)*.
- **For ROC AUC and AP, name both choices.** Write OvR or OvO and macro, weighted or micro, because OvR macro is sensitive to imbalance and OvO macro is not[^skrocauc].
- **Do not compare across averages.** On the toy below, the same predictions give F1 from 0.653 to 0.800 depending on the average, so a macro F1 from one paper and a micro F1 from another say nothing about which model is better *(inference)*.

How to lay out a full results section is covered by the [reporting Finding](reporting-classification-results.md) *(inference)*.

### Example: the shared multiclass toy
This matrix is the shared multiclass example for this Topic; later Findings (reporting) reuse it, so its counts should not be changed *(inference)*. It has three classes, 0, 1 and 2, with supports 50, 30 and 10, so $n = 90$ *(inference)*. Class 2 is rare, and the classifier handles it badly: it predicts class 0 for 7 of its 10 samples *(inference: a constructed example)*.

$$
C \;=\;
\begin{array}{r|ccc|c}
 & \hat y = 0 & \hat y = 1 & \hat y = 2 & s_k \\ \hline
y = 0 & 48 & 1 & 1 & 50 \\
y = 1 & 7 & 22 & 1 & 30 \\
y = 2 & 7 & 1 & 2 & 10 \\ \hline
\text{predicted} & 62 & 24 & 4 & 90
\end{array}
$$

*Figure: the shared multiclass toy confusion matrix, with rows for the actual class and columns for the predicted class, as in scikit-learn's `confusion_matrix`[^skcm]. The row sums are the supports and the column sums the predicted counts (inference).*

**Per-class one-vs-rest counts and metrics.** From the formulas above, $FP_k$ is the column sum minus the diagonal and $FN_k$ the row sum minus the diagonal *(inference)*:

| class $k$ | $s_k$ | $TP_k$ | $FP_k$ | $FN_k$ | $TN_k$ | $P_k$ | $R_k$ | $F_{1,k}$ |
|---|---|---|---|---|---|---|---|---|
| 0 | 50 | 48 | $7 + 7 = 14$ | $1 + 1 = 2$ | 26 | $48/62 = 24/31 \approx 0.774$ | $48/50 = 24/25 = 0.960$ | $96/112 = 6/7 \approx 0.857$ |
| 1 | 30 | 22 | $1 + 1 = 2$ | $7 + 1 = 8$ | 58 | $22/24 = 11/12 \approx 0.917$ | $22/30 = 11/15 \approx 0.733$ | $44/54 = 22/27 \approx 0.815$ |
| 2 | 10 | 2 | $1 + 1 = 2$ | $7 + 1 = 8$ | 78 | $2/4 = 1/2 = 0.500$ | $2/10 = 1/5 = 0.200$ | $4/14 = 2/7 \approx 0.286$ |
| sum | 90 | 72 | 18 | 18 | | | | |

*Figure: one-vs-rest counts and metrics per class (inference: arithmetic from the matrix, with $F_{1,k} = 2TP_k/(2TP_k + FP_k + FN_k)$). $\sum_k FP_k = \sum_k FN_k = 18$, the number of misclassified samples, as the micro proof requires (inference).*

**Macro** *(inference: arithmetic)*:
$$\text{macro-}P = \tfrac13\big(\tfrac{24}{31} + \tfrac{11}{12} + \tfrac12\big) = \tfrac13 \cdot \tfrac{288 + 341 + 186}{372} = \tfrac{815}{1116} \approx 0.730$$
$$\text{macro-}R = \tfrac13\big(\tfrac{24}{25} + \tfrac{11}{15} + \tfrac15\big) = \tfrac13 \cdot \tfrac{72 + 55 + 15}{75} = \tfrac{142}{225} \approx 0.631$$
$$\text{macro-}F_1 = \tfrac13\big(\tfrac67 + \tfrac{22}{27} + \tfrac27\big) = \tfrac13 \cdot \tfrac{216 + 154}{189} = \tfrac{370}{567} \approx 0.653$$

**Micro** *(inference: arithmetic)*: $\text{micro-}P = \dfrac{72}{72 + 18} = \dfrac45$, $\text{micro-}R = \dfrac{72}{72 + 18} = \dfrac45$, $\text{micro-}F_1 = \dfrac{2 \cdot 72}{2 \cdot 72 + 18 + 18} = \dfrac{144}{180} = \dfrac45$, and accuracy $= \dfrac{48 + 22 + 2}{90} = \dfrac{72}{90} = \dfrac45 = 0.800$.

**Weighted** *(inference: arithmetic)*:
$$\text{weighted-}P = \tfrac{1}{90}\big(50 \cdot \tfrac{24}{31} + 30 \cdot \tfrac{11}{12} + 10 \cdot \tfrac12\big) = \tfrac{1}{90}\big(\tfrac{1200}{31} + \tfrac{65}{2}\big) = \tfrac{4415}{5580} = \tfrac{883}{1116} \approx 0.791$$
$$\text{weighted-}R = \tfrac{1}{90}\big(50 \cdot \tfrac{24}{25} + 30 \cdot \tfrac{11}{15} + 10 \cdot \tfrac15\big) = \tfrac{48 + 22 + 2}{90} = \tfrac45 = 0.800$$
$$\text{weighted-}F_1 = \tfrac{1}{90}\big(50 \cdot \tfrac67 + 30 \cdot \tfrac{22}{27} + 10 \cdot \tfrac27\big) = \tfrac{1}{90}\big(\tfrac{320}{7} + \tfrac{220}{9}\big) = \tfrac{4420}{5670} = \tfrac{442}{567} \approx 0.780$$

**F1 of averages** (the second macro F1) *(inference: arithmetic)*:
$$F_1(\bar P, \bar R) = \frac{2 \cdot \tfrac{815}{1116} \cdot \tfrac{142}{225}}{\tfrac{815}{1116} + \tfrac{142}{225}} = \frac{231460}{341847} \approx 0.677$$

| average | precision | recall | F1 |
|---|---|---|---|
| macro (scikit-learn: mean of per-class F1) | $815/1116 \approx 0.730$ | $142/225 \approx 0.631$ | $370/567 \approx 0.653$ |
| macro, F1 of averages | $815/1116 \approx 0.730$ | $142/225 \approx 0.631$ | $231460/341847 \approx 0.677$ |
| weighted | $883/1116 \approx 0.791$ | $4/5 = 0.800$ | $442/567 \approx 0.780$ |
| micro | $4/5 = 0.800$ | $4/5 = 0.800$ | $4/5 = 0.800$ |
| accuracy | | | $4/5 = 0.800$ |

*Figure: every average on the shared multiclass toy (inference: exact fractions as worked above; all values also checked with scikit-learn 1.9.1's `precision_recall_fscore_support`, `accuracy_score` and `balanced_accuracy_score` in a throwaway script, not shown). Macro recall 142/225 equals the balanced accuracy, which scikit-learn defines as the macro-average of per-class recall[^skguide].*

![Bar chart of per-class F1 on the shared multiclass toy: class 0 with support 50 at 0.857, class 1 with support 30 at 0.815, class 2 with support 10 at 0.286. Three horizontal lines cross the bars: micro F1 at 0.800 solid, weighted F1 at 0.780 dashed, macro F1 at 0.653 dotted](assets/multiclass-averaging/per-class-f1-averages.svg)
*Figure: per-class F1 of the shared multiclass toy, with the micro (solid), weighted (dashed) and macro (dotted) F1 drawn across (inference: values from the tables above). Macro is the plain mean of the three bars, so the short class-2 bar pulls it down by a third of its shortfall, while weighted and micro give class 2 a weight of only 10/90 and sit near the two large classes (inference). scikit-learn describes macro as giving equal weight to each class and weighted as weighting by support[^skguide].*

Reading the results:
- **Macro against micro.** Macro F1 is 0.653 and micro F1 is 0.800, a gap of about 0.15, and the per-class table shows why: class 2 has F1 0.286 *(inference)*. Holding the other two classes' F1 fixed, raising class 2's F1 from $2/7$ to 1 would add $(5/7)/3 = 5/21 \approx 0.238$ to macro F1 but only $(10/90)(5/7) = 5/63 \approx 0.079$ to weighted F1 *(inference: a hypothetical bound, since fixing class 2's errors would also change class 0's false positives)*.
- **Weighted F1 below both.** Weighted F1 0.780 is below weighted precision 0.791 and weighted recall 0.800, the case scikit-learn warns about[^skprfs] *(inference: the values)*. Their mean is about 0.796, and the support-weighted loss from taking harmonic rather than arithmetic means per class is about 0.016, more than half the 0.009 gap between them *(inference: from step 3 of the argument above)*. Every class contributes to that loss, because class 0 has $P_0 < R_0$ and classes 1 and 2 have $P_k > R_k$ *(inference)*.
- **The two macro F1s.** The F1 of averages, 0.677, is above the averaged F1, 0.653, by about 0.025 *(inference)*. This toy fits Opitz and Burst's strict case: one class has $P < R$ (class 0) and others have $P > R$ (classes 1 and 2)[^ob] *(inference: the classification of the toy's classes)*.
- **Micro with a class left out.** Restricting to labels $\{1, 2\}$, as one would to ignore class 0, gives $TP = 24$, $FP = 2 + 2 = 4$ and $FN = 8 + 8 = 16$, so micro-precision $= 24/28 = 6/7 \approx 0.857$ and micro-recall $= 24/40 = 3/5$ *(inference: arithmetic, also checked with scikit-learn 1.9.1)*. With a label left out, the two no longer match each other or accuracy, as the proof predicted *(inference)*.

### Example: macro F1 on the binary toy
The binary toy of the [first Finding](confusion-matrix-basic-metrics.md#example-the-shared-toy-dataset) is unchanged: at threshold 0.5, $TN = 11$, $FP = 3$, $FN = 2$, $TP = 4$ *(inference)*. For binary data, scikit-learn's default `average='binary'` returns F1 for `pos_label` only, while `'macro'`, `'weighted'` or `'micro'` ignores `pos_label`, computes F1 for both classes, and averages them[^skf1]. So "the F1" of a binary problem is class 1's F1, while a binary macro F1 also scores the negative class *(inference)*.

Treat class 0 as positive and swap the roles of the cells: $TP_0 = TN = 11$, $FP_0 = FN = 2$, $FN_0 = FP = 3$ *(inference)*. Then *(inference: arithmetic)*

$$P_0 = \frac{11}{11 + 2} = \frac{11}{13} \approx 0.846, \qquad R_0 = \frac{11}{11 + 3} = \frac{11}{14} \approx 0.786, \qquad F_{1,0} = \frac{2 \cdot 11}{2 \cdot 11 + 2 + 3} = \frac{22}{27} \approx 0.815.$$

Class 1 has $F_{1,1} = 8/13 \approx 0.615$, the F1 of the first Finding *(inference)*. So *(inference: arithmetic)*

| `average` | F1 on the binary toy |
|---|---|
| `'binary'` (class 1 only) | $8/13 \approx 0.615$ |
| `'macro'` | $\tfrac12\big(\tfrac{22}{27} + \tfrac{8}{13}\big) = \tfrac{286 + 216}{702} = \tfrac{251}{351} \approx 0.715$ |
| `'weighted'` | $\tfrac{1}{20}\big(14 \cdot \tfrac{22}{27} + 6 \cdot \tfrac{8}{13}\big) = \tfrac{265}{351} \approx 0.755$ |
| `'micro'` | $15/20 = 3/4 = 0.750$, the accuracy |

*Figure: F1 of the binary toy under each `average` setting (inference: exact fractions, also checked with scikit-learn 1.9.1's `f1_score`). The meaning of each setting is from scikit-learn's `f1_score` documentation[^skf1].*

- Macro F1 is 0.10 above the binary F1 here, because the majority negative class is easier and now counts *(inference)*. On imbalanced binary data, a macro F1 can look good while the minority class does poorly, so a binary paper should say which F1 it reports *(inference)*.
- The binary macro recall is $\tfrac12\big(\tfrac{11}{14} + \tfrac23\big) = \tfrac{61}{84} \approx 0.726$, the balanced accuracy of the [class-imbalance Finding](class-imbalance-metric-choice.md#example-one-classifier-at-two-prevalences) *(inference)*, as scikit-learn's definition of balanced accuracy as macro-averaged recall predicts[^skguide].
- How F1 changes when the other class is called positive is a separate open Question in the [Topic README](README.md) *(inference)*.

## Follow-ups
- When does one-vs-one (Hand and Till) multiclass ROC AUC disagree with one-vs-rest macro AUC, and which should be reported under class imbalance?
- When should a majority or background class be left out of micro averaging through `labels` (for example the "O" tag in named-entity recognition), and how should the resulting micro-precision and micro-recall be reported?

[^skguide]: [scikit-learn User Guide: Metrics and scoring (1.9.1)](sources/sklearn-model-evaluation.md)
[^skcm]: [scikit-learn API: confusion_matrix (1.9.1)](sources/sklearn-confusion-matrix.md)
[^skprfs]: [scikit-learn API: precision_recall_fscore_support (1.9.1)](sources/sklearn-precision-recall-fscore-support.md)
[^skf1]: [scikit-learn API: f1_score (1.9.1)](sources/sklearn-f1-score.md)
[^skrocauc]: [scikit-learn API: roc_auc_score (1.9.1)](sources/sklearn-roc-auc-score.md)
[^skap]: [scikit-learn API: average_precision_score (1.9.1)](sources/sklearn-average-precision-score.md)
[^ob]: [Opitz and Burst, Macro F1 and Macro F1](sources/opitz-burst-2019-macro-f1.md)
