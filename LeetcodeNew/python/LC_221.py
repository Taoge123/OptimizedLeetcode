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

class Solution:
    def maximalSquare(self, matrix):

        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]
        temp = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0
                temp = max(dp[i][j], temp)
        res = max(max(row) for row in dp)
        print(dp)
        print(temp)
        return temp ** 2





