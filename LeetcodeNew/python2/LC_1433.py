import collections
import string


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        count1 = collections.Counter(s1)
        count2 = collections.Counter(s2)
        return self.check(count1, count2) or self.check(count2, count1)

    def check(self, count1, count2):
        s = 0
        for ch in string.ascii_lowercase:
            s += count1[ch] - count2[ch]
            if s < 0:
                return False
        return True


