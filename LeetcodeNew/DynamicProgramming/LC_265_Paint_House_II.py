
"""
其状态转移方程应为：　dp[i][j] = min(dp[i-1].begin(), dp[i-1].end()) + costs[i][j], 并且列不为j．


There are a row of n houses, each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color 0;
costs[1][2] is the cost of painting house 1 with color 2,
and so on... Find the minimum cost to paint all houses.

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
"""
This is a Markov Chain (dp) with k states (color 1, color 2...color k) and n stages, 
we simply update the costs matrix to keep track of the optimal value for each state at current stage.
min1 means we paint all other states with the minimum cost, 
while min2 means we cannot paint consecutive houses with same color so we choose the second lowest cost to add up with.
"""
class Solution1:
    def minCostII(self, costs):
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        for i in xrange(1, n):
            min1 = min(costs[i-1])
            idx = costs[i-1].index(min1)
            min2 = min(costs[i-1][:idx] + costs[i-1][idx+1:])
            for j in xrange(k):
                if j == idx:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        return min(costs[-1])


# A straight-forward version of DP implementation is this:
class Solution2:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]: return 0
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                costs[i][j] += min(costs[i - 1][:j] + costs[i - 1][j + 1:])
        return min(costs[-1])

# To avoid the redundany in min(costs[i - 1][:j] + costs[i - 1][j + 1:]), we can calculate the two least numbers in advance.
class Solution22:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]: return 0
        for i in range(1, len(costs)):
            dp = sorted(costs[i - 1])[:2]
            for j in range(len(costs[0])):
                costs[i][j] += dp[costs[i - 1][j] == dp[0]]
        return min(costs[-1])


class SolutionCaikehe:
    # dp, O(nk) space
    def minCostII1(self, costs):
        if not costs:
            return 0
        r, c = len(costs), len(costs[0])
        dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
        dp[0] = costs[0]
        for i in xrange(1, r):
            for j in xrange(c):
                dp[i][j] = costs[i][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1:])
        return min(dp[-1])

    # dp, O(k) space
    def minCostII(self, costs):
        if not costs:
            return 0
        r, c = len(costs), len(costs[0])
        cur = costs[0]
        for i in xrange(1, r):
            pre = cur[:]  # take care here
            for j in xrange(c):
                cur[j] = costs[i][j] + min(pre[:j] + pre[j + 1:])
        return min(cur)



class Solution3:
    def minCostII(self, costs):
        if not costs:
            return 0

        n = len(costs)
        m = len(costs[0])

        dp = costs[0]

        for i in range(1, n):
            left = [float("inf") for _ in range(m)]
            right = [float("inf") for _ in range(m)]

            for j in range(1, m):
                left[j] = min(left[j - 1], dp[j - 1])
            for j in range(m - 2, -1, -1):
                right[j] = min(right[j + 1], dp[j + 1])
            for j in range(m):
                dp[j] = min(left[j], right[j]) + costs[i][j]

        return min(dp)





