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

class Solution:

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






