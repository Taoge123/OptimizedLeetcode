
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

import collections


class SolutionTonyDFS2:
    def islandPerimeter(self, grid):

        visited = set()
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            elif grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            res = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                res += dfs(x, y)
            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j)



class SolutionBFS:
    def islandPerimeter(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                    count += 1
        return count



class SolutionTonyDFS:
    def islandPerimeter(self, grid):

        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return self.dfs(grid, i, j, visited)

    def dfs(self, grid, i, j, visited):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[i]) - 1:
            return 1
        elif grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        res = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = i + dx
            y = j + dy
            res += self.dfs(grid, x, y, visited)
        return res




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










