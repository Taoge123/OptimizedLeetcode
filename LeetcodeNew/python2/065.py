
class Solution:
    def minPathSum(self, grid):
        if not grid:
            return
        m, n = len(grid) ,len(grid[0])
        cur = [0] * n
        cur[0] = grid[0][0]

        for j in range(1, n):
            cur[j] = cur[ j -1] + grid[0][j]
        for i in range(1, m):
            cur[0] += grid[i][0]
            for j in range(1, n):
                cur[j] = min(cur[ j -1], cur[j]) + grid[i][j]
        return cur[-1]







