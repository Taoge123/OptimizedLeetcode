import collections

class Solution1:
    def validTree(self, n, edges):
        parent = range(n)

        def find(x):
            return x if parent[x] == x else find(parent[x])

        def union(xy):
            x, y = map(find, xy)
            parent[x] = y
            return x != y

        return len(edges) == n - 1 and all(map(union, edges))


class Solution2:
    def validTree(self, n, edges):
        parent = range(n)

        def find(x):
            return x if parent[x] == x else find(parent[x])

        for e in edges:
            x, y = map(find, e)
            if x == y:
                return False
            parent[x] = y
        return len(edges) == n - 1



class Solution3:
    def validTree(self, n, edges):
        parent = range(n)

        def find(x):
            return x if parent[x] == x else find(parent[x])

        for e in edges:
            x, y = map(find, e)
            if x == y:
                return False
            parent[x] = y
        return len(edges) == n - 1


"""
Topological sort:
This solution looks like topological-sort, 
which iteratively removes the nodes with degree of 1.
--->
The base condition is that a single node with no edges is a tree. 
By induction, if the graph is a tree, with the leaves removed, 
the rest part of it is still a tree.

"""

class Solution:
    # @param {integer} n
    # @param {integer[][]} edges
    # @return {boolean}
    def validTree(self, n, edges):
        graph = {i:set() for i in range(n)}
        for p, q in edges:
            graph[p].add(q)
            graph[q].add(p)
        while len(graph) > 0:
            leaves = list()
            for node, neighbors in graph.iteritems():
                if len(neighbors) <= 1:
                    leaves.append(node)
            if len(leaves) == 0:
                return False # a cycle exists
            for n in leaves:
                if len(graph[n]) == 0:
                    # must be one connected component
                    return len(graph) == 1
                nei = graph[n].pop()
                graph[nei].remove(n)
                del graph[n]
        return True


from collections import defaultdict
class Solution3:
    def hasCycle(self,graph,parent,node,visited):
        visited.add(node)
        for v in graph[node]:
            if v != parent:
                if v in visited or self.hasCycle(graph,node,v,visited):
                    return True
        return False
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        visited = set()
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return not self.hasCycle(graph,-1,0,visited) and len(visited) == n


class Solution4:
    def validTree(self, n, edges):
        visited, adj = [0] * n, collections.defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        def dfs(i, pre):
            visited[i] = 1
            for v in adj[i]:
                if v != pre and (visited[v] or not dfs(v, i)):
                    return False
            return True
        return dfs(0, -1) and sum(visited) == n



