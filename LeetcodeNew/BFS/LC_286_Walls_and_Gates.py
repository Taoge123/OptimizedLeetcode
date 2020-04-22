
"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647
to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a gate, it should be filled with INF.

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


class SolutionReadable:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        queue = collections.deque([])

        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        dis = 0
        while queue:
            length = len(queue)
            dis += 1
            for i in range(length):
                cur = queue.popleft()
                for dir in dirs:
                    nextPos = (cur[0] + dir[0], cur[1] + dir[1])
                    if nextPos[0] >= 0 and nextPos[0] < m and nextPos[1] >= 0 and nextPos[1] < n and rooms[nextPos[0]][nextPos[1]] == 2147483647:
                        rooms[nextPos[0]][nextPos[1]] = dis
                        queue.append(nextPos)


class SolutionCaikehe:
    def wallsAndGates(self, rooms):
        if not rooms:
            return
        r, c = len(rooms), len(rooms[0])
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    queue = collections.deque([])
                    queue.append((i + 1, j, 1));
                    queue.append((i - 1, j, 1))
                    queue.append((i, j + 1, 1));
                    queue.append((i, j - 1, 1))
                    visited = set()
                    while queue:
                        x, y, val = queue.popleft()
                        if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] in [0, -1] or (x, y) in visited:
                            continue
                        visited.add((x, y))
                        rooms[x][y] = min(rooms[x][y], val)
                        queue.append((x + 1, y, val + 1))
                        queue.append((x - 1, y, val + 1))
                        queue.append((x, y + 1, val + 1))
                        queue.append((x, y - 1, val + 1))


from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        h = len(rooms)
        w = len(rooms[0])

        q = deque()
        for i in range(h):
            for j in range(w):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while q:
            row, col = q.popleft()
            dist = rooms[row][col] + 1
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dy
                c = col + dx
                if 0 <= r < h and 0 <= c < w and rooms[r][c] == 2147483647:
                    rooms[r][c] = dist
                    q.append((r, c))



class SOlutionDFS:
    def wallsAndGates(self, a):

        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 0:
                    self.helper(i, j, a, 0)

    def helper(self, ii, jj, a, dist):
        if ii < 0 or jj < 0 or ii >= len(a) or jj >= len(a[0]) or a[ii][jj] < dist:
            return
        a[ii][jj] = dist
        self.helper(ii + 1, jj, a, dist + 1)
        self.helper(ii - 1, jj, a, dist + 1)
        self.helper(ii, jj + 1, a, dist + 1)
        self.helper(ii, jj - 1, a, dist + 1)







