"""
https://www.youtube.com/watch?v=_426VVOB8Vo
"""

class SolutionTLE:
    def largestIsland(self, grid) -> int:
        res = -1
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    visited = [[False for i in range(n)] for j in range(m)]
                    res = max(res, self.dfs(grid, i, j, visited))
                    grid[i][j] = 0
        return res if res != -1 else m * n

    def dfs(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or visited[i][j]:
            return 0

        visited[i][j] = True
        count = self.dfs(grid, i - 1, j, visited) + \
                self.dfs(grid, i + 1, j, visited) + \
                self.dfs(grid, i, j - 1, visited) + \
                self.dfs(grid, i, j + 1, visited) + 1
        return count



class SolutionLee:
    def largestIsland(self, grid):
        n = len(grid)

        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < n and 0 <= y + j < n:
                    yield x + i, y + j

        def dfs(x, y, index):
            res = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res + 1

        # DFS every island and give it an index of island
        index = 2
        areas = {0: 0}
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(areas.values())
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y))
                    res = max(res, sum(areas[index] for index in possible) + 1)
        return res




