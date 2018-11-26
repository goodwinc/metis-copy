### Pair Problem

You are given a square matrix T. T[x,y] gives the time it takes to go from city x to city y. T[x,x] is zero. All other values are positive integers. T[x,y]=T[y,x]. Naturally, when traveling from x to y, sometimes its faster to go through another city than going directly from x to y.

Here is an example matrix for 6 cities. Your function can take the input matrix T as a list of lists or a numpy array/matrix.

|  |  |  |  |  |  | 
| --- | --- | --- | --- | --- | --- | 
| 0 | 4 | 9 | 3 | 1 | 2 | 
| 4 | 0 | 2 | 1 | 4 | 2 | 
| 9 | 2 | 0 | 7 | 2 | 1 | 
| 3 | 1 | 7 | 0 | 6 | 6 | 
| 1 | 4 | 2 | 6 | 0 | 2 | 
| 2 | 2 | 1 | 6 | 2 | 0 | 

1) Write a function that will give you the shortest travel time from city A to city B, with at most one stop-over (Ex. A->E->B).

2) Modify the function to give the shortest travel time from city A to city B, with **at most two stop-overs**.

3) Write a function to find the shortest travel time from city A to city B with any number of stop-overs. And what is the complexity of the function? Can you improve it? Note, I'm not interested in the actual path, only the time it will take on the shortest possible path.
