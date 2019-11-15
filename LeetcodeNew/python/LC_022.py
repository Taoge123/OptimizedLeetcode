"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

class Solution:
    def generateParenthesis(self, n):
        res = []
        self.backtrack(n, n, "", res)
        return res

    def backtrack(self, left, right, path, res):
        if right < left:
            return
        if not right and not left:
            res.append(path)
        if left:
            self.backtrack(left - 1, right, path + '(', res)
        if right:
            self.backtrack(left, right - 1, path + ')', res)




