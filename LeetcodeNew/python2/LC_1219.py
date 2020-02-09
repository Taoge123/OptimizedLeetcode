


class SolutionTony:
    def __init__(self):
        self.res = 0

    def getMaximumGold(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                self.helper(grid, i, j, 0, visited)

        return self.res

    def helper(self, grid, i, j, count, visited):
        m, n = len(grid), len(grid[0])
        if i< 0 or j < 0 or i >= m or j >= n or visited[i][j] or not grid[i][j]:
            return
        visited[i][j] = True
        count += grid[i][j]
        self.res = max(self.res, count)
        self.helper(grid, i - 1, j, count, visited)
        self.helper(grid, i + 1, j, count, visited)
        self.helper(grid, i, j - 1, count, visited)
        self.helper(grid, i, j + 1, count, visited)
        visited[i][j] = False
        count -= grid[i][j]





class Solution:
    def getMaximumGold(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for j in range(n):
            for i in range(m):
                res = max(res, self.helper(grid, i, j, 0))
        return res

    def helper(self, grid, i, j, summ):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or not grid[i][j] or grid[i][j] > 100:
            return summ
        summ += grid[i][j]
        grid[i][j] += 1000
        maxi = 0
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            maxi = max(self.helper(grid, x, y, summ), maxi)

        grid[i][j] -= 1000
        return maxi









