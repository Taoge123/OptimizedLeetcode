
"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:

        visited = set()
        for char in s:
            if char not in visited:
                visited.add(char)
            else:
                visited.remove(char)

        return len(s) - len(visited) + 1 if len(visited) > 0 else len(s)


class Solution2:
    def longestPalindrome(self, s: str) -> int:

        res = 0
        count = collections.Counter(s)
        for char, num in count.items():
            if num % 2 == 0 or res % 2 == 0:
                res += num
            else:
                res += num - 1
        return res


class Solution3:
    def longestPalindrome(self, s: str) -> int:

        table = collections.Counter(s)
        odd = 0
        res = 0

        for char in table.keys():
            if table[char] % 2:
                odd += 1
            res += table[char]
        return min(res, res - odd + 1)










