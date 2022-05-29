

class SolutionDFS:
    def closedIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            # reach perimeter, then return 1, so this is not a closed island
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1

            if grid[i][j] != 0:
                return 0

            grid[i][j] = -1

            res = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                res += dfs(x, y)

            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                if dfs(i, j) == 0:
                    res += 1
        return res




class SolutionTony:
    def closedIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                if self.dfs(grid, i, j, m, n) == 0:
                    res += 1
        return res

    def dfs(self, grid, i, j, m, n):
        #reach perimeter, then return 1, so this is not a closed island
        if i < 0 or j < 0 or i >= m or j >= n:
            return 1

        if grid[i][j] != 0:
            return 0

        grid[i][j] = -1

        up = self.dfs(grid, i - 1, j, m, n)
        down = self.dfs(grid, i + 1, j, m, n)
        left = self.dfs(grid, i, j - 1, m, n)
        right = self.dfs(grid, i, j + 1, m, n)

        return up or down or left or right





class Solution:
    def closedIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(grid, i, j, m, n):
            if i< 0 or j < 0 or i >= m or j >= n:
                return 1

            if grid[i][j] != 0:
                return 0

            grid[i][j] = -1

            up = dfs(grid, i - 1, j, m, n)
            down = dfs(grid, i + 1, j, m, n)
            left = dfs(grid, i, j - 1, m, n)
            right = dfs(grid, i, j + 1, m, n)

            return up or down or left or right

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                if dfs(grid, i, j, m, n) == 0:
                    res += 1

        return res



class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i

        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[min(rootA, rootB)] = max(rootA, rootB)


class SolutionRika:  # for loop once
    def closedIsland(self, grid):
        # num of island - num of island that connected with 边边
        uf = UnionFind()

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        uf.union(i * n + j, m * n)
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                            uf.union(i * n + j, x * n + y)

        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    root = uf.find(i * n + j)
                    if root != m * n and root not in visited:
                        visited.add(root)
        return len(visited)



