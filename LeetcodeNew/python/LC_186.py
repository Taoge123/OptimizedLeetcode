
"""
Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?

"""


class Solution:

    def reverseWords(self, s):
        self.reverse(s, 0, len(s) - 1)

        beg = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, beg, i - 1)
                beg = i + 1
            elif i == len(s) - 1:
                self.reverse(s, beg, i)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

class Solution2:
    def reverseWords(self, s):
        s[:] = list(' '.join(reversed(''.join(s).split(' '))))


