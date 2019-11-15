
class Solution:
    def maxSubArray(self, nums):

        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[ i -1 ] +nums[i], nums[i])
        return max(dp)



