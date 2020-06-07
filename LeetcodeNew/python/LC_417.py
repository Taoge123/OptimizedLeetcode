
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

    def dfs(self, matrix, i, j, cache, m, n):
        cache[i][j] = True
        for direction in self.directions:
            x, y = i + direction[0], j + direction[1]
            if x < 0 or y < 0 or x >= m or y >= n or cache[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, cache, m, n)


