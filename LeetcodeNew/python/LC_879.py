
"""
dp[person+x][profit+y] += d[person][profit]

"""

import copy

"""
dp[person+x][profit+y] += d[person][profit]

"""

"""
dp[k][i][j] means for first k crime with i members and at least j profit, what is total schemes can be chosen.
And we need this Math.max(0, j - p), because this is for at least j profit.

dp[k][i][j] = dp[k - 1][i][j] + dp[k - 1][i - current group][Math.max(0, j - current profit)]

This is 3d original solution:
"""

from functools import lru_cache


class SolutionTD:
    def profitableSchemes(self, G: int, P: int, group, profit) -> int:
        @lru_cache(None)
        def dp(i, total_profit, members_left):
            if i == len(profit):
                return 0

            take = 0
            we_can_take = members_left - group[i] >= 0
            if we_can_take:
                profit_here = 1 if total_profit + profit[i] >= P else 0
                take = profit_here + dp(i + 1, min(P, total_profit + profit[i]), max(0, members_left - group[i]))
            skip = dp(i + 1, total_profit, members_left)

            return take + skip

        return dp(0, 0, G) % (10 ** 9 + 7)



class Solution:
    def profitableSchemes(self, G: int, P: int, group, profit) -> int:
        dp = [[[0] * (P + 1) for i in range(G + 1)] for j in range(len(group) + 1)]
        mod = 10 ** 9 + 7
        # no person and no profit的方案有1种
        dp[0][0][0] = 1
        for k in range(1, len(group) + 1):
            g = group[k - 1]
            p = profit[k - 1]
            # for person
            for i in range(G + 1):
                # for profit, profit can be 0
                for j in range(P + 1):
                    dp[k][i][j] = dp[k - 1][i][j]
                    if i >= g:
                        pp = max(0, j - p)
                        dp[k][i][j] += dp[k - 1][i - g][pp]
                        dp[k][i][j] %= mod

        res = 0
        for i in range(G + 1):
            res += dp[-1][i][P]
            res %= mod
        return res



class Solution2:
    def profitableSchemes(self, G: int, P: int, group, profit) -> int:
        dp = [[0 for i in range(P + 1)] for j in range(G + 1)]
        mod = 10 ** 9 + 7
        dp[0][0] = 1

        for k in range(1, len(group) + 1):
            g = group[k - 1]
            p = profit[k - 1]
            for i in range(G, g - 1, -1):
                for j in range(P, -1, -1):
                    pp = max(0, j - p)
                    dp[i][j] += dp[i - g][pp]
                    dp[i][j] %= mod

        res = 0
        for i in range(G + 1):
            res += dp[i][P]
            res %= mod
        return res



"""
It's a variant of knapsack.
Suppose dp[p][g] represents the number of schemes when profit is p and group size is g. So for a specific scheme (p, g), dp[i+p][j+g] += dp[i][j]. dp[0][0] is initialized as 1.
We need to count the number backwards to avoid repeated counting. As for current (p, g), dp[i][j] is always updated later than dp[i+p][j+g] so that what is added to dp[i+p][j+g] is always the dp[i][j] from the previous iteration.
Besides, final profit can exceed P, so we just count all dp[i>P] to dp[P]. And we can use trick like dp[min(P,i+p)][g+j] += dp[i][j]. While j+g should be strictly bounded within G.
"""

class Solution3:
    def profitableSchemes(self, G, P, group, profit):
        dp = [[0] * (G + 1) for i in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(i + p, P)][j + g] += dp[i][j]
        return sum(dp[P]) % (10**9 + 7)



class SolutionWrong:
    def profitableSchemes(self, G: int, P: int, group, profit) -> int:

        dp = [[0 for i in range(P + 1)] for j in range(G + 1)]
        mod = 10 ** 9 + 7
        # no person and no profit的方案有1种
        dp[0][0] = 1

        for k in range(len(group)):
            x = group[k]
            y = profit[k]
            # for person
            for i in range(G + 1):
                # for profit, profit can be 0
                for j in range(P + 1):
                    # 符合人数条件
                    if i + x <= G:
                        # profit > P的时候, 我们还是取P
                        pp = min(j + y, P)
                        print(i+x, pp, i, j)
                        dp[i + x][pp] = dp[i][j]
                        dp[i + x][pp] %= mod

        print(dp)
        res = 0
        for i in range(G + 1):
            res += dp[i][P]
            res %= mod
        return res

