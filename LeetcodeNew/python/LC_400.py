

"""
https://leetcode.com/problems/nth-digit/discuss/88417/4-liner-in-Python-and-complexity-analysis

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""


class Solution:
    def findNthDigit(self, n):
        start = 1
        size = 1
        step = 9
        while n > size * step:
            n = n - (size * step)
            size += 1
            step *= 10
            #第size位的最开始的数是在start开始的
            start *= 10
        return int(str(start + (n - 1) // size)[(n - 1) % size])


n = 1994516
a = Solution()
print(a.findNthDigit(n))


