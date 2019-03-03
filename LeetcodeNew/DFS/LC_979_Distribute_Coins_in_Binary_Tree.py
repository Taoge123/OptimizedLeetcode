"""
Solution 1
Quite similar problem as this one 968.Binary Tree Cameras.
So I put this as the first solution.
Write a dfs helper, return the number of coins given to the parent.

"""

class SolutionLee1:
    res = 0
    def distributeCoins(self, root):
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res += abs(left) + abs(right)
            return root.val + left + right - 1

        dfs(root)
        return self.res



class Solution:
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans

# Give the parent node so we can move the coins to the parent directly.
class SolutionLee3:
    def distributeCoins(self, root, pre=None):
        if not root: return 0
        res = self.distributeCoins(root.left, root) + self.distributeCoins(root.right, root)
        if pre: pre.val += root.val - 1
        return res + abs(root.val - 1)









