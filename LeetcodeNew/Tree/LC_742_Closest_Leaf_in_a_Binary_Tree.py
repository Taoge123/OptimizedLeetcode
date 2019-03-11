
"""
https://leetcode.com/problems/closest-leaf-in-a-binary-tree/discuss/109934/Intuitive-Python-O(n)-BFS-on-Undirected-Graph


Given a binary tree where every node has a unique value,
and a target key k, find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled
on the binary tree to reach any leaf of the tree.
Also, a node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row.
The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.

"""

"""
Intuition

Instead of a binary tree, if we converted the tree to a general graph, 
we could find the shortest path to a leaf using breadth-first search.

Algorithm

We use a depth-first search to record in our graph each edge travelled from parent to node.

After, we use a breadth-first search on nodes that started with a value of k, 
so that we are visiting nodes in order of their distance to k. 
When the node is a leaf (it has one outgoing edge, 
where the root has a "ghost" edge to null), it must be the answer.
这道题对指定的target k和叶子节点的定义可以理解是一个无向图里面找寻k节点最近的邻居(这个邻居要满足是叶子节点的条件)

有了以上思路，先Preorder扫一遍Tree，然后创建一个图，具体参考子方程dfs，期间记住存储以下叶子节点，
方便与之后处理邻居满足叶子节点这一返回条件

当图建立好了以后，在图里面进行遍历，如果找到的邻居也满足叶子条件的话，返回即可。


"""
import collections




class Solution0:
    def findClosestLeaf(self, root, k):
        from collections import defaultdict
        self.res = None
        self.dic, self.leaves = defaultdict(list), set()
        self.dfs(root)
        self.bfs(k)
        return self.res

    def dfs(self, root):
        '''Preorder through the Tree and construct graph'''
        if not root: return
        if not root.left and not root.right:
            self.leaves.add(root.val)
            return
        if root.left:
            self.dic[root.val].append(root.left.val)
            self.dic[root.left.val].append(root.val)
            self.dfs(root.left)
        if root.right:
            self.dic[root.val].append(root.right.val)
            self.dic[root.right.val].append(root.val)
            self.dfs(root.right)

    def bfs(self, k):
        '''Find the closest neighbor of k that is also a leaf'''
        q = [k]
        while q:
            new_q = []
            for node in q:
                if node in self.leaves:
                    self.res = node
                    return
                new_q += self.dic.pop(node, [])
            q = new_q





class Solution1:
    def findClosestLeaf(self, root, k):
        graph = collections.defaultdict(list)
        def dfs(node, par = None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        queue = collections.deque(node for node in graph
                                  if node and node.val == k)
        seen = set(queue)

        while queue:
            node = queue.popleft()
            if node:
                if len(graph[node]) <= 1:
                    return node.val
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)


"""
Say from each node, we already knew where the closest leaf in it's subtree is. 
Using any kind of traversal plus memoization, we can remember this information.

Then the closest leaf to the target (in general, not just subtree) 
has to have a lowest common ancestor with the target that is on the path 
from the root to the target. We can find the path from root to target via any kind of traversal, 
and look at our annotation for each node on this path to determine all leaf candidates, 
choosing the best one.
"""







class Solution2:
    def findClosestLeaf(self, root, k):
        annotation = {}
        def closest_leaf(root):
            if root not in annotation:
                if not root:
                    ans = float('inf'), None
                elif not root.left and not root.right:
                    ans = 0, root
                else:
                    d1, leaf1 = closest_leaf(root.left)
                    d2, leaf2 = closest_leaf(root.right)
                    ans = min(d1, d2) + 1, leaf1 if d1 < d2 else leaf2
                annotation[root] = ans
            return annotation[root]

        #Search for node.val == k
        path = []
        def dfs(node):
            if not node:
                return
            if node.val == k:
                path.append(node)
                return True
            path.append(node)
            ans1 = dfs(node.left)
            if ans1: return True
            ans2 = dfs(node.right)
            if ans2: return True
            path.pop()

        dfs(root)
        dist, leaf = float('inf'), None
        for i, node in enumerate(path):
            d0, leaf0 = closest_leaf(node)
            d0 += len(path) - 1 - i
            if d0 < dist:
                dist = d0
                leaf = leaf0

        return leaf.val



class Solution3:
    def findClosestLeaf(self, root, k):
        self.key = None
        adj = collections.defaultdict(list)
        def recurse(node):
                if node.val == k:
                    self.key = node
                if node.left:
                    adj[node].append(node.left)
                    adj[node.left].append(node)
                    recurse(node.left)
                if node.right:
                    adj[node].append(node.right)
                    adj[node.right].append(node)
                    recurse(node.right)
        recurse(root)
        visited = set()
        q = collections.deque()
        q.append(self.key)
        while q:
            node = q.popleft()
            if node not in visited:
                if not node.left and not node.right:
                    return node.val
                visited.add(node)
                for neighbor in adj[node]:
                    q.append(neighbor)





