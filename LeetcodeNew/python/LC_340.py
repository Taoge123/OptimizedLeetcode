
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

class SolutionRika:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window = collections.defaultdict(int)

        count = 0
        left, right = 0, 0

        while right < len(s):
            ch1 = s[right]
            window[ch1] += 1

            while right < len(s):
                ch2 = s[left]
                window[ch2] -= 1
                if window[ch2] == 0:
                    del window[ch2]
                left += 1
            count = max(count, right - left + 1)
            right += 1

        return count



class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        res = 0
        table = collections.defaultdict(int)
        for right, char in enumerate(s):
            table[char] = right
            if len(table) > k:
                left = min(table.values())
                del table[s[left]]
                left += 1
            res = max(right - left + 1, res)
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






