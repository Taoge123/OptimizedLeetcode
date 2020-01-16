"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

"""

class Solution:
    def reverse(self, x):

        if x < 0:
            return -self.reverse(-x)

        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        return res if res <= 0x7fffffff else 0

