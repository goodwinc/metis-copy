Today, we design a new machine learning algorithm from scratch. 
This algorithm learns how to correct for the mistakes it's made in the past by training a series of "base learners" one by one.

1) Load the california housing data and do a train-test split as below:

    import pandas as pd

    from sklearn.datasets import california_housing
    from sklearn.model_selection import train_test_split

    housing_dataset = california_housing.fetch_california_housing()
    X = pd.DataFrame(housing_dataset.data)
    X.columns = housing_dataset.feature_names
    y = housing_dataset.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2018)
    
        
2) Ok that wasn't hard. Fit a simple linear regression on train and score it on test as a baseline.

3) That also wasn't so bad. Now the hard part: create a python class or series of functions that follows the steps below to create a predictive model from training data **X, y and a hyperparameter n_estimators**.

**A.** Set C = mean of y. This is our initial prediction, a constant prediction; track the current residuals y_i - C for all the target values

**B.** Do the following n_estimators times: using sklearn DecisionTreeRegressor, fit a tree of max_depth 3 to (X, current residuals). Save the tree in a list, and update the residuals by subtracting the tree's predicted values on X from the current residuals.

**C.** To make predictions on new data, you must sum the predictions made by all of the trees in your list, then add C. Fit your model on the training data and predict on the test data. Score your model on the test data. Try to get above .70 R^2. N_estimators = 10 is a good starting point to try.

**D.** Time permitting, expand your model by adding hyperparameters **max_depth** that adjust the max_depth of each tree, as well as **learning_rate**. With learning rate, when you update the residuals subtract learning_rate * tree.predict(X) (what does this remind you of?) Also, when predicting multiply the predictions made by each tree by the learning_rate.

Why do you think this works well? Where have we seen iterative mistake corrections with small step sizes come up before? Can you push your model to do even better?
