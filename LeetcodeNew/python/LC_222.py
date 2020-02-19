"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        left = self.helper(root, True)
        right = self.helper(root, False)
        if left == right:
            return (1 << left) - 1

        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def leftDepth(self, root):
        res = 0
        while root:
            res += 1
            root = root.left
        return res

    def rightDepth(self, root):
        res = 0
        while root:
            res += 1
            root = root.right
        return res

    def helper(self, root, isLeft):
        if not root:
            return 0
        return self.helper(root.left, isLeft) + 1 if isLeft else self.helper(root.right, isLeft) + 1

