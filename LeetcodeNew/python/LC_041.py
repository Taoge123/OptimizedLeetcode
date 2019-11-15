
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = len(nums) + 5

        for i in range(n):
            absolute = abs(nums[i])
            if absolute <= n:
                nums[absolute -1] = -abs(nums[absolute -1])

        # the positive number is the result
        for i in range(n):
            if nums[i] > 0:
                return i+ 1
        return n + 1

