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





class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        if self.parent[a] == a:
            return a
        # need this line fast
        self.parent[a] = self.find(self.parent[a])
        return self.find(self.parent[a])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return True
        self.parent[x] = self.parent[y]
        return False


class Solution2:
    def minCostToSupplyWater(self, n, well, pipes):
        uf = UnionFind(n + 1)
        for i in range(len(well)):
            pipes.append([0, i + 1, well[i]])

        pipes = sorted(pipes, key=lambda v: v[2])
        res = 0
        for u, v, cost in pipes:
            if not uf.union(u, v):
                res += cost
        return res


