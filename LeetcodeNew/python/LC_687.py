
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0
        self.helper(root, root.val)
        return self.res

    def helper(self, node, val):
        if not node:
            return 0

        left = self.helper(node.left, node.val)
        right = self.helper(node.right, node.val)

        self.res = max(self.res, left + right)
        if val == node.val:
            return max(left, right) + 1

        return 0

