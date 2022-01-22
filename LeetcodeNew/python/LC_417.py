
"""Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.


Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

import collections


class SolutionTonyDFS:
    def pacificAtlantic(self, heights):

        p_visited = set()
        a_visited = set()

        m, n = len(heights), len(heights[0])

        def dfs(i, j, visited):
            visited.add((i, j))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy

                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if heights[x][y] < heights[i][j]:
                    continue
                if (x, y) in visited:
                    continue
                # visited.add((x, y))
                dfs(x, y, visited)

        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n - 1, a_visited)
        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m - 1, j, a_visited)

        res = []
        for i in range(m):
            for j in range(n):
                if (i, j) in p_visited and (i, j) in a_visited:
                    res.append([i, j])
        return res



class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix:
            return []
        self.directions = [(-1, 0) ,(1, 0) ,(0, -1) ,(0, 1)]
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False for i in range(n)] for j in range(m)]
        a_visited = [[False for i in range(n)] for j in range(m)]
        res = []
        for i in range(m):
            self.dfs(matrix, i, 0, p_visited, m, n)
            self.dfs(matrix, i, n - 1, a_visited, m, n)
        for j in range(n):
            self.dfs(matrix, 0, j, p_visited, m, n)
            self.dfs(matrix, m - 1, j, a_visited, m, n)
        for i in range(m):
            for j in range(n):
                if a_visited[i][j] and p_visited[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, i, j, visited, m, n):
        visited[i][j] = True
        for dx, dy in self.directions:
            x, y = i + dx, j + dy
            if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)


class SolutionBFS:
    def pacificAtlantic(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])

        def bfs(ocean):
            queue = collections.deque(ocean)
            while queue:
                (i, j) = queue.popleft()
                for (di, dj) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= di + i < m and 0 <= dj + j < n and (di + i, dj + j) not in ocean \
                            and matrix[di + i][dj + j] >= matrix[i][j]:
                        queue.append((di + i, dj + j))
                        ocean.add((di + i, dj + j))
            return ocean

        pacific = set([(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)])
        atlantic = set([(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n - 1)])
        return list(bfs(pacific) & bfs(atlantic))

