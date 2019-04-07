
"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

"""
class Solution1:
    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)


class Solution2:
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-2:])


class Solution3:
    def minCostClimbingStairs(self, cost):

        cost.append(0)
        for i in range(2,len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return cost[-1]

class Solution4:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        cost.append(0)
        dp = [0] * (n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(n+1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return dp[n]



