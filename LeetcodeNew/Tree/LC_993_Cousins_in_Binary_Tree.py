
"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values,
and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
"""

"""
Intuition

Nodes are cousins if they have the same depth but different parents. 
A straightforward approach is to be able to know the parent and depth of each node.

Algorithm

We can use a depth-first search to annotate each node. 
For each node with parent par and depth d, we will record results in hashmaps: 
parent[node.val] = par and depth[node.val] = d.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    depth1 = 0
    parent = None

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return False
        self.countDepth(root, x, 0, None)
        x_depth, parent1 = self.depth1, self.parent
        self.countDepth(root, y, 0, None)
        y_depth, parent2 = self.depth1, self.parent
        return (x_depth == y_depth and parent1.val != parent2.val)

    def countDepth(self, root, val, depth, parent):
        if root is None:
            return
        if root.val == val:
            self.depth1 = depth
            self.parent = parent
        self.countDepth(root.left, val, depth + 1, root)
        self.countDepth(root.right, val, depth + 1, root)


class Solution2:
    def isCousins(self, root, x, y):
        parent = {}
        depth = {}
        def dfs(node, par = None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]








