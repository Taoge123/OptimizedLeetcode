


class Solution:
    def findShortestWay(self, maze, ball, hole):
        m, n = len(maze), len(maze[0])
        queue = [(0, "", ball[0], ball[1])]
        directions = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]
        dp = collections.defaultdict(list)
        dp[(ball[0], ball[1])] = [0, ""]

        while queue:
            dist, pattern, i, j = heapq.heappop(queue)
            if [i, j] == hole:
                return pattern

            for dx, dy, d in directions:
                step, x, y = dist, i, j
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] != 1:
                    x += dx
                    y += dy
                    step += 1
                    if [x, y] == hole:
                        break

                if (x, y) not in dp or [step, pattern + d] < dp[(x, y)]:
                    dp[(x, y)] = [step, pattern + d]
                    heapq.heappush(queue, [step, pattern + d, x, y])
        return 'impossible'

