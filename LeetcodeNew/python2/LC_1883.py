
"""
https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/discuss/1241923/From-binary-search-to-Top-down-then-bottom-up.-O(N2)-greater-O(N2)
https://leetcode-cn.com/problems/minimum-skips-to-arrive-at-meeting-on-time/solution/python-zhuan-huan-cheng-zheng-shu-de-dpw-nazt/

"""

import functools


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:

        n = len(dist)

        @functools.lru_cache(None)
        def dfs(i, k):
            if k == -1:
                return 1e9

            if i == -1:
                return 0

            res = 1e9
            res = min(res, dfs(i - 1, k - 1) + dist[i] / speed)
            res = min(res, ceil(dfs(i - 1, k) + dist[i] / speed - 1e-9))
            return res

        for i in range(n):
            if dfs(n - 1, i) <= hoursBefore:
                return i
        return -1










