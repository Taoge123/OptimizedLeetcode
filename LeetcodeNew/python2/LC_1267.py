
class SolutionDFS:
    def countServers(self, grid):

        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            grid[i][j] = 0
            total = 1
            for row in range(m):
                if grid[row][j] == 1:
                    total += dfs(row, j)
            for col in range(n):
                if grid[i][col] == 1:
                    total += dfs(i, col)
            return total

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = dfs(i, j)
                    if count > 1:
                        res += count
        return res




class Solution:
    def countServers(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        row = [0] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1):
                    res += 1

        return res



