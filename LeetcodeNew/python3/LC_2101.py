import collections


class SolutionDFS:
    def maximumDetonation(self, bombs):

        n = len(bombs)
        graph = collections.defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                dx = bombs[i][0] - bombs[j][0]
                dy = bombs[i][1] - bombs[j][1]
                if bombs[i][2] ** 2 >= dx ** 2 + dy ** 2:
                    graph[i].append(j)

        def dfs(node):
            for nei in graph[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                dfs(nei)

        res = 0
        for node in range(n):
            visited = set()
            visited.add(node)
            dfs(node)
            res = max(res, len(visited))
        return res




class SolutionBFS:
    def maximumDetonation(self, bombs):

        n = len(bombs)
        graph = collections.defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                dx = bombs[i][0] - bombs[j][0]
                dy = bombs[i][1] - bombs[j][1]
                if bombs[i][2] ** 2 >= dx ** 2 + dy ** 2:
                    graph[i].append(j)

        def bfs(queue):
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    queue.append(nei)

        res = 0
        for node in range(n):
            visited = set()
            visited.add(node)
            queue = collections.deque()
            queue.append(node)
            bfs(queue)
            res = max(res, len(visited))
        return res


