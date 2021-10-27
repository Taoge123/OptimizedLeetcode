import copy
import functools

class SolutionTD:
    def minFallingPathSum(self, matrix) -> int:

        m, n = len(matrix), len(matrix[0])
        @functools.lru_cache(None)
        def dfs(i, j):
            if j < 0 or i >= m or j >= n:
                return float('inf')

            if i == m - 1:
                return matrix[i][j]

            return matrix[i][j] + min(dfs(i + 1, j - 1), dfs(i + 1, j), dfs(i + 1, j + 1))

        res = float('inf')
        for j in range(n):
            res = min(res, dfs(0, j))
        return res



class Solution:
    def minFallingPathSum(self, A) -> int:
        m, n = len(A), len(A[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp = copy.deepcopy(A)

        for i in range(1, m):
            for j in range(n):
                dp[i][j] = dp[ i -1][j]
                if j- 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 1])
                dp[i][j] += A[i][j]

        return min(dp[-1])




