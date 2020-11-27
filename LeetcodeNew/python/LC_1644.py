
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.count = 0
        res = self.dfs(root, p, q)
        if self.count == 2:
            return res
        else:
            return None

    def dfs(self, root, p, q):
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            self.count += 1

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if root.val == p.val or root.val == q.val:
            return root

        if left and right:
            return root

        if left and not right:
            return left

        if not left and right:
            return right

        if not left and not right:
            return None


