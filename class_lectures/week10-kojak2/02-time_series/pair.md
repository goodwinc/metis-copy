#### Pair Problem

#### Part 1

Write a function that will take two arguments, both lists of lists representing tables of data. The function will combine the two tables into one. Each of the inner lists represents a row of data, with the first element being the "key" for that row.

For example, your function would take these two lists of lists:

```python
[[27, 'dog', 5],
 [19, 'cat', 9],
 [33, 'bat', 3]]

[[14, 8, 'elf'],
 [33, 7, 'owl'],
 [27, 2, 'rat']]
```

In this case, your function would return this result:

```python
[[27, 'dog', 5, 2, 'rat'],
 [33, 'bat', 3, 7, 'owl']]
```

#### Part 2

Once you have a solution working, consider how your code would perform if the inputs were large. What is the complexity? Can you improve the performance of your solution?

Put in this piece of code:

```python
import random
random.seed(127)
numbers = range(1000)
random.shuffle(numbers)
test1 = [[index] + [random.random() for _ in range(100)] for index in numbers]
random.shuffle(numbers)
test2 = [[index] + [random.random() for _ in range(100)] for index in numbers]
```

And test the performance using this:

```python
%timeit yourfuction(test1, test2)
```

If you are on a Macbook Air, try to get your time under 10 ms. And on a Pro, under 6 ms.

#### Part 3

So far, you probably assumed that the values on the first column is unique. Modify your code to deal with not unique values.

For example, your function would take these two lists of lists:

```python
[[27, 'dog', 5],
 [19, 'cat', 9],
 [27, 'bat', 3]]

[[27, 8, 'elf'],
 [33, 7, 'owl'],
 [27, 2, 'rat']]
```

In this case, your function would return this result (order doesn't matter.. just that we get all four rows):

```python
[[27, 'dog', 5, 8, 'elf'],
 [27, 'bat', 3, 8, 'elf'],
 [27, 'dog', 5, 2, 'rat'],
 [27, 'bat', 3, 2, 'rat']]
```
