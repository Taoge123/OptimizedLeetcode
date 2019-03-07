
"""
Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""

class Solution:
    def sumOfLeftLeaves(self, root):
        if not root: return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)   # isn't leave


class Solution2:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.findleftleaves(root)
        return self.ans

    def findleftleaves(self, root):
        if not root:
            return
        if root.left and self.isLeaves(root.left):
            self.ans += root.left.val
        self.findleftleaves(root.left)
        self.findleftleaves(root.right)
        return

    def isLeaves(self, root):
        return root.left == None and root.right == None


