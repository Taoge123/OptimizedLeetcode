
"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class SolutionTony:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.res = float('-inf')
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.res = max(self.res, left + right)

        return max(left, right) + 1



class Solution:
    def diameterOfBinaryTree(self, root) -> int:

        if not root:
            return 0
        self.res = float('-inf')
        self.dfs(root)
        return self.res - 1

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.res = max(self.res, left + right + 1)
        return max(left, right) + 1









