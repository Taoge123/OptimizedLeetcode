import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder):
        self.idx = 0
        n = len(preorder)

        def dfs(lower, upper):
            if self.idx == n:
                return None

            val = preorder[self.idx]
            if val < lower or val > upper:
                return None

            self.idx += 1
            root = TreeNode(val)
            root.left = dfs(lower, val)
            root.right = dfs(val, upper)
            return root

        return dfs(-math.inf, math.inf)



