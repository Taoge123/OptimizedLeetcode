
"""
Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.


https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)


"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def sameTree(self, tree1, tree2):

        if not (tree1 and tree2):
            return tree1 is tree2

        return (tree1.val == tree2.val and self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right,
                                                                                                   tree2.right))

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        if self.sameTree(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)







