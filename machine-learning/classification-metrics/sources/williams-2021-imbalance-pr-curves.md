# Williams, "The Effect of Class Imbalance on Precision-Recall Curves" (arXiv:2007.01905v3, 2021)

Supports: with $\pi = P/(P+N)$ and $r = P/N = \pi/(1-\pi)$, the normalized confusion table is fully characterized by TPR, FPR and $r$; the population ROC curve is invariant to $r$, while empirical ROC curves show some variability as $r$ varies; eq. 2, $\text{Prec} = \text{TPR}/(\text{TPR} + \tfrac{1}{r}\text{FPR})$, so precision tends to 1 as $\pi \to 1$ and to 0 as $\pi \to 0$ if FPR > 0, and decreasing $r$ at fixed recall lowers precision; eq. 2 predicts the PR curve at one $r$ from another, with good agreement in Fig. 1; eq. 6, $F_\beta = (1+\beta^2)\,\text{TPR}/(\text{TPR} + \tfrac{1}{r}\text{FPR} + \beta^2)$; Hoiem et al. (2012) proposed "normalized precision" with a standard $r$ across classes, and Siblini et al. (2020) use a fixed ratio $r_0$ to define $r$-independent AUPR and F-scores; class imbalance in the training data shifts the threshold but does not change the sequence of confusion matrices behind the test ROC and PR curves.

- URL: <https://arxiv.org/abs/2007.01905> (PDF read: <https://arxiv.org/pdf/2007.01905>, v3 dated 27 Apr 2021)
- Local copy: none.
- Fetched: 2026-10-28
