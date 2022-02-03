import collections


class Solution:
    def validPath(self, n: int, edges, source, destination):

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = set()
        def dfs(node, target):
            if node == target:
                return True
            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:
                if dfs(nei, target):
                    return True
            return False

        return dfs(source, destination)




