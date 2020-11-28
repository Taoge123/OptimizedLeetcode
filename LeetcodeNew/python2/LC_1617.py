"""
max diameter = d, what are the subtrees? -> constructive
Given a substree, what is its max diameter -> deterministic
(101100100)
1. start with any node A, find the farthest point B, w.r.t. A
   We claim B is one of the two points of the max diameter
2. start with B, find the farthest point C w.r.t B

the max diameter is B-> C

for subtree = ...:
    if (subtree is not connected):
        continue
    compute max diameter for this subtree
    count[max_diameter] += 1


"""

import collections

class Solution:
    def countSubgraphsForEachDiameter(self, n, edges):

        # Since cities form a tree so maximum distance between 2 cities always < n
        dist = [[float('inf')] * n for _ in range(n)]
        for u, v in edges:
            dist[u - 1][v - 1] = 1
            dist[v - 1][u - 1] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        res = [0] * (n - 1)
        for state in range(1, 2 ** n):
            d = self.maxDistance(state, dist, n)
            if d > 0:
                res[d - 1] += 1
        return res

    def maxDistance(self, state, dist, n):  # return: maximum distance between any two cities in our subset. O(n^2)
        edge, city_node, maxDist = 0, 0, 0
        for i in range(n):
            # Skip if city `i` not in our subset
            if (state >> i) & 1 == 0:
                continue
            city_node += 1
            for j in range(i + 1, n):
                # Skip if city_node `j` not in our subset
                if (state >> j) & 1 == 0:
                    continue
                edge += (dist[i][j] == 1) #?
                maxDist = max(maxDist, dist[i][j])
        # Subset form an invalid subtree!
        if edge != city_node - 1:
            return -1
        return maxDist



class SolutionBFS:
    def countSubgraphsForEachDiameter(self, n, edges):

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        res = [0] * (n - 1)
        for state in range(1, 2 ** n):
            d = self.maxDistance(graph, state, n)
            if d > 0:
                res[d - 1] += 1
        return res

    def bfs(self, graph, src, cities):
        visited = {src}
        queue = collections.deque([(src, 0)])  # Pair of (vertex, distance)
        maxDist = 0  # Farthest distance from src to other nodes
        while queue:
            node, dist = queue.popleft()
            # maxDist = dist
            for nei in graph[node]:
                if nei not in visited and nei in cities:
                    visited.add(nei)
                    queue.append((nei, dist + 1))
        return dist, visited

    def maxDistance(self, graph, state, n):  # return: maximum distance between any two cities in our subset. O(n^2)
        cities = set()
        for i in range(n):
            if (state >> i) & 1 == 1:
                cities.add(i)
        res = 0
        for i in cities:
            maxDist, visited = self.bfs(graph, i, cities)
            # Can't visit all nodes of the tree -> Invalid tree
            if len(visited) < len(cities):
                return 0
            res = max(res, maxDist)
        return res





n = 4
edges = [[1,2],[2,3],[2,4]]
a = Solution()
print(a.countSubgraphsForEachDiameter(n, edges))


