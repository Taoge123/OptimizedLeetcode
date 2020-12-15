"""
https://leetcode.com/problems/optimize-water-distribution-in-a-village/discuss/472033/Python-Solution-Easy-to-Understand
"""

import collections
import heapq

class Solution:
    def minCostToSupplyWater(self, n: int, wells, pipes) -> int:
        graph = collections.defaultdict(list)
        for u, v, cost in pipes:
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        for i in range(len(wells)):
            graph[0].append((i + 1, wells[i]))

        res = 0
        # cost, v, u
        heap = [(0, 0, -1)]
        parents = {}
        while heap:
            cost, v, u = heapq.heappop(heap)
            if v in parents:
                continue
            parents[v] = u
            res += cost
            for nei, newCost in graph[v]:
                if nei not in parents:
                    heapq.heappush(heap, (newCost, nei, v))

        return res


