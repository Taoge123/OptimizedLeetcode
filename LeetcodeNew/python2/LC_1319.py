class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)

        if x == y:
            return

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        elif self.rank[y] > self.rank[x]:
            x, y = y, x

        self.parent[y] = x

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]


class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n - 1:
            return -1

        uf = UnionFind()

        for num in range(n):
            uf.parent[num] = num
            uf.rank[num] = 1

        for i, j in connections:
            uf.union(i, j)

        return sum(uf.find(num) == num for num in range(n)) - 1




