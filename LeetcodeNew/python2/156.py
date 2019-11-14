class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:

        if not root or (not root.left and not root.right):
            return root

        newRoot = self.upsideDownBinaryTree(root.left)

        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None

        return newRoot





