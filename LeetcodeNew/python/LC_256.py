"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
             Minimum cost: 2 + 5 + 3 = 10.

"""


class Solution:
    def minCost(self, costs) -> int:

        if not costs:
            return 0

        m, n = len(costs), len(costs[0])

        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0] = costs[0]
        for i in range(1, m):
            dp[i][0] = costs[i][0] + min(dp[ i -1][1:])
            dp[i][1] = costs[i][1] + min(dp[ i -1][0], dp[ i -1][2])
            dp[i][2] = costs[i][2] + min(dp[ i -1][:2])

        return min(dp[-1])


class Solution:
    def minCost(self, costs) -> int:

        if not costs:
            return 0

        m, n = len(costs), len(costs[0])

        dp = [[0 for i in range(n)] for i in range(2)]

        dp[0] = costs[0]
        for i in range(1, m):
            dp[i % 2][0] = costs[i][0] + min(dp[(i - 1) % 2][1:])
            dp[i % 2][1] = costs[i][1] + min(dp[(i - 1) % 2][0], dp[(i - 1) % 2][2])
            dp[i % 2][2] = costs[i][2] + min(dp[(i - 1) % 2][:2])

        return min(dp[(m - 1) % 2])


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n = len(costs)
        r, b, g = costs[0]

        for i in range(1, n):
            r, b, g = min(b, g) + costs[i][0], min(r, g) + costs[i][1], min(r, b) + costs[i][2]

        return min(r, g, b)


