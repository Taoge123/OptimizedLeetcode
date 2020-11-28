
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.dfs(root, root.val, root.val)

    def dfs(self, root, maxi, mini):
        if not root:
            return maxi - mini

        maxi = max(maxi, root.val)
        mini = min(mini, root.val)

        left = self.dfs(root.left, maxi, mini)
        right = self.dfs(root.right, maxi, mini)

        return max(left, right)

