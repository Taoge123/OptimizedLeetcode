import collections

class Solution:
    def numSplits(self, s: str) -> int:
        left = collections.Counter()
        right = collections.Counter(s)
        res = 0

        for ch in s:
            left[ch] += 1
            right[ch] -= 1
            if right[ch] == 0:
                del right[ch]

            if len(left) == len(right):
                res += 1

        return res


