
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

import functools


class Solution:
    def profitableSchemes(self, n, minProfit, group, profit):

        @functools.lru_cache(None)
        def dfs(i, g, p):
            if i >= len(group):
                return p >= minProfit

            # 不犯这个罪
            no_take = dfs(i + 1, g, p)
            take = 0
            # 如果人数够，考虑犯这个罪
            if g >= group[i]:
                # min(P,p+profit[i]) 如果超过P,统一计为P,降低复杂度
                take = dfs(i + 1, g - group[i], min(minProfit, p + profit[i]))
            return take + no_take

        # res = dfs(0, n, 0) % (10**9+7)
        # dfs.cache_clear()
        return dfs(0, n, 0) % (10 ** 9 + 7)



class SolutionTLE:
    def profitableSchemes(self, n: int, minProfit: int, group, profit) -> int:

        @functools.lru_cache(None)
        def dfs(i, g, p):
            print(i, g, p)
            if i >= len(group):
                return p >= minProfit

            no_take = dfs(i + 1, g, p)
            take = 0
            if g >= group[i]:
                take = dfs(i + 1, g - group[i], p + profit[i])
            return take + no_take

        # res = dfs(0, n, 0) % (10**9+7)
        # dfs.cache_clear()
        return dfs(0, n, 0) % (10 ** 9 + 7)




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

