class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.dfs(root, None, None)

    def dfs(self, root, p, gp):
        if not root:
            return 0

        left = self.dfs(root.left, root, p)
        right = self.dfs(root.right, root, p)
        if p and gp and gp.val % 2 == 0:
            return root.val + left + right
        else:
            return left + right


