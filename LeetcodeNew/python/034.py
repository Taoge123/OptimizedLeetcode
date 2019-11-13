class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

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


