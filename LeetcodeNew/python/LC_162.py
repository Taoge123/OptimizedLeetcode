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
