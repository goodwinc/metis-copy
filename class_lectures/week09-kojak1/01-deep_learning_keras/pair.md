#### Pair Problem

Let's bootstrap!  Recall that bootstrapping is sampling with replacement from a dataset to produce a new dataset of the same size. For example, a bootstrapped sample of [1, 2, 3, 4, 5] could be [1, 2, 2, 4, 4]. Bootstrapping is used in random forests to guard against overfitting.  It also has wide application in many other areas of statistics, including as a computational approach to estimating confidence intervals as you will implement below:

1) Produce a bootstrapped estimate of the median and 95 percent confidence interval over the median of the dependent variable in the [attached dataset](pair_boot.csv).

2) Use the attached data to run a linear regression. Produce bootstrapped estimates of the model coefficients b1,...,bp, and a 95% confidence interval over them.

For estimating confidence intervals, what are the pros/cons of using the bootstrap vs. analytical estimates?

Why does bootstrapping help prevent overfitting in random forests?