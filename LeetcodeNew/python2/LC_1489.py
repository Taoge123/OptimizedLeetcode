class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
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
    def __init__(self, N: int):
        # initially, every node forms a partition of size 1
        self.parent = list(range(N))  # the partition to which every node belongs
        self.size = [1] * N           # the size of ...

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, i: int, j: int) -> bool:
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.size[y] = self.size[x]
        return True

    def size(self, x: int) -> int:
        return self.size[self.find(x)]


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





