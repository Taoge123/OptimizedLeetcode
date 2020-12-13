"""
Its a simple BFS, with additional constraint of having alternate colored edges in path.
By navigating the paths, and remembering which colored edge we came from, the next set of edges are chosen with the opposite color.

The implicit visited set, is composed of edges (not Nodes), so every time i traverse an edge, i remove it from the graph.


"""

import collections


class SolutionTony:
    def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):
        res = [-1] * n
        visited = {(0, 'inf')}
        graph = [[] for _ in range(n)]
        for u, v in red_edges:
            graph[u].append((v, 1))
        for u, v in blue_edges:
            graph[u].append((v, -1))

        queue = collections.deque()
        queue.append((0, 'inf'))
        step = 0
        while queue:
            size = len(queue)
            # print(queue)
            for i in range(size):
                node, color = queue.popleft()
                if res[node] == -1:
                    res[node] = step
                for nei, nei_color in graph[node]:
                    if nei_color != color and (nei, nei_color) not in visited:
                        queue.append((nei, nei_color))
                        visited.add((nei, nei_color))
            step += 1
        return res


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):

        graph = collections.defaultdict(lambda: collections.defaultdict(set))
        red, blue = 0, 1

        for u, v in red_edges:
            graph[u][red].add(v)

        for u, v in blue_edges:
            graph[u][blue].add(v)

        res = [float('inf')] * n

        queue = collections.deque()
        queue.append([0, red])
        queue.append([0, blue])

        step = 0

        while queue:
            size = len(queue)
            for i in range(size):
                node, color = queue.popleft()
                newColor = 1 - color
                res[node] = min(step, res[node])
                neighbors = graph[node][newColor]
                for nei in list(neighbors):
                    graph[node][newColor].remove(nei)
                    queue.append([nei, newColor])
            step += 1
        return [node if node != float('inf') else -1 for node in res]




