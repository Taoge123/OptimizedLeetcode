"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        queue, res = collections.deque([root]), []
        while queue:
            res.append(queue[-1].val)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

class Solution1:
    def rightSideView(self, root):
        self.res = []
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, depth):
        if not root:
            return

        if depth >= len(self.res):
            self.res.append(root.val)

        self.dfs(root.right, depth + 1)
        self.dfs(root.left, depth + 1)











