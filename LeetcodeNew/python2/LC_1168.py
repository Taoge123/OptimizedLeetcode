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
    def __init__(self, N: int):
        # initially, every node forms a partition of size 1
        self.parent = list(range(N))  # the partition to which every node belongs
        self.size = [1] * N  # the size of ...

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, i: int, j: int) -> bool:
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.size[y] = self.size[x]
        return True


class Solution:
    def minCostToSupplyWater(self, n, well, pipes):
        uf = UnionFind(n + 1)
        for i in range(len(well)):
            pipes.append([0, i + 1, well[i]])

        pipes = sorted(pipes, key=lambda v: v[2])
        res = 0
        for u, v, cost in pipes:
            if uf.union(u, v):
                res += cost
        return res


"""
   \ 
   /\    /\

     o
  /\    /\

"""


class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [1] * N

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[y] += 1
        return True


class SolutionTony:
    def minCostToSupplyWater(self, n: int, wells, pipes) -> int:
        uf = UnionFind(n + 1)
        for i in range(len(wells)):
            pipes.append([0, i + 1, wells[i]])
        pipes = sorted(pipes, key=lambda x: x[2])

        res = 0
        for u, v, cost in pipes:
            if uf.union(u, v):
                res += cost
        return res





