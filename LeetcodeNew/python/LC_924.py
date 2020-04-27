
import collections

class Solution:
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    def minMalwareSpread(self, graph, initial):
        # init
        n = len(graph)
        self.parent = [i for i in range(n)]
        # union
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j] == 1:
                    self.union(i, j)

        size = collections.Counter(self.find(i) for i in range(n))
        malware = collections.Counter(self.find(i) for i in initial)
        maxi, res = 0, min(initial)
        for i in initial:
            if malware[self.find(i)] == 1:
                if size[self.find(i)] > maxi:
                    size, res = size[self.find(i)], i
                elif size[self.find(i)] == maxi:
                    res = min(res, i)
        return res


"""
0123 4567 8
3333 6666 8
Area = 
3 : 4
6 : 3
8 : 1
initial = [ 0,1]
malware
3 : 2
 
Save =  4 
Res = 0

"""

class SolutionBetter:
    def find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        p1, p2 = self.find(i), self.find(j)
        if p1 == p2:
            return
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        self.rank[p1] += self.rank[p2]
        self.parents[p2] = p1

    def minMalwareSpread(self, graph, initial):
        self.rank = [1] * len(graph)
        self.parents = [i for i in range(len(graph))]
        for i in range(len(graph)):
            for j in range(i, len(graph)):
                if graph[i][j] == 1:
                    self.union(i, j)
        topList = [0] * len(graph)
        initial.sort()

        maxi = 0
        for i in initial:
            topList[i] = self.rank[self.find(i)]
            maxi = max(maxi, topList[i])

        for i in initial:
            if topList[i] == maxi:
                return i













