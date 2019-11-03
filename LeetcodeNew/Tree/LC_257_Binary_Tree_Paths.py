
"""
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

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        return self.dfs(root, [], '')

    def dfs(self, root, res, path):

        if not root:
            return
        if root and (not root.left and not root.right):
            res.append(path + str(root.val))

        self.dfs(root.left, res, path + str(root.val) + '->')
        self.dfs(root.right, res, path + str(root.val) + '->')
        return res







