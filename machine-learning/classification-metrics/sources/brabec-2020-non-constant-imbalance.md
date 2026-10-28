# Brabec, Komárek, Franc and Machlica, "On Model Evaluation under Non-constant Class Imbalance" (arXiv:2001.05571v2, 2020)

Supports: eq. 2–4, $\text{TPR} = P(h(x)=1 \mid y=1)$, $\text{FPR} = P(h(x)=1 \mid y=-1)$ and $\text{Prec}(\eta) = \text{TPR}\cdot\eta / (\text{TPR}\cdot\eta + \text{FPR}\cdot(1-\eta))$ for positive prevalence $\eta$, derived with Bayes' theorem, with TPR and FPR unaffected by prevalence and precision affected (Section 2); PR curves have little value without the imbalance ratio, and the imbalance changes the order of classifiers (Section 1); test sets are often less imbalanced than deployment data, which makes PR-based results too optimistic, and the remedy is a test set that estimates TPR and FPR with low variance plus the precision formula at the ratios of interest (Section 3); PR-AUC and F1 can swap the order of two classifiers as imbalance changes, which can be misused to cherry-pick an imbalance rate, shown for F1 against log prevalence in Fig. 3 (Section 4); report the imbalance ratio, and keep all samples rather than subsampling to a target imbalance (Sections 1, 7).

- URL: <https://arxiv.org/abs/2001.05571> (PDF read: <https://arxiv.org/pdf/2001.05571>, v2 dated 15 Apr 2020)
- Local copy: none.
- Fetched: 2026-10-28
