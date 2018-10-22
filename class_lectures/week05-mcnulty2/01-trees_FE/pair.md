#### Pair Problem

Naive Bayes, as promised! Please use the [starter notebook](Pair_NaiveBayesStarter.ipynb).

Here is a [dataset of movie reviews](http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz), 1000 positive and 1000 negative.

Write your own Naive Bayes solver.

TIPS:

For the dataset:

    1) Save the review_polarity.tar.gz file onto your computer
    2) On command line 'gunzip review_polarity.tar.gz'
    3) Then do 'tar -xvf review_polarity.tar'
    4) You will have a folder called txt_sentoken, and within that there will be pos and neg folders
    5) Split data into train, test and holdout: easiest way is to manually create seperate folders and move some files there
    
For Naive Bayes (the starter code does steps 1 & 2 for you):

    1) To read multiple files in python, use this resource:
        http://stackoverflow.com/questions/18262293/python-open-every-file-in-a-folder
    2) Convert each test review into a list of words
    3) Count how often a word appears in the positive (and negative) training set (use dictionaries)
    4) Change that count to log probabilities
    6) For each review in the test set, simply sum up it's words' log probability for being positive and negative
    7) Compare the two sums and assign the class that scores higher
