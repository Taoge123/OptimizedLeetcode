
import collections


class SolutionWisdom:
    def minDays(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        count = self.island(grid)
        if count > 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                grid[i][j] = 0
                count = self.island(grid)
                if count > 1:
                    return 1
                grid[i][j] = 1

        return 2

    def island(self, grid):
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                queue = collections.deque()
                queue.append([i, j])
                visited.add((i, j))
                count += 1

                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        newX = x + directions[k][0]
                        newY = y + directions[k][1]

                        if newX < 0 or newX >= m or newY < 0 or newY >= n:
                            continue
                        if (newX, newY) in visited:
                            continue
                        if grid[newX][newY] == 0:
                            continue

                        queue.append([newX, newY])
                        visited.add((newX, newY))
                if count > 1:
                    return 2

        return count
