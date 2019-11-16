
"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).


Note: There are at least two nodes in this BST.
"""


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






