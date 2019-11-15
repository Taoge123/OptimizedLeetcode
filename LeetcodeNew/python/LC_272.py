"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Solution:
    def closestKValues(self, root: TreeNode, target, k):

        res = collections.deque([])
        self.dfs(root, target, res, k)
        return res

    def dfs(self, root, target, res, k):
        if not root:
            return

        self.dfs(root.left, target, res, k)
        if len(res) == k:
            if abs(root.val - target) < abs(res[0] - target):
                res.popleft()
            else:
                return
        res.append(root.val)
        self.dfs(root.right, target, res, k)






