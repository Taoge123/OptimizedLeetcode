"""
https://www.youtube.com/watch?v=tXrCgWR7maQ
"""


class Solution:
    def largest1BorderedSquare(self, grid) -> int:

        m, n = len(grid), len(grid[0])

        top = [a[:] for a in grid]
        left = [a[:] for a in grid]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i:
                        top[i][j] = top[i - 1][j] + 1
                    if j:
                        left[i][j] = left[i][j - 1] + 1

        for k in range(min(m, n), 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if min(top[i + k - 1][j], top[i + k - 1][j + k - 1], left[i]
                    [j + k - 1], left[i + k - 1][j + k - 1]) >= k:
                        return k * k

        return 0









