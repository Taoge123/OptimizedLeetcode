import collections

class UnionFind:
    def __init__(self, n):
        self.parent = {i :i for i in range(n)}

    def find(self, i):

        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB


class Solution:
    def matrixRankTransform(self, matrix):
        m, n = len(matrix), len(matrix[0])

        position = collections.defaultdict(list)

        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                position[val].append((i ,j))

        res = [[0] * n for _ in range(m)]
        rowMaxRank = [0] * m
        colMaxRank = [0] * n

        for val in sorted(position):
            uf = UnionFind( m +n)
            for i, j in position[val]:
                uf.union(i, j + m)            # group nums on the same row/col

            rank = collections.defaultdict(int) # calculate new rank for the nums which have the same root(on the same row/col)
            for i, j in position[val]:
                root = uf.find(i)
                rank[root] = max(rank[root], max(rowMaxRank[i], colMaxRank[j]) + 1)

            for i, j in position[val]:      # update the res and row/colMaxRank
                root = uf.find(i)
                r = rank[root]
                res[i][j] = r
                rowMaxRank[i] = r
                colMaxRank[j] = r

        return res


