"""
https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/C%2B%2BJavaPython-3-DP-Explanation-with-pictures.


"""

import functools

class Solution:
    def maxPoints(self, points) -> int:
        m, n = len(points), len(points[0])

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m:
                return 0
            res = 0

            for k in range(n):
                # just started, then no cost
                if i == -1:
                    res = max(res, dfs(i + 1, k))
                else:
                    res = max(res, dfs(i + 1, k) + points[i][j] - abs(j - k))

            return res

        res = dfs(-1, 0)
        dfs.cache_clear()
        return res



