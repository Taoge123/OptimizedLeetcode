# DP, O(n) space
def maxSubArray(self, nums):
    if not nums:
        return None
    dp = [0] * len(nums)
    res = dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        res = max(res, dp[i])
    return res


# DP, constant space
def maxSubArray2(self, nums):
    if not nums:
        return None
    loc = glo = nums[0]
    for i in xrange(1, len(nums)):
        loc = max(loc + nums[i], nums[i])
        glo = max(loc, glo)
    return glo