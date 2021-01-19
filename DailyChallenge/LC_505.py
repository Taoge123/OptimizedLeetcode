
import collections
import heapq


class Solution:
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
                while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                    x += dx
                    y += dy
                    step += 1
                x -= dx
                y -= dy
                step -= 1
                if (x, y) not in distance or step < distance[(x, y)]:
                    distance[(x, y)] = step
                    heapq.heappush(heap, (step, x, y))
        return -1


