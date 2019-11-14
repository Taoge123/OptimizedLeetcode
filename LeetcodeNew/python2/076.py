import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res = ""
        left = 0
        minLen = float('inf')
        total = 0
        count = collections.Counter(t)

        for i, char in enumerate(s):
            count[char] -= 1
            if count[char] >= 0:
                total += 1
            while total == len(t):
                if minLen > i - left + 1:
                    minLen = i - left + 1
                    res = s[left: i + 1]
                count[s[left]] += 1
                if count[s[left]] > 0:
                    total -= 1
                left += 1
        return res





