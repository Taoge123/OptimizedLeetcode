"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""



class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        count, num, base, highBase = 0, n, 1, 10
        while num:
            num, mod = divmod(num, 10)

            if mod == 0:
                count += (n // highBase) * base
            elif mod == 1:
                count += (n // highBase) * base + (n % base + 1)
            else:
                count += (n // highBase + 1) * base

            base *= 10
            highBase *= 10

        return count




