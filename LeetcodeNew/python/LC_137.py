
"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""


class Solution:
    def singleNumber(self, nums) -> int:
        a = set(nums)
        a = sum(a) * 3 - sum(nums)
        a = a // 2
        return a


class Solution:
    def singleNumber(self, nums) -> int:
        ones, twos = 0, 0

        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones

        return ones




