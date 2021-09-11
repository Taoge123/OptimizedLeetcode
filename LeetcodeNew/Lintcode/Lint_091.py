class Solution:
    def MinAdjustmentCost(self, A, target):
        res = float('inf')
        memo = {}
        for num in range(1, 101):
            res = min(res, self.dfs(A, 1, num, target, memo) + abs(A[0] - num))
        return res

    def dfs(self, nums, pos, num, target, memo):
        if (pos, num) in memo:
            return memo[(num, pos)]

        if pos == len(nums):
            return 0

        res = float('inf')
        for nxt in range(max(num - target, 1), min(num + target + 1, 101)):
            res = min(res, self.dfs(nums, pos + 1, nxt, target, memo) + abs(nums[pos] - nxt))

        memo[(pos, num)] = res
        return res


