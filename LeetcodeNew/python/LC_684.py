
import collections


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return [i, j]
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1


class Solution:
    def findRedundantConnection(self, edges):
        uf = UnionFind(1001)
        for i, j in edges:
            if uf.union(i, j):
                return i, j


class SolutionDFS:
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(list)

        def dfs(node, target):
            if node in visited:
                return False
            if node == target:
                return True

            visited.add(node)

            for nei in graph[node]:
                if dfs(nei, target):
                    return True
            return False

        res = []
        for u, v in edges:
            visited = set()
            if dfs(u, v):
                res = [u, v]
            graph[u].append(v)
            graph[v].append(u)
        return res

