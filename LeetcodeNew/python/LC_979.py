
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root):
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        # 输出输入经过node的总和
        self.res += abs(left) + abs(right)
        # 当前node能否消化输出输入
        return left + right + root.val - 1



