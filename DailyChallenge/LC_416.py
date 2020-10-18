
class Solution:
    def canPartition(self, nums) -> bool:
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        nums.sort()
        memo = {}
        target = summ // 2

        return self.dfs(nums, 0, 0, target, memo)

    def dfs(self, nums, idx, cur, target, memo):
        if (cur, idx) in memo:
            return memo[(cur, idx)]

        if cur == target:
            return True

        # if idx == len(nums):
        #     return False

        for i in range(idx, len(nums)):
            if self.dfs(nums, i+ 1, cur + nums[i], target, memo):
                memo[cur, idx] = True
                return memo[cur, idx]
        memo[cur, idx] = False
        return memo[cur, idx]

