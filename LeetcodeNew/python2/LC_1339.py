class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionTony:
    def maxProduct(self, root):
        self.sum = 0
        self.res = float('-inf')
        self.findSum(root)
        self.dfs(root)
        return self.res % (10 ** 9 + 7)

    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        summ = left + right + node.val
        self.res = max(self.res, summ * (self.sum - summ))
        return left + right + node.val

    def findSum(self, node):
        if not node:
            return

        self.sum += node.val
        self.findSum(node.left)
        self.findSum(node.right)



class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        mod = 10 ** 9 + 7
        self.res = 0
        total = self.dfs(root, 0)
        self.dfs(root, total)
        return self.res % mod

    def dfs(self, node, total):
        if not node:
            return 0
        left = self.dfs(node.left, total)
        right = self.dfs(node.right, total)
        self.res = max(self.res, left * (total - left), right * (total - right))
        return left + right + node.val

