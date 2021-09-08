
"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.


Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums or not target:
            return 0
        nums.sort()
        return self.dfs(nums, target, {})

    def dfs(self, nums, target, memo):
        if not target:
            return 1
        elif nums[0] > target:
            return 0
        if target in memo:
            return memo[target]
        res = 0
        for i in range(len(nums)):
            res += self.dfs(nums, target - nums[i], memo)
        memo[target] = res
        return res


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        return self.dfs(nums, target, memo)

    def dfs(self, nums, target, memo):
        if target in memo:
            return memo[target]
        if target == 0:
            return 1
        if target < 0:
            return 0
        res = 0
        for num in nums:
            res += self.dfs(nums, target - num, memo)
        memo[target] = res
        return res



class SolutionTony:
    def combinationSum4(self, nums, target: int) -> int:

        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):

            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]




class Solution:
    def combinationSum4(self, nums, target: int) -> int:

        n = len(nums)
        nums = sorted(nums)
        dp = [1] + [0] * target
        for i in range(1, target+1):
            for num in nums:
                if i - num < 0:
                    break
                dp[i] += dp[i-num]

        return dp[target]






