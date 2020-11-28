class SolutionTony:
    def closedIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                if self.dfs(grid, i, j, m, n) == 0:
                    res += 1
        return res

    def dfs(self, grid, i, j, m, n):
        #reach perimeter, then return 1, so this is not a closed island
        if i < 0 or j < 0 or i >= m or j >= n:
            return 1

        if grid[i][j] != 0:
            return 0

        grid[i][j] = -1

        up = self.dfs(grid, i - 1, j, m, n)
        down = self.dfs(grid, i + 1, j, m, n)
        left = self.dfs(grid, i, j - 1, m, n)
        right = self.dfs(grid, i, j + 1, m, n)

        return up or down or left or right





class Solution:
    def closedIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(grid, i, j, m, n):
            if i< 0 or j < 0 or i >= m or j >= n:
                return 1

            if grid[i][j] != 0:
                return 0

            grid[i][j] = -1

            up = dfs(grid, i - 1, j, m, n)
            down = dfs(grid, i + 1, j, m, n)
            left = dfs(grid, i, j - 1, m, n)
            right = dfs(grid, i, j + 1, m, n)

            return up or down or left or right

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                if dfs(grid, i, j, m, n) == 0:
                    res += 1

        return res



