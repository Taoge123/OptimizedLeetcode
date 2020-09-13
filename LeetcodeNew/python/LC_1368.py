"""
https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/discuss/527871/Two-kinds-of-BFS%3A-deque-BFS-and-layer-by-layer-BFS-(python)
https://www.youtube.com/watch?v=ox8Z8maR6R8

"""

import heapq
import collections


class SolutionDJ:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        path = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heapq.heappush(path, (0, 0, 0))

        visited = set()

        while True:
            cost, i, j = heapq.heappop(path)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == m - 1 and j == n - 1:
                return cost
            for num, (dx, dy) in enumerate(directions):
                x = i + dx
                y = j + dy
                if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visited:

                    if grid[i][j] == (num + 1):
                        heapq.heappush(path, (cost, x, y))
                    else:
                        heapq.heappush(path, (cost + 1, x, y))





class SolutionLee:
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



class Solution3:
    def minCost(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = collections.deque([(0, 0, 0)])
        table = {}

        while queue:
            i, j, cost = queue.popleft()
            while 0 <= i < m and 0 <= j < n and (i, j) not in table:
                table[i, j] = cost
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    queue.append([x, y, cost + 1])
                dx, dy = directions[grid[i][j] - 1]
                i, j = i + dx, j + dy

        return table[m - 1, n - 1]





grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]

a = SolutionTest()
print(a.minCost(grid))



