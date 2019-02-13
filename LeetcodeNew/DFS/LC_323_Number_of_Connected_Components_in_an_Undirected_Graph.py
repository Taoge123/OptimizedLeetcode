
#UNion Find

class Solution0:
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


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.size = [1] * n
        self.id = range(n)

    def find(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        idp, idq = map(self.find, (p, q))
        if idp == idq:
            return

        less, more = (
            (idp, idq) if self.size[idp] < self.size[idq] else (idq, idp))

        self.id[less] = self.id[more]
        self.size[more] += self.size[less]

        self.count -= 1


class Solution1:
    def countComponents(self, n, edges):
        unionFind = UnionFind(n)
        [unionFind.union(*e) for e in edges]
        return unionFind.count

"""-------------------------------------------------------------------------------------------"""

class Solution3:
    def countComponents(self, n, edges):
        count = n
        parent = range(n)
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] # path compression
                x = parent[x]
            return x
        for e in edges:
            x,y = map(find, e)
            if x != y:
                parent[x] = y
                count -= 1
        return count

"""
Depth First Search: O(V+E)

Build a graph using the list of edges. 
Maintain a set called visited to track the nodes which have been visited so far.
Iterate through all vertices and call DFS on each unvisited vertex. 
The DFS on that vertex will mark all reachable nodes with that vertex. 
That constitutes a component abd we increment the count for components.
"""


class G:
    def __init__(self, n, edges):
        self.nbr = {}
        for i in range(n):
            self.nbr[i] = []
        for edge in edges:
            u, v = edge[0], edge[1]
            self.nbr[u].append(v)
            self.nbr[v].append(u)
        return

    def adj(self, u):
        return self.nbr[u]


class Solution2:
    def dfs(self, v, visited, g):
        visited.add(v)
        for nbr in g.adj(v):
            if nbr not in visited:
                self.dfs(nbr, visited, g)
        return

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        g = G(n, edges)
        visited = set([])
        components = 0
        for v in range(n):
            if v not in visited:
                self.dfs(v, visited, g)
                components += 1
        return components

class SolutionDFS:
    def countComponents(n, edges):
        def dfs(n, g, visited):
            if visited[n]:
                return
            visited[n] = 1
            for x in g[n]:
                dfs(x, g, visited)

        visited = [0] * n
        g = {x: [] for x in range(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ret = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, g, visited)
                ret += 1

        return ret








