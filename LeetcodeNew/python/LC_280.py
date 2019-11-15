"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]

"""


class Solution:
    def numSquares(self, n):
        dp = [n ] *( n +1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+ 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]




