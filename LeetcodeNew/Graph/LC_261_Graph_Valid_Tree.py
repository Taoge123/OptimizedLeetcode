
"""

http://www.cnblogs.com/grandyang/p/5257919.html


Given n nodes labeled from 0 to n-1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check
whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

Note: you can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.


"""


"""
This solution looks like topological-sort, which iteratively removes the nodes with degree of 1.
The base condition is that a single node with no edges is a tree. 
By induction, if the graph is a tree, with the leaves removed, 
the rest part of it is still a tree.

下面我们来看BFS的解法，思路很相近，需要用queue来辅助遍历，
这里我们没有用一维向量来标记节点是否访问过，而是用了一个set，如果遍历到一个节点，
在set中没有，则加入set，如果已经存在，则返回false，还有就是在遍历邻接链表的时候，
遍历完成后需要将节点删掉，参见代码如下：

"""
import collections

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
            for node, neighbors in graph.items():
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


class Solution2:
    def validTree(self, n, edges):
        dic = {i: set() for i in range(n)}
        for i, j in edges:
            dic[i].add(j)
            dic[j].add(i)

        stack = [dic.keys()[0]]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for neighbour in dic[node]:
                stack.append(neighbour)
                dic[neighbour].remove(node)
            dic.pop(node)
        return not dic

"""
这道题给了我们一个无向图，让我们来判断其是否为一棵树，我们知道如果是树的话，所有的节点必须是连接的，
也就是说必须是连通图，而且不能有环，所以我们的焦点就变成了验证是否是连通图和是否含有环。
我们首先用DFS来做，根据pair来建立一个图的结构，用邻接链表来表示，
还需要一个一位数组v来记录某个节点是否被访问过，然后我们用DFS来搜索节点0，遍历的思想是，
当DFS到某个节点，先看当前节点是否被访问过，如果已经被访问过，说明环存在，直接返回false，
如果未被访问过，我们现在将其状态标记为已访问过，然后我们到邻接链表里去找跟其相邻的节点继续递归遍历，
注意我们还需要一个变量pre来记录上一个节点，以免回到上一个节点，这样遍历结束后，
我们就把和节点0相邻的节点都标记为true，然后我们在看v里面是否还有没被访问过的节点，如果有，
则说明图不是完全连通的，返回false，反之返回true
"""
#DFS
class Solution3:
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


class Solution4:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        visited = set()
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return not self.hasCycle(graph,-1,0,visited) and len(visited) == n

    def hasCycle(self,graph,parent,node,visited):
        visited.add(node)
        for v in graph[node]:
            if v != parent:
                if v in visited or self.hasCycle(graph,node,v,visited):
                    return True
        return False


#union Find
class Solution5:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        parent = [i for i in range(n)]
        for edge in edges:
            root1 = self.find(parent, edge[0])
            root2 = self.find(parent, edge[1])
            if root1 == root2:
                return False
            else:
                parent[root1] = root2
        return len(edges) == n - 1

    def find(self, parent, p):
        if parent[p] == p:
            return p
        else:
            return self.find(parent, parent[p])



