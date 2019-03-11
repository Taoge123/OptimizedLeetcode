"""
There is a ball in a maze with empty spaces and walls.
The ball can go through empty spaces by rolling up, down, left or right,
but it won't stop rolling until hitting a wall. When the ball stops,
it could choose the next direction.

Given the ball's start position, the destination and the maze,
find the shortest distance for the ball to stop at the destination.
The distance is defined by the number of empty spaces traveled by the ball
from the start position (excluded) to the destination (included).
If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall
and 0 means the empty space. You may assume that the borders of the maze are all walls.
The start and destination coordinates are represented by row and column indexes.



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



"""
#LC743

import heapq


class Solution:
    def shortestDistance(self, maze, start, destination):
        m, n, q, stopped = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]):0}
        while q:
            dist, x, y = heapq.heappop(q)
            if [x, y] == destination:
                return dist
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                if (newX, newY) not in stopped or dist + d < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = dist + d
                    heapq.heappush(q, (dist + d, newX, newY))
        return -1


class Solution3:
    def shortestDistance(self, maze, start, destination):
        N, M = len(maze), len(maze[0])
        hq = [(0, start[0], start[1])]
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visit = set()
        while hq:
            move, i, j = heapq.heappop(hq)
            if (i, j) in visit:
                continue
            if [i, j] == destination:
                return move
            visit.add((i, j))
            for x, y in directions:
                tmpmove, ni, nj = 0, i + x, j + y
                while 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 0:
                    tmpmove += 1
                    ni += x
                    nj += y
                ni -= x
                nj -= y
                if (ni, nj) not in visit:
                    heapq.heappush(hq, (move + tmpmove, ni, nj))
        return -1


"""
This question is similar to the regular BFS traversal in a grid, 
with the only exeception being that we cannot change direction until we hit the boundary/obstacle. 
This forces us to traverse along thr maze till one of the two conditions are met. 
The other catch is unlike regular BFS, where we are gaurenteed 
that we have the shortest distance the first time we reach our destination, 
is no longer true(as due to above condition, we are changing the fundamental assumption 
in BFS shortest paths that all edges are of equal distance, this is no longer true). 
Therefore, we have to exhaustively search all the paths.
"""


from collections import deque
import heapq
class Solution:
    def shortestDistance(self, maze, start, destination):
        [sx,sy] = start
        [ex,ey] = destination
        if not any(maze):
            return -1
        m,n = len(maze), len(maze[0])
        visited = {(sx,sy) : 0}
        q = deque([(0, sx, sy)])
    ## For Djikstra's method ==>
    ## q = [(0,sx, sy)]
        while q:
            (pd,px,py) = q.popleft()
            # For Djikstra's method ==>
        # (pd,px,py) = heapq.heappop(q)
            for dx,dy in [(0,1),(-1,0),(0,-1),(1,0)]:
                d,x,y=pd,px,py
                while 0<=x+dx<m and 0<=y+dy<n and maze[x+dx][y+dy] == 0:
                    x,y,d = x+dx, y+dy, d+1
                if (x,y) not in visited or visited[(x,y)] > d:
                    visited[(x,y)] = d
                    if (x,y) == (ex,ey):
                        continue
            # For Djikstra's method ==>
            # return d

                    q.append((d,x,y))
            # For Djikstra's method ==>
            # q = heapq.heappush(q, (0,sx, sy))

        return visited.get((ex,ey), -1)





class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        dest=tuple(destination)
        m=len(maze)
        n=len(maze[0])
        res=None
        def go(start, direction):
            # return the stop position and length
            i, j = start
            ii, jj = direction
            l=0
            while 0<=i+ii<m and 0<=j+jj<n and maze[i+ii][j+jj]!=1:
                i+=ii
                j+=jj
                l+=1
            return l, (i,j)
        # bfs (dijkstra: https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
        visited={}
        q=[]
        heapq.heappush(q, (0, tuple(start)))
        while q:
            length, cur = heapq.heappop(q)
            visited[cur]=length
            if cur == dest:
                return length
            for direction in [(-1, 0), (1, 0), (0,-1), (0,1)]:
                l, np = go(cur, direction)
                if np not in visited or visited[np]>length+l:
                    visited[np]=length+l
                    heapq.heappush(q, (length+l, np))
        return -1
