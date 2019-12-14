"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

import collections

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        self.directions = [(-1, 0) ,(1, 0) ,(0, -1) ,(0, 1)]
        visited = [[False for i in range(n)] for j in range(m)]
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not visited[r][c]:
                    res += 1
                    self.dfs(r, c, grid, m, n, visited)

        return res

    def dfs(self, r, c, grid, m, n, visited):
        if r< 0 or c < 0 or r >= m or c >= n or grid[r][c] != '1' or visited[r][c]:
            return
        visited[r][c] = True
        for direction in self.directions:
            x, y = r + direction[0], c + direction[1]
            self.dfs(x, y, grid, m, n, visited)


class Solution2:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        M, N = len(grid), len(grid[0])
        queue = collections.deque()
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    queue.append((i, j))
                    while queue:
                        x, y = queue.pop()
                        for d in directions:
                            nx, ny = x + d[0], y + d[1]
                            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                queue.append((nx, ny))
        return res





