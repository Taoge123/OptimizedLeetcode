
class Solution:
    def numDistinctIslands2(self, grid):

        m, n = len(grid), len(grid[0])
        self.directions = [(1 ,1), (1 ,-1), (-1 ,1), (-1 ,-1)]
        res = set() # set of (list of pairs)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # list of pair(x,y)
                    cells = list()
                    self.dfs(grid, i, j, cells)
                    shape = ((self.normalize(cells)))
                    res.add(shape)
        return len(res)

    def dfs(self, grid, x, y, cells): # dfs searching
        m, n = len(grid), len(grid[0])
        if 0<= x < m and 0 <= y < n and grid[x][y] == 1:
            # avoid duplicated accessing the same point
            grid[x][y] = 0
            cells.append([x, y])
            for x2, y2 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                self.dfs(grid, x2, y2, cells)

    # normalize an island, 8 possible changes, 0, 90, 180, 270 and mirror's 0, 90, 180, 270
    def normalize(self, cells):
        shapes = [[] for _ in range(8)]
        for i, j in cells:
            idx = 0
            for x, y in [(i, j), (j, i)]:
                for dx, dy in self.directions:
                    newX, newY = x * dx, y * dy
                    shapes[idx].append((newX, newY))
                    idx += 1
        for shape in shapes:
            shape.sort()
            for i in range(len(shape) - 1, -1, -1):
                shape[i] = (shape[i][0] - shape[0][0], shape[i][1] - shape[0][1])
                # relative position justification based on shape[0]
        shapes.sort()
        return tuple(shapes[0])


