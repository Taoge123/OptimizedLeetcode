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

class Solution:
    def minPathSum(self, grid):
        if not grid:
            return
        m, n = len(grid), len(grid[0])
        cur = [0] * n
        cur[0] = grid[0][0]

        for j in range(1, n):
            cur[j] = cur[j - 1] + grid[0][j]
        for i in range(1, m):
            cur[0] += grid[i][0]
            for j in range(1, n):
                cur[j] = min(cur[j - 1], cur[j]) + grid[i][j]
        return cur[-1]







