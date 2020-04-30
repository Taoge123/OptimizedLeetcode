
"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""

import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        start = 0
        res = 0

        for i, char in enumerate(s):

            count[char] += 1
            while len(count) > k:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    del count[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res


class Solution2:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        start, res = 0, 0
        table = collections.defaultdict(int)

        for i, char in enumerate(s):

            table[char] = i
            if len(table) > k:
                start = min(table.values())
                del table[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res






