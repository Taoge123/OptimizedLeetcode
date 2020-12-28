import collections

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        start, res = 0, 0
        table = collections.defaultdict(int)
        for i, char in enumerate(s):
            table[char] = i
            if len(table) > 2:
                start = min(table.values())
                del table[s[start]]
                start += 1
            res = max(i - start + 1, res)
        return res


