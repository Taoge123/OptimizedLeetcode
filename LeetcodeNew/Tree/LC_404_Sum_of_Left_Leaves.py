
"""
Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return

        if root.left and not root.left.left and not root.left.right:
            self.res += root.left.val

        self.helper(root.left)
        self.helper(root.right)



