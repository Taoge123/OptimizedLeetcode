
class Solution:
    def letterCasePermutation(self, S):
        res = []
        self.helper(S, "", res)
        return res

    def helper(self, s, p, res):
        if s == "":
            res.append(p)
            return
        if s[0].isdigit():
            self.helper(s[1:], p+ s[0], res)
        else:
            self.helper(s[1:], p + s[0].upper(), res)
            self.helper(s[1:], p + s[0].lower(), res)




