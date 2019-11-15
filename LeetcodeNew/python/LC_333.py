
"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10
   / \
  5  15
 / \   \
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SubTree:
    def __init__(self, largest, size, min, max):
        self.largest = largest
        self.size = size
        self.min = min
        self.max = max


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return res.largest

    def dfs(self, root):
        if not root:
            return SubTree(0, 0, float('inf'), float('-inf'))

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root.val > left.max and root.val < right.min:
            size = left.size + right.size + 1
        else:
            size = float('-inf')

        largest = max(left.largest, right.largest, size)

        return SubTree(largest, size, min(root.val, left.min), max(root.val, right.max))











