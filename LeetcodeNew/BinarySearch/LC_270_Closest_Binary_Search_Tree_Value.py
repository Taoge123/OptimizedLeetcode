
"""
Given a non-empty binary search tree and a target value,
find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

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

class Solution1:
    def closestValue(self, root, target):
        res = root.val
        while root:
            if abs(root.val - target) < abs(r - target):
                res = root.val
            root = root.left if target < root.val else root.right
        return res


class Solution2:
    def closestValue(self, root, target):

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


