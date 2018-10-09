#### Pair Problem

Same deal as yesterday. There are 4 datasets in the 'data' folder. I didn't split to train-test. Do the split yourself and see how high you can get the score on the test set to be.

I'd prefer that you explore all the datasets. So don't spend too much time on one. Also, some of these are tough/tricky, but there is a little lesson behind each. Feel free to ask me for hints/suggestions.

For #3 and #4, I have descriptive column names. My suggestion would be to copy those somewhere and then rename the columns to x1,x2,y in the datafile before reading in (for ease).

Here is starter code:

    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    import pandas as pd
    df = pd.read_csv('data/1.csv')
    X_train, X_test, y_train, y_test = train_test_split(df[['x1','x2','x3','x4','x5']], df['y'], test_size=0.33, random_state=42)
    m = LinearRegression()
    m.fit(X_train,y_train)
    m.score(X_train,y_train)
    m.score(X_test,y_test)
