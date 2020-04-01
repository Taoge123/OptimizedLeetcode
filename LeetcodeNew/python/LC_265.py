"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Follow up:
Could you solve it in O(nk) runtime?

"""


class Solution:
    def minCostII(self, costs) -> int:

        if not costs:
            return 0

        m, n = len(costs) ,len(costs[0])

        dp = costs[0]
        for i in range(1, m):
            pre = dp[:]
            for j in range(n):
                dp[j] = costs[i][j] + min(pre[:j] + pre[j+1:])
        return min(dp)



class Solution:
    def minCostII(self, costs) -> int:

        if not costs:
            return 0

        m, n = len(costs), len(costs[0])

        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0] = costs[0]
        for i in range(1, m):
            for j in range(n):
                temp = dp[i-1][:j] + dp[i-1][j+1:]
                dp[i][j] = costs[i][j] + min(temp)
        return min(dp[-1])



class Solution:
    def minCostII(self, costs) -> int:

        if not costs:
            return 0

        m, n = len(costs), len(costs[0])

        dp = [0 for i in range(n)]
        dp = costs[0]
        for i in range(1, m):
            dpCopy = dp[:]
            for j in range(n):
                temp = dpCopy[:j] + dpCopy[j+1:]
                dp[j] = costs[i][j] + min(temp)
        return min(dp)

costs = [[1,5,3],
         [2,9,4],
         [3,3,3],
         [4,5,6],
         ]

a = Solution()
print(a.minCostII(costs))




