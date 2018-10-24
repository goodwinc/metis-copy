#### Pair Problem

| 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| o |   |   |   | x |

Above is a gameboard of length 4. You start your coin at position 0 and you want to end at position 4. You have N moves. In each move, you have two options, One space forward or stay put. And you can never step outside the board. And at the end of your last move, you want to be at the last square.

Given a board of length D and N moves, calculate the number of possible solutions.

For the example above, D = 4. Let's say N = 5. Then we have,

    FFFFS
    FFFSF
    FFSFF
    FSFFF
    SFFFF
    
That gives a total of 5 solutions.

Write a function "def Way(n,d)" that would return the number of possible solutions.

See if you can do this without recursion and with recursion.

#### Extension

If you are done, try this extension:

In addition to a forward and stay move, you now also have the option to move backwards.

So for D = 2 and N = 5, we would have,

    FFSSS
    FFBFS
    FBSFF
    Etc.
    
How many possible solutions are there? Keep in mind that the board is limited and you can't step out in either direction.

Again, try both the recursive and non-recursive approach.

This problem is not trivial. So take your time to think, talk and work it out.
