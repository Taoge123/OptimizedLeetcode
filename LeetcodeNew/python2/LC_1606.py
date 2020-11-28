
from sortedcontainers import SortedList
import collections
import heapq

class Solution:
    def busiestServers(self, k, arrival, loads):
        res = collections.Counter()
        busy = []
        free = SortedList(range(k))
        for req, (time, load) in enumerate(zip(arrival, loads)):
            while busy and busy[0][0] <= time:
                free.add(heapq.heappop(busy)[1])
            if not free:
                continue
            i = free.bisect_left(req % k)
            if i >= len(free):
                i = 0
            id_ = free.pop(i)
            heapq.heappush(busy, (time+load, id_))
            res[id_] += 1
        maxi = max(res.values())
        return [h for h in res if res[h] == maxi]








