class SolutionTony:
    def findMaxAverage(self, nums, k: int) -> float:
        n = len(nums)
        summ = 0
        res = float('-inf')
        for i in range(n):
            summ += nums[i]
            if i >= k:
                summ -= nums[i - k]
            if i >= k - 1:
                res = max(res, summ / k)
        return res



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


