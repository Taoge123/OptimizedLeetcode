class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, i):
        if i == self.parent[i]:
            return self.parent[i]
        return self.find(self.parent[i])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return False
        self.parent[x] = y
        return True


class Solution:
    def minimumCost(self, N: int, connections) -> int:
        connections = sorted(connections, key=lambda x: x[2])
        res = 0
        uf = UnionFind(N)
        for u, v, cost in connections:
            if uf.union(u - 1, v - 1):
                res += cost

        count = 0
        for i in range(N):
            if uf.parent[i] == i:
                count += 1
                if count > 1:
                    return -1
        return res


