"""
0123 456 7
3333 666 7
1.
2.if group contains 2 nodes in intial, continue

0 - 3
4 -

graph = [
     0 1 2
0   [1,1,0]
1   [1,1,0]
2   [0,0,1]

initial= [0, 1, 2]
parent = [0, 0, 2]

"""

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
                    size = size[self.find(i)]
                    res = i
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


"""
必须正着求， 反过来不行， 删除0或者1都没用
[[1,1,0],[1,1,0],[0,0,1]]
[0,1,2]

"""

class SolutionDFS2:
    def minMalwareSpread(self, graph, initial):

        def dfs(node):
            visited.add(node)
            for nei, val in enumerate(graph[node]):
                if nei in visited:
                    continue
                if val == 1:
                    dfs(nei)

        min_infected = float("+inf")
        best_node = -1

        for node_removed in sorted(initial):
            visited = set()
            for node in initial:
                if node == node_removed:
                    continue
                if node in visited:
                    continue
                dfs(node)
            if len(visited) < min_infected:
                min_infected = len(visited)
                best_node = node_removed

        return best_node



class SolutionDFS:
    def minMalwareSpread(self, graph, initial):

        rank = collections.defaultdict(list)
        initial = set(initial)

        def dfs(i):
            visited.add(i)
            for j in range(len(graph[i])):
                if j in visited:
                    continue
                if graph[i][j]:
                    dfs(j)

        for node in sorted(initial):
            visited = set()
            dfs(node)
            if visited & initial == {node}:
                rank[len(visited)].append(node)
        if rank:
            return rank[max(rank)][0]
        return min(initial)









