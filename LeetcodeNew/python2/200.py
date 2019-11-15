
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        self.directions = [(-1, 0) ,(1, 0) ,(0, -1) ,(0, 1)]
        visited = [[False for i in range(n)] for j in range(m)]
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not visited[r][c]:
                    res += 1
                    self.dfs(r, c, grid, m, n, visited)

        return res

    def dfs(self, r, c, grid, m, n, visited):
        if r< 0 or c < 0 or r >= m or c >= n or grid[r][c] != '1' or visited[r][c]:
            return
        visited[r][c] = True
        for direction in self.directions:
            x, y = r + direction[0], c + direction[1]
            self.dfs(x, y, grid, m, n, visited)







