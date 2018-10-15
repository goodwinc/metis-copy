### Schedule

**9:00 am**: [Pair Problem](pair_factorial.md)

		Arianna, Iggy
		Michael, Emma
		Saif, John
		Rob, Goodwin
		Amine, Vitoria
		Maddy, Elizabeth
		Angad, Krisztian
		Druce, Adam
		Matt, Laila
		Andree
		Dan, Brendon

**10:00 am**: [Error metrics for classification](Classification_Errors.pdf)

**10:30 am**: [Intro to SQL](intro_to_sql_notes.md)

**10:45 am**: [SQL Lab](SQL_lab.md)

**12:00pm**: Lunch

**1:00 pm**: Investigation Presentation

**1:30pm**: Challenges and project work!


### More on structuring data, databases, and SQL

 * You could go through Zed Shaw's [Learn SQL the Hard Way](http://sql.learncodethehardway.org/book/), which will still take you through lots of SQL with SQLite.
 * For more introductory SQL, check out the [Mode Analytics "SQL School"](http://sqlschool.modeanalytics.com/).

 ### More on Error Metrics

 * [Precision, recall, sensitivity, specificity](http://uberpython.wordpress.com/2012/01/01/precision-recall-sensitivity-and-specificity/)
 * [Wikipedia page on precision and recall](http://en.wikipedia.org/wiki/Precision_and_recall)
 * [Scikit learn on classification metrics](http://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
 * [Receiver Operating Characteristic](http://gim.unmc.edu/dxtests/roc2.htm)
 * [Area under curve (ROC)](http://gim.unmc.edu/dxtests/roc3.htm)


##### What is the relationship between F1 and Fß?

If you have found the [metrics function](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html) in `sklearn` that spits out your precision, recall, and F score, you might have found yourself asking: "What is Fß? Is it the same as F1?"

The answer is ... yes. F1 combines precision and recall. Fß does
the same thing, but uses a weight so that you can weigh one of these
two (precision or recall) more than the other when combining them. It
is a way to tune your score if you care more about precision than
recall, for example. F1 is the Fß for which ß = 1. In
`sklearn`, the default value for ß is 1.

The [wikipedia page](http://en.wikipedia.org/wiki/F1_score) has more on this relationship.

