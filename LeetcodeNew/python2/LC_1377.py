"""
https://leetcode.com/problems/frog-position-after-t-seconds/discuss/532486/Python-DFS-in-a-Tree
https://www.youtube.com/watch?v=B5nDIxkoEyo

"""


class Solution:
    def frogPosition(self, n, edges, t, target):
        if n == 1:
            return 1.0
        graph = [[] for i in range(n + 1)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = [0] * (n + 1)
        return self.dfs(graph, 1, t, visited, target)

    def dfs(self, graph, i, t, visited, target):
        if i != 1 and len(graph[i]) == 1 or t == 0:
            return i == target
        visited[i] = 1
        res = sum(self.dfs(graph, j, t - 1, visited, target) for j in graph[i] if not visited[j])
        return res * 1.0 / (len(graph[i]) - (i != 1))



