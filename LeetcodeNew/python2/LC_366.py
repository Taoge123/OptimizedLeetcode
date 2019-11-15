"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.



Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]


Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         /
        2


2. Now removing the leaf [2] would result in this tree:

          1


3. Now removing the leaf [1] would result in the empty tree:

          []
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findLeaves(self, root):
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







