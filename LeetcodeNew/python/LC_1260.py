class Solution:
    def shiftGrid(self, grid, k: int):
        m, n = len(grid), len(grid[0])

        for _ in range(k):
            # Create a new grid to copy into.
            new_grid = [[0] * n for _ in range(m)]

            # Case 1: Move everything not in the last column.
            for row in range(m):
                for col in range(n - 1):
                    new_grid[row][col + 1] = grid[row][col]

            # Case 2: Move everything in last column, but not last row.
            for row in range(m - 1):
                new_grid[row + 1][0] = grid[row][n - 1]

            # Case 3: Move the bottom right.
            new_grid[0][0] = grid[m - 1][n - 1]

            grid = new_grid

        return grid





class Solution2:
    def shiftGrid(self, grid, k: int):
        m, n = len(grid), len(grid[0])
        for _ in range(k):
            prev = grid[-1][-1]
            for row in range(m):
                for col in range(n):
                    temp = grid[row][col]
                    grid[row][col] = prev
                    prev = temp

        return grid


