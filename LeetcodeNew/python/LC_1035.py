
class Solution:
    def maxUncrossedLines(self, A, B) -> int:
        m = len(A)
        n = len(B)

        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[ i -1] == B[ j -1]:
                    dp[i][j] = 1 + dp[ i -1][ j -1]
                else:
                    dp[i][j] = max(dp[i][ j -1], dp[ i -1][j])

        return dp[m][n]



