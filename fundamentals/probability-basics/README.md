# Probability basics
The probability that classification metrics need, and no more. A conditional probability $P(A \mid B) = P(A \cap B)/P(B)$ is the probability of $A$ among the cases where $B$ holds, and in general $P(A \mid B) \ne P(B \mid A)$. The law of total probability splits $P(B)$ over the cases of $A$: $P(B) = P(B \mid A)\,P(A) + P(B \mid \neg A)\,P(\neg A)$. Bayes' rule, $P(A \mid B) = P(B \mid A)\,P(A)/P(B)$, turns a likelihood and a prior into a posterior; in odds form, posterior odds equal prior odds times the likelihood ratio. In a classifier, the prevalence is the prior $P(y = 1)$, TPR and FPR are the likelihoods $P(\hat y = 1 \mid y = 1)$ and $P(\hat y = 1 \mid y = 0)$, and precision is the posterior $P(y = 1 \mid \hat y = 1)$.

## Questions
- [ ] What is a conditional probability, and why is $P(A \mid B)$ usually not $P(B \mid A)$ (the base-rate fallacy)?
- [ ] How does Bayes' rule follow from the definition of conditional probability and the law of total probability?
- [ ] What is the odds form of Bayes' rule, and what is a likelihood ratio?
