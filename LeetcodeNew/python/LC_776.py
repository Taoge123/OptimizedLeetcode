
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def splitBST(self, root: TreeNode, V: int):
        if not root:
            return [None, None]
        elif root.val > V:
            res = self.splitBST(root.left, V)
            root.left = res[1]
            res[1] = root
            return res
        else:
            res = self.splitBST(root.right, V)
            root.right = res[0]
            res[0] = root
            return res


