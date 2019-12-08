"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = "" if num >= 0 else "-"
        num = abs(num)
        res = ''
        while num:
            res = str(num % 7) + res
            num //= 7

        return sign + res or "0"


class Solution2:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return '-' + self.convertToBase7(-num)

        if num < 7:
            return str(num)

        return self.convertToBase7(num // 7) + str(num % 7)







