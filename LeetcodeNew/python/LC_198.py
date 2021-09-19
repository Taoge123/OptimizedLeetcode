"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

"""


class SolutionTony1:
    def rob(self, nums) -> int:

        memo = {}
        return self.dfs(nums, 0, memo)

    def dfs(self, nums, i, memo):

        if i in memo:
            return memo[i]

        if i >= len(nums):
            return 0

        rob = self.dfs(nums, i + 2, memo) + nums[i]
        no_rob = self.dfs(nums, i + 1, memo)

        memo[i] = max(rob, no_rob)
        return memo[i]



class SolutionTD:
    def rob(self, nums) -> int:
        if not nums:
            return 0

        memo = {}
        return self.dfs(nums, len(nums) - 1, memo)

    def dfs(self, nums, i, memo):
        if i < 0:
            return 0
        if i in memo:
            return memo[i]

        res = max(self.dfs(nums, i - 1, memo), self.dfs(nums, i - 2, memo) + nums[i])
        memo[i] = res
        return memo[i]



class SolutionTD2:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        memo = {}
        return self.dfs(nums, 0, memo)

    def dfs(self, nums, pos, memo):
        n = len(nums)
        if pos > n:
            return 0
        if pos in memo:
            return memo[pos]

        res = 0
        for i in range(pos, len(nums)):
            res = max(res, nums[i] + self.dfs(nums, i + 2, memo))
        memo[pos] = res
        return res



class Solution:
    def rob(self, nums) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        res = dp[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            if dp[i] > res:
                res = dp[i]
        return res


class Solution1:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        cur = nums[0]
        pre = max(nums[:2])
        for i in range(2, len(nums)):
            cur = max(cur + nums[i], pre)
            cur, pre = pre, cur
        return pre


class Solution2:
    def rob(self, nums):
        rob = noRob = 0
        for i in range(len(nums)):
            rob, noRob = max(nums[i] + noRob, rob), rob
        return rob



nums = [2,7,9,3,1]
a = Solution()
print(a.rob(nums))




