
"""
Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

"""


"""
Let's create a recursive solution.

If both trees are empty then we return empty.
Otherwise, we will return a tree. The root value will be t1.val + t2.val, except these values are 0 if the tree is empty.
The left child will be the merge of t1.left and t2.left, except these trees are empty if the parent is empty.
The right child is similar.
"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        if not t1 and not t2:
            return None
        root = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        root.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        root.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return root

class Solution2:
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

