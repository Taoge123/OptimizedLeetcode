
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, p, q):
        if p and q:
            return p.val == q.val and self.dfs(p.left, q.right) and self.dfs(p.right, q.left)

        return p == q





