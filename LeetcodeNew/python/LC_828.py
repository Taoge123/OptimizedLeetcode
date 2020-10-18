
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        lastPos = [0] * 26
        contribution = [0] * 26

        res = 0
        for i in range(len(s)):
            c = ord(s[i]) - ord('A')
            contribution[c] = i + 1 - lastPos[c]
            for j in range(26):
                res += contribution[j]
            lastPos[c] = i + 1

        return res




