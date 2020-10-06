import collections


class Solution:
    def countCornerRectangles(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(n)]
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                for k in range(j + 1, n):
                    if grid[i][k] == 1:
                        res += dp[j][k]
                        dp[j][k] += 1
        return res


class SolutionSlow:
    def countCornerRectangles(self, grid) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m - 1):
            for j in range(i + 1, m):
                count = 0
                for k in range(n):
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        count += 1
                res += count * (count - 1) // 2
        return res


class Solution:
    def countCornerRectangles(self, grid):
        count = collections.Counter()
        res = 0
        for row in grid:
            for i, v1 in enumerate(row):
                if v1:
                    for j in range(i + 1, len(row)):
                        if row[j]:
                            res += count[i, j]
                            count[i, j] += 1
        return res

