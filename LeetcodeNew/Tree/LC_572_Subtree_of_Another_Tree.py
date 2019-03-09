
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

class Solution0:
    def isMatch(self, s, t):
        if not(s and t):
            return s is t
        return (s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # check if two trees are the same
        def sametree(p, q):
            if p and q:
                return p.val == q.val and sametree(p.left, q.left) and sametree(p.right, q.right)
            return p is q

        if s is None:
            return False
        if sametree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)








