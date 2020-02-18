"""
34. Find First and Last Position of Element in Sorted Array
Medium

2201

103

Favorite

Share
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums, target):

        low = self.search(nums, target)
        high = self.search(nums, target + 1) - 1

        if target in nums[low:low + 1]:
            return [low, high]
        else:
            return [-1, -1]

    def search(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = (right + left) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left


class Solution2:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]

        left = self.search(nums, target - 0.5)
        right = self.search(nums, target + 0.5)
        if right - left == 0:
            return [-1, -1]
        return [left, right - 1]

    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (end - start) // 2 + start
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start





