"""
--> d->(x, y)
<- k <-
从任意一点开始，对同一个value的所有像素做常规的遍历。如果遍历的过程中遇到了之前访问过的格子，那么就是有环。
注意遍历的过程中不能走“回头路”，即从A遍历到B，那么从B开始的遍历就不能包括A。
"""

import collections

class Solution:
    def containsCycle(self, grid) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 1:
                    continue
                queue = collections.deque()  # {x, y, direction to [x, y]}
                queue.append([i, j, -1])
                visited[i][j] = 1
                while queue:
                    x, y, d = queue.popleft()
                    for k in range(4):
                        if (d, k) in ((0, 1), (1, 0), (2, 3), (3, 2)):
                            continue
                        newX = x + directions[k][0]
                        newY = y + directions[k][1]
                        if newX < 0 or newX >= m or newY < 0 or newY >= n:
                            continue
                        # characters布一样也跳过
                        if grid[newX][newY] != grid[x][y]:
                            continue
                        if visited[newX][newY] == 1:
                            return True
                        visited[newX][newY] = 1
                        queue.append([newX, newY, k])

        return False




