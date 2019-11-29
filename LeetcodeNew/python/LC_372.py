
"""
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
"""

"""
n1*n2 % 1337 == (n1 % 1337)*(n2 % 1337) % 1337
If b = m*10 + d, we have a**b == (a**d)*(a**10)**m
"""


class Solution:
    def superPow(self, a, b):
        if not b:
            return 1
        return pow(a, b.pop(), 1337) * self.superPow(pow(a, 10, 1337), b) % 1337









