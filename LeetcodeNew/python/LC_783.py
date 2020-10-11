
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.prev = None
        self.res = float('inf')
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        if self.prev:
            self.res = min(self.res, root.val - self.prev)
        self.prev = root.val
        self.helper(root.right)


