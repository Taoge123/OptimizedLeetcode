
"""
There are a row of n houses, each house can be painted with one of the three colors:
red, blue or green. The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color red;
costs[1][2] is the cost of painting house 1 with color green, and so on...
Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
             Minimum cost: 2 + 5 + 3 = 10.

"""

class SolutionCaikehe:
    # O(n*3) space
    def minCost1(self, costs):
        if not costs:
            return 0
        r, c = len(costs), len(costs[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0] = costs[0]
        for i in range(1, r):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1:3])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][:2])
        return min(dp[-1])

    # change original matrix
    def minCost2(self, costs):
        if not costs:
            return 0
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1:3])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][:2])
        return min(costs[-1])

    # O(1) space
    def minCost3(self, costs):
        if not costs:
            return 0
        dp = costs[0]
        for i in range(1, len(costs)):
            pre = dp[:]  # here should take care
            dp[0] = costs[i][0] + min(pre[1:3])
            dp[1] = costs[i][1] + min(pre[0], pre[2])
            dp[2] = costs[i][2] + min(pre[:2])
        return min(dp)

    # O(1) space, shorter version, can be applied
    # for more than 3 colors
    def minCost(self, costs):
        if not costs:
            return 0
        dp = costs[0]
        for i in range(1, len(costs)):
            pre = dp[:]  # here should take care
            for j in range(len(costs[0])):
                dp[j] = costs[i][j] + min(pre[:j] + pre[j + 1:])
        return min(dp)



class Solution2:
    class Solution(object):
        def minCost(self, costs):
            if not costs:
                return 0

            for i, cost in enumerate(costs[1:], 1):
                costs[i][0] = min(costs[i - 1][1], costs[i - 1][2]) + cost[0]
                costs[i][1] = min(costs[i - 1][0], costs[i - 1][2]) + cost[1]
                costs[i][2] = min(costs[i - 1][0], costs[i - 1][1]) + cost[2]

            return min(costs[-1])


# Very Basic DP solution
class Solution3:
    # time complexity O(n), space complexity O(n)
    def minCost(self, costs):

        length = len(costs)
        dp = [[0] * 3 for _ in range(length + 1)]
        for i in range(1, length + 1):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i - 1][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i - 1][1]
            dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + costs[i - 1][2]
        return min(dp[-1])


# Better DP solution, space complexity is reduced to O(1)
class Solution4:
    def minCost(self, costs):

        red, blue, green = 0, 0, 0
        for redCur, blueCur, greenCur in costs:
            red = min(blue, green) + redCur
            blue = min(red, green) + blueCur
            green = min(red, blue) + greenCur
        return min([red, blue, green])


