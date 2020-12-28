import functools

class Solution:
    def findBall(self, grid):
        m, n = len(grid), len(grid[0])

        @functools.lru_cache(None)
        def dfs(col, row):
            # print(row)
            if row == m:
                return col
            nxt = col + grid[row][col]
            if 0 <= nxt < n and grid[row][nxt] + grid[row][col] != 0:
                return dfs(nxt, row + 1)
            return -1

        return [dfs(i, 0) for i in range(n)]

