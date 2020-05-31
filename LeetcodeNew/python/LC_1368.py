"""
https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/discuss/527871/Two-kinds-of-BFS%3A-deque-BFS-and-layer-by-layer-BFS-(python)
https://www.youtube.com/watch?v=ox8Z8maR6R8

"""


class Solution:
    def minCost(self, grid):
        n, m = len(grid), len(grid[0])
        k = 0
        dp = [[float('inf')] * m for i in range(n)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = []

        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m and dp[x][y] == float('inf')):
                return
            dp[x][y] = k
            queue.append([x, y])
            dfs(x + directions[grid[x][y] - 1][0], y + directions[grid[x][y] - 1][1])

        dfs(0, 0)
        while queue:
            k += 1
            queue, newQueue = [], queue
            [dfs(x + i, y + j) for x, y in newQueue for i, j in directions]
        return dp[-1][-1]





