# Classification Evaluation Metrics Practice

1. Load the Wisconsin breast cancer data from sklearn (binary classification problem), do a train/test split, and fit a logistic regression and 10 nearest neighbors model. Instead of using any built-in sklearn scoring methods, write your own accuracy, precision, recall, and F1 evaluation functions that take arrays of actual and predicted target labels as arguments. Score your models on the test set.
    * e.g.  `def accuracy(actuals, preds)`

2. Write your own function for generating an ROC curve plot from model predictions without using sklearn's assistance. Remember that ROC plots true positive rate (recall) vs. false positive rate for a given probability decision threshold. So you should loop over a range of probability cutoffs from 1 to 0, convert a model's predicted probabilities (`model.predict_proba()[:,1]`) to target labels using each cutoff, and plot the results as a curve.  