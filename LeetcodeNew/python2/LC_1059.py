import collections


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        visited = [0 for i in range(n)]
        return self.dfs(graph, source, destination, visited)

    def dfs(self, graph, node, target, visited):
        if visited[node] == 1:
            return True
        if visited[node] == -1:
            return False

        # at last step, if we didnt reach target, then this path wont reach target node
        if len(graph[node]) == 0:
            return node == target

        visited[node] = -1
        for nei in graph[node]:
            if not self.dfs(graph, nei, target, visited):
                return False
        visited[node] = 1
        return True



