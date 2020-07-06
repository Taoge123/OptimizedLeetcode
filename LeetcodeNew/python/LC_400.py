

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
        length = 1
        count = 9  # 每个bucket里面多少数字
        start = 1
        while n > length * count:
            # size * step, 看看是不是1-9之间
            n -= length * count
            length += 1
            # 1-9， 10-99， 100-999, ...
            count *= 10
            start *= 10
        # 找到那个数字
        start += (n - 1) / length
        return int(str(start)[(n - 1) % length])


n = 1994516
a = Solution()
print(a.findNthDigit(n))


