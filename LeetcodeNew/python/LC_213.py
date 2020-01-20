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







