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

        left, res = 0, 0
        table = collections.defaultdict(int)
        for right, char in enumerate(s):
            table[char] = right
            if len(table) > 2:
                left = min(table.values())
                del table[s[left]]
                left += 1
            res = max(right - left + 1, res)
        return res


class SolutionRika:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window = collections.defaultdict(int)

        count = 0
        left, right = 0, 0

        while right < len(s):
            ch1 = s[right]
            window[ch1] += 1

            if len(window) > 2:
                ch2 = s[left]
                window[ch2] -= 1
                if window[ch2] == 0:
                    del window[ch2]
                left += 1
            count = max(count, right - left + 1)
            right += 1

        return count
