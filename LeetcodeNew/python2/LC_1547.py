
"""
dp[i][j] = min{cuts[j]-cuts[i] + dp[i][k] + dp[k][j]} for k in i+1, i+2, ...., j-1

"""

import functools

class Solution:
    def minCost(self, n: int, cuts) -> int:
        cuts.sort()
        cuts.insert(0, 0)
        cuts.append(n)
        m = len(cuts)
        dp = [[float('inf') for i in range(m)] for j in range(m)]

        for i in range( m -1):
            dp[i][ i +1] = 0

        for step in range(3, m+ 1):
            for i in range(m - step + 1):
                j = i + step - 1
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], cuts[j] - cuts[i] + dp[i][k] + dp[k][j])

        return dp[0][m - 1]



class SolutionTD:
    def minCost(self, n: int, cuts) -> int:

        cuts.sort()
        cuts = [0] + cuts + [n]
        @functools.lru_cache(None)
        def dfs(i, j):
            if j - i == 1:
                return 0

            res = float('inf')
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + (cuts[j] - cuts[i]))
            return res

        return dfs(0, len(cuts) - 1)




class SolutionTony:
    def minCost(self, n: int, cuts) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        memo = {}
        return self.dfs(cuts, 0, len(cuts) - 1, memo)

    def dfs(self, cuts, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if j - i == 1:
            return 0

        res = float('inf')
        for k in range(i + 1, j):
            res = min(res, self.dfs(cuts, i, k, memo) + self.dfs(cuts, k, j, memo) + (cuts[j] - cuts[i]))

        memo[(i, j)] = res
        return memo[(i, j)]


n = 7
cuts = [1,3,4,5]

a = SolutionTony()
print(a.minCost(n, cuts))



