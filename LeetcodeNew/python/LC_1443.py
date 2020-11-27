import collections

class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        return self.dfs(graph, hasApple, 0, visited)

    def dfs(self, graph, hasApple, node, visited):
        visited.add(node)
        res = 0

        for nei in graph[node]:
            if nei in visited:
                continue

            cost = self.dfs(graph, hasApple, nei, visited)

            if cost or hasApple[nei]:
                res += cost + 2

        return res


