# scikit-learn API, `sklearn.metrics.f1_score` (1.9.1)

Supports: F1 $= 2\,\text{TP}/(2\,\text{TP} + \text{FP} + \text{FN})$, the harmonic mean of precision and recall; multiclass and multilabel data are treated as a collection of binary problems, one for each label; for binary data `average='binary'` returns F1 for `pos_label`, and any other `average` ignores `pos_label`, computes F1 for both classes and averages them; `average` is required for multiclass/multilabel targets, with `'micro'` (global counts of TP, FN and FP), `'macro'` (unweighted mean per label, not taking label imbalance into account), `'weighted'` (mean weighted by support, which "can result in an F-score that is not between precision and recall") and `'samples'` (only meaningful for multilabel classification).

- URL: <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html> (page title says scikit-learn 1.9.1)
- Local copy: none.
- Fetched: 2026-10-28
