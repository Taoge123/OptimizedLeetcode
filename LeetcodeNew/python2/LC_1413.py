
class Solution:
    def minStartValue(self, nums) -> int:
        minSum = 0
        curSum = 0
        for num in nums:
            curSum += num
            minSum = min(minSum, curSum)
        return abs(minSum) + 1


