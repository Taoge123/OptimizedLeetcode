
"""
https://www.youtube.com/watch?v=3M8q-wB2tmw
"""


class Solution:
    def maxSumAfterPartitioning(self, A, K) -> int:
        n = len(A)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            maxi = float('-inf')
            for k in range(1, min(i, K) + 1):
                maxi = max(maxi, A[i - k])
                dp[i] = max(dp[i], dp[i - k] + maxi * k)

        return dp[n]




