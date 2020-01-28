"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""
"""
This question is very similar to the Max Area of Island question but here instead of counting the area for each island, we find out the shape of each island.

The shape of the island can be represented by taking the relative position of the connected cells from the leftmost cell on the top row of the island
(the first cell of each island we will visit). For each island we visit, we are guaranteed to visit the top row's leftmost cell first if we iterate the matrix row by row,
left to right direction. We will get the same order of cells for islands of the same shape if we perform the search in a consistent manner.

Here are some examples of how to represent the shape of each island by using cell positions relative to the top left cell.

# First coordinate is row difference,
# Second coordinate is column difference.
11 -> ((0, 1)) # One cell to the right

11 -> ((0, 1), (1, 1)) # One cell to the right, one cell to the right and bottom
01
"""


class Solution1:
    def numDistinctIslands(self, grid):
        steps = []
        distinctIslands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # 'o' for origin
                    self.dfs(grid, i, j, 'o', steps)
                    distinctIslands.add(''.join(steps))
                    steps = []
        print(distinctIslands)
        return len(distinctIslands)

    def dfs(self, grid, i, j, direct, steps):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            steps.append(direct)
            grid[i][j] = 0
            self.dfs(grid, i + 1, j, 'd', steps)  # down
            self.dfs(grid, i - 1, j, 'u', steps)  # upper
            self.dfs(grid, i, j + 1, 'r', steps)  # right
            self.dfs(grid, i, j - 1, 'l', steps)  # left
            steps.append('b')  # back


class Solution2:
    def numDistinctIslands(self, grid):
        islands = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    self.dfs(i, j, path, (0, 0), grid)
                    islands.add(tuple(path))
        return len(islands)

    def dfs(self, i, j, path, pos, grid):
        grid[i][j] = -1
        m, n = len(grid), len(grid[0])
        for direction in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            x, y = i + direction[0], j + direction[1]
            if (0 <= x < m and 0 <= y < n) and grid[x][y] == 1:
                nxt = (pos[0] + direction[0], pos[1] + direction[1])
                path.append(nxt)
                self.dfs(x, y, path, nxt, grid)











