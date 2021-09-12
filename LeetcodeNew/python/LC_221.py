"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


class SolutionTD:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        memo = {}
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    res = max(res, self.dfs(matrix, i, j, memo))
        return res ** 2

    def dfs(self, matrix, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            return 0

        if matrix[i][j] == '1':
            memo[(i, j)] = 1 + min(self.dfs(matrix, i + 1, j, memo), self.dfs(matrix, i, j + 1, memo),
                                   self.dfs(matrix, i + 1, j + 1, memo))
            return memo[(i, j)]
        return 0



class Solution:
    def maximalSquare(self, matrix):
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                res = max(res, dp[i][j])
        return res * res





