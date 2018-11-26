1) Write a simple function that takes two matrices of equal dimensions (a target and a filter), multiplies together their entries element by element, then sums across all the results. You can think of this as a sort of 2-dimensional dot product.

For example, with these matrices: you should get 8 when running your function with the below: 1 * 1 + 0 * 0 + 2 * 1 + 2 * 0 ...

```
mat = np.array([[1,0,2],
                [2,1,1],
                [1,1,3]])

filt = np.array([[1,0,1],
                 [0,1,0],
                 [1,0,1]])
```

2) Now write a function that utilizes the first as follows: assume the filter matrix has odd dimensions hence has a center (e.g. 3x3). Starting from the top left corner of the target matrix and moving right then down, find all entries that can be aligned with the center of the filter matrix such that you can call the function you just wrote (i.e. you can fit the filter into that part of the matrix). 

As you find valid centers, call your function on the corresponding subsection and store the results in a 2-dim array (matrix). The dimensions are given by the number of total steps you can validly take horizontally and vertically.

So for example, with a 4x5 target matrix and a 3x3 filter, the output dimensions will be 2x3.

You should get [[5,2,13],[4,4,2]] when running this new function with the below. The valid centers are the entries at (1,1), (1,2), (1,3), (2,1), ... 

```
1*1 + 1*1 + 3* 1 = 5  
0 * 1 + 1 * 1 + 1 * 1 = 2 
2 * 1 + 4 * 1 + 8 * 1 = 12 
2 * 1 + 1 * 1 + 1 * 1 = 4 
...
```

```
mat = np.array([[1,0,2,3,3],
                [2,1,1,4,1],
                [1,1,3,1,7],
                [1,1,1,0,0]])

filt = np.array([[1,0,0],
                 [0,1,0],
                 [0,0,1]])
```

This is a convolution!
