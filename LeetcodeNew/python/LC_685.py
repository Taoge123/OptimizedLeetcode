"""
https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases
https://leetcode.com/problems/redundant-connection-ii/discuss/254733/Python-Union-Find-Clear-Logic
https://leetcode.com/problems/redundant-connection-ii/discuss/278105/topic
https://leetcode.com/problems/redundant-connection-ii/discuss/108045/C%2B%2BJava-Union-Find-with-explanation-O(n)
"""

import collections

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return False
        self.parent[x] = self.parent[y]
        return True


class SolutionCsp:
    def findRedundantDirectedConnection(self, edges):
        uf = UnionFind(len(edges) + 1)
        res1 = []
        res2 = []
        for u, v in edges:
            x = uf.find(u)
            y = uf.find(v)
            if y != v:
                res1 = [u, v]
            elif x == y:
                res2 = [u, v]
            else:
                uf.parent[y] = x

        if not res1:
            return res2
        if not res2:
            return res1

        for u, v in edges:
            if v == res1[1]:
                return [u, v]
        return [0, 0]


class SolutionDFS:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        children = collections.defaultdict(list)
        parent = collections.defaultdict(list)

        def dfs(node, target):
            if node == target:
                return True
            if node in visited:
                return False
            visited.add(node)
            for nei in children[node]:
                if dfs(nei, target):
                    return True
            return False

        # to mark the node with 2 parents
        node = -1
        for u, v in edges:
            children[u].append(v)
            parent[v].append(u)
            if len(parent[v]) == 2:
                node = v

        # if 2-parent case happened
        if node != -1:
            visited = set()
            # this node can reach its parent, then there is a cycle
            if dfs(node, parent[node][0]):
                return [parent[node][0], node]
            else:
                return [parent[node][1], node]
        # If there are multiple answers, return the answer that occurs last in the given 2D-array.
        # to find the last edge in the cycle
        for i in range(n - 1, -1, -1):
            v, u = edges[i]
            visited = set()
            if dfs(u, v):
                return [v, u]




class Solution:
    def findRedundantDirectedConnection(self, edges):
        cand1, cand2 = None, None
        point_to = {}
        for u, v in edges:
            if v in point_to:
                cand1 = point_to[v]
                cand2 = [u, v]
                break
            point_to[v] = [u, v]

        ds = UnionFind(len(edges))
        for u, v in edges:
            if [u, v] == cand2:
                continue
            if not ds.union(u - 1, v - 1):
                if cand1:
                    return cand1
                return [u, v]
        return cand2




class Solution2:
    def findRedundantDirectedConnection(self, edges):
        def find(u):  # union find
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]

        def detect_cycle(edge):  # check whether you can go from u to v (forms a cycle) along the parents
            u, v = edge
            while u != v and u in parents:
                u = parents[u]
            return u == v

        candidates = []  # stores the two edges from the vertex where it has two parents
        parents = {}
        for u, v in edges:
            if v not in parents:
                parents[v] = u
            else:
                candidates.append((parents[v], v))
                candidates.append((u, v))

        if candidates:  # case 2 & case 3 where one vertex has two parents
            return candidates[0] if detect_cycle(candidates[0]) else candidates[1]
        else:  # case 1, we just perform a standard union find, same as redundant-connection
            p = list(range(len(edges)))
            for edge in edges:
                u, v = map(find, edge)
                if u == v:
                    return edge
                p[u] = p[v]




