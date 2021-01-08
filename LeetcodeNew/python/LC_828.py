
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        lastPos = [0] * 26
        contribution = [0] * 26

        res = 0
        for i in range(len(s)):
            num = ord(s[i]) - ord('A')
            contribution[num] = i + 1 - lastPos[num]
            for j in range(26):
                res += contribution[j]
            lastPos[num] = i + 1

        return res




