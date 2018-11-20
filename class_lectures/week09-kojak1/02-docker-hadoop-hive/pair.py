from __future__ import print_function
from functools import reduce

numbers = range(1, 101)

# With one list comprehension
print([x**2 for x in numbers if x**2 % 2 == 1])

# With `map` and `filter`, separating out steps
squares = map(lambda x: x**2, numbers)
odd_squares = filter(lambda x: x % 2 == 1, squares)
print(odd_squares)

# A typical usage of reduce
print(reduce(lambda x, y: x + y, numbers))

# Less typical usages
squares = reduce(lambda agg, x: agg + [x**2], numbers, [])
odd_squares = reduce(lambda agg, x: agg + [x] if x % 2 == 1 else agg,
                     squares, [])
print(odd_squares)

# Reduce is the über-function!
