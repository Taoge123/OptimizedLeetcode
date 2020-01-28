
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res.append(self.dfs(grid, i, j, m, n))

        return max(res) if res else 0

    def dfs(self, grid, i, j, m, n):
        if i >= 0 and i < m and j >= 0 and j < n and grid[i][j]:
            grid[i][j] = 0
            return self.dfs(grid, i - 1, j, m, n) \
                   + self.dfs(grid, i + 1, j, m, n) \
                   + self.dfs(grid, i, j - 1, m, n) \
                   + self.dfs(grid, i, j + 1, m, n) + 1
        return 0



