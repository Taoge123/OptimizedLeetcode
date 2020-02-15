
class Solution:
    def letterCasePermutation(self, S):
        res = []
        self.helper(S, "", res)
        return res

    def helper(self, s, path, res):
        if not s:
            res.append(path)
            return

        if s[0].isdigit():
            self.helper(s[1:], path + s[0], res)
        else:
            self.helper(s[1:], path + s[0].lower(), res)
            self.helper(s[1:], path + s[0].upper(), res)





