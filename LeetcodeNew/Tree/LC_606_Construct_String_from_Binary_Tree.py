

"""

https://leetcode.com/problems/construct-string-from-binary-tree/solution/
Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair
to break the one-to-one mapping relationship between the input and the output.
"""

"""
We do this recursively.

If the tree is empty, we return an empty string.
We record each child as '(' + (string of child) + ')'
If there is a right child but no left child, 
we still need to record '()' instead of empty string.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t):
        if not t: return ''
        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)


class Solution2:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        res = ""
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if left or right:
            res += "(%s)" % left
        if right:
            res += "(%s)" % right
        return str(t.val) + res



class Solution3:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def preorder(root):
            if root is None:
                return ""
            s=str(root.val)
            l=preorder(root.left)
            r=preorder(root.right)
            if r=="" and l=="":
                return s
            elif l=="":
                s+="()"+"("+r+")"
            elif r=="":
                s+="("+l+")"
            else :
                s+="("+l+")"+"("+r+")"
            return s
        return preorder(t)


"""
Easy
from TreeBase import genTree

Algorithm:
1. Preorder Traversal to generate the string
2. Place ( and ) at the start and end of left and right child calculations
3. We only need to put a () if left child is absent but there is a right child, in order to
recognize that the child is right we put the left as empty
4. Return the whole string as the result
"""
