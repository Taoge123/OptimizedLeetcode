
class Solution:
    def rob(self, nums):
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        res = dp[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[ i -2] + nums[i], dp[ i -1])
            if dp[i] > res:
                res = dp[i]
        return res



