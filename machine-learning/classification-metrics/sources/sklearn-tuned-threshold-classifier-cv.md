# scikit-learn API, `sklearn.model_selection.TunedThresholdClassifierCV` (1.9.1)

Supports: the class post-tunes the decision threshold (cut-off point) that converts `predict_proba` or `decision_function` output into a class label, by optimizing a binary metric, "potentially constrained by another metric"; added in version 1.5; `scoring` defaults to `"balanced_accuracy"`; `thresholds` defaults to 100, the number of thresholds used to discretize the classifier output, or an explicit array; `cv` defaults to 5-fold stratified K-fold, a float gives a single shuffle split, and `"prefit"` skips cross-validation, with a warning that passing the same data used to fit the estimator is "subject to undesired overfitting"; `refit` refits the classifier on the whole training set once the threshold is found; the fitted attributes `best_threshold_` and `best_score_` hold the chosen threshold and the objective score there.

- URL: <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html> (page title says scikit-learn 1.9.1)
- Local copy: none.
- Fetched: 2026-10-28
