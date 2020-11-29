import collections


class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        table = {}
        for i in range(1, N + 1):
            if i in table:
                continue
            if not self.dfs(graph, table, i, 1):
                return False
        return True

    def dfs(self, graph, table, node, color):
        if node in table:
            return table[node] == color

        table[node] = color
        for nei in graph[node]:
            if not self.dfs(graph, table, nei, -color):
                return False
        return True




class SolutionBFS:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        table = {}
        for i in range(1, N + 1):
            if i in table:
                continue
            if not self.bfs(graph, table, i, 1):
                return False
        return True

    def bfs(self, graph, table, node, color):
        table[node] = color
        queue = collections.deque([node])

        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if nei in table:
                    if table[node] == table[nei]:
                        return False
                else:
                    table[nei] = -table[node]
                    queue.append(nei)

        return True

