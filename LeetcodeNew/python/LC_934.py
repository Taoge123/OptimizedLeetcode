import collections


class Solution:
    def shortestBridge(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        visited = [[0 for _ in range(n)] for _ in range(m)]
        queue = collections.deque()

        def dfs(x, y):
            visited[x][y] = 1
            queue.append((x, y))
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dfs(nx, ny)

        flag = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    flag = 1
                    break
            if flag:
                break

        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n and visited[x][y] == 0:
                        if grid[x][y] == 0:
                            queue.append((x, y))
                            visited[x][y] = 1
                        else:
                            return step
            step += 1
        return -1


