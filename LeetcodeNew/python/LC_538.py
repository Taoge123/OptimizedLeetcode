
"""
Given a Binary Search Tree (BST), convert it to a Greater Tree
such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionTony:
    def convertBST(self, root):
        self.summ = 0
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return 0

        right = self.dfs(root.right)
        self.summ += root.val
        root.val = self.summ
        left = self.dfs(root.left)
        # return root



class Solution:
    def convertBST(self, root):
        self.sum = 0
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return
        self.helper(root.right)
        root.val += self.sum
        self.sum = root.val
        self.helper(root.left)





