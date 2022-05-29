"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res = 0, 0
        table = {}
        n = len(s)
        for right in range(n):
            if s[right] in table and left <= table[s[right]]:
                left = table[s[right]] + 1
            else:
                res = max(res, right - left + 1)
            table[s[right]] = right
        return res


