class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def equalToDescendants(self, root) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):

        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if left + right == node.val:
            self.res += 1

        return node.val + left + right



