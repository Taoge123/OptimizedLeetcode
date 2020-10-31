
"""

1140.Stone-Game-II
本题是典型的决策问题。设计solve(i,M)表示当前玩家可以从第i堆石头开始取、所取的堆数的上下限是[1,2M]，那么截止游戏结束所能得到的最大收益。

假设当前玩家取X堆，那么对手在之后所能得到的最大收益就是solve(i+X, max(X,M))。这就说明，对于当前玩家而言，如果本回合取X堆，
根据此消彼长的规则，意味着截止游戏时能得到的最大收益就是sufSum[i] - solve(i+X, max(X,M))。所以为了使solve(i,M)最大，我们必然会取能使sufSum[i] - solve(i+X, max(X,M))最大的X。

递归的边界条件就是当i==n的时候，玩家不能再取石头，返回零。最终的答案就是solve(0,1)。


M = 1  [1, 2] X = 2
M = 2  [1, 4] X = 3
M = 3  [1, 6] X = 1
M = 3  [1, 6] X = ...

maximize:      dp[state]
minimize:  max(dp[state'])



"""


from functools import lru_cache

"""
M = 1  [1, 2] X = 2
M = 2  [1, 4] X = 3
M = 3  [1, 6] X = 1
M = 3  [1, 6] X = ...

maximize:      dp[state]
minimize:  max(dp[state'])



"""


class Solution:
    def stoneGameII(self, piles) -> int:
        self.dp = {}
        return self.dfs(0, 1, piles)

    def dfs(self, i, M, piles):
        n = len(piles)
        if i >= n:
            return 0

        # take all if possible
        if n - i <= 2 * M:
            return sum(piles[i:])

        # memoization
        if (i, M) in self.dp:
            return self.dp[(i, M)]

        res = 0
        # explore each x
        for x in range(1, 2 * M + 1):
            # diff is the current palyers score, keep max
            res = max(res, sum(piles[i:]) - self.dfs(i + x, max(x, M), piles))
        self.dp[(i, M)] = res
        return res




class SolutionLee:
    def stoneGameII(self, piles) -> int:
        N = len(piles)
        for i in range(N - 2, -1, -1):
            piles[i] += piles[i + 1]
        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= N:
                return piles[i]
            return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        return dp(0, 1)






