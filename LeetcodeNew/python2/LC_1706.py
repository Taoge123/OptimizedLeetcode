"""
https://leetcode.com/problems/where-will-the-ball-fall/discuss/1443268/Python-3-or-DFS-Simulation-or-Explanation

Explanation
Simulate the process
When current board is 1 (right), ball will move to right only if the right neighbor of current position is also 1
When current board is -1 (left), ball will move to left only if the left neighbor of current position is also -1
Repeat above process until the ball drop to bottom or return -1 if it won't
DFS is not necessary, you can implement it using an iterative way instead
Time: O(m*n)

"""


import functools


class SolutionMemo:
    def findBall(self, grid):
        m, n = len(grid), len(grid[0])

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m:
                return j
            elif grid[i][j] == 1 and j + 1 < n and grid[i][j + 1] == 1:
                return dfs(i + 1, j + 1)
            elif grid[i][j] == -1 and j - 1 >= 0 and grid[i][j - 1] == -1:
                return dfs(i + 1, j - 1)
            else:
                return -1

        return [dfs(0, j) for j in range(n)]




class Solution:
    def findBall(self, grid):
        m, n = len(grid), len(grid[0])

        @functools.lru_cache(None)
        def dfs(col, row):
            # print(row)
            if row == m:
                return col
            nxt = col + grid[row][col]
            if 0 <= nxt < n and grid[row][nxt] + grid[row][col] != 0:
                return dfs(nxt, row + 1)
            return -1

        return [dfs(i, 0) for i in range(n)]

