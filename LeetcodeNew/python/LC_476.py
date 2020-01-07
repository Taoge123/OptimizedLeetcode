

"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""


class Solution:
    def findComplement(self, num: int) -> int:

        i = 1
        while i <= num:
            i = i << 1
        return (i-1) ^ num



class Solution2:
    def findComplement(self, num: int) -> int:
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num


num = 5
a = Solution()
print(a.findComplement(num))


