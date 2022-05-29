import collections


class SolutionTony:
    def possibleBipartition(self, n, dislikes):
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        table = {}

        def dfs(node, color):
            if node in table:
                return table[node] == color

            table[node] = color
            for nei in graph[node]:
                if not dfs(nei, -color):
                    return False
            return True

        for node in range(1, n + 1):
            if node in table:
                continue
            if not dfs(node, 1):
                return False
        return True



class SolutionDFS:
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





class Solution886Tony:
    def possibleBipartition(self, n: int, dislikes) -> bool:

        color = {}

        def bfs(queue):
            while queue:
                node, c = queue.popleft()
                for nei in graph[node]:
                    if nei not in color:
                        color[nei] = 1 - c
                        queue.append([nei, 1 - c])
                    else:
                        if color[node] == color[nei]:
                            return False

            return True

        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        for node in range(n):
            queue = deque()
            queue.append([node, 1])
            if node in color:
                continue
            if not bfs(queue):
                return False
        return True



