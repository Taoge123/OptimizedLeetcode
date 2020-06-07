
class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        dp = [[False] * n for i in range(n)]

        for i, j in prerequisites:
            dp[i][j] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])

        return [dp[i][j] for i, j in queries]


