import collections

class Solution:
    def leadsToDestination(self, n: int, edges, source: int, destination: int) -> bool:

        graph = collections.defaultdict(set)
        visited = collections.defaultdict(int)

        for x, y in edges:
            graph[x].add(y)

        def dfs(node):
            if visited[node] == 1:
                return True

            elif visited[node] == -1:
                return False

            # if no neighbors anymore, check if we already arrived
            elif len(graph[node]) == 0:
                return node == destination

            else:
                visited[node] = -1
                for nei in graph[node]:
                    if not dfs(nei):
                        return False
                visited[node] = 1
                return True

        return dfs(source)

