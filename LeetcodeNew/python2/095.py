
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, start, end):
        res = []
        if start > end:
            res.append(None)

        for rootVal in range(start, end + 1):
            for left in self.dfs(start, rootVal - 1):
                for right in self.dfs(rootVal + 1, end):
                    root = TreeNode(rootVal)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res










