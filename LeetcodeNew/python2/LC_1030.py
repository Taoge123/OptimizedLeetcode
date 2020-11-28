import collections


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        def dist(point):
            pi, pj = point
            return abs(pi - r0) + abs(pj - c0)

        points = [(i, j) for i in range(R) for j in range(C)]
        return sorted(points, key=dist)




class SolutionBFS:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        queue = collections.deque()
        queue.append([r0, c0])
        visited = set()
        visited.add((r0, c0))
        res = [(r0, c0)]

        while queue:
            size = len(queue)
            for i in range(size):
                i, j = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= R or y < 0 or y >= C:
                        continue
                    if (x, y) in visited:
                        continue
                    queue.append([x, y])
                    visited.add((x, y))
                    res.append([x, y])
        return res





