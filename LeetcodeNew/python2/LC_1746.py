class Solution:
    def maxSumAfterOperation(self, nums):

        memo = {}
        self.dfs(nums, 0, True, memo)
        return max(memo.values())

    def dfs(self, nums, i, can_square, memo):
        if (i, can_square) in memo:
            return memo[(i, can_square)]

        if i >= len(nums):
            return 0

        res = float('-inf')
        if can_square:
            res = max(self.dfs(nums, i + 1, False, memo) + nums[i] * nums[i], nums[i] * nums[i])

        res = max(res, self.dfs(nums, i + 1, can_square, memo) + nums[i], nums[i])

        memo[(i, can_square)] = res
        return res
