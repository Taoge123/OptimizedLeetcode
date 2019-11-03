"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""
import collections
"""
Let's look at a naive recursive algorithm:

Suppose you are given 1--n, and you want to generate all binary search trees. 
How do you do it? Suppose you put number i on the root, then simply

Generate all BST on the left branch by running the same algorithm
with 1--(i-1),
Generate all BST on the right branch by running the
same algorithm with (i+1)--n.
Take all combinations of left branch
and right branch, and that's it for i on the root.
Then you let i go from 1 to n. And that's it. If you want to write it in code, it's like
"""

class RevursiveSolution:
    def countTrees(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1

        Result = 0
        for i in range(n):
            LeftTrees = self.countTrees(i)
            RightTrees = self.countTrees(n - i - 1)
            Result += LeftTrees * RightTrees
        return Result


"""
The only problem is, it's very slow, because for large n, 
you'll need to calculate countTrees(i) many many times, 
where i is a small number. Naturally, to speed it up, 
you just need to remember the result of countTrees(i), 
so that when you need it next time, you don't need to calculate. 
Let's do that explicitly by having a list of n+1 numbers to store the calculation result!


n = 3, there are 5 unique BST

root : 1 left : 0 right : 2 f(0) * f(2)
root : 2 left : 1 right : 1 f(1) * f(1)
root : 3 left : 2 right : 0 f(2) * f(0)

f(n) = f(0) * f(n-1) + f(1) * f(n-2) + f(n-2) * f(1)


"""


# class Solution:
#     def numTrees(self, n: int) -> int:
#         res = [0] * (n+1)
#         res[0] = 1

#         for i in range(1, n+1):
#             for j in range(i):
#                 res[i] += res[j] * res[i-j-1]
#         return res[-1]

class SolutionTony:

    def numTrees(self, n: int) -> int:
        cache = collections.defaultdict(int)
        return self.dfs(n, cache)

    def dfs(self, n, cache):
        if n == 0:
            return 1
        if n == 1:
            return 1

        if cache[n] != 0:
            return cache[n]

        res = 0
        for i in range(n):
            left = self.dfs(i, cache)
            right = self.dfs(n - i - 1, cache)
            res += left * right
        cache[n] = res
        return res

