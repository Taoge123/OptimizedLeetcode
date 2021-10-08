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


class SolutionTony:
    def countSquares(self, matrix) -> int:

        m, n = len(matrix), len(matrix[0])
        res = 0
        memo = {}
        for i in range(m):
            for j in range(n):
                res += self.dfs(matrix, i, j, memo)
        return res

    def dfs(self, matrix, i, j, memo):
        # if (i, j) in memo:
        #     return memo[(i, j)]

        m, n = len(matrix), len(matrix[0])
        # print(i, j)
        if i < 0 or i >= m or j < n or j >= n:
            return 0

        if matrix[i][j] == 0:
            return 0

        down = self.dfs(matrix, i + 1, j, memo)
        if down == 0:
            return 1
        right = self.dfs(matrix, i, j + 1, memo)
        if right == 0:
            return 1
        dia = self.dfs(matrix, i + 1, j + 1, memo)
        if dia == 0:
            return 1
        return min([down, right, dia]) + 1


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



matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
a = SolutionTony()
print(a.countSquares(matrix))





