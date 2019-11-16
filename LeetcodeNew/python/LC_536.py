
"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   /
  3   1 5
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
"""


# https://leetcode.com/problems/construct-binary-tree-from-string/discuss/100422/Python-Straightforward-with-Explanation
# https://leetcode.com/problems/construct-binary-tree-from-string/discuss/300543/Python-stack-solution-with-comment-beats-95-on-time-and-space

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        stack = []
        num = ''
        root = None

        for idx, char in enumerate(s):
            if char == '(':
                pass
            elif char == ')':
                stack.pop()
            else:
                num += char
                if idx + 1 >= len(s) or not s[idx + 1].isdigit():
                    curr = TreeNode(int(num))
                    num = ''
                    if not stack:
                        root = curr
                    else:
                        parent = stack[-1]
                        if not parent.left:
                            parent.left = curr
                        else:
                            parent.right = curr

                    stack.append(curr)

        return root




