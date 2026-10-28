# scikit-learn User Guide, "3.1. Cross-validation: evaluating estimator performance" (1.9.1)

Supports: testing a prediction function on the data it was trained on is a methodological mistake (overfitting), so a test set is held out; tuning hyperparameters until the estimator performs well on the test set lets knowledge about the test set "leak" into the model, and the remedy is a separate validation set, with final evaluation on the test set once the experiment seems successful; a three-way split reduces the training data and makes results depend on the random choice of (train, validation) sets (introduction); `cross_val_score` results are summarised as "the mean score and the standard deviation" (Section 3.1.1); `StratifiedKFold` keeps approximately the same percentage of each class in every fold (Sections 3.1.2.2, 3.1.2.2.1); "stratification can artificially shrink the spread of the metric measured across cross-validation iterations", so inter-fold variability no longer reflects the uncertainty in the presence of rare classes (Section 3.1.2.2, Note).

- URL: <https://scikit-learn.org/stable/modules/cross_validation.html> (page title says scikit-learn 1.9.1)
- Local copy: none.
- Fetched: 2026-10-28
