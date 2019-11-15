"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)

        res = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[l] + nums[i] + nums[r]
                if abs(s - target) < abs(res - target):
                    res = s
                elif s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return res

