import collections

class Solution:
    def maximumDetonation(self, bombs):

        n = len(bombs)
        graph = collections.defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
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




