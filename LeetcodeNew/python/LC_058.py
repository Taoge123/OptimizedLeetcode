
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(' ').split(' ')[-1])

class Solution:
    def lengthOfLastWord(self, s):
        start, res = 0, 0
        calc = True
        s += " "
        for i in range(len(s)):
            cur = s[i]
            if cur == ' ' and calc:
                res = i - start
                calc = False
            elif cur != ' ' and not calc:
                start = i
                calc = True
        return res



