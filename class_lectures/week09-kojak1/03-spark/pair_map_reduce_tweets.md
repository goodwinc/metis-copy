# Streaming map-reduce with Python

Map-reduce is a famous programming model that extends simple analytics to massive data sets, spread across HDFS - the Hadoop Distributed Filesystem.  
It is an important development of "Big Data," which has generated much excitement everywhere.  This week we will be setting up and getting started 
with some big-data systems and applications, but we start here with a much smaller map-reduce problem, designed to run locally on our machines.
From an analytic viewpoint, Map-reduce is simple. Files are mapped, line by line, into key value pairs.  A "shuffle and sort" algorithm
pulls together these keys and sorts them, then sends them to a reducer program, which counts the number of occurrences of each class.  The end 
results are simply counts, similar to what we would've gotten with value_counts in Pandas.  The difference is that this code might
be sent to multiple machines, each housing their own partitions of the data.  The "shuffle and sort" work happens on a master computer (name node)
which sends map and reduce tasks to worker nodes.  As a result, we are able to operate on massive datasets, much 
larger than the datasets that fit on a single machine.  Much of the motivation for developing MapReduce was to build a web crawler,
capable of indexing now billions of web pages with many inter-linkages. 

Map-reduce is designed to run in batch mode, and so we must write stand-alone scripts to handle the map and reduce jobs.
We will be using python, so we will be creating .py files.  input.txt contains stringified rows in dictionary data structures.
These are tweets, stored in dict form. Each tweet dict occupies a new line.  Our goal is to read this file, line by line, 
extracting the user screen_name in the map job. We will then sort on the screen name using the Unix "sort" function (which implements merge sort.)
Finally we will use a reduce function to count the sorted output by screen name to give us a final output file.  
Once the map and reduce functions are created, we will run the following command in Unix: 

# What you're going to do 

**We want to count the tweets of each user in a Map-Reduce format.** You will make a map.py script and a reduce.py script. The data we'll work with is in `input.txt`. This might seem hokey on a few dozen tweets but writing code in this way would allow it to execute efficiently in distributed file systems.

0. (suggested) write out in pseudocode how you would write the map function and the reduce function. Test it out on paper.
1. The map.py function should take every line of the file and output the result of some function. Think: if the input file has N observations/rows, the output of map.py should have how many observations/rows.
2. The reduce.py file should take the (potentially shuffled then sorted) result of many map functions and reduce them. Think: if the input file has N observations/rows, the output of reduce.py might have how many observations/rows.
3. Write your code in a format that allows use to execute it with the following bash command:

```
cat input.txt | ./tweets_map.py | sort | ./tweets_reduce.py > output
```

Hint:
- in order for a script.py file to take input from a pipe, look up the python module `sys`, specifically `sys.stdin`. 

Where tweets_map.py contains the mapping function, and tweets_reduce.py contains the reduce code.  output will be a file
containing the user names next to the number of their tweets, one user per row.  The pipes between commands indicate that the output from one function/program/command is passed to the next function/program/command.   
Cat reads the input file in and passes it to tweets_map.py, which in turn passes its output to the Unix sort function, and so on.  Your challenge is to create
tweets_map.py and tweets_reduce.py.


### Hints for the mapping function:

1. The mapping function will have to find each user_name.  Hint: it's nested.  You might use pretty-print to figure out the data structure.  
Try using sys.stdin.readline() to read just one line and deduce its structure.
eval(line) will turn the stringified dictionary into an actual dict data structure, from which you can use dictionary logic. 
2. Use sys.stdin to read the Twitter data in streaming fashion, line-by-line.  It creates an iterator on lines.
4. We want fail-safe code.  (More on distributed fault tolerance later.)  Make sure your code doesn't bomb if it doesn't find a user_name in the line.
5. You can simply use the print function to generate output to send to the sort step.

### Hints for the reducer code:

1. This code simply moves down the sorted output lines from 'sort', adding 1 to the count every time it sees a tweet from the same user.
2. When it sees a new user in the sorted output, it outputs the count from the previous user:  print(current_handle, counter) and switches current_handle to the new user and resets the counter.
3. Sometimes data contains unwanted spaces.  Use strip() to make sure they're gone.
4. We should end with just one count per user, with the count printed next to the user name and sent to the output file, one user per line.

Finally, the Unix command above prints the output of these streaming jobs to an output file.  Use `cat` to see it!
