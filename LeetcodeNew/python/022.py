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




