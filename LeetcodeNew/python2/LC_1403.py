
class Solution:
    def minSubsequence(self, nums):
        cur = 0
        nums = sorted(nums)[::-1]
        total = sum(nums)
        for i, num in enumerate(nums):
            cur += num
            if cur * 2 > total:
                return nums[: i +1]

        return nums



