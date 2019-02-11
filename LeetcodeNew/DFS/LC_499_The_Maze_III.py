"""
We can use Dijkstra's algorithm to find the shortest distance from the ball to the hole.
If you are unfamiliar with this algorithm, how it works is that we process events in priority order,
where the priority is (distance, path_string). When an event is processed,
it adds neighboring nodes with respective distance.
To repeatedly find the highest priority node to process,
we use a heap (priority queue or 'pq'), where we can add nodes with logarithmic time complexity,
and maintains the invariant that pq[0] is always the smallest (highest priority.)
When we reach the hole for the first time (if we do),
we are guaranteed to have the right answer in terms of having the shortest distance
and the lexicographically smallest path-string.

When we look for the neighbors of a location in the matrix,
we simulate walking up/left/right/down as long as we are inside the bounds of the matrix
and the path is clear. If during this simulation we reach the hole prematurely,
we should also stop. If after searching with our algorithm it is the case that we never reached the hole,
then the task is impossible.

"""
import heapq

class Soilution:
    def findShortestWay(self, A, ball, hole):
        ball, hole = tuple(ball), tuple(hole)
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for dr, dc, di in [(-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd')]:
                cr, cc, dist = r, c, 0
                while (0 <= cr + dr < R and 0 <= cc + dc < C and not A[cr + dr][cc + dc]):
                    cr += dr
                    cc += dc
                    dist += 1
                    if (cr, cc) == hole:
                        break
                yield (cr, cc), di, dist

        pq = [(0, '', ball)]
        seen = set()
        while pq:
            dist, path, node = heapq.heappop(pq)
            if node in seen: continue
            if node == hole: return path
            seen.add(node)
            for nei, di, nei_dist in neighbors(*node):
                heapq.heappush(pq, (dist + nei_dist, path + di, nei))

        return "impossible"



class Solution:
    def findShortestWay(self, maze, ball, hole):
        m, n, q, stopped = len(maze), len(maze[0]), [(0, "", ball[0], ball[1])], {(ball[0], ball[1]): [0, ""]}
        while q:
            dist, pattern, x, y = heapq.heappop(q)
            if [x, y] == hole:
                return pattern
            for i, j, p in ((-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                    if [newX, newY] == hole:
                        break
                if (newX, newY) not in stopped or [dist + d, pattern + p] < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = [dist + d, pattern + p]
                    heapq.heappush(q, (dist + d, pattern + p, newX, newY))
        return "impossible"








