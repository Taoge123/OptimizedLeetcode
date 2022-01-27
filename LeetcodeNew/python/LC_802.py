
import collections


class SolutionTony:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        visited = [0 for _ in range(n)]

        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True

            visited[node] = -1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node] = 1
            return True

        res = []
        for node in range(n):
            if dfs(node):
                res.append(node)
        return res




class SolutionBFS:
    def eventualSafeNodes(self, graph):
        res = []
        if not graph:
            return res

        degree = [0] * len(graph)
        table = collections.defaultdict(set)

        for node in range(len(graph)):
            for nei in graph[node]:
                table[nei].add(node)
                degree[node] += 1

        res = set()
        queue = collections.deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                res.add(i)
                queue.append(i)

        while queue:
            node = queue.popleft()
            res.add(node)
            if node in table:
                for nei in table[node]:
                    degree[nei] -= 1
                    if degree[nei] == 0:
                        queue.append(nei)

        return sorted(list(res))



