
"""
https://leetcode.com/problems/the-maze-iii/discuss/97808/Simple-Python-Explanation

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.



Example 1:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"

Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".

Example 2:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)

Output: "impossible"

Explanation: The ball cannot reach the hole.



Note:

There is only one ball and one hole in the maze.
Both the ball and hole exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and the width and the height of the maze won't exceed 30.
We can use Dijkstra's algorithm to find the shortest distance from the ball to the hole. If you are unfamiliar with this algorithm, how it works is that we process events in priority order, where the priority is (distance, path_string). When an event is processed, it adds neighboring nodes with respective distance. To repeatedly find the highest priority node to process, we use a heap (priority queue or 'pq'), where we can add nodes with logarithmic time complexity, and maintains the invariant that pq[0] is always the smallest (highest priority.) When we reach the hole for the first time (if we do), we are guaranteed to have the right answer in terms of having the shortest distance and the lexicographically smallest path-string.

When we look for the neighbors of a location in the matrix, we simulate walking up/left/right/down
as long as we are inside the bounds of the matrix and the path is clear. If during this simulation we reach the hole prematurely,
we should also stop. If after searching with our algorithm it is the case that we never reached the hole, then the task is impossible.

One important point is, when you reach a hole while moving, don't return the moves yet. Because it's NOT garanteed shortest path.

"""

import collections, heapq

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



maze = [[0,0,0,1,0],
        [1,1,0,0,1],
        [0,0,0,0,0],
        [0,1,0,0,1],
        [0,1,0,0,0]]
ball = [0,0]
hole = [2,2]


a = Solution()
print(a.findShortestWay(maze, ball, hole))


