# Statistical inference
The inference that reporting classification results needs, and no more. A metric computed on a test set is an estimate, and its sampling distribution describes how it would vary over other test sets drawn from the same population; the standard deviation of one run's score is not the standard error of a mean over runs, which shrinks with the number of independent runs. A confidence interval is a range built so that, over repeated samples, it contains the true value with a stated probability (its coverage). A hypothesis test rejects a null hypothesis, such as "two classifiers have equal error", and its Type I error is the chance of rejecting it when it is true. The bootstrap approximates the sampling distribution by recomputing the statistic on samples drawn with replacement from the data, and correlated scores (such as cross-validation folds) break the independence that the usual standard-error and t-test formulas assume.

## Questions
- [ ] What is a sampling distribution, and how do the standard deviation and the standard error differ?
- [ ] What does the coverage of a confidence interval mean, and why is a 95% interval not a 95% probability that the true value lies inside it?
- [ ] How does the nonparametric bootstrap approximate a sampling distribution, and when does it fail?
- [ ] What are Type I and Type II errors and the power of a test, and why does correlation between paired scores inflate a t-test's Type I error?
