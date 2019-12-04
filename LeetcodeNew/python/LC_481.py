

"""
A magical string S consists of only '1' and '2' and obeys the following rules:

The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.

The first few elements of string S is the following: S = "1221121221221121122……"

If we group the consecutive '1's and '2's in S, it will be:

1 22 11 2 1 22 1 22 11 2 11 22 ......

and the occurrences of '1's or '2's in each group are:

1 2 2 1 1 2 1 2 2 1 2 2 ......

You can see that the occurrence sequence above is the S itself.

Given an integer N as input, return the number of '1's in the first N number in the magical string S.

Note: N will not exceed 100,000.

Example 1:
Input: 6
Output: 3
Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.
"""

import collections

class Solution:
    def magicalString(self, n: int) -> int:

        if n <= 0:
            return 0

        if n <= 3:
            return 1

        n -= 3
        queue = collections.deque([2])
        val = 1
        res = 1

        while n:
            count = queue.popleft()
            for i in range(count):
                queue.append(val)
                if val == 1:
                    res += 1
                n -= 1
                if n == 0:
                    return res
            val ^= 3
        return res







