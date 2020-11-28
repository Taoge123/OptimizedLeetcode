
import collections



class SolutionTony:
    def shortestPath(self, grid, K: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        queue = collections.deque([(0, 0, 0)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        visited = set()
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j, k = queue.popleft()
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == 1 and k < K and (x, y, k + 1) not in visited:
                            visited.add((x, y, k + 1))
                            queue.append((x, y, k + 1))
                        if grid[x][y] == 0 and (x, y, k) not in visited:
                            if (x, y) == (m - 1, n - 1):
                                return step + 1
                            visited.add((x, y, k))
                            queue.append((x, y, k))
            step += 1
        return -1




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


"""
step 0: (0, 0)
step 0: (0, 1) (1, 0)
step 1: (1, 1) (0, 2) (2, 0) 

"""


class SolutionWisdom:
    def shortestPath(self, grid, K: int) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        queue = collections.deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue.append([0, 0, 0])
        visited.add((0, 0, 0))
        step = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, k = queue.popleft()
                for t in range(4):
                    i = x + directions[t][0]
                    j = y + directions[t][1]
                    if i < 0 or i >= m or j < 0 or j >= n:
                        continue
                    if i == m - 1 and j == n - 1:
                        return step + 1

                    # if its a wall
                    if grid[i][j] == 1:
                        if k == K:
                            continue
                        if (i, j, k + 1) in visited:
                            continue
                        visited.add((i, j, k + 1))
                        queue.append([i, j, k + 1])
                    else:
                        if (i, j, k) in visited:
                            continue
                        visited.add((i, j, k))
                        queue.append([i, j, k])

            step += 1
        return -1


grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
K = 1
a = SolutionWisdom()
print(a.shortestPath(grid, K))


