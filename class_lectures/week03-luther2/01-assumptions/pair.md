#### Pair Problem

Practice Lasso regularization technique in five steps:

1) Load Diabetes Dataset from SK Learn (`sklearn.datasets.load_diabetes()`).  Note that data may already be normalized.

2) Using sklearn model selection's `train_test_split`, hold out a portion of the data for final testing.

3) Use the KFold function from sklearn's cross validation module to divide the data into 5 training/validation sets.  Randomize the KFold (via the shuffle parameter with Random State of 0).

4) Tune the lambda (alpha) parameter in the lasso model by looping over a grid of possible lambdas (sklearn: lasso)
and scoring each value on each validation fold.

```
For each candidate lambda, loop over the 5 training/test sets.  
On each training/test set run the lasso model on the training set and then compute and record the prediction error in the test set.  
Finally total the prediction error for the 5 training/test sets.
```

5) Set lambda to be the value that minimizes prediction error on validation folds.

6) Run the lasso model again on the entire train+validation data with the optimal lambda determined in step 3. 
Which variables would you consider excluding on the basis of these results?

7) Try with Ridge and ElasticNet and base LinearRegression Models.  Compare your results.

Once you've selected what you think is the best model, train it on train+validation, predict on your held out test data,
and report the final result.

**Extra Credit**:  Try some Feature Engineering (Polynomials etc) to fit the data better.  Plot the data to see relationships.
