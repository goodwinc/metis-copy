#### Pair Problem

I have generated some data and I want sese to how you can model it using Linear Regression (sklearn).

There are three file pairs in the data folder. For each pair ((1_train.csv, 1_test.csv for example) build a model using the features and target in the training data, and then test on the test data. 

For this problem, better the score a model can produce on the test set, the better the model is. Your task is to get the best possible model. You are welcome to view, plot and explore the training data as much as you please (you can also generate new features, drop rows, etc). But you can only do two things with the test data: read it to a dataframe and use that to score your model.

Here is some starter code. You can use this as a starting point for all three datasets and try to improve the score.

    from sklearn.linear_model import LinearRegression
    import pandas as pd
    df = pd.read_csv('data/1_train.csv')
    df_test = pd.read_csv('data/1_test.csv')
    m = LinearRegression()
    m.fit(df[['x1','x2']],df['y'])
    m.score(df[['x1','x2']],df['y'])
    m.score(df_test[['x1','x2']],df_test['y'])
