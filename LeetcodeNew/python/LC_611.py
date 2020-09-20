class Solution(object):
    def triangleNumber(self, nums):
        nums = sorted(nums)
        count = 0

        for i in range(1, len(nums)):
            left, right = 0, i - 1
            while (left < right):
                if nums[left] + nums[right] > nums[i]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1

        return count



