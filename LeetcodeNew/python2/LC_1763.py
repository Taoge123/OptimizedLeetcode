class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2: return ""
        chars = set(list(s))
        for i in range(len(s)):
            if s[i].lower() not in chars or s[i].upper() not in chars:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i + 1:])
                return s2 if len(s2) > len(s1) else s1
        return s


