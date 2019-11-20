"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""

import collections

class Solution:
    def wallsAndGates(self, rooms):
        if not rooms:
            return

        if not rooms:
            return []

        m, n = len(rooms), len(rooms[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= row + x < m and 0 <= col + y < n and rooms[row + x][col + y] > rooms[row][col]:
                    rooms[row + x][col + y] = rooms[row][col] + 1
                    queue.append((row + x, col + y))

