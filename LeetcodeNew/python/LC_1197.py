import collections

"""
let's do bfs
Because of the symmetry, we can just look into the first
quadrant and also push only positive coordinates to the queue
also look for x >= -5 and y >= -5 case.
x >= 0 and y >= 0 is sufficient to pass all the leetcode test case,
but code fails when x = 1 and y = 1 ( [0,0]->[-1,2]->[1,1] )
"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        return self.bfs(abs(x), abs(y))


    def bfs(self, x, y):
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        queue = collections.deque([(0, 0, 0)])
        visited = set()
        visited.add((0, 0))
        while queue:
            i, j, dis = queue.popleft()
            for move in directions:
                a, b = i + move[0], j + move[1]
                if (a,b) not in visited and a >= -5 and b >= -5:
                    if a == x and b == y:
                        return dis + 1
                    queue.append((a, b, dis+1))
                    visited.add((a, b))



"""
Solution Explanation
The idea is to use BFS to find the shortest path with optimizations:

don't go down visited paths by using a set to keep track of visited paths.
pruning out directions that head away from the target x,y.
Time Complexity
O(n)

Space Complexity
O(2n) -> O(n)

Code
"""
class SolutionFast:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        queue = collections.deque([(0, 0, 0)])
        visited = set([(0, 0)])

        while queue:
            i, j, step = queue.popleft()
            if (i, j) == (x, y):
                return step

            d = []
            for node in directions:
                row = i + node[0]
                col = j + node[1]
                d.append((row, col))

            # 2) determine closest next placements, and sort based on the directions that are closest to the target x,y
            d.sort(key=lambda num: abs(x - num[0]) + abs(y - num[1]))
            print(d)

            # 2) only enqueue towards the 2 or 4 directions closest to target x,y
            count = 2
            if step < 2:
                count = 4

            for row, col in d[:count]:
                if (row, col) not in visited:
                    queue.append((row, col, step + 1))
                    visited.add((row, col))




