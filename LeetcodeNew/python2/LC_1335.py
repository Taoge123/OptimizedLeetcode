
"""
https://www.youtube.com/watch?v=eRBpfoWujQM

本题翻译成人话就是：将数组分成d个subarray，最小化“每个subarray最大值的和”。

因为题意明确要求分成若干个subarray，这非常强烈地暗示了这是我所归纳的第一类区间型DP解法。具体的状态定义就是dp[i][k]代表将前i个工作分配在k天内完成的最优 解（即最小化“每个subarray最大值的和”）。
状态转移的核心就是判断最后一个subarray的起始点在哪里，找到最优的下标j，使得dp[i][k]分解为dp[j-1][k-1]和arr[j:i]两个子问题，然后相加。

本题中，处理arr[j:i]所需要做的就是找到其中的最大值。所以我们将j从后往前搜索比较方便，可以顺便将这个arr[j:i]区间内的最大值给一路更新了。

整体的时间复杂度就是o(NND).

813
1278

for i in range(1, n+1):
    for k in range(1, min(d, i) + 1):
        for j in range(1, i+1):
            dp[i][k] = min(dp[i][k], dp[j-1][k-1] + max(j:i))

"""

"""
for i in range(1, n+1):
    for k in range(1, min(d, i) + 1):
        for j in range(1, i+1):
            dp[i][k] = min(dp[i][k], dp[j-1][k-1] + max(j:i))

"""


class Solution:
    def minDifficulty(self, nums, d: int) -> int:
        n = len(nums)
        if d > n:
            return -1
        dp = [[float('inf') for i in range(d + 1)] for j in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for k in range(1, min(d, i) + 1):
                maxi = 0
                for j in range(i - 1, k - 2, -1):
                    maxi = max(maxi, nums[j])
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + maxi)

        return dp[n][d]



