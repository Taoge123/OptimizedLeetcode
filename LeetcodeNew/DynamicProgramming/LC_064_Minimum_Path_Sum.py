
"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution1:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


class Solution11:
    def minPathSum(self, g):
        m = len(g)
        n = len(g[0])
        if m < 1:
            return 0

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j > 0:
                    g[i][j] += g[i][j - 1]
                elif j == 0 and i > 0:
                    g[i][j] += g[i - 1][j]
                else:
                    g[i][j] += min(g[i - 1][j], g[i][j - 1])
        return g[-1][-1]



class SolutionCaikehe:
    # O(m*n) space
    def minPathSum(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = grid[0][0]
        for i in range(1, r):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, c):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

    # O(2*n) space
    def minPathSum2(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        pre = cur = [0] * c
        pre[0] = grid[0][0]
        for i in range(1, c):
            pre[i] = pre[i - 1] + grid[0][i]
        for i in range(1, r):
            cur[0] = pre[0] + grid[i][0]
            for j in range(1, c):
                cur[j] = min(cur[j - 1], pre[j]) + grid[i][j]
            pre = cur
        return cur[-1]

    # O(n) space
    def minPathSum(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        cur = [0] * c
        cur[0] = grid[0][0]
        for i in range(1, c):
            cur[i] = cur[i - 1] + grid[0][i]
        for i in range(1, r):
            cur[0] += grid[i][0]
            for j in range(1, c):
                cur[j] = min(cur[j - 1], cur[j]) + grid[i][j]
        return cur[-1]

    # change the grid itself
    def minPathSum4(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        for i in range(1, c):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, r):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


"""

Dynamic Programming using Memoization

Start Point: 0, 0. Destination Point: M-1, N-1
Cost[i,j]: The cost to reach destination from (i,j). Matrix is initialized to inf.
The solution will be cost(0,0)
Initialize the cost matrix with boundary condition. cost[M-1,N-1]=grid[M-1,N-1]
Be careful with what you return for out of bound grid points. Make sure you return infinity so that they are ignored within the min equation
Time and Space Complexity: O(MN)
"""

class Solution2:
    def helper(self, x, y, grid, cost):
        M, N = len(grid), len(grid[0])
        if x == M or y == N:
            return float('inf')
        elif cost[x][y] != -1:
            return cost[x][y]
        else:
            right, down = self.helper(x, y + 1, grid, cost), self.helper(x + 1, y, grid, cost)
            cost[x][y] = min(right, down) + grid[x][y]
        return cost[x][y]

    def minPathSum(self, grid):

        M, N = len(grid), len(grid[0])
        cost = [[-1] * N for _ in range(M)]
        cost[M - 1][N - 1] = grid[M - 1][N - 1]
        return self.helper(0, 0, grid, cost)


"""
Dynamic Programming: O(MN) space

Start Point: 0, 0. Destination Point: M-1, N-1
Cost[i,j]: The cost to reach (i,j) from (0,0). We initialize
The solution will be cost(M-1,N-1)
Time & Space Complexity:O(MN)
"""

class Solution3:
    def minPathSum(self, grid):

        M, N = len(grid), len(grid[0])
        cost = [[0]*N for _ in range(M)]
        cost[0][0] = grid[0][0]
        for j in range(1,N):
            cost[0][j] = grid[0][j] + cost[0][j-1]
        for i in range(1,M):
            cost[i][0] = grid[i][0] + cost[i-1][0]
        for i in range(1,M):
            for j in range(1,N):
                cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]
        return cost[M-1][N-1]


"""
Dynamic Programming: Using O(N) space

Space complexity can be reduced to O(N) since we only require the previous row to compute the current row.
Note that we initialize the cost array to inf. Note how we initialize cost[0] at every row iteration.
"""
class Solution4:
    def minPathSum(self, grid):

        M, N = len(grid), len(grid[0])
        cost = [float('inf')]*N
        for i in range(M):
            cost[0] = grid[i][0] + cost[0] if i > 0 else grid[i][0]
            for j in range(1,N):
                cost[j] = min(cost[j-1], cost[j]) + grid[i][j]
        return cost[-1]


"""
Dynamic Programming: Using O(1) space

Space complexity can be reduced to O(1) as grid can be reused as cost matrix
Notice how we iterate the two loops and the special condition we use for i=0
"""

class Solution5:
    def minPathSum(self, grid):

        M, N = len(grid), len(grid[0])
        for i in range(M):
            grid[i][0] = grid[i][0] + grid[i-1][0] if i > 0 else grid[i][0]
            for j in range(1,N):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j] if i > 0 else grid[i][j-1]+grid[i][j]
        return grid[-1][-1]



