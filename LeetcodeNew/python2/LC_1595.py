"""
i : 001, 011, 111
dp[i][state]: considering the first i points on the left, and the visited points on the right corresponds to state,
              then the minimum cost

xx1xx1xx1

00000 ~ 11111 2^n

1. dp[i-1][....] + i visites a subset of state -> dp[i][state]
2. dp[i-1][....] + i visites an already visited points with minimum edge -> dp[i][state]

return dp[m-1][1<<n-1]


Intuition
As usual, it pays to analyze problem constraints. Since we only have up to 12 points, we can track which ones are connected using a bit mask.

Solution
Staightforward top-down DP for the first group. At the same time, we track which elements from the second group were connected in mask.

After finishing with the first group, we detect elements in group 2 that are still disconnected, and connect them with the "cheapest" node in the first group.



"""
from functools import lru_cache

class SolutionTLEbutGood:
    def connectTwoGroups(self, cost) -> int:
        m, n = len(cost), len(cost[0])
        dp = [[0 for i in range(1 << 12)] for j in range(12)]
        dp[0][0] = float('inf')

        for state in range(1, 1 << n):
            summ = 0
            for j in range(n):
                if ((state >> j) & 1) == 1:
                    summ += cost[0][j]
            dp[0][state] = summ

        for i in range(1, m):
            dp[i][0] = float('inf')
            for state in range(1, 1 << n):
                dp[i][state] = float('inf')
                subset = state
                while subset > 0:
                    summ = 0
                    for j in range(n):
                        if ((subset >> j) & 1) == 1:
                            summ += cost[i][j]

                    # option 1
                    dp[i][state] = min(dp[i][state], dp[i - 1][state - subset] + summ)
                    # 遍历子集
                    subset = (subset - 1) & state

                minPath = float('inf')
                for j in range(n):
                    minPath = min(minPath, cost[i][j])
                # option 2
                dp[i][state] = min(dp[i][state], dp[i - 1][state] + minPath)

        return dp[m - 1][(1 << n) - 1]



class SolutionTD:
    def connectTwoGroups(self, cost) -> int:
        m, n = len(cost), len(cost[0])
        dp = [min([cost[i][j] for i in range(m)]) for j in range(n)]

        @lru_cache(None)
        def dfs(i: int, mask: int):
            if i >= m:
                res = 0
            else:
                res = float('inf')
            if i >= m:
                for j in range(n):
                    if mask & (1 << j) == 0:
                        res += dp[j]
            else:
                for j in range(n):
                    res = min(res, cost[i][j] + dfs(i + 1, mask | (1 << j)))
            return res

        return dfs(0, 0)



