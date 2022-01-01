
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionTony:
    def maxAncestorDiff(self, root):
        self.res = 0
        self.dfs(root, root.val, root.val)
        return self.res

    def dfs(self, node, mini, maxi):
        if not node:
            self.res = max(self.res, abs(maxi - mini))
            return

        mini = min(mini, node.val)
        maxi = max(maxi, node.val)
        self.dfs(node.left, mini, maxi)
        self.dfs(node.right, mini, maxi)



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




