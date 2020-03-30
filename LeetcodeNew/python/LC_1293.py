
import collections


class Solution:
    def shortestPath(self, grid, k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque([[0, 0, 0]])    # row, col, num of obstables met so far
        visited = {(0, 0) : 0}                    # row, col   =>   num of obstables met so far
        steps = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                r, c, obs = queue.popleft()
                if obs > k:
                    continue
                if r == m - 1 and c == n - 1:
                    return steps
                for x, y in [[r +1, c], [r -1, c], [r, c+ 1], [r, c - 1]]:
                    if 0 <= x < m and 0 <= y < n:
                        next_obs = obs + 1 if grid[x][y] == 1 else obs
                        if next_obs < visited.get((x, y), float('inf')):
                            visited[(x, y)] = next_obs
                            queue.append([x, y, next_obs])
            steps += 1
        return -1




class Solution2:
    def shortestPath(self, grid, k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        queue = collections.deque([(0, 0, 0, 0)])
        m, n = len(grid), len(grid[0])
        visited = set()

        while queue:
            x, y, obstacle, steps = queue.popleft()
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 1 and obstacle < k and (i, j, obstacle + 1) not in visited:
                        visited.add((i, j, obstacle + 1))
                        queue.append((i, j, obstacle + 1, steps + 1))
                    if grid[i][j] == 0 and (i, j, obstacle) not in visited:
                        if (i, j) == (m - 1, n - 1):
                            return steps + 1
                        visited.add((i, j, obstacle))
                        queue.append((i, j, obstacle, steps + 1))

        return -1






