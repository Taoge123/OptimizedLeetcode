"""
[
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]]

Input: grid = [
  ["0","0","0","0","0"],
  ["0","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

res = 0
for i in range(m):
    for j in rang(n):
        if grid[i][j] == '1':
            res += 1
            bfs([i, j])
            while queue

(0, 1) (1, 0)

Input: grid = [
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"]
]

"""

import collections

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for i in range(n)] for j in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(i, j, grid, m, n, visited)
                    res += 1

        return res

    def dfs(self, i, j, grid, m, n, visited):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1' or visited[i][j]:
            return
        visited[i][j] = True
        for dx, dy in self.directions:
            x, y = i + dx, j + dy
            self.dfs(x, y, grid, m, n, visited)



class SolutionBFS:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        M, N = len(grid), len(grid[0])
        queue = collections.deque()
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    queue.append((i, j))
                    visited.add((i, j))
                    while queue:
                        x, y = queue.pop()
                        for d in directions:
                            nx, ny = x + d[0], y + d[1]
                            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == '1' and (nx, ny) not in visited:
                                grid[nx][ny] = '0'
                                queue.append((nx, ny))
        return res


class Solution2:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        M, N = len(grid), len(grid[0])
        queue = collections.deque()
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    queue.append((i, j))
                    while queue:
                        x, y = queue.pop()
                        for d in directions:
                            nx, ny = x + d[0], y + d[1]
                            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                queue.append((nx, ny))
        return res


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution3:
    def isValid(self, grid, r, c):
        m, n = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True

    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        uf = UnionFind(grid)

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for dx, dy in directions:
                        x = i + dx
                        y = j + dy
                        if self.isValid(grid, x, y) and grid[x][y] == '1':
                            uf.union(i * n + j, x * n + y)
        return uf.count




class SolutionTony:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for j in range(n)] for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j, visited)
                    res += 1
        return res

    def bfs(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        queue = [[i, j]]
        if visited[i][j]:
            return False
        visited[i][j] = True
        while queue:
            node = queue.pop(0)
            grid[node[0]][node[1]] = '0'
            for dx, dy in self.directions:
                x = node[0] + dx
                y = node[1] + dy
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != '1' or visited[x][y]:
                    continue
                queue.append([x, y])
                grid[x][y] = '0'
                visited[x][y]



class SolutionTest:
    def numIslands(self, grid) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    res += 1
        return res

    def bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        queue.append([i, j])
        grid[i][j] = '0'

        while queue:
            i, j = queue.popleft()
            print(queue)
            for dx, dy in self.directions:
                x = i + dx
                y = j + dy
                if x < 0 or y < 0 or x >= m or y >= n:
                    continue
                if grid[x][y] == '0':
                    continue

                queue.append([x, y])
                grid[x][y] = '0'

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

a = SolutionTest()
print(a.numIslands(grid))
