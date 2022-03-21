
"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.



Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""

import collections


class SolutionTonyBFS:
    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])

        queue = collections.deque()
        queue.append([start[0], start[1]])
        visited = set()

        while queue:
            i, j = queue.popleft()
            if [i, j] == destination:
                return True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i
                y = j
                while x >= 0 and x <= m - 1 and y >= 0 and y <= n - 1 and maze[x][y] == 0:
                    x += dx
                    y += dy
                x -= dx
                y -= dy
                if (x, y) in visited:
                    continue
                queue.append([x, y])
                visited.add((x, y))

        return False


class Solution2:
    def hasPath(self, maze, start, destination) -> bool:
        m, n = len(maze), len(maze[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return self.dfs(maze, start[0], start[1], destination, set(), m, n)

    def dfs(self, maze, i, j, destination, visited, m, n):

        if (i, j) in visited:
            return False
        if [i, j] == destination:
            return True
        visited.add((i, j))
        for dx, dy in self.directions:
            x, y = i, j
            while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] != 1:
                x += dx
                y += dy

            if self.dfs(maze, x, y, destination, visited, m, n):
                return True

        return False


class Solution22:
    def hasPath(self, maze, start, destination) -> bool:
        queue = collections.deque()
        queue.append([start[0], start[1]])
        visited = set()
        visited.add((start[0], start[1]))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            i, j = queue.popleft()
            if [i, j] == destination:
                return True
            for dx, dy in directions:
                x, y = i, j
                while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy

                if (x, y) not in visited:
                    visited.add((x, y))
                    queue.append((x, y))





