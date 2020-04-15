
"""
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

class Solution:
    def search(self, nums, target):

        if not nums:
            return False

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left)//2 + left
            print(left, right, mid)
            if nums[mid] == target:
                return True

            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                right -= 1

        return nums[left] == target


"""
777789123333 4444456777



789123456

4567  89123


1 3
left = 0
right = 1
mid = 0


"""


class SolutionTony:
    def search(self, nums, target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                left += 1

            while right > 0 and nums[right] == nums[right - 1]:
                right -= 1

            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True

            if nums[mid] < nums[right]:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False


nums = [7,8,9,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6]
target = 3
a = Solution()
print(a.search(nums, target))




