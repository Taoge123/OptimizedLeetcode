
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, N: int):
        memo = {}
        memo[0] = []
        memo[1] = [TreeNode(0)]
        return self.dfs(N, memo)

    def dfs(self, N, memo):
        if N in memo:
            return memo[N]
        res = []
        for x in range(1, N - 1, 2):
            y = N - 1 - x
            for left in self.dfs(x, memo):
                for right in self.dfs(y, memo):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        memo[N] = res
        return memo[N]





