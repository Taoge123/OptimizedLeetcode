
class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        memo = {}
        return self.dfs(nums, S, 0, 0, memo)

    def dfs(self, nums, target, pos, summ, memo):
        if (pos, summ) in memo:
            return memo[(pos, summ)]

        if pos == len(nums):
            if target == summ:
                return 1
            else:
                return 0

        plus = self.dfs(nums, target, pos + 1, summ + nums[pos], memo)
        minus = self.dfs(nums, target, pos + 1, summ - nums[pos], memo)
        res = plus + minus
        memo[(pos, summ)] = res
        return memo[(pos, summ)]
