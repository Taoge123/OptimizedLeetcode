
"""
dp[i]: the cost for the first i days you can travel
dp[8] = 9
dp[9] = dp[8]
dp[10] = dp[9]

if i not in days:
    dp[i] = dp[i-1]

dp[i] = min(dp[i-1]+cost[0], dp[i-7]+cost[1], dp[i-30]+cost[2])

"""

import bisect
import functools


class SolutionTony:
    def mincostTickets(self, days, costs) -> int:
        n = len(days)
        @functools.lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0
            return min(costs[0] + dfs(bisect.bisect_left(days, days[i] + 1)),
                       costs[1] + dfs(bisect.bisect_left(days, days[i] + 7)),
                       costs[2] + dfs(bisect.bisect_left(days, days[i] + 30)))

        return dfs(0)



class SolutionTony2:
    def mincostTickets(self, days, costs) -> int:
        # if there are no days,
        if not days:
            return 0
        n = 366

        @functools.lru_cache(None)
        def dfs(i):

            # base condition where day is invalid
            if i >= n:
                return 0

            # if day is not in days calendar, obtain the cost from previous day
            if i not in days:
                return dfs(i + 1)

            # okay, day in the calendar now, obtain all possible costs
            single_day_pass = costs[0] + dfs(i + 1)
            week_pass = costs[1] + dfs(i + 7)
            month_pass = costs[2] + dfs(i + 30)

            # minimum of all three costs
            return min(single_day_pass, week_pass, month_pass)

        # figure cost at the end of calendar
        return dfs(0)


class Solution:
    def mincostTickets(self, days, costs):
        dp = [0] * 366
        for i in range(366):
            if i not in days:
                dp[i] = dp[i - 1]
                continue
            dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
        return dp[-1]



