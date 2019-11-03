
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        if not root:
            return 0
        self.res = float('inf')
        self.pre = None
        self.helper(root)
        return self.res

    def helper(self, root):

        if not root:
            return

        self.helper(root.left)
        if self.pre:
            self.res = min(root.val - self.pre.val, self.res)
        self.pre = root
        self.helper(root.right)








