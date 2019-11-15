"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        return self.dfs(root, [], '')

    def dfs(self, root, res, path):

        if not root:
            return
        if root and (not root.left and not root.right):
            res.append(path + str(root.val))

        self.dfs(root.left, res, path + str(root.val) + '->')
        self.dfs(root.right, res, path + str(root.val) + '->')
        return res




