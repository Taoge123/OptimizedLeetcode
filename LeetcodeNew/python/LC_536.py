
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


class Solution1:
    def str2tree(self, s):
        i = s.find('(')
        if i < 0:
            return TreeNode(int(s)) if s else None

        bal = 0
        for j, char in enumerate(s):
            if char == '(':
                bal += 1
            if char == ')':
                bal -= 1
            if j > i and bal == 0:
                break

        root = TreeNode(int(s[:i]))
        root.left = self.str2tree(s[i + 1: j])
        root.right = self.str2tree(s[j + 2: -1])
        return root



class Solution2:
    def str2tree(self, s: str) -> TreeNode:
        if not s or len(s) == 0:
            return None
        root, index = self.helper(s, 0)
        return root

    def helper(self, s, i):
        start = i
        while i < len(s) and (s[i] == '-' or s[i].isdigit()):
            i += 1
        if start == i:
            return None, i
        node = TreeNode(int(s[start:i]))
        if i < len(s) and s[i] == "(":  # left subtree
            i += 1  # skip (
            node.left, i = self.helper(s, i)
            i += 1  # skip )
        if i < len(s) and s[i] == "(":  # right subtree
            i += 1  # skip (
            node.right, i = self.helper(s, i)
            i += 1  # skip )
        return node, i


s = "4(2(3)(1))(6(5))"
a = Solution1()
print(a.str2tree(s))


