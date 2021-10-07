
"""
https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/discuss/1241923/From-binary-search-to-Top-down-then-bottom-up.-O(N2)-greater-O(N2)
https://leetcode-cn.com/problems/minimum-skips-to-arrive-at-meeting-on-time/solution/python-zhuan-huan-cheng-zheng-shu-de-dpw-nazt/

"""

import functools
import math


class SolutionTony:
    def minSkips(self, dist, speed: int, hoursBefore: int) -> int:

        n = len(dist)

        @functools.lru_cache(None)
        def dfs(i, k):
            if k < 0:
                return float('inf')

            if i >= n:
                return 0

            skip = dfs(i + 1, k - 1) + dist[i] / speed
            no_skip = math.ceil(dfs(i + 1, k) + dist[i] / speed - 1e-9)
            return min(skip, no_skip)

        for k in range(n):
            if dfs(0, k) <= hoursBefore:
                return k
        return -1


class Solution:
    def minSkips(self, dist, speed: int, hoursBefore: int) -> int:

        n = len(dist)
        @functools.lru_cache(None)
        def dfs(i, k):
            if k < 0:
                return float('inf')

            if i >= n:
                return 0

            res = float('inf')
            res = min(res, dfs(i + 1, k - 1) + dist[i] / speed)
            res = min(res, math.ceil(dfs(i +1, k) + dist[i] / speed - 1e-9))
            return res

        for k in range(n):
            if dfs(0, k) <= hoursBefore:
                return k
        return -1










