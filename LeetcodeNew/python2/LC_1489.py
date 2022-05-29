"""
https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solution/python3-kruskalbing-cha-ji-by-smiletm-jt9y/
https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solution/python-zui-xiao-sheng-cheng-shu-bing-cha-4zrw/
https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solution/yi-xu-xi-nan-yu-shang-qing-tian-by-lu-sh-ncft/



"""

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges):
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def kruskal(edges, edge=None, isUse=False):
            parent = {i: i for i in range(n)}
            res = 0
            if edge and isUse:
                # first connect edge
                u, v, cost = edge
                parent[u] = v
                res += cost

            for u, v, cost in sorted(edges, key=lambda x: x[2]):
                if edge and [u, v, cost] == edge:
                    continue

                x = find(parent, u)
                y = find(parent, v)
                if x == y:
                    continue
                # do not forgot this
                parent[x] = y
                res += cost
            count = len(set([find(parent, x) for x in parent]))
            return res if count == 1 else (2 ** 31 - 1)

        minWeight = kruskal(edges)

        criticalList, noncritical = [], []

        for i in range(len(edges)):
            # remove edges[i] from edges and run mst algorithm again and check if the weight is larger, if larger, current edge is "critical"
            edges2 = edges[:i] + edges[i + 1:]
            mstweight = kruskal(edges2, edges[i], isUse=False)

            if mstweight > minWeight:
                criticalList.append(i)  # i is the index for current edge!
            else:
                # must use edges[i] and check if the result weight is same with the best weight, if yes, this is a noncritical!
                mstweight2 = kruskal(edges2, edges[i], isUse=True)
                if mstweight2 == minWeight:
                    noncritical.append(i)
        return [criticalList, noncritical]


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1
        return True


class Solution2:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges):
        edges = sorted((w, u, v, i) for i, (u, v, w) in enumerate(edges))
        critical, non_critical = [], []
        for iw, iu, iv, i in edges:
            dsu1 = UnionFind(n)
            dsu2 = UnionFind(n)
            dsu1.union(iu, iv)
            s1, s2 = iw, 0
            for w, u, v, j in edges:
                if i == j:
                    continue
                if dsu1.union(u, v):
                    s1 += w
                if dsu2.union(u, v):
                    s2 += w
            if s1 == s2:
                non_critical.append(i)
            elif s1 < s2 or dsu2.union(iu, iv):
                critical.append(i)

        return [critical, non_critical]





