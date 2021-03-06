
"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

import functools

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(matrix), len(matrix[0])
        cache = [[-1 for i in range(n)] for j in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                curLen = self.dfs(matrix, i, j, cache, m, n)
                res = max(res, curLen)
        return res

    def dfs(self, matrix, i, j, cache, m, n):
        if cache[i][j] != -1:
            return cache[i][j]
        res = 1
        for direction in self.directions:
            x, y = i + direction[0], j + direction[1]
            if x < 0 or y < 0 or x >= m or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            length = 1 + self.dfs(matrix, x, y, cache, m, n)
            res = max(res, length)
        cache[i][j] = res
        return res


class SolutionDFS2:
    def longestIncreasingPath(self, matrix):
        if not matrix: return 0
        h, w = len(matrix), len(matrix[0])

        @functools.lru_cache(None)
        def dfs(i, j):
            cur = matrix[i][j]
            res = 0

            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < h and 0 <= y < w and cur < matrix[x][y]:
                    res = max(res, dfs(x, y))

            return res + 1

        return max(dfs(i, j) for i in range(h) for j in range(w))






