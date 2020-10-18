class SolutionTLE:
    def largestIsland(self, grid) -> int:
        res = -1
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    visited = [[False for i in range(n)] for j in range(m)]
                    res = max(res, self.dfs(grid, i, j, visited))
                    grid[i][j] = 0
        return res if res != -1 else m * n

    def dfs(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or visited[i][j]:
            return 0

        visited[i][j] = True
        count = self.dfs(grid, i - 1, j, visited) + \
                self.dfs(grid, i + 1, j, visited) + \
                self.dfs(grid, i, j - 1, visited) + \
                self.dfs(grid, i, j + 1, visited) + 1
        return count


