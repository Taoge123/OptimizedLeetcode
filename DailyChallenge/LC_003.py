


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, res = 0, 0
        table = {}
        n = len(s)
        for i in range(n):
            if s[i] in table and start <= table[s[i]]:
                start = table[s[i]] + 1
            else:
                res = max(res, i - start + 1)
            table[s[i]] = i
        return res

