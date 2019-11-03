"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew),
but you can’t invert a binary tree on a whiteboard so f*** off.


"""
#
# 这是一个post-order的处理，先找到左右的叶子节点，再返回之前，跟换左右node的位置。
#
# DFS Recursive

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root



