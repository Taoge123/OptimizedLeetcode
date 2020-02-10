






class UnionFindSet(object):
    def __init__(self):
        self.parents = range(1001)
        self.rank = [0] * 1001

    def find(self, val):
        """find with path compression"""
        if self.parents[val] != val:
            self.parents[val] = self.find(self.parents[val])
        return self.parents[val]

    def union(self, v1, v2):
        """union by rank, check whether union two vertics will lead to a cycle"""
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return True
        elif self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parents[p1] = p2
        else:
            self.rank[p2] += 1
            self.parents[p1] = p2
        return False


class SolutionBest:
    def findRedundantDirectedConnection(self, edges):
        redundant_edges = None
        count = {}
        for e in edges:
            if e[1] not in count:
                count[e[1]] = []
            count[e[1]].append(e)
            if len(count[e[1]]) == 2:
                redundant_edges = count[e[1]]
                break

        if redundant_edges:
            ufs = UnionFindSet()
            for edge in edges:
                if edge == redundant_edges[1]:
                    continue
                if ufs.union(edge[0], edge[1]):
                    return redundant_edges[0]
            return redundant_edges[1]
        else:
            ufs = UnionFindSet()
            for edge in edges:
                if ufs.union(edge[0], edge[1]):
                    return edge


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




