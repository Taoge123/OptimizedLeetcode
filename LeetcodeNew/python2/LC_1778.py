
"""
https://leetcode.com/problems/shortest-path-in-a-hidden-grid/discuss/1100020/Python-DSF-to-explore-the-graph-and-BFS-to-find-minimum-distance
https://www.youtube.com/watch?v=tfNTJtdOW6c

"""


import collections


class GridMaster:
   def canMove(self, direction: str) -> bool:
       pass

   def move(self, direction: str) -> bool:
       pass

   def isTarget(self) -> None:
       pass


class Solution:
    def findShortestPath(self, master: 'GridMaster') -> int:

        # first use dfs to find all possible reachable positions
        directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        anti = {"U": "D", "D": "U", "L": "R", "R": "L"}

        isValid = {}
        isValid[(0, 0)] = master.isTarget()

        def dfs(i, j):
            for d in directions:
                dx, dy = directions[d]
                x = i + dx
                y = j + dy
                if (x, y) not in isValid and master.canMove(d):
                    # move forward
                    master.move(d)
                    isValid[(x, y)] = master.isTarget()
                    dfs(x, y)
                    # move back
                    master.move(anti[d])

        dfs(0, 0)

        # now use bfs to find the minimum distance
        queue = collections.deque([(0, 0, 0)])  # (r, c, step)
        seen = set()
        while queue:
            i, j, step = queue.popleft()
            if isValid[(i, j)] == True:
                return step

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                if (x, y) in isValid and (x, y) not in seen:
                    seen.add((x, y))
                    queue.append((x, y, step + 1))

        return -1

