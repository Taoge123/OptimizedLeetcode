import copy


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




