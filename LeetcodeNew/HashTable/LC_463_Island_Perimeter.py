
"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

"""

"""
这题直接暴力求解了，对于每个格子，检查与其相邻的4个格子：

如果格子超出边界，则周长+1；否则
如果格子是水，则周长+1
这样最终得到的周长就是结果了。
"""

class Solution0:
    def islandPerimeter(self, grid):
        def is_water(i, j):
            return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0

        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        perimeter = 0
        for (i, row) in enumerate(grid):
            for (j, item) in enumerate(row):
                if item == 1:
                    for direction in directions:
                        if is_water(i + direction[0], j + direction[1]):
                            perimeter += 1
        return perimeter
class Solution1:
    def islandPerimeter(self, grid):
        if not grid:
            return 0

        def sum_adjacent(i, j):
            adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
            res = 0
            for x, y in adjacent:
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
                    res += 1
            return res

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += sum_adjacent(i, j)
        return count

class Solution2:
    def islandPerimeter(self, grid):

        s, m = len(grid), len(grid[0])
        ans = 0
        for x in xrange(s):
            for y in xrange(m):
                if grid[x][y] == 1:
                    ans += 4
                    if x < s - 1 and grid[x + 1][y] == 1:
                        ans -= 2
                    if y < m - 1 and grid[x][y + 1] == 1:
                        ans -= 2

        return ans



class Solution3:
    def islandPerimeter(self, grid):

        m, n = len(grid), len(grid[0])
        num = 0

        for r in xrange(m):
            for c in xrange(n):
                if grid[r][c] == 1:
                    if r == 0 or grid[r-1][c] == 0:
                        num += 1
                    if r == m-1 or grid[r+1][c] == 0:
                        num += 1
                    if c == 0 or grid[r][c-1] == 0:
                        num += 1
                    if c == n-1 or grid[r][c+1] == 0:
                        num += 1
        return num




