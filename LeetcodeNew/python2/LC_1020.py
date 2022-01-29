
"""
一个矩阵,四周都是海水, 1是沙子, 0海水灌不进来，如果1被0包围了也灌不进来，
海水进来以后看有几个坑

"""

import collections


class SolutionTonyDFS:
    def numEnclaves(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                    continue
                dfs(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)
        return sum(sum(row) for row in grid)



class SolutionDFS:
    def numEnclaves(self, grid):
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    self.dfs(grid, i, j)
        return sum(sum(row) for row in grid)

    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        grid[i][j] = 0
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if x >= 0 and x < m and y >= 0 and y < n and grid[x][y]:
                self.dfs(grid, x, y)




class SolutionBFS:
    def numEnclaves(self, A) -> int:
        m, n = len(A), len(A[0])
        res = 0
        queue = collections.deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                res += A[i][j]
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and A[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            i, j = queue.popleft()
            A[i][j] = 0
            res -= 1

            for node in directions:
                x = i + node[0]
                y = j + node[1]
                if x >= 0 and x < m and y >= 0 and y < n and A[x][y] == 1 and (x, y) not in visited:
                    queue.append((x, y))
                    visited.add((x, y))
                    A[x][y] = 0

        return res




