
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

"""
3 -> 4 -> 5 -> 6 -> depth
4    3    2    1

{6 : 1}
{5 : 2}
{4 : 3}

"""



import functools


class SolutionTony:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])

        @functools.lru_cache(None)
        def dfs(i, j):
            res = 1
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if matrix[x][y] > matrix[i][j]:
                    res = max(res, dfs(x, y) + 1)
            return res

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res




class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(matrix), len(matrix[0])
        memo = {}
        res = 0
        for i in range(m):
            for j in range(n):
                curLen = self.dfs(matrix, i, j, memo, m, n)
                res = max(res, curLen)
        return res

    def dfs(self, matrix, i, j, memo, m, n):
        if (i, j) in memo:
            return memo[(i, j)]
        res = 1
        for dx, dy in self.directions:
            x, y = i + dx, j + dy
            if x < 0 or y < 0 or x >= m or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            length = 1 + self.dfs(matrix, x, y, memo, m, n)
            res = max(res, length)
        memo[(i, j)] = res
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






