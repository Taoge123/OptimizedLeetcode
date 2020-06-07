import itertools


class Solution:
    def maxPower(self, s: str) -> int:
        res = count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            res = max(res, count)
        return res


class Solution2:
    def maxPower(self, s: str) -> int:
        group = itertools.groupby(s)
        res = 1
        for i, group in group:
            res = max(res, len(list(group)))
        return res


