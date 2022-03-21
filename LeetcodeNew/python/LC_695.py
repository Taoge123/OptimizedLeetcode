
import collections


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res.append(self.dfs(grid, i, j, m, n))

        return max(res) if res else 0

    def dfs(self, grid, i, j, m, n):
        if i >= 0 and i < m and j >= 0 and j < n and grid[i][j]:
            grid[i][j] = 0
            return self.dfs(grid, i - 1, j, m, n) \
                   + self.dfs(grid, i + 1, j, m, n) \
                   + self.dfs(grid, i, j - 1, m, n) \
                   + self.dfs(grid, i, j + 1, m, n) + 1
        return 0



class SolutionBFS:
    def maxAreaOfIsland(self, grid):

        m, n = len(grid), len(grid[0])
        def bfs(i, j):
            queue = collections.deque()
            queue.append((i, j))
            visited.add((i, j))
            count = 0
            while queue:
                i, j = queue.popleft()
                if grid[i][j] == 1:
                    count += 1

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                        continue
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    queue.append((x, y))
            return count

        res = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = bfs(i, j)
                    res = max(res, count)
        return res






