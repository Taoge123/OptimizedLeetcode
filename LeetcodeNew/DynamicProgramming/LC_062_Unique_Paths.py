
"""
https://leetcode.com/problems/unique-paths/discuss/23040/Python-Solution-with-Detailed-Explanation

Similar questions:
91. Decode Ways
70. Climbing Stairs
509. Fibonacci Number


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

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
import math

class Solution0:
    def uniquePaths(self, m, n):
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]

class Solution1:
    def uniquePaths(self, m, n):

        #### DP solution ####

        # edge cases
        if m <= 0 or n <= 0:
            return 0
        if m == 1 or n == 1:
            return 1

        # build an empty matrix
        matrix = [[1 for j in range(n)] for i in range(m)]
        print(matrix)

        # record steps for each cell using DP (Expect the first row and the first column, since there are only one way to get the cells in these places..)
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[-1][-1]


class SolutionCaikehe:
    # math C(m+n-2,n-1)
    def uniquePaths1(self, m, n):
        if not m or not n:
            return 0
        return math.factorial(m + n - 2) / (math.factorial(n - 1) * math.factorial(m - 1))

    # O(m*n) space
    def uniquePaths2(self, m, n):
        if not m or not n:
            return 0
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # O(n) space
    def uniquePaths(self, m, n):
        if not m or not n:
            return 0
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]


class Solution3:

    def uniquePaths(self, m, n):
        cache = {}
        return self.findPath(m, n, cache)

    def findPath(self, m, n, cache):
        if (m, n) in cache:
            return cache[(m, n)]
        elif m == 1 or n == 1:
            return 1

        cache[(m, n)] = self.findPath(m - 1, n, cache) + self.findPath(m, n - 1, cache)

        return cache[(m, n)]



