class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        grid = [[N] * N for i in range(N)]

        for mine in mines:
            grid[mine[0]][mine[1]] = 0

        for i in range(N):
            l, r, u, d = 0, 0, 0, 0
            for j, k in zip(range(N), reversed(range(N))):
                l = l + 1 if grid[i][j] else 0
                grid[i][j] = min(grid[i][j], l)

                r = r + 1 if grid[i][k] else 0
                grid[i][k] = min(grid[i][k], r)

                u = u + 1 if grid[j][i] else 0
                grid[j][i] = min(grid[j][i], u)

                d = d + 1 if grid[k][i] else 0
                grid[k][i] = min(grid[k][i], d)

        res = 0
        for i in range(N):
            for j in range(N):
                if res < grid[i][j]:
                    res = grid[i][j]

        return res



