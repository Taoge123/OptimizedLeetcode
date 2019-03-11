
"""
Directed graph

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3




Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3


https://leetcode.com/problems/redundant-connection-ii/discuss/108058/one-pass-disjoint-set-solution-with-explain
https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases

This problem is very similar to "Redundant Connection".
But the description on the parent/child relationships is much better clarified.

There are two cases for the tree structure to be invalid.
1) A node having two parents;
   including corner case: e.g. [[4,2],[1,5],[5,2],[5,3],[2,4]]
2) A circle exists
If we can remove exactly 1 edge to achieve the tree structure,
a single node can have at most two parents. So my solution works in two steps.

1) Check whether there is a node having two parents.
    If so, store them as candidates A and B, and set the second edge invalid.
2) Perform normal union find.
    If the tree is now valid
           simply return candidate B
    else if candidates not existing
           we find a circle, return current edge;
    else
           remove candidate A instead of B.

解题方法: 并查集
上一次看这个题的时候，我知道使用并查集去做，但是并没有做出来。这次再次心平气和的看的时候，已经能一遍写出来了。

关于并查集，这个知识点有点大。简而言之，告诉你一条边，去集合里查找这条边的两个节点分别属于哪个树。
根据是否属于同一个树，做后续的判断。我之前的一篇文章讲述了并查集的一种应

下面的代码实现了并查集查找根节点的代码，并且做了路径压缩，防止树太高导致查找根节点缓慢。

具体到这个题，虽然说是返回最后一个边，但我们知道只需要去除一条边就够了，之前的边不会构成环，直至多余的那条边出现。

另外要注意，当一条边的左右节点的根节点不同时，要把他们设置相同，这样等下次判断某条边的左右节点相同的情况时，
说明是多余的那条边了。
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/80487064
版权声明：本文为博主原创文章，转载请附上博文链接！
"""


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = [-1] * (len(edges) + 1)
        for edge in edges:
            a = self.findRoot(edge[0], tree)
            b = self.findRoot(edge[1], tree)
            if a != b:
                tree[a] = b
            else:
                return edge

    def findRoot(self, x, tree):
        if tree[x] == -1:
            return x
        else:
            root = self.findRoot(tree[x], tree)
            tree[x] = root
            return root

"""
给定二维数组edges表示的一棵“树”。二维数组的每个元素[u, v]表示v是u的孩子。

树中多余一条边，在edges中恰好移除一条边，可以使得剩余边组成一棵没有环的树。

求移除的边，若存在多种答案，移除在edges中顺序靠后的那一条。

"""

class UnionFind:
    def __init__(self, n):
        self.set = range(n)

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution2:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        cand1, cand2 = [], []
        parent = {}
        for edge in edges:
            if edge[1] not in parent:
                parent[edge[1]] = edge[0]
            else:
                cand1 = [parent[edge[1]], edge[1]]
                cand2 = edge

        union_find = UnionFind(len(edges)+1)
        for edge in edges:
            if edge == cand2:
                continue
            if not union_find.union_set(*edge):
                return cand1 if cand2 else edge
        return cand2


class Solution3:
    def union(self, a, b):
        self.uf[self.find(b)] = self.find(a)

    def find(self, a):
        while self.uf[a] != a:
            a = self.uf[a]
        return self.uf[a]

    def detectCycle(self, V):
        self.visited[V] = True
        for i in range(len(self.adjList[V])):
            nextV = self.adjList[V][i]
            if self.visited[nextV]:
                return (V, nextV)
            ret = self.detectCycle(nextV)
            if ret[0]:
                return ret
        return (None, None)

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.uf = [0] + [i + 1 for i in range(len(edges))]
        self.adjList = [[] for i in range(len(edges) + 1)]  # Adjancency List
        hasFather = [False] * (len(edges) + 1)  # Whether a vertex has already got a parent
        criticalEdge = None

        for i, edge in enumerate(edges):
            w, v = edge[0], edge[1]
            self.adjList[w].append(v)
            if hasFather[v]:
                criticalEdge = (w, v)  # If a vertex has more than one parent, record the last edge
            hasFather[v] = True
            if self.find(w) == self.find(v):  # If a loop is found, record the edge that occurs last
                cycleEdge = (w, v)
            self.union(w, v)

        if not criticalEdge:  # Case 1
            return cycleEdge
        self.visited = [False] * (len(edges) + 1)
        (w, v) = self.detectCycle(criticalEdge[1])
        return (w, v) if w else criticalEdge


class Solution4:
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


"""--------------------------------------------------------------------------------"""
"""
685. Redundant Connection II 从前面的无向图升级到了有向图，
对应的要求从原来的仅要求不形成环路升级到在不形成环路的基础上，拓扑必须要是一棵合法树，
也就是每个点只能有一个父节点，例如 [[2,1],[3,1]] 这两条边虽然没有形成环路，但是 1 有两个父亲节点（2和3），因此不是一棵合法的树。

由于题目说明了输入只有一条不合法的边，因此首先可以统计一下这些边中是否存在某个点有两个父亲节点，
假如有，则需要移除的边必定为连着这个点的两条边中的一条，通过上面 Union-find 的方法，
可以判断出假如移除掉连着这个点的第一条边时，是否会形成回路。如果会，则说明需要移除第二条边，
否则直接移除第一条边。 如果统计的结果中没有点含有两个父亲节点，
那么可以直接通过第一题的方法直接找到形成回路的最后那条边
"""


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
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
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







