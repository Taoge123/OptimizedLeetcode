class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if (abs(len(s) - len(t))) > 1:
            return False
        if s == t:
            return False
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                return s[i + 1:] == t[i + 1:] or s[i:] == t[i + 1:] or s[i + 1:] == t[i:]

        return True

