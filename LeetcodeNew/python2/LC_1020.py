
"""
一个矩阵,四周都是海水, 1是沙子, 0海水灌不进来，如果1被0包围了也灌不进来，
海水进来以后看有几个坑

"""

import collections

class Solution:
    def numEnclaves(self, A) -> int:
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    self.dfs(A, i, j)
        return sum(sum(row) for row in A)

    def dfs(self, A, i, j):
        m, n = len(A), len(A[0])
        A[i][j] = 0
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if x >= 0 and x < m and y >= 0 and y < n and A[x][y]:
                self.dfs(A, x, y)



class SolutionBFS2:
    def numEnclaves(self, A) -> int:
        res = sum(map(sum, A))
        m, n = len(A), len(A[0])
        land = []
        for i in range(m):
            if A[i][0]:
                A[i][0] = 0
                land.append([i, 0])

            if A[i][n - 1]:
                A[i][n - 1] = 0
                land.append([i, n - 1])

        for j in range(n):
            if A[0][j]:
                A[0][j] = 0
                land.append([0, j])
            if A[m - 1][j]:
                A[m - 1][j] = 0
                land.append([m - 1, j])

        res -= len(land)

        while land:
            land2 = []
            for x0, y0 in land:
                for i, j in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                    x = x0 + i
                    y = y0 + j
                    if x >= 0 and x < m and y >= 0 and y < n and A[x][y]:
                        A[x][y] = 0
                        land2.append([x, y])
            land = land2
            res -= len(land)
        return res



class SolutionBFS:
    def numEnclaves(self, A) -> int:
        m, n = len(A), len(A[0])
        res = 0
        queue = collections.deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                res += A[i][j]
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and A[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            i, j = queue.popleft()
            A[i][j] = 0
            res -= 1

            for node in directions:
                x = i + node[0]
                y = j + node[1]
                if x >= 0 and x < m and y >= 0 and y < n and A[x][y] == 1 and (x, y) not in visited:
                    queue.append((x, y))
                    visited.add((x, y))
                    A[x][y] = 0

        return res




