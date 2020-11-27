import collections

class Solution:
    def calcEquation(self, equations, values, queries):

        graph = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val

        res = []
        for u, v in queries:
            if u in graph and v in graph:
                res.append(self.dfs(graph, u, v, set()))
            else:
                res.append(-1)

        return res

    def dfs(self, graph, i, j, visited):

        if i == j:
            return 1

        for nei in graph[i]:
            if nei in visited:
                continue
            visited.add(nei)
            div = self.dfs(graph, nei, j, visited)
            if div > 0:
                return graph[i][nei] * div

        return -1


