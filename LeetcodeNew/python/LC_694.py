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


class SolutionTony1:
    def numDistinctIslands(self, grid):
        m, n = len(grid), len(grid[0])
        visited = set()
        res = set()

        def dfs(i, j, path):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or grid[i][j] == 0:
                return
            # grid[i][j] = 0
            visited.add((i, j))
            for dx, dy, d in [(1, 0, 'd'), (-1, 0, 'u'), (0, -1, 'l'), (0, 1, 'r')]:
                x = i + dx
                y = j + dy
                path.append(d)
                dfs(x, y, path)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    path = []
                    dfs(i, j, path)
                    res.add(tuple(path))
        return len(res)



class SolutionTony2:
    def numDistinctIslands(self, grid):
        m, n = len(grid), len(grid[0])
        res = set()

        def dfs(i, j, path):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            grid[i][j] = 0
            for dx, dy, d in [(1, 0, 'd'), (-1, 0, 'u'), (0, -1, 'l'), (0, 1, 'r')]:
                x = i + dx
                y = j + dy
                path.append(d)
                dfs(x, y, path)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, path)
                    res.add(tuple(path))
        return len(res)




class SolutionDFS2:
    def numDistinctIslands(self, grid):
        res = set()
        m, n = len(grid), len(grid[0])

        def dfs(i, j, path, prev):
            grid[i][j] = -1
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                x = i + dx
                y = j + dy
                if (0 <= x < m and 0 <= y < n) and grid[x][y] == 1:
                    nxt = (prev[0] + dx, prev[1] + dy)
                    path.append(nxt)
                    dfs(x, y, path, nxt)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, path, (0, 0))
                    res.add(tuple(path))
        return len(res)








