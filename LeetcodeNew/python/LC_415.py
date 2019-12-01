

"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

import itertools

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        res = ""
        carry = 0
        m, n = len(num1), len(num2)
        if m < n:
            num1 = "0" * (n - m) + num1
        else:
            num2 = "0" * (m - n) + num2

        n = max(m, n)

        for i in range(n - 1, -1, -1):
            summ = int(num1[i]) + int(num2[i]) + carry
            if summ >= 10:
                carry = 1
                summ -= 10
            else:
                carry = 0

            res = str(summ) + res
        if carry:
            res = "1" + res
        return res


class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        carry, res = 0, ""
        for x, y in itertools.izip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            summ = (int(x) + int(y) + carry)
            if summ >= 10:
                carry = 1
                summ -= 10
            else:
                carry = 0

            res = str(summ) + res
        if carry > 0:
            res = "1" + res
        return res


class Solution3:
    def addStrings(self, num1, num2):
        i, j = len(num1)-1, len(num2)-1
        res, summ = [], 0
        while i >=0 or j >= 0 or summ:
            if i >= 0:
                summ += int(num1[i])
                i -= 1
            if j >= 0:
                summ += int(num2[j])
                j -= 1
            res.append(str(summ % 10))
            summ //= 10
        return ''.join(res[::-1])





