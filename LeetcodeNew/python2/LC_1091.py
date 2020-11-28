class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        queue = [(0, 0, 1)]
        for i, j, step in queue:
            if i == n - 1 and j == n - 1:
                return step
            for x, y in ((i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                         (i + 1, j + 1)):
                if x >= 0 and y >= 0 and x < n and y < n and not grid[x][y]:
                    grid[x][y] = 1
                    queue.append((x, y, step + 1))

        return -1



