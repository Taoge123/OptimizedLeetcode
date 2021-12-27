
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionTony:
    def longestUnivaluePath(self, root):

        if not root:
            return 0

        self.res = float('-inf')
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if node.left and node.val == node.left.val:
            left += 1
        else:
            left = 0
        if node.right and node.val == node.right.val:
            right += 1
        else:
            right = 0

        self.res = max(self.res, left + right)

        return max(left, right)



class Solution:
    def longestUnivaluePath(self, root):
        self.ans = 0
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        l = r = 0
        if node.left and node.left.val == node.val:
            l = left + 1
        if node.right and node.right.val == node.val:
            r = right + 1
        self.ans = max(self.ans, l + r)
        return max(l, r)


class Solution2:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0
        self.helper(root, root.val)
        return self.res

    def helper(self, node, val):
        if not node:
            return 0

        left = self.helper(node.left, node.val)
        right = self.helper(node.right, node.val)

        self.res = max(self.res, left + right)
        if val == node.val:
            return max(left, right) + 1

        return 0

