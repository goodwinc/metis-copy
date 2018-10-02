#### Pair Problem #1

Solve this on paper (think of it like a puzzle): 

There are 10 kids that want ice cream. Each one can choose between chocolate, vanilla or strawberry. You'll collect their choices and make one order, something like: 5 chocolate, 3 vanilla and 2 strawberry. How many possible orders can you make? 5c-3v-2s is one and 4c-4v-2s is another. But 3v-5c-2s doesn't count now because it's the same as the first order.


#### Pair Problem #2

These problems involves first doing some math, either in your head or with pencil and paper, and only afterward verifying with Python.

For each problem, there is a matrix `X` and a vector `y`. You are looking for a vector `w` so that when you take a row of `X` and multiply each element by its corresponding element of `w` and then sum the results (the dot product of the row of `X` with `w`) you get the value at the corresponding position of `y`. For example, if we have:

```
X = [[5, 3, 7],   y = [537,
     [2, 4, 1]]        241]
```

A solution is `w = [100, 10, 1]`.

For each problem, answer two things:

 1. How many solutions are there? Why?
 2. If there are any solutions, what is one?


Problem A:

```
X = [[2]]        y = [8]
```


Problem B:

```
X = [[0]]        y = [8]
```


Problem C:

```
X = [[2, 4]]     y = [8]
```


Problem D:

```
X = [[2, 4],     y = [8,
     [0, 1]]          3]
```


Problem E:

```
X = [[2, 4],     y = [8,
     [0, 1],          3,
     [9, 5]]          1]
```


Problem F:

```
X = [[2, 2],     y = [4,
     [3, 3]]          6]
```


Problem G:

```
X = [[1, 1, 0],    y = [8,
     [1, 0, 1]]         6]
```


After finishing the problems, use `numpy` to check your solutions. Can you use `numpy` to _find_ solutions?
