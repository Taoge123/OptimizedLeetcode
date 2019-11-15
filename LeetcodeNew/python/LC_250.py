"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return self.res
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return True

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left and right:
            if root.left and root.left.val != root.val:
                return False
            if root.right and root.right.val != root.val:
                return False

            self.res += 1
            return True

        return False







