

"""
https://www.geeksforgeeks.org/roots-tree-gives-minimum-height/

https://leetcode.com/problems/minimum-height-trees/discuss/216472/Follow-up-after-most-voted-post
https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts


For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree.
Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph,
write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1.
You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia:
“a tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


"""
"""
First let's review some statement for tree in graph theory:

(1) A tree is an undirected graph in which any two vertices are
connected by exactly one path.

(2) Any connected graph who has n nodes with n-1 edges is a tree.

(3) The degree of a vertex of a graph is the number of
edges incident to the vertex.

(4) A leaf is a vertex of degree 1. An internal vertex is a vertex of
degree at least 2.

(5) A path graph is a tree with two or more vertices that is not
branched at all.

(6) A tree is called a rooted tree if one vertex has been designated
the root.

(7) The height of a rooted tree is the number of edges on the longest
downward path between root and a leaf.
"""
import collections

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0]
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves


"""
基本思路是“逐层删去叶子节点，直到剩下根节点为止”

有点类似于拓扑排序

最终剩下的节点个数可能为1或者2

时间复杂度：O(n)，其中n为顶点的个数。
"""

class Solution2:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        children = collections.defaultdict(set)
        for s, t in edges:
            children[s].add(t)
            children[t].add(s)
        vertices = set(children.keys())
        while len(vertices) > 2:
            leaves = [x for x in children if len(children[x]) == 1]
            for x in leaves:
                for y in children[x]:
                    children[y].remove(x)
                del children[x]
                vertices.remove(x)
        return list(vertices) if n != 1 else [0]


"""
题解：

求给定图中，能形成树的最矮的树。第一直觉就是BFS，跟Topological Sorting的Kahn方法很类似，
利用无向图每个点的degree来计算。但是却后继无力，于是还是参考了Discuss中Dietpepsi和Yavinci大神的代码。

方法有两种，一种是先计算每个点的degree，然后将degree为1的点放入list或者queue中进行计算，
把这些点从neighbours中去除，然后计算接下来degree = 1的点。最后剩下1 - 2个点就是新的root

另外一种是用了类似给许多点，求一个点到其他点距离最短的原理。找到最长的一点leaf to leaf path，
然后找到这条path的一个或者两个中点median就可以了。
"""
"""
这道题虽然是树的题目，但是跟其最接近的题目是Course Schedule 课程清单和Course Schedule II 课程清单之二。
由于LeetCode中的树的题目主要都是针对于二叉树的，而这道题虽说是树但其实本质是想考察图的知识，
这道题刚开始在拿到的时候，我最先想到的解法是遍历的点，以每个点都当做根节点，算出高度，然后找出最小的，
但是一时半会又写不出程序来，于是上网看看大家的解法，发现大家推崇的方法是一个类似剥洋葱的方法，
就是一层一层的褪去叶节点，最后剩下的一个或两个节点就是我们要求的最小高度树的根节点，
这种思路非常的巧妙，而且实现起来也不难，跟之前那到课程清单的题一样，我们需要建立一个图g，
是一个二维数组，其中g[i]是一个一维数组，保存了i节点可以到达的所有节点。
我们开始将所有只有一个连接边的节点(叶节点)都存入到一个队列queue中，然后我们遍历每一个叶节点，
通过图来找到和其相连的节点，并且在其相连节点的集合中将该叶节点删去，如果删完后此节点也也变成一个叶节点了，
加入队列中，再下一轮删除。那么我们删到什么时候呢，当节点数小于等于2时候停止，
此时剩下的一个或两个节点就是我们要求的最小高度树的根节点啦"""

class Solution3:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        leaves = collections.defaultdict(set)
        for u, v in edges:
            leaves[u].add(v)
            leaves[v].add(u)
        que = collections.deque()
        for u, vs in leaves.items():
            if len(vs) == 1:
                que.append(u)
        while n > 2:
            _len = len(que)
            n -= _len
            for _ in range(_len):
                u = que.popleft()
                for v in leaves[u]:
                    leaves[v].remove(u)
                    if len(leaves[v]) == 1:
                        que.append(v)
        return list(que)















