import functools

class Solution:
    def assignBikes(self, workers, bikes) -> int:

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        @functools.lru_cache(None)
        def dfs(state, i):
            if i == len(workers):
                return 0

            res = float('inf')
            for j in range(len(bikes)):
                if not state & (1 << j):
                    res = min(res, dist(workers[i], bikes[j]) + dfs(state | 1 << j, i + 1))
            return res

        return dfs(0, 0)




