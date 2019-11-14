
class Solution:
    def findMin(self, nums):

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid if nums[mid] != nums[right] else right - 1

        return nums[left]





