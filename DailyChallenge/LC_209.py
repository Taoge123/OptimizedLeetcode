

class Solution:
    def minSubArrayLen(self, s, nums):

        summ, left = 0, 0
        res = float('inf')

        for right, num in enumerate(nums):
            summ += num
            while summ >= s:
                res = min(res, right - left + 1)
                summ -= nums[left]
                left += 1

        return res if res <= len(nums) else 0


