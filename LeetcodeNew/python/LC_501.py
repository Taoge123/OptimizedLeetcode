

"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root):
        cache = collections.defaultdict(int)
        self.max = -1
        self.inorder(root, cache)
        return [k for k, v in cache.items() if v == self.max]

    def inorder(self, root, cache):
        if not root:
            return
        cache[root.val] += 1
        self.max = max(self.max, cache[root.val])
        self.inorder(root.left, cache)
        self.inorder(root.right, cache)





