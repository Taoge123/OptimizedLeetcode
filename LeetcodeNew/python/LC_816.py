
"""
if s == "0": return [S]
if s == "XXX0": return [S]
return [S, "X.XXX", "XX.XX", "XXX.X"]
if s == "": return []
if s == "0XXX0": return []
if s == "0XXX": return [0.XXX]
if s == "0": return [S]
if s == "XXX0": return [S]

"""



class Solution:
    def ambiguousCoordinates(self, S: str):
        n = len(S)
        res = []
        for i in range(1, n- 2):
            left = self.helper(S[1:i + 1])
            right = self.helper(S[i + 1:n - 1])
            print(left, right)
            for s1 in left:
                for s2 in right:
                    res.append("(" + s1 + ", " + s2 + ")")
        return res

    def helper(self, s):
        n = len(s)
        res = []
        if n == 0 or (n > 1 and s[0] == '0' and s[-1] == '0'):
            return res
        if n > 1 and s[0] == '0':
            res.append("0." + s[1:])
            return res
        res.append(s)
        if n == 1 or s[n - 1] == "0":
            return res
        for i in range(1, n):
            res.append(s[:i] + '.' + s[i:])

        return res



