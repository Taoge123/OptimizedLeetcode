
"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

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

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""
import collections, heapq


class SolutionTonyBFS:
    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])

        heap = []
        heapq.heappush(heap, [0, start[0], start[1]])
        visited = set()
        step = 0

        while heap:
            dist, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))

            if [i, j] == destination:
                return dist

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i
                y = j
                new_dist = dist
                while x >= 0 and x <= m - 1 and y >= 0 and y <= n - 1 and maze[x][y] == 0:
                    x += dx
                    y += dy
                    new_dist += 1
                x -= dx
                y -= dy
                new_dist -= 1
                heapq.heappush(heap, [new_dist, x, y])

        return -1



class SolutionTony:
    def shortestDistance(self, maze, start, destination):

        m, n = len(maze), len(maze[0])
        heap = []
        heapq.heappush(heap, (0, start[0], start[1]))
        visited = set()
        while heap:
            dist, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if [i, j] == destination:
                return dist

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i
                y = j
                d = 0
                while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                    x += dx
                    y += dy
                    d += 1
                x -= dx
                y -= dy
                d -= 1
                # This is not correct
                # if (x, y) in visited:
                #     continue
                # visited.add((x, y))
                heapq.heappush(heap, (dist + d, x, y))
        return -1




class Solution2:
    def shortestDistance(self, maze, start, destination) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heap = [(0, start[0], start[1])]
        distance = collections.defaultdict(int)

        while heap:
            dist, i, j = heapq.heappop(heap)
            if [i, j] == destination:
                return dist
            for dx, dy in directions:
                x, y, new_dist = i, j, dist
                while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                    x += dx
                    y += dy
                    new_dist += 1
                x -= dx
                y -= dy
                new_dist -= 1
                if (x, y) not in distance or new_dist < distance[(x, y)]:
                    distance[(x, y)] = new_dist
                    heapq.heappush(heap, (new_dist, x, y))
        return -1





class Solution22:
    def shortestDistance(self, maze, start, destination) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heap = [(0, start[0], start[1])]
        distance = collections.defaultdict(int)

        while heap:
            dist, i, j = heapq.heappop(heap)
            if [i, j] == destination:
                return dist
            for dx, dy in directions:
                x, y, step = i, j, dist
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] != 1:
                    x += dx
                    y += dy
                    step += 1
                if (x, y) not in distance or step < distance[(x, y)]:
                    distance[(x, y)] = step
                    heapq.heappush(heap, (step, x, y))
        return -1



class SolutionRikaTLE_DFS:  # TLE
    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[start[0]][start[1]] = 0
        visited = set()
        i, j = start[0], start[1]
        self.dfs(maze, m, n, i, j, destination, dist)

        if dist[destination[0]][destination[1]] != float('inf'):
            return dist[destination[0]][destination[1]]
        else:
            return -1

    def dfs(self, maze, m, n, i, j, destination, dist):

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i
            y = j
            steps = 0
            while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                x += dx
                y += dy
                steps += 1
            x -= dx
            y -= dy
            steps -= 1
            update_dist = dist[i][j] + steps

            if dist[x][y] > update_dist:
                dist[x][y] = update_dist
                self.dfs(maze, m, n, x, y, destination, dist)



class SolutionDFSTLE:
    def shortestDistance(self, maze, start, destination):
        def dfs(i, j, visited):
            if (i, j) == destination:
                return 0
            path_dist = []
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                x = i + dx
                y = j + dy
                dist = 0
                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                    x += dx
                    y += dy
                    dist += 1
                x -= dx
                y -= dy
                val = -1
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                val = dfs(x, y, visited)
                visited.remove((x, y))

                if val != -1:
                    path_dist.append(dist + val)
            return min(path_dist, default=-1)

        start, destination = tuple(start), tuple(destination)
        return dfs(start[0], start[1], set())















