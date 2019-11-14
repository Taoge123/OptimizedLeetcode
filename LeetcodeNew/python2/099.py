# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:

        if not root:
            return

        self.prev, self.first, self.second = None, None, None
        self.helper(root)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp

    def helper(self, root):
        if not root:
            return

        self.helper(root.left)
        if self.prev and self.prev.val >= root.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.helper(root.right)







