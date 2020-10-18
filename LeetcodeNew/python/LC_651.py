class Solution:
    def maxA(self, N: int) -> int:
        dp = [0] * (N + 1)
        for i in range(N + 1):
            dp[i] = i
            for j in range(1, i - 2):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))

        return dp[-1]



class Solution2:
    def maxA(self, N):
        dp = [i for i in range(N+1)]
        for i in range(7, N+1):
            dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)

        return f[N]

