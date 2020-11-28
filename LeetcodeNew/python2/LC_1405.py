import heapq

import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for count, token in (-a, 'a'), (-b, 'b'), (-c, 'c'):
            if count:
                heapq.heappush(maxHeap, (count, token))
        res = []
        while maxHeap:
            count, token = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-2] == res[-1] == token:
                if not maxHeap:
                    break
                count, token = heapq.heapreplace(maxHeap, (count, token))
            res.append(token)
            if count + 1: heapq.heappush(maxHeap, (count + 1, token))
        return ''.join(res)




