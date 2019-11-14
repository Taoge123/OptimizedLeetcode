
class Solution:
    def __init__(self):
        self.dic = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.dic:
            return self.dic[(s1, s2)]
        if sorted(s1) != sorted(s2) or len(s1) != len(s2):
            self.dic[(s1, s2)] = False
            return False
        if s1 == s2:
            self.dic[(s1, s2)] = True
            return True

        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or
                    self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        self.dic[(s1, s2)] = False
        return False





