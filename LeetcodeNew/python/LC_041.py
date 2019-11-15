"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

"""

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = len(nums) + 5

        for i in range(n):
            absolute = abs(nums[i])
            if absolute <= n:
                nums[absolute -1] = -abs(nums[absolute -1])

        # the positive number is the result
        for i in range(n):
            if nums[i] > 0:
                return i+ 1
        return n + 1

