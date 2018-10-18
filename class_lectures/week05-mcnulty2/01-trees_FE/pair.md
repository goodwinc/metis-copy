#### Pair Problem

Naive Bayes, as promised! Please use the [starter notebook](Pair_NaiveBayesStarter.ipynb).

Here is a [dataset of movie reviews](http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz), 1000 positive and 1000 negative.

Write your own Naive Bayes solver.

TIPS:

For the dataset:

    1) Save the review_polarity.tar.gz file onto your computer
    2) On command line 'gunzip review_polarity.tar.gz'
    3) Then do 'tar -xvf review_polarity.tar'
    4) You will have a folder called txt_sentoken and within that, there will be pos and neg folders
    5) To read multiple files in python, use this resource:
        http://stackoverflow.com/questions/18262293/python-open-every-file-in-a-folder
    
For Naive Bayes:

    1) Split data into train and test: easiest way is to create a seperate folder for test and move some files there
    2) Count how often a word appears in the positive training set and negative training set (the starter code brings you have way here)
    3) Change that into log probabilities
    4) For each review in the test set, simply sum up it's words' log probability for being positive and negative
    5) Compare the two sums and assign the class that scores higher
