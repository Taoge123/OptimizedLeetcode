
class Solution:
    def getMaximumGold(self, grid) -> int:
        self.res = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                self.helper(grid, i, j, m, n, 0, visited)
        return self.res

    def helper(self, grid, i, j, m, n, count, visited):
        if i < 0 or j < 0 or i >= m or j >= n or visited[i][j] or not grid[i][j]:
            return
        visited[i][j] = True
        count += grid[i][j]
        self.res = max(self.res, count)
        self.helper(grid, i + 1, j, m, n, count, visited)
        self.helper(grid, i - 1, j, m, n, count, visited)
        self.helper(grid, i, j + 1, m, n, count, visited)
        self.helper(grid, i, j - 1, m, n, count, visited)
        visited[i][j] = False
        count -= grid[i][j]


