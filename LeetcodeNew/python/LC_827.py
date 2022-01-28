"""
https://www.youtube.com/watch?v=_426VVOB8Vo
"""


class SolutionTonyDFSTLE:
    def largestIsland(self, grid):

        m, n = len(grid), len(grid[0])

        def dfs(i, j, visited):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or (i, j) in visited:
                return 0

            visited.add((i, j))
            count = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                count += dfs(x, y, visited)
            count += 1
            return count

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    res = max(res, dfs(i, j, set()))
                    grid[i][j] = 0

        return res if res != 0 else m * n





class SolutionTLE:
    def largestIsland(self, grid) -> int:
        res = 0
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



class SolutionDFS:
    def largestIsland(self, grid):
        n = len(grid)

        def move(i , j):
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= i + dx < n and 0 <= j + dy < n:
                    yield i + dx, j + dy

        def dfs(i, j, index):
            res = 0
            grid[i][j] = index
            for x, y in move(i, j):
                if grid[x][y] == 1:
                    res += dfs(x, y, index)
            return res + 1

        # DFS every island and give it an index of island
        index = 2
        areas = {0: 0}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[index] = dfs(i, j, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(areas.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    possible = set(grid[x][y] for x, y in move(i, j))
                    res = max(res, sum(areas[index] for index in possible) + 1)
        return res




class SolutionTonyIncorrect:
    def largestIsland(self, grid):

        n = len(grid)

        def dfs(i, j, idx):
            res = 0
            grid[i][j] = idx
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x = i + dx
                y = j + dy
                if x < 0 or x >= n or y < 0 or y >= n:
                    continue
                if grid[i][j] == 1:
                    res += dfs(x, y, idx)
            # plus itself
            return res + 1

        # DFS
        idx = 2
        table = {0: 0}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    table[idx] = dfs(i, j, idx)
                    idx += 1

        res = max(table.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    possible = set()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        x = i + dx
                        y = j + dy
                        if x < 0 or x >= n or y < 0 or y >= n:
                            continue
                        possible.add(grid[x][y])
                    res = max(res, sum(table[idx] for idx in possible) + 1)
        return res


