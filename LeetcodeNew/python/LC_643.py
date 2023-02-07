
class SolutionTony:
    def findMaxAverage(self, nums, k: int) -> float:

        n = len(nums)
        summ = sum(nums[:k])
        res = summ
        for i in range(k, n):
            summ += nums[i]
            summ -= nums[i-k]
            res = max(res, summ)
        return res / k



class Solution:
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



