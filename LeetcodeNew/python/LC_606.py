class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""

        if not t.left and not t.right:
            return str(t.val) + ""

        if not t.right:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"

        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"


