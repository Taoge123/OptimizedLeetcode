"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""



# can't use inner function since we need memo.values()
class SolutionTD:
    def maxSubArray(self, nums) -> int:
        memo = {}
        self.dfs(nums, 0, memo)
        return max(memo.values())

    def dfs(self, nums, i, memo):
        if i in memo:
            return memo[i]

        if i == len(nums):
            return 0

        res = max(nums[i], nums[i] + self.dfs(nums, i + 1, memo))
        memo[i] = res
        return res



class Solution:
    def maxSubArray(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)



