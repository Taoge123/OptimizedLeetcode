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


