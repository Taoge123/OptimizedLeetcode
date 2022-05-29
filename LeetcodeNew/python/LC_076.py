"""
3. Longest Substring Without Repeating Characters
76. Minimum Window Substring
159. Longest Substring with At Most Two Distinct Characters
209. Minimum Size Subarray Sum
992. Subarrays with K Different Integers
340. Longest Substring with At Most K Distinct Characters
424. Longest Repeating Character Replacement
713. Subarray Product Less Than K
1208. Get Equal Substrings Within Budget

"""

import collections


class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        minLen = float('inf')
        start = 0
        left, right = 0, 0

        window = collections.defaultdict(int)
        needs = collections.defaultdict(int)

        for ch in t:
            needs[ch] += 1

        match = 0
        while right < m:
            c1 = s[right]
            if c1 in needs:
                window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1
            while match == len(needs):
                if right - left < minLen:
                    start = left
                    minLen = right - left
                c2 = s[left]
                if c2 in needs:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        if minLen == float('inf'):
            return ""
        return s[start:start + minLen]



class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res = ""
        left = 0
        minLen = float('inf')
        total = 0
        count = collections.Counter(t)

        for right, ch in enumerate(s):
            count[ch] -= 1
            if count[ch] >= 0:
                total += 1
            while total == len(t):
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    res = s[left: right + 1]
                count[s[left]] += 1
                if count[s[left]] > 0:
                    total -= 1
                left += 1
        return res





