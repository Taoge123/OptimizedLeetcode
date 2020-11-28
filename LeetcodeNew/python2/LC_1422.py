
class Solution:
    def maxScore(self, s: str) -> int:
        cur = 0
        ones = 0
        res = float('-inf')
        for i, char in enumerate(s):
            if char == '0':
                cur += 1
            else:
                cur -= 1
                ones += 1

            if i < len(s) - 1:
                res = max(res, cur)

        return res + ones

