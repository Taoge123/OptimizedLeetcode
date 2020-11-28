"""
there are two cases that source node cannot reach target node
case 1 is the blocked points and boundary points form a closed interval and one node(source or target) in,another out.
case 2 is only the blocked points form a closed interval and one node(source or target) in,another out.

the key point is the length of blocked is smaller than 200, so the closed area will not too large
we can just use bfs to search from the source, and set a maximum step.
after moving maximum step, if we can still move, then it must can reach the target point

here the maximum step should be the length of blocked, seen in case 3
of course, we should handled the different situation with the starting node
"""


import collections


class Solution:
    def isEscapePossible(self, blocked, source, target) -> bool:
        if not blocked:
            return True

        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        blocked = set(map(tuple, blocked))
        return self.bfs(blocked, source, target) and self.bfs(blocked, target, source)

    def bfs(self, blocked, source, target):
        step = 0
        queue = collections.deque([source])
        visited = set()
        while queue:
            size = len(queue)
            for i in range(size):
                i, j = queue.popleft()
                if [i, j] == target:
                    return True
                for dx, dy in self.directions:
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= 10 ** 6 or y < 0 or y >= 10 ** 6 or (x, y) in visited:
                        continue
                    if (x, y) in blocked:
                        continue
                    visited.add((x, y))
                    queue.append((x, y))

            step += 1
            if step == len(blocked):
                break

            if len(queue) == 0:
                return False
        return True






class SolutionLee:
    def isEscapePossible(self, blocked, source, target) -> bool:
        self.directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        blocked = [tuple(item) for item in blocked]
        return self.bfs(blocked, source, target) and self.bfs(blocked, target, source)

    def bfs(self, blocked, source, target):
        queue = [source]
        visited = {tuple(source)}
        for i, j in queue:
            for node in self.directions:
                print(i, j)
                x = i + node[0]
                y = j + node[1]
                if x >= 0 and y >= 0 and x < 10 ** 6 and y < 10 ** 6 and (x, y) not in visited and (x, y) not in blocked:
                    if [x, y] == target:
                        return True
                    queue.append([x, y])
                    visited.add((x, y))

            if len(queue) >= 20000:
                return True
        return False



blocked = []
source = [0,0]
target = [999999,999999]

a = SolutionLee()
print(a.isEscapePossible(blocked, source, target))



