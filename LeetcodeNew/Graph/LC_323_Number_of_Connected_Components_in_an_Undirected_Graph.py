
"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0]
and thus will not appear together in edges.
"""

#DFS
import collections
class SolutionDFS:
    def countComponents(n, edges):
        def dfs(n, graph, visited):
            if visited[n]:
                return
            visited[n] = 1
            for x in graph[n]:
                dfs(x, graph, visited)

        visited = [0] * n
        graph = {x: [] for x in range(n)}
        #graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        ret = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, graph, visited)
                ret += 1

        return ret


class SolutionBFS:
    def countComponents(n, edges):
        g = {x: [] for x in range(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ret = 0
        for i in range(n):
            queue = [i]
            ret += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]

        return ret


class SolutionUF:
    def countComponents(n, edges):
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(xy):
            x, y = map(find, xy)
            if rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1

        parent, rank = range(n), [0] * n
        map(union, edges)
        return len({find(x) for x in parent})












