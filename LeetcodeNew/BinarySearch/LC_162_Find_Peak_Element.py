
"""

https://leetcode.com/problems/find-peak-element/discuss/50259/My-clean-and-readable-python-solution

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
"""

import sys

class Solution1:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        # handle condition 3
        while left < right - 1:
            mid = (left + right) / 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        # handle condition 1 and 2
        return left if nums[left] >= nums[right] else right


class SolutionCaikehe:
    # O(n) time
    def findPeakElement1(self, nums):
        i = 0
        while i <= len(nums) - 1:
            while i < len(nums) - 1 and nums[i] < nums[i + 1]:
                i += 1
            return i

            # O(lgn) time

    def findPeakElement2(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l

        # Recursively

    def findPeakElement(self, nums):
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, l, r):
        if l == r:
            return l
        mid = l + (r - l) // 2
        if nums[mid] > nums[mid + 1]:
            return self.helper(nums, l, mid)
        else:
            return self.helper(nums, mid + 1, r)

    # O(n) time
    def findPeakElement(self, nums):
        if not nums:
            return 0
        nums.insert(0, -(sys.maxint + 1))
        nums.append(-(sys.maxint + 1))
        for i in xrange(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i - 1

    # O(lgn) time
    def findPeakElement(self, nums):
        if not nums:
            return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                return l
            mid = l + (r - l) // 2
            # due to "mid" is always the left one if the length of the list is even,
            # so "mid+1" is always valid.
            if (mid - 1 < 0 or nums[mid - 1] < nums[mid]) and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1


"""
类型：考虑边界 
Time Complexity (logN )
Time Spent on this question: 50 mins | 重刷
这题套惯用的模板要考虑Edge Case，因为判定条件是:

上坡：nums[mid-1] < nums[mid]
下坡： nums[mid] > nums[mid+1]

然后这里mid + 1 和 mid - 1在数组大小为 1 或者 2的时候，很容易就越界了，
所以在大小范围增加最小值和最大值。得到：
if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
"""

class Solution3:
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
                return mid;
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1

"""这道题目也可以套另外一个模板，可以不用考虑越界的问题：
"""
class Solution4:
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l








