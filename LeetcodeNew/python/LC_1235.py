
import bisect
import heapq


class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda v : v[1])

        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect_left(dp, [s + 1]) - 1
            cur = dp[i][1] + p
            if cur > dp[-1][1]:
                dp.append([e, cur])

        return dp[-1][1]




class Solution2:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key = lambda v: v[0])
        heap = []
        res = 0

        for s, e, p in jobs:
            while heap and heap[0][0] <= s:
                node = heapq.heappop(heap)
                res = max(res, node[1])

            heapq.heappush(heap, (e, p + res))

        while heap:
            node = heapq.heappop(heap)
            res = max(res, node[1])

        return res





