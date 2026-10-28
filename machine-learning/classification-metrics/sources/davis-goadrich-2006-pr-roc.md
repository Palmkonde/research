# Davis and Goadrich, "The Relationship Between Precision-Recall and ROC Curves" (Proceedings of the 23rd ICML, Pittsburgh, 2006)

Supports: ROC curves can give an overly optimistic view of performance under large class skew, and PR curves are cited as the alternative for such tasks (Section 1); recall, precision, TPR and FPR definitions (Fig. 2); Theorem 3.1, a one-to-one correspondence between ROC and PR curves for a fixed dataset when recall ≠ 0; Theorem 3.2, a curve dominates in ROC space if and only if it dominates in PR space; Section 4, ROC points may be interpolated linearly, but in PR space linear interpolation "is a mistake that yields an overly-optimistic estimate", with the count interpolation $\big(\tfrac{TP_A+x}{\text{Total Pos}},\ \tfrac{TP_A+x}{TP_A+x+FP_A+\frac{FP_B-FP_A}{TP_B-TP_A}x}\big)$ for integer $1 \le x \le TP_B-TP_A-1$, the worked example in Table 1, the AUC-PR example 0.031 (correct) vs 0.50 (linear), AUC-ROC by trapezoids equal to the Wilcoxon-Mann-Whitney statistic; Section 5, optimizing AUC-ROC does not guarantee optimizing AUC-PR.

- URL: <https://doi.org/10.1145/1143844.1143874> (PDF read: <https://ftp.cs.wisc.edu/machine-learning/shavlik-group/davis.icml06.pdf>, the authors' department server)
- Local copy: none.
- Fetched: 2026-10-28
