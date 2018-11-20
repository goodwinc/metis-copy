# Amoebas, Amoebas!

At time zero there is one amoeba in a petri dish. It splits with probability ps. With probability 1-ps it dies without splitting, 
and its entire line (only itself at this point) is eliminated. If it splits, on the other hand, it produces two amoeba that both live 
to next period (period 1.) At period 1, if there are any amoeba, each has a probability ps of splitting and 1-ps of dying 
without splitting. This occurs again and again as long as there are amoeba in the dish; at evenly spaced intervals, if there are any 
amoeba left, each one splits and survives with probability ps and dies without splitting with probability 1-ps. 

```
1. What is the probability that the amoeba line continues forever, 
	* if ps=3/4? 
	* if ps=1/2? 
	* if ps=9/10?  One formula should solve all cases.
2. Can you simulate a bunch of amoeba lines for a number of periods?  
	What percentage of the lines still have amoeba at the end?  
	Does the empirical frequency seem to match the theoretic probability, from part 1?
```

Both of these are tricky.  If you can't get one, try the other.  Some hints:
* Sometimes it's helpful to formulate the probability of an event _not_ occuring.  What is the probability of the line NOT surviving forever?
* For simulation, choose the right probability function for random draws.  It's possible to make this very inefficient. If so, you might only be able to run it around 20 time periods.  A better choice could yield hundreds of time periods for a thousand amoeba lines.
* If the number of amoeba gets too large, Python will hit memory problems and start making the counts negative.  This causes problems for random draws and might throw an error if the cumulative count dips negative.  I didn't have problems when simulating about 50 periods.


