
"""
dp[i]: the cost for the first i days you can travel
dp[8] = 9
dp[9] = dp[8]
dp[10] = dp[9]

if i not in days:
    dp[i] = dp[i-1]

dp[i] = min(dp[i-1]+cost[0], dp[i-7]+cost[1], dp[i-30]+cost[2])

"""


class Solution:
    def mincostTickets(self, days, costs):
        dp = [0] * 366
        for i in range(366):
            if i not in days:
                dp[i] = dp[i - 1]
                continue
            dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
        return dp[-1]



