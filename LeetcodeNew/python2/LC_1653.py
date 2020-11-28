"""
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/discuss/935739/Python-solution

"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        res = [0] * n
        count = 0
        if s[0] == 'b':
            count = 1

        for i in range(1, n):
            if s[i] == 'a':
                res[i] = min(res[ i -1] + 1, count)
            else:
                count += 1
                res[i] = res[ i -1]

        return res[-1]




class Solution2:
    def minimumDeletions(self, s: str) -> int:
        a, b = 0, 0
        for ch in s:
            if ch == 'a':
                a += 1

        res = a
        for ch in s:
            if ch == 'a':
                a -= 1
            else:
                b += 1
            res = min(a + b, res)
        return res




