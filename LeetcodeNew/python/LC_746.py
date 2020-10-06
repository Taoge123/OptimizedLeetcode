
class Solution1:
    def minCostClimbingStairs(self, cost):
        dp = [0] * (len(cost))
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2] + cost[i], dp[i - 1] + cost[i])

        return min(dp[-2], dp[-1])




class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        a, b = cost[0], cost[1]

        for i in range(2, len(cost)):
            cur = min(a, b) + cost[i]
            a = b
            b = cur
        return min(a, b)






