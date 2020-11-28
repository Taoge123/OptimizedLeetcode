import heapq
import collections


class SolutionPrim:
    def minCostConnectPoints(self, points) -> int:
        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        res = 0
        n = len(points)
        visited = set()
        vertices = [(0, 0, 0)]

        while len(visited) < n:
            w, u, v = heapq.heappop(vertices)
            if u in visited and v in visited:
                continue
            res += w
            visited.add(v)
            for nei in range(n):
                if nei not in visited and nei != v:
                    heapq.heappush(vertices, (manhattan(points[nei], points[v]), v, nei))
        return res



class SolutionPrim2:
    def minCostConnectPoints(self, points) -> int:
        graph = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i].append((abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1]), j))

        heap = [(0, 0)]
        res = 0
        visited = set()
        while heap:
            weight, dest = heapq.heappop(heap)
            if dest in visited:
                continue
            res += weight
            visited.add(dest)

            for cost, nei in graph[dest]:
                if nei not in visited:
                    heapq.heappush(heap, (cost, nei))

        return res




class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.rank[x] += self.rank[y]
        else:
            self.parent[x] = y
            self.rank[y] += self.rank[x]

    def find(self, i):
        if self.parent[i] == i:
            return self.parent[i]
        return self.find(self.parent[i])




class SolutionKruskal:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        # sort based on cost (i.e. distance)
        edges.sort()
        # using Kruskal's algorithm to find the cost of Minimum Spanning Tree
        res = 0
        uf = UnionFind(n)
        for cost, u, v in edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                res += cost
        return res





