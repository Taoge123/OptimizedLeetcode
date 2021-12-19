
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.count = 0
        self.dfs(root, p, q)
        print(self.count)
        if self.count == 2:
            return self.dfs(root, p, q)
        return None

    def dfs(self, root, p, q):
        if not root:
            return None

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if root == p or root == q:
            self.count += 1
            return root

        if left and right:
            return root
        if left or right:
            return left or right
        if not left and not right:
            return None




