### Plan for Thursday, August 16 

#### Overview

Today we'll talk about **Vector Space Models** for NLP.  Our goal for all of these is just finding the best method to turn words into vectors. We'll cover methods that are appropriate for capturing semantics (LSA, which is really just TF-IDF passed through SVD usually) and ones that capture both semantics and syntax (Word2Vec). Once we've done that, we can do just about anything :smile:


**Remember:**
* By now you've hopefully made a lot of progress on getting your Fletcher data! Try to have it by the weekend. 

#### Schedule

**8:45 am**: Let's go!

**9:00 am**: Pair Programming:  
  * Pair: [LDA fun](pair.md)   
  
    Arianna, Amine
    Maddy, Rob
    Angad, Saif
    Druce, Michael
    Matt, Iggy
    Emma
    Dan, John
    Brendon, Goodwin
    Andree, Vitoria
    Laila, Elizabeth
    Adam, Krisztian

**10:00 am**: 
  * [VSMs](VSMs.ipynb) 
  * [Pretrained Word2Vec](Word2Vec_pretrained.ipynb)

**12:00 pm**: Break time!

**1:00 pm**: Investigation Presentation

**1:15 pm**: Work
* [Project 4: Fletcher](/projects/04-fletcher)

#### More Resources
##### TFIDF and Naive Bayes Classification
* [tf-idf on Wikipedia](http://en.wikipedia.org/wiki/Tf%E2%80%93idf)
* [tf-idf tutorial with textblob](http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/)
* [Stanford slides on text classification with naive Bayes](https://web.stanford.edu/class/cs124/lec/naivebayes.pdf)
* [Naive Bayes on Wikipedia](http://en.wikipedia.org/wiki/Naive_Bayes_classifier)
* [Naive Bayes Spam Filtering on Wikipedia](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)

Empirically, naive Bayes works really well on text classification. One example is spam filtering. Two classes (spam/not spam). A bag of words model (treating each word as an independent feature), using tf-idf values as weights for the features in `MultinomialNB` works wonders.

However, naive Bayes is not necessarily the ultimate text classifier. It works reasonably well if you don't have ginormous amounts of data. However, if you have enough data, generally successful classifiers like SVMs can surpass it (but they may take longer to train). So don't be shy in trying other classifiers.

##### word2vec
* [Deep Learning, NLP, and Representations](http://colah.github.io/posts/2014-07-NLP-RNNs-Representations/)
