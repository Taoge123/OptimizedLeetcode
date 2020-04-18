"""
https://leetcode.com/problems/couples-holding-hands/
https://leetcode.com/problems/redundant-connection/
305. Number of Islands II
684. Redundant Connection
765. Couples Holding Hands
947. Most Stones Removed with Same Row or Column




"""


class UnionFind:
    def __init__(self, stones):
        self.parent = [i for i in range(len(stones))]
        self.rank = [0 for i in range(len(stones))]
        self.count = len(stones)

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] > self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] += 1
        self.count -= 1


class Solution:
    def removeStones(self, stones) -> int:
        uf = UnionFind(stones)
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        return len(stones) - uf.count


class DSU:
    def __init__(self, N):
        self.p = [i for i in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr


class Solution2:
    def removeStones(self, stones):
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})



"""
[[0,0],
 [0,1],
 [1,0],
 [1,2],
 [2,1],
 [2,2]]

   0 1 2
0  1 0 0
1  0 0 1
2  1 0 0

0, 10000
2, 10001
2, 10000





"""

