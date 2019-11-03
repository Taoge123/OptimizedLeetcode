

"""
Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    /
   2
  /
 1

Output: 2

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.helper(root, 0, root.val)
        return self.res

    def helper(self, root, count, target):
        if not root:
            return 0

        if root.val == target:
            count += 1
        else:
            count = 1
        self.res = max(self.res, count)

        self.helper(root.left, count, root.val + 1)
        self.helper(root.right, count, root.val + 1)






