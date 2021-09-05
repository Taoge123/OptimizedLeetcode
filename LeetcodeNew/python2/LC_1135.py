class UnionFind:
    def __init__(self, N: int):
        self.parent = list(range(N))
        self.size = [1] * N

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

    def size(self, x: int) -> int:
        return self.size[self.find(x)]


class Solution:
    def minimumCost(self, N: int, connections) -> int:
        connections = sorted(connections, key=lambda x: x[2])
        res = 0
        count = 0
        uf = UnionFind(N)

        for u, v, cost in connections:
            if uf.union(u - 1, v - 1):
                res += cost
                count += 1

        if count == N - 1:
            return res
        return -1







