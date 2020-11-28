
"""
N connected nodes, M edges (M <= N*(N-1)//2)
what is the minimum number of edges to connect N nodes?



"""



class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.ranks = [1] * n
        self.size = 1

    def find(self, u):
        if u == self.parent[u]:
            return self.parent[u]
        return self.find(self.parent[u])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return False
        if self.ranks[x] > self.ranks[y]:
            self.parent[y] = x
        elif self.ranks[y] > self.ranks[x]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.ranks[y] += 1
        self.size += 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        uf1 = UnionFind(n)
        uf2 = UnionFind(n)
        res = 0

        for t, u, v in edges:
            if t != 3:
                continue
            if not uf1.union(u - 1, v - 1) or not uf2.union(u - 1, v - 1):
                res += 1

        for t, u, v in edges:
            if t == 1 and not uf1.union(u - 1, v - 1):
                res += 1
            elif t == 2 and not uf2.union(u - 1, v - 1):
                res += 1

        return res if uf1.size == n and uf2.size == n else -1



