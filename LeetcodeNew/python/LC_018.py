"""
Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

import collections

class Solution(object):
    def fourSum(self, nums, target):

        dic = collections.defaultdict(set)
        n = len(nums)
        nums.sort()

        if n < 4:
            return []

        res = set()

        for i in range(n - 1):
            for j in range(i + 1, n):
                sum = nums[i] + nums[j]

                for sub in dic[target - sum]:
                    res.add(tuple(list(sub) + [nums[j], nums[i]]))

            for j in range(i):
                dic[nums[i] + nums[j]].add((nums[j], nums[i]))

        return list(res)

