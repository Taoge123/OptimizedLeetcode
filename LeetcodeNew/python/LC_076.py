"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

"""

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





