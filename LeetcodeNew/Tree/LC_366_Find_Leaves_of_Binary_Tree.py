
"""
Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]

"""

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findLeaves(self, root: TreeNode):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if not root:
            return -1

        left = self.helper(root.left, res)
        right = self.helper(root.right, res)

        level = max(left, right) + 1
        if level >= len(res):
            res.append([])
        res[level].append(root.val)

        return level







