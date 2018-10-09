#### Pair Problem

I have generated some data and I want sese to how you can model it using Linear Regression (sklearn).

For each of the three file pairs (1_train.csv, 1_test.csv for example), build a model using the features and target in the training data and test on the test data. For this problem, better the score a model can produce on the test set, the better the model is. Your task is to get the best possible model. You are welcome to view, plot and explore the training data as much as you please. You can only do two things with the test data: read it to a dataframe and use that score your model.

Here is some starter code. You can use this as a starting point for all three datasets and try to improve the score.

    df = pd.read_csv('1_train.csv')
    df_test = pd.read_csv('1_test.csv')
    m = LinearRegression()
    m.fit(df[['x1','x2']],df['y'])
    m.score(df[['x1','x2']],df['y'])
    m.score(df_test[['x1','x2']],df2['y'])
 
