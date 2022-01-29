"""
https://leetcode.com/problems/shortest-bridge/discuss/1467748/Clean-Python-solution(BFS-and-DFS)

"""



import collections


class SolutionDFS:
    def shortestBridge(self, grid):

        m, n = len(grid), len(grid[0])
        queue = collections.deque()

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return

            grid[i][j] = 2
            queue.append([i, j])
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                x = i + dx
                y = j + dy
                dfs(x, y)

        def first():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return [i, j]

        row, column = first()
        dfs(row, column)
        res = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                # if grid[i][j] == 1:
                #     return res
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    x = i + dx
                    y = j + dy

                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    if grid[x][y] == 0:
                        grid[x][y] = 3
                        queue.append([x, y])
                    elif grid[x][y] == 1:
                        return res
            res += 1




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


