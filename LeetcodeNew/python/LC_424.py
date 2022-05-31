
"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""


import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left, maxi, res = 0, 0, 0
        count = collections.Counter()

        for right in range(len(s)):
            count[s[right]] += 1
            # find the character that has the maximum frequency
            maxi = max(maxi, count[s[right]])
            # Then we change all other characters into the max frequency character
            while right - left + 1 - maxi > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res




