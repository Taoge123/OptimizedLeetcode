import collections
import math

class Solution:
    def largestComponentSize(self, A) -> int:
        uf = UnionFind(max(A))
        # attribute each element in A
        #   to all the groups that lead by its factors.
        for num in A:
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    uf.union(num, factor)
                    uf.union(num, num // factor)

        # count the size of group one by one
        res = 0
        count = collections.defaultdict(int)
        for num in A:
            group_id = uf.find(num)
            count[group_id] += 1
            res = max(res, count[group_id])
        return res


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        # the two nodes share the same set
        if x == y:
            return x

        # otherwise, connect the two sets (components)
        if self.size[x] > self.size[y]:
            # add the node to the union with less members.
            # keeping px as the index of the smaller component
            x, y = y, x
        # add the smaller component to the larger one
        self.parent[x] = y
        self.size[y] += self.size[x]
        # return the final (merged) group
        return y








