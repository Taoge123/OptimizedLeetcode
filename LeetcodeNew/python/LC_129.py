
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        return self.helper(root, 0)

    def helper(self, root, res):
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val + res * 10

        return self.helper(root.left, res * 10 + root.val) + self.helper(root.right, res * 10 + root.val)






