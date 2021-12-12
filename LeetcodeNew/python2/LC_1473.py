"""

https://leetcode.com/problems/paint-house-iii/discuss/674466/Python3-DFS-with-Memo-easy-to-understand
https://leetcode.com/problems/paint-house-iii/discuss/1504386/Python-%3A%3A-Memoization


There are 3 parameters for dfs()
i : current house index
remain : number of remaining unassigned neighborhoods
prev_color : color of previous house, we use this to determine decrease remain or not

"""

import functools


class Solution:
    def minCost(self, houses, cost, m, n, target) -> int:

        @functools.lru_cache(None)
        def dfs(i, prev_color, remain):
            if remain < 0 or remain > m - i:
                return float('inf')
            if i == m:
                if remain == 0:
                    return 0
                else:
                    return float('inf')

            res = float('inf')
            if houses[i]:
                if houses[i] != prev_color:
                    res = dfs(i + 1, houses[i], remain - 1)
                else:
                    res = dfs(i + 1, houses[i], remain)
            else:
                for j in range(1, n + 1):
                    if j != prev_color:
                        res = min(res, cost[i][j - 1] + dfs(i + 1, j, remain - 1))
                    else:
                        res = min(res, cost[i][j - 1] + dfs(i + 1, j, remain))
            return res

        # no house paint with 0 so it guarantee to form the first neighborhoods
        res = dfs(0, 0, target)
        return res if res < float('inf') else -1


