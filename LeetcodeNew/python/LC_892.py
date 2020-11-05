
class Solution:
    def surfaceArea(self, grid) -> int:
        n = len(grid)
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    res += 2
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        x = i + dx
                        y = j + dy
                        if x< 0 or x >= n or y < 0 or y >= n:
                            val = 0
                        else:
                            val = grid[x][y]

                        res += max(grid[i][j] - val, 0)
        return res



