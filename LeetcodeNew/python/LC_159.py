"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""


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


