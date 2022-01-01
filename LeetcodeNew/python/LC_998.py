"""
It is not insert a val into the tree, but to append a val to A, and then construct a tree...

https://leetcode.com/problems/maximum-binary-tree-ii/discuss/243188/How-many-people-can't-understand-what-the-question-means

比较root.val and val
1 - 如果root.val > val, 说明val必然在root的右子数中，直接地柜调用
2 - 反之，说明val直接是新的root
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoMaxTree(self, root, val: int):
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root

        newRoot = TreeNode(val)
        newRoot.left = root
        return newRoot



