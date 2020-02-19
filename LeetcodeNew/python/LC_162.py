"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

"""


class Solution:
    def findPeakElement(self, nums):

        return self.findPeakElementUtil(nums, 0, len(nums) - 1)

    def findPeakElementUtil(self, nums, left, right):

        if left == right:
            return left

        mid = (left + right) // 2

        # if nums[mid] > nums[mid -1] and nums[mid] > nums[mid + 1]:
        #     return mid

        if nums[mid] > nums[mid + 1]:
            return self.findPeakElementUtil(nums, left, mid)

        return self.findPeakElementUtil(nums, mid + 1, right)


class Solution2:
    def findPeakElement(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        if nums[left] > nums[right]:
            return left
        return right



