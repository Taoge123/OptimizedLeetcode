"""
1277.Count-Square-Submatrices-with-All-Ones
此题和222.Maximal Square几乎是同一道题，本质就是求01矩阵里面，以(i,j)为右下角的正方形最大边长是多少。
边长多大，就意味着以(i,j)为右下角的正方形能有多少个。

解这类题目有一个非常有名的动态转移方程，就是dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1.
也就是说，以(i,j)为右下角的正方形能有多大，取决于：以(i-1,j)为右下角的最大正方形，
以(i,j-1)为右下角的最大正方形，以(i-1,j-1)为右下角的最大正方形，这三者最小的那一个。
这是动态规划题目里最经典的“非典型应用”，希望能够记牢。

注意第一行和第一列需要单独处理dp值。并且(0,0)元素不要重复计算。
"""


class Solution:
    def countSquares(self, matrix) -> int:
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
                res += dp[i][j]
        return res









