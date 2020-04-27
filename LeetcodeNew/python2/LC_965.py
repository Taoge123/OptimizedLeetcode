
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def isUnivalTree(self, root: TreeNode) -> bool:
        res = []
        self.helper(root, res)
        return len(set(res)) == 1

    def helper(self, root, res):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)


class Solution2:
    def isUnivalTree(self, root):
        left = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))

        right = (not root.right or root.val == root.right.val
                 and self.isUnivalTree(root.right))

        return left and right




