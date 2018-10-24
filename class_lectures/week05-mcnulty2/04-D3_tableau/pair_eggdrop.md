#### Pair Problem

Let's give recursion one last shot!

With recursion you have to take that leap. You have to believe you have solved a smaller version of the same problem. So let's do this one a little differently. Let's not do the simple case by hand, get an understanding of the problem and then try to extend it. None of that is neccessary for recursion. It's just a matter of jumping in and doing it.

**There is a tall building and a basket of eggs. If any of the eggs are dropped from a certain cut-off floor or above, it will break. If it's dropped from any of the floors below, it wouldn't break, however many times you dropped it. We need to find the cut-off floor. The question is, given N floors and M eggs, we need to find out how many tries are necessary.**

    def neededTries(n,m):

Remember the steps for recursion:

    1) What is the simplest first action you will take. (For example: In yesterday's problem it was whether stay or move forward)
    2) What are the possible results of the action above
    3) How do those outcomes reduce our inputs (N and M in this case)
    4) How should we combine the results of those various outcomes
    5) What are the end conditions

And you are done!

This is not an easy problem. It's okay if you don't solve it completely. See which of the above steps you can complete. And I'll slack answers to each of the question above, one at a time. Flag me if any of it is unclear.
