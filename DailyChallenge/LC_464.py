
class Solution:
    def canIWin(self, n: int, target: int) -> bool:
        if n * ( n +1) // 2 < target:
            return False
        memo = {}
        nums = [i for i in range(1, n+ 1)]
        return self.dfs(nums, target, memo)

    def dfs(self, nums, target, memo):
        if tuple(nums) in memo:
            return memo[tuple(nums)]

        if not nums:
            return False

        if nums[-1] >= target:
            return True

        for i in range(len(nums)):
            if not self.dfs(nums[:i] + nums[i + 1:], target - nums[i], memo):
                memo[tuple(nums)] = True
                return memo[tuple(nums)]

        memo[tuple(nums)] = False
        return memo[tuple(nums)]


