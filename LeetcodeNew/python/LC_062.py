"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

"""

from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        # dp = [[1 for i in range(n)] for j in range(m)]
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # dp[i][j] = dp[i-1][j] + dp[i][j-1]
                dp[j] += dp[j - 1]
        return dp[-1]


class Solution1:
    def uniquePaths(self, x: int, y: int) -> int:
        return self.helper(x, y)

    @lru_cache(None)
    def helper(self, x, y):
        if x <= 0 or y <= 0:
            return 0

        if x == 1 and y == 1:
            return 1

        return self.helper(x - 1, y) + self.helper(x, y - 1)


class SolutionCache:
    def uniquePaths(self, x: int, y: int) -> int:
        cache = {}
        return self.helper(x, y, cache)

    def helper(self, x, y, cache):
        if x <= 0 or y <= 0:
            return 0

        if x == 1 and y == 1:
            return 1

        if (x, y) in cache:
            return cache[(x, y)]

        cache[(x, y)] = self.helper(x - 1, y, cache) + self.helper(x, y - 1, cache)
        return cache[(x, y)]



