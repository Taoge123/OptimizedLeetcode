
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getLonelyNodes(self, root: TreeNode):
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return

        if root.left and not root.right:
            res.append(root.left.val)

        if not root.left and root.right:
            res.append(root.right.val)

        self.dfs(root.left, res)
        self.dfs(root.right, res)



