

"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 2 ** 64 - 1
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # for overflow condition like
        # -1
        #  1
        return a & mask if b > mask else a




class SolutionTLE:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a

        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1

        return a



