"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes
from some starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return

        self.res = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)
        self.res = max(self.res, root.val + left + right)
        return max(left, right) + root.val




