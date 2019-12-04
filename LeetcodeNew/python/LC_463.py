
"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
"""


class Solution:
    def islandPerimeter(self, grid):
        if not grid:
            return 0

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += self.helper(grid, i, j)
        return res

    def helper(self, grid, i, j):
        adjacent = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        count = 0

        for x, y in adjacent:
            if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
                count += 1
        return count



class Solution2:
    def islandPerimeter(self, grid):

        res = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if i < m - 1 and grid[i + 1][j] == 1:
                        res -= 2
                    if j < n - 1 and grid[i][j + 1] == 1:
                        res -= 2
        return res










