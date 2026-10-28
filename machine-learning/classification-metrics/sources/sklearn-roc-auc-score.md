# scikit-learn API, `sklearn.metrics.roc_auc_score` (1.9.1)

Supports: for multiclass targets `y_score` has shape (n_samples, n_classes) and holds probability estimates that must sum to 1 across classes; `multi_class` defaults to `'raise'`, so `'ovr'` or `'ovo'` must be passed; `'ovr'` computes the AUC of each class against the rest, treats the multiclass case like the multilabel case, and is "sensitive to class imbalance even when average == 'macro', because class imbalance affects the composition of each of the 'rest' groupings"; `'ovo'` computes the average AUC of all pairwise combinations of classes and is "insensitive to class imbalance when average == 'macro'"; `average='micro'` and `average=None` are only implemented for `'ovr'`; `'macro'` is the unweighted mean per label, `'weighted'` the support-weighted mean, and `'micro'` considers each element of the label indicator matrix as a label.

- URL: <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html> (page title says scikit-learn 1.9.1)
- Local copy: none.
- Fetched: 2026-10-28
