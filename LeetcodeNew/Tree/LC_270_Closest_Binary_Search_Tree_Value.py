
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


class SolutionCaikehe:
    # works for normal binary tree
    def closestValue1(self, root, target):
        if not root:
            return 0
        self.res = root.val
        self.findClosest(root, target)
        return self.res

    def findClosest(self, root, target):
        if root:
            if abs(root.val - target) == 0:
                self.res = root.val
                return  # backtracking
            if abs(root.val - target) < abs(self.res - target):
                self.res = root.val
            self.findClosest(root.left, target)
            self.findClosest(root.right, target)

    # works for normal binary tree
    def closestValue2(self, root, target):
        if not root:
            return sys.maxint
        if not root.left and not root.right:
            return root.val
        l = self.closestValue(root.left, target)
        r = self.closestValue(root.right, target)
        return min([root.val, l, r], key=lambda x: abs(x - target))

    # works for binary search tree
    def closestValue(self, root, target):
        if not root:
            return sys.maxint
        if not root.left and not root.right:
            return root.val
        node = root.right if target > root.val else root.left
        if not node:
            return root.val
        tmp = self.closestValue(node, target)
        return min((tmp, root.val), key=lambda x: abs(x - target))


class SolutionT:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root is None:
            return float('inf')

        if root.val == target:
            return root.val
        elif root.val < target:
            rightRes = self.closestValue(root.right, target)
            return root.val if abs(root.val - target) < abs(rightRes - target) else rightRes
        elif root.val > target:
            leftRes = self.closestValue(root.left, target)
            return root.val if abs(root.val - target) < abs(leftRes - target) else leftRes



class Solution2:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closest = float('inf')

        def helper(root, value):
            if not root:
                return
            if abs(root.val - target) < abs(self.closest - target):
                self.closest = root.val

            # Target should be located on left subtree
            if target < root.val:
                helper(root.left, target)

            # target should be located on right subtree
            if target > root.val:
                helper(root.right, target)

        helper(root, target)
        return self.closest

