import heapq

class Solution:
    def connectSticks(self, sticks) -> int:
        res = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            res += (a + b)
            heapq.heappush(sticks, a + b)
        return res


