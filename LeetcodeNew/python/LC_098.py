"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        self.inorder(root, res)

        for i in range(1, len(res)):
            if res[i-1] >= res[i]:
                return False
        return True

    def inorder(self, root, res):
        if not root:
            return

        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)



class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack, res = [root], []

        while stack:
            node = stack.pop()
            if isinstance(node, int):
                res.append(node)
                continue

            if node.right:
                stack.append(node.right)

            stack.append(node.val)

            if node.left:
                stack.append(node.left)


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        self.flag = True
        res = []
        self.helper(root, res)
        return self.flag

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            if res and res[-1] >= root.val:
                self.flag = False
                return
            res.append(root.val)
            self.helper(root.right, res)


class Solution3:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, low, high):
        if not root:
            return True

        if not root.left and not root.right:
            return low < root.val < high

        return low < root.val < high and self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)















