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


class SolutionTony:
    def letterCombinations(self, digits):
        self.n = len(digits)
        self.phone = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}
        if not digits:
            return []

        res = []
        self.dfs(0, [], res, digits)
        return res

    def dfs(self, index, path, res, digits):
        if len(path) == self.n:
            res.append("".join(path))
            return

        for i in range(index, self.n):
            for char in self.phone[digits[i]]:
                self.dfs(i + 1, path + [char], res, digits)

        return res






digits = '23'
a = SolutionTest()
print(a.letterCombinations(digits))





