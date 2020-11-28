"""
Idea

This problem is about connect pair of cities then check if there is a connection between any 2 cities. This is clearly Union-Find problem. Implementation of Union-Find.
The difficult things is that n <= 10^4, we can't check all combination pairs of cities which is O(n^2) which will cause TLE. So we can borrow a bit idea of Sieve of Eratosthenes which help to reduces time complexity down to ~ O(NlogN)
Example
Input: n = 6, all pair of cities:

i = 1, j = [2, 3, 4, 5, 6]
i = 2, j = [4, 6]
i = 3, j = [6]
i = 4: j = []
i = 5, j = []
i = 6, j = []

"""

class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.size = [1] * n

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if self.size[x] < self.size[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
        return True

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]


class Solution:
    def areConnected(self, n: int, threshold: int, queries):
        uf = UnionFind(n + 1)
        for city1 in range(threshold + 1, n + 1):
            for city2 in range(2 * city1, n + 1, city1):
                uf.union(city1, city2)  # make two cities connected.

        res = []
        for u, v in queries:
            res.append(uf.find(u) == uf.find(v))
        return res




class Solution2:
    def areConnected(self, n: int, threshold: int, queries):
        uf = UnionFind(n + 1)
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):  # step by i
                if i > threshold:
                    uf.union(i, j)

        res = []
        for u, v in queries:
            res.append(uf.find(u) == uf.find(v))
        return res

