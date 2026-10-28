# scikit-learn API, `sklearn.metrics.average_precision_score` (1.9.1)

Supports: AP summarizes a PR curve as the weighted mean of precisions at each threshold, weighted by the increase in recall, $\text{AP} = \sum_n (R_n - R_{n-1}) P_n$; the implementation is not interpolated and differs from the trapezoidal area under the PR curve, "which uses linear interpolation and can be too optimistic"; since version 0.19 precisions are weighted by the change in recall instead of linearly interpolated. Also (for the multiclass-averaging Finding): `y_true` may be multi-class labels, `average` defaults to `'macro'` (unweighted mean per label), and `'micro'` considers each element of the label indicator matrix as a label.

- URL: <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html> (page title says scikit-learn 1.9.1)
- Local copy: none.
- Fetched: 2026-10-28
