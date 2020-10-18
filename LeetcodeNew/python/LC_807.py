
class Solution:
    def maxIncreaseKeepingSkyline(self, grid) -> int:
        n = len(grid[0])
        row = [0] * n
        col = [0] * n

        for i in range(n):
            for j in range(n):
                row[i] = max(row[i], grid[i][j])
                col[j] = max(col[j], grid[i][j])

        res = 0
        for i in range(n):
            for j in range(n):
                res += min(row[i], col[j]) - grid[i][j]
        return res




