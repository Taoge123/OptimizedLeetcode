
"""
684. Redundant Connection 这道题目实际上就是要找到一个无向图中形成环路的最后那条边
(输入保证了所有边会形成回路)。首先，看一种最简单的解决方法
这种方法中每次 Find 的时间复杂度为 O(1)（即 parents[v1] 操作）, 每次 Union 则需要遍历所有的点，
时间复杂度是 O(n)，总体时间复杂度是 O(mn), m 为边的数目，而 n 为点的数目。

而我们也可以改变思路，就是进行 Union 操作时不再将某个连通分量中所有点的 parent 改为另一个连通分量的 parent，
而是只改变那个连通分量的代表；这样进行 Find 操作的时候只需要递归的查找即可，下面为这种思路对应的代码

"""


class Solution:
    def findRedundantConnection(self, edges):
        parents = range(1001)
        for edge in edges:
            v1, v2 = edge[0], edge[1]
            if parents[v1] == parents[v2]:
                return edge
            tmp = parents[v2]
            for i in range(len(parents)):
                if parents[i] == tmp:
                    parents[i] = parents[v1]
        return None


class UnionFindSet(object):
    def __init__(self):
        self.parents = range(1001)

    def find(self, val):
        if self.parents[val] != val:
            return self.find(self.parents[val])
        else:
            return self.parents[val]

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return True
        else:
            self.parents[p1] = p2
            return False


class Solution2:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ufs = UnionFindSet()
        for edge in edges:
            if ufs.union(edge[0], edge[1]):
                return edge



#Path compression

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


class Solution3(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ufs = UnionFindSet()
        for edge in edges:
            if ufs.union(edge[0], edge[1]):
                return edge
