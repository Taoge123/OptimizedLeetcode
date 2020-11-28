
"""
https://www.youtube.com/watch?v=JI4OPKSu7f4
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float('-inf'))

    def dfs(self, root, maxi):
        res = int(root.val >= maxi)
        if root.left:
            res += self.dfs(root.left, max(maxi, root.val))

        if root.right:
            res += self.dfs(root.right, max(maxi, root.val))

        return res




