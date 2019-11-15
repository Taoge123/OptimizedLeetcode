"""
Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution:
    def letterCombinations(self, digits):
        self.phone = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}
        res = []
        if digits:
            self.backtrack("", digits, res)
        return res

    def backtrack(self, path, digits, res):
        if not digits:
            res.append(path)
        else:
            for letter in self.phone[digits[0]]:
                self.backtrack(path + letter, digits[1:], res)


