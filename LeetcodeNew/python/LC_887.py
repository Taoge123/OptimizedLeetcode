"""
1. broken : we have K-1 egges left, and we know 0<=F<i, i-1 (1~i-1) floors left -> D(K-1, i-1)
1. Unbroken : we still have K eggs, and we know 0<=F<=N, N-i (i+1~N) floors left -> D(K, N-i)

We need to know the worst case -> max(D(K-1, i), D(K, N-i))

"""

from functools import lru_cache

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = [[float('inf') for i in range(N + 1)] for j in range(K + 1)]

        @lru_cache(None)
        def dp(k, n):
            if k == 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n
            res = memo[k][n]
            for i in range(1, n + 1):
                res = min(res, 1 + max(dp(k - 1, i - 1), dp(k, n - i)))
            return res

        return dp(K, N)



class SolutionLee:
    def superEggDrop(self, K, N):
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N:
                return m






