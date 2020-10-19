
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



class SolutionWisdom:
    def canPartition(self, nums) -> bool:
        summ = sum(nums)
        if summ % 2 == 1:
            return False

        target = summ // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            old_dp = copy.copy(dp)
            for i in range(target + 1):
                if i >= num:
                    dp[i] = dp[i] or old_dp[i - num]

        return dp[-1]


class SolutionReversed:
    def canPartition(self, nums) -> bool:
        summ = sum(nums)
        if summ % 2 == 1:
            return False

        target = summ // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # old_dp = copy.copy(dp)
            for i in reversed(range(target + 1)):
                if i >= num:
                    dp[i] = dp[i] or dp[i - num]

        return dp[-1]

