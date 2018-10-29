This morning we'll implement a method for featurizing text, i.e. turning words into numeric values that can be fed to machine learning models. We'll use a small set of amazon reviews with positive/negative sentiment labels (balanced classes), and a simple multinomial naive bayes model to test our method.

You can use sklearn for everything except the Count Vectorizer methods :)

**Steps:**

**1.** Read in the data, take a quick look, and do a train/test split. This one's a gift to you:

```
df = pd.read_csv("Data/amazon_cells_labelled.txt", sep='\t', names=['text', 'sentiment'])

df.head()
```

```
# train test split
X_train, X_test, y_train, y_test = train_test_split(df.text, df.sentiment,
                                                    test_size=.2, random_state=2018)
```    

**2.** We want to predict the sentiment of the review only using the text. ??? How do we turn words into numeric features? 

This is where the **Count Vectorizer** method comes into play. It turns out we can do something pretty simple - just count word occurences across all of our different text samples (documents). Each word in the the entire corpus (collection of documents) gets its own feature column. 

Your major task is to write a class and/or series of functions that accomplish the following:

* Iterate through a corpus and collect all of the distinct words that occur into a global **vocabulary**. Hint: try using Counter from the collections library.

* To each word in the vocabulary, assign a consistent ordered position - for example, you could sort by the number of occurences (but any consistent positioning is fine).

* **Transform a corpus into a numeric dataframe**, with one column for each word in the vocabulary. For each document in the corpus (row in the dataframe), count occurences of each word and fill the corresponding dataframe columns with the appropriate counts. The positioning in bullet 2 allows you to do this consistently. This output is called a **document-term matrix**. 

**3.** Once you've built your Count Vectorizer, apply it to the review data. Build your vocabulary off of the entire corpus (df.text), and convert the train and test corpuses (X_train, X_test) to document-term matrices using your transform function. Congrats, you now have numeric features and targets! Fit a multinomial naive bayes model to the train data and score it for accuracy on the test data.
