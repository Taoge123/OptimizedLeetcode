class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        summ = 0
        for i in range(k):
            summ += nums[i]
        res = summ
        for i in range(k, len(nums)):
            summ += nums[i] - nums[i - k]
            res = max(res, summ)
        return res / k


