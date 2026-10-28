# NeurIPS Paper Checklist Guidelines (as hosted on the NeurIPS 2026 site)

Supports: item 6, "Experimental setting/details", asks whether all training details (data splits, hyperparameters, how they were chosen) are specified, with the important details in the main paper; item 7, "Experiment statistical significance", asks for error bars, confidence intervals or statistical significance tests at least for the experiments that support the main claims, and says that the factors of variability the error bars capture should be stated (train/test split, initialization, random drawing of some parameter, or overall run), the method for computing them explained (closed form, library call, bootstrap), the assumptions given (for example Normally distributed errors), and that it should be clear whether the error bar is the standard deviation or the standard error of the mean; 1-sigma error bars are fine if stated; "The authors should preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis of Normality of errors is not verified" (wording as on the page); asymmetric distributions should not get symmetric error bars that leave the valid range, such as negative error rates.

- URL: <https://neurips.cc/public/guides/PaperChecklist>
- Local copy: none.
- Fetched: 2026-10-28
