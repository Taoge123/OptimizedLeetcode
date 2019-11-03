
"""
https://www.cnblogs.com/yrbbest/p/5031304.html
https://www.bbsmax.com/A/amd0mrLmzg/

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

"""

import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.res = float('inf')
        self.dfs(root, target)
        return self.res

    def dfs(self, root, target):
        if not root:
            return

        if (abs(root.val - target) < abs(self.res - target)):
            self.res = root.val

        self.dfs(root.left, target)
        self.dfs(root.right, target)

class Solution2:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.res = float('inf')
        self.dfs(root, target)
        return self.res

    def dfs(self, root, target):
        if not root:
            return

        if (abs(root.val - target) < abs(self.res - target)):
            self.res = root.val

        if target < root.val:
            self.dfs(root.left, target)
        else:
            self.dfs(root.right, target)


