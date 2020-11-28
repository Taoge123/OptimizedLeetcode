"""
dp[k][i] = dp[k-1][i-1] + dp[k-1][i] + dp[k-1][i+1]

"""


class SolutionTLE:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = arrLen
        dp = [[0 for i in range(n)] for j in range(steps + 1)]
        mod = 10 ** 9 + 7
        dp[0][0] = 1
        for k in range(1, steps + 1):
            for i in range(n):
                if i == 0:
                    dp[k][i] = dp[k - 1][i] + dp[k - 1][i + 1]
                elif i == n - 1:
                    dp[k][i] = dp[k - 1][i - 1] + dp[k - 1][i]
                else:
                    dp[k][i] = dp[k - 1][i - 1] + dp[k - 1][i] + dp[k - 1][i + 1]

        return dp[steps][0] % mod



class SolutionOnlySteps:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = arrLen
        dp = [[0 for i in range(steps // 2 + 2)] for j in range(steps + 1)]
        mod = 10 ** 9 + 7
        dp[0][0] = 1
        for k in range(1, steps + 1):
            for i in range(steps // 2 + 1):
                if i == 0:
                    dp[k][i] = dp[k - 1][i] + dp[k - 1][i + 1]
                elif i == n - 1:
                    dp[k][i] = dp[k - 1][i - 1] + dp[k - 1][i]
                else:
                    dp[k][i] = dp[k - 1][i - 1] + dp[k - 1][i] + dp[k - 1][i + 1]
                dp[k][i] %= mod

        return dp[steps][0] % mod



