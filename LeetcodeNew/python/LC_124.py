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




