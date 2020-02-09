



class Solution:
    def countSubstrings(self, s):
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    res += 1
        return res

class Solution2:
    def countSubstrings(self, s):
        if not s: return 0
        count = 0
        for i in range(len(s)):
            if self.ispalindrom(s[:i + 1]): count += 1
        count += self.countSubstrings(s[1:])
        return count

    def ispalindrom(self, s):
        return s == s[::-1]


