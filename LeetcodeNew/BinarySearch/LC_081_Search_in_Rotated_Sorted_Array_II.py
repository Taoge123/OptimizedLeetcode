
"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/177150/Search-in-Rotated-Sorted-Array-I-python-code

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""

class SolutionCaikehe1:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]:  # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


class SolutionCaikehe2:
    def search(self, nums, target):
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return nums[l] == target


"""
1. 这道题与“搜索旋转排序数组 I”相比，不同之处就在于判断中间位置mid时需作预处理：

while low < high and nums[low] == nums[high]:
	low += 1  
这也导致算法的最坏时间复杂度变为O(n)。整体还是基于二分查找

2. 同时，我在I的基础优化了分类的方式：首先判断mid位置（属于高区还是低区）、进一步判断target位置是否在一个特定范围(所谓特定范围是指类似于正常排序的可二分查找的范围)直接分成四类。（可参考最后的图片）

3. python知识点： 2<x<3在python里可以直接写，不用拆分开来
"""


class Solution2:
    def search(self, nums, target):
        if not nums:
            return False
        low = 0
        high = len(nums) - 1
        while low <= high:
            while low < high and nums[low] == nums[high]:#这样的目的是为了能准确判断mid位置，所以算法的最坏时间复杂度为O(n)
                low += 1
            mid = (low+high)//2
            if target == nums[mid]:
                return True
            elif nums[mid] >= nums[low]: #高区
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:  #低区
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False


class Solution3:
    def search(self, nums, target):


        left, right = 0, len(nums) - 1
        while left < right and nums[left] == nums[right]:       # to distinguish left ascending array and right ascending array
            left += 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:                         # nums[mid] at left ascending array
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:                                           # nums[mid] < target
                    left = mid + 1
            elif nums[mid] <= nums[right]:                      # nums[mid] at right ascending array
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:                                           # nums[mid] > target
                    right = mid - 1
        return False
