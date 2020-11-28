
class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        if len(s1) == len(s2):
            return s1 if s1 == s2 else ''
        else:
            if len(s1) < len(s2):
                s1, s2 = s2, s1
            if s1[:len(s2)] == s2:
                return self.gcdOfStrings(s1[len(s2):], s2)
            else:
                return ''


