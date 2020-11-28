"""
https://www.youtube.com/watch?v=zcbFn8DH0PU
https://buptwc.com/2019/05/02/Leetcode-1034-Coloring-A-Border/
"""


class Solution:
    def colorBorder(self, grid, r0, c0, color):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])

        self.dfs(grid, r0, c0, grid[r0][c0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    grid[i][j] = color

        return grid

    def dfs(self, grid, i, j, origin):
        grid[i][j] = -origin
        m, n = len(grid), len(grid[0])

        for node in self.directions:
            x = node[0] + i
            y = node[1] + j

            if x >= 0 and y >= 0 and x < m and y < n:
                if grid[x][y] == origin:
                    self.dfs(grid, x, y, origin)

        if i > 0 and i < m - 1 and j > 0 and j < n - 1:
            if (abs(grid[i - 1][j]) == origin and
                    abs(grid[i + 1][j]) == origin and
                    abs(grid[i][j + 1]) == origin and
                    abs(grid[i][j - 1]) == origin):
                grid[i][j] = origin

        return


class SolutionBFS:
    def colorBorder(self, grid, r0, c0, color):
        m, n = len(grid), len(grid[0])
        queue = [[r0, c0]]
        boarder = set()
        component = set([(r0, c0)])

        while queue:
            i, j = queue.pop(0)
            for node in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = i + node[0]
                y = j + node[1]
                if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == grid[r0][c0]:
                    if (x, y) not in component:
                        queue.append([x, y])
                        component.add((x, y))

                else:
                    boarder.add((i, j))

        for x, y in boarder:
            grid[x][y] = color

        return grid




class SolutionLee:
    def colorBorder(self, grid, r0, c0, color):
        m, n = len(grid), len(grid[0])
        visited = set()

        self.dfs(grid, visited, r0, c0, grid[r0][c0], color)
        return grid

    def dfs(self, grid, visited, x, y, origin, color):
        if (x, y) in visited:
            return True
        m, n = len(grid), len(grid[0])
        if not (0 <= x < m and 0 <= y < n and grid[x][y] == origin):
            return False
        visited.add((x, y))
        if self.dfs(grid, visited, x + 1, y, origin, color) + \
                self.dfs(grid, visited, x - 1, y, origin, color) + \
                self.dfs(grid, visited, x, y + 1, origin, color) + \
                self.dfs(grid, visited, x, y - 1, origin, color) < 4:
            grid[x][y] = color
        return True








