"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


class Solution1:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if not root.left or not root.right:
            return max(left, right) + 1

        return min(left, right) + 1



