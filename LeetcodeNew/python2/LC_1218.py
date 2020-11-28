
import collections

class Solution:
    def longestSubsequence(self, arr, diff: int) -> int:
        dp = collections.defaultdict(int)

        res = 0

        for num in arr:
            dp[num] = dp[num - diff] + 1

        return max(dp.values())




