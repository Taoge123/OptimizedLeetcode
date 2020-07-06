
"""
if T > 0: ATTTTTTB -> TTTTTT必须是+
if T < 0: AB


"""


class Solution:
    def kConcatenationMaxSum(self, arr, k: int) -> int:
        if not arr:
            return 0
        summ = sum(arr)
        mod = 10 ** 9 + 7
        if k == 1:
            return max(0, self.kadane(arr)) % mod
        else:
            return max(0, (k - 2) * max(summ, 0) + self.kadane(arr + arr)) % mod

    def kadane(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)





