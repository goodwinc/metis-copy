### Schedule

**9:00 am**: [Pair programming](pair.md).

		Arianna, Matt
		Druce
		Dan, Angad
		Brendon, Maddy
		Andree, Amine
		Laila, Rob
		Adam, Saif
		Krisztian, Michael
		Elizabeth, Iggy
		Vitoria, Emma
		Goodwin, John

**10:00 am**: [Intro to NLP notebook](06_NLP_for_class.ipynb) - NB with solutions is [here](06_NLP_with_Solutions.ipynb) 

Extra NLP content:
* [Assorted NLTK functions, including textblob sentiment analysis, and sklearn CountVectorizer/ tf-idf ](NLP_nltk.ipynb)
* [Naive Bayes text classification example](Naive_Bayes.ipynb)
* [NLP topics overview](NLP.ipynb)

**12:00 pm**: Lunch

**1:00 pm**: Investigation Presentation


### More Resources

 * [Overencompassing yet still short nltk tutorial](http://www.nltk.org/book/) The official book of the nltk
 * [TextBlob tutorial](http://textblob.readthedocs.org/en/latest/quickstart.html): Awesome, easy to read, very short but to the point. Check this out.
 * [TextBlob full documentation](http://textblob.readthedocs.org/en/dev/): Great documentation
 * [TextBlob Sentiment: Calculating Polarity and Subjectivity](http://planspace.org/20150607-textblob_sentiment/)
 * [List of part-of-speech tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html): What does VBZ mean? etc.
 * [Chunking tutorial](http://www.eecis.udel.edu/~trnka/CISC889-11S/lectures/dongqing-chunking.pdf)
 * [MIT slides on chunking](http://web.media.mit.edu/~havasi/MAS.S60/PNLP7.pdf): If you want to learn more on chunking and prepare your own chunking classifiers, these will help.
 * [Demo for different tokenizers](http://text-processing.com/demo/tokenize/) / [Demo for different stemmers](http://text-processing.com/demo/stem/): These let you get a feel for what different classes do.
 * [tf-idf on Wikipedia](http://en.wikipedia.org/wiki/Tf%E2%80%93idf)
 * [tf-idf tutorial with textblob](http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/)
 * [Stanford slides on text classification with naive Bayes](https://web.stanford.edu/class/cs124/lec/naivebayes.pdf)
 * [Naive Bayes on Wikipedia](http://en.wikipedia.org/wiki/Naive_Bayes_classifier)
 * [Naive Bayes Spam Filtering on Wikipedia](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)

Empirically, naive Bayes works really well on text classification. One example is spam filtering. Two classes (spam/not spam). A bag of words model (treating each word as an independent feature), using tf-idf values as weights for the features in `MultinomialNB` works wonders.

However, naive Bayes is not necessarily the ultimate text classifier. It works reasonably well if you don't have ginormous amounts of data. However, if you have enough data, generally successful classifiers like SVMs can surpass it (but they may take longer to train). So don't be shy in trying other classifiers.
