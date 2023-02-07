"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

"""


class SolutionTony:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(self.dfs(nums[1:], 0, {}), self.dfs(nums[:-1], 0, {}))

    def dfs(self, nums, i, memo):
        if i in memo:
            return memo[i]

        if i >= len(nums):
            return 0

        rob = self.dfs(nums, i + 2, memo) + nums[i]
        no_rob = self.dfs(nums, i + 1, memo)

        memo[i] = max(rob, no_rob)
        return memo[i]



class SolutionTonyAnother:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        memo = {}
        a = self.dfs(nums[:-1], 0, False, memo)
        memo = {}
        b = self.dfs(nums[1:], 0, False, memo)
        return max(a, b)

    def dfs(self, nums, i, robbed, memo):
        n = len(nums)
        if (i, robbed) in memo:
            return memo[(i, robbed)]
        if i >= n:
            return 0
        no_rob = 0
        robbing = 0
        # If we robbed before, then we can't rob this time
        no_rob = self.dfs(nums, i + 1, False, memo)
        # if we did not robbed, then we cna either rob or not rob this time
        if not robbed:
            robbing = self.dfs(nums, i + 1, True, memo) + nums[i]
        memo[(i, robbed)] = max(robbing, no_rob)
        return memo[(i, robbed)]

class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        res = dp[1]

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i -1])
            if dp[i] > res:
                res = dp[i]
        return res



class Solution2:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, nums):
        rob = noRob = 0
        for i in range(len(nums)):
            rob, noRob = max(nums[i] + noRob, rob), rob
        return rob







