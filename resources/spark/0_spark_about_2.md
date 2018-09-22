#Spark Resources

##RDD Operations

Transformations | Actions 
--- | --- 
*lazy*  | *executing* 
**map(func):** pass each element of source through func, return new RDD | **reduce(func):** aggregate elements with func
**filter(func):** select elements of the source for which func returns true, return new distributed RDD | **take(n):** copy top n elements to driver
**distinct():** return duplicate-free RDD | **collect():** copy all elements to driver
**sample(withReplacement, fraction [seed]):** sample RDD, with or without replacement |  **foreach(func):** apply provided func to each element of RDD
[more Transformations](http://spark.apache.org/docs/latest/programming-guide.html#transformations) | [more Actions](http://spark.apache.org/docs/latest/programming-guide.html#actions)

####transformations - are considered lazy, operation that will be evaluated later on  
####action -  when those transformations are actually executed  
```
pagecountsEnAllDF
  .select($"project", $"requests")   //transformation
  .groupBy($"project")               //transformation
  .sum()                             //transformation
  .orderBy($"sum(requests)".desc)    //transformation
  .show()                            //action
```
If you comment out `show()`, nothing will happen.  It won't execute.  

---

##Comparing Hadoop and Spark

feature | Hadoop | Spark
--- |--- | ---
purpose | big-data framework | big-data framework
created in | 2005 | 2009
created by | Doug Cutting and Mike Cafarella at Yahoo |  Matei Zaharia at UC Berkeley's AMPLab
what they do | distributed data infrastructure: It distributes massive data collections across multiple nodes within a cluster of commodity servers | data-processing tool that operates on those distributed data collections
high level operators | has 2: **map** and **reduce**  | has > 80 
functioning | uses HDFS read/write iteratively | Uses memory storage wherever possible
how it works | MapReduce operates in steps | operates on the whole data set in one fell swoop
speed       |        | 10-100 x faster
language written in  | Java  | Scala (but has bindings for Java, Python (PySpark), and R)

 

##RDD:  Sample Execution Plan

Item | Step |   |  | 
---- | ---- |----|----| 
1   | Create RDD from text file             | RDD            | `sc.textFile(“/dirpath/textfile.txt”)`  
2   | Flattens lists of words into one list  | `flatMap`      | `.flatMap(lambda x: x.split())`
3   | Remove punctuation, convert to upper case  | `.map()`   | `.map(lambda x: x.replace('|', '').replace('.', '').replace('-', '').replace(' ', '').replace('&', '').replace('#','').upper())`
4   | Word count **mapper** function            | `.map()`       | `.map(lambda x: (x, 1))`
5   | Word count **reducer** function           | `.reducer()`   | `.reduceByKey(lambda a, b: a + b)`   `.sortByKey(ascending=False)`
6a  | copy to driver: all items       | `collect()`    |  `.collect()`
6b  | copy to driver: 10 items        | `take()`       | `.take(10)`
6c  | copy to driver: first item      | `first()`      | `.first()`

---

###Spark APIs (v 1.6)

* RDD
* DataFrame
* Dataset

##Spark 2.0
* [What's New in 2.0](http://zdatainc.com/2016/05/spark-2-0-whats-new/)
  * More SQL friendly
  * APIs (2, instead of 3)
    * *DataFrames* is a higher level structured data API (Spark dataframe does allow nested columns in data (versus flat file) )
    * *DataFrame* and *Dataset* unified into one API
  * Single entry point
    * Spark 2.0 introduces SparkSession
    * only need to connect to one "context"
      * For instance to connect to SQL we required SQLContext and StreamContext for Streaming. While using DataFrames API a common confusion is to decide which “context” to use
  * even faster
  * Structured Streaming
    * improves real-time applications for developers
  * DataFrame based ML API
    * (original spark.mllib package is preserved, but no new development on it)
  
* Docker has not yet released a PySpark image for Jupyter yet (as of Aug 2016)

##Coming up, after Spark 2.0, currently in development

* Advanced Analytics
  * support vis libraries:  plot.ly, bokeh
  * 3rd party ML integrations:  sci-kit learn, tensor flow (deep learning)



---

##Resources

####Recommended Books
* [Learning Spark](http://shop.oreilly.com/product/0636920028512.do)
* [Advanced Analytics with Spark](http://shop.oreilly.com/product/0636920035091.do)

####[Databricks](https://databricks.com/)  
* Founded out of the UC Berkeley AMPLab by the team that created Apache Spark.  
* Explore the [Databricks cloud environment](https://databricks.com/product/getting-started-with-apache-spark-on-databricks)

####GitHub 

* [Opinionated stacks of ready-to-run Jupyter applications in Docker](https://github.com/jupyter/docker-stacks)

####What's Next, after Spark:  Scala
* [Scala](http://www.scala-lang.org/index.html) is an acronym for “Scalable Language”. This means that Scala grows with you. You can play with it by typing one-line expressions and observing the results. But you can also rely on it for large mission critical systems, as many companies, including Twitter, LinkedIn, or Intel do.
* [Scala tutorial](http://www.tutorialspoint.com/scala/)
  

