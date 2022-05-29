
import heapq
import functools
import collections


class SolutionTonyRikahelpedAtinybit:
    def maximumMinimumPath(self, grid) -> int:
        left, right = 0, max(max(row for row in grid))
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def check(i, j, limit):
            if (i, j) in visited or i < 0 or j < 0 or i >= m or j >= n:
                return False
            if grid[i][j] < limit:
                return False
            if (i, j) == (m - 1, n - 1):
                return True
            visited.add((i, j))

            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if check(x, y, limit):
                    return True
            return False

        while left <= right:
            mid = (right - left) // 2 + left
            visited = set()
            if check(0, 0, mid) == True:
                left = mid + 1
            else:
                right = mid - 1
        if left - 1 >= 0:
            return left - 1
        return left




class SolutionHeap:
    def maximumMinimumPath(self, grid):
        m, n = len(grid), len(grid[0])
        heap = [[-grid[0][0], 0, 0]]
        res = float('inf')

        visited = set()

        while True:
            score, i, j = heapq.heappop(heap)
            res = min(res, -score)
            if (i, j) == (m - 1, n - 1):
                return res

            for node in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                x = node[0] + i
                y = node[1] + j
                if x >= 0 and y >= 0 and x < m and y < n and (x, y) not in visited:
                    visited.add((x, y))
                    heapq.heappush(heap, [-grid[x][y], x, y])




class SolutionDFS:
    def maximumMinimumPath(self, grid):
        m, n = len(grid), len(grid[0])

        @functools.lru_cache(None)
        def canPass(val):
            visited = set()

            def dfs(i, j):
                if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited or grid[i][j] < val:
                    return False
                if i == m - 1 and j == n - 1:
                    return True
                visited.add((i, j))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x = i + dx
                    y = j + dy
                    if dfs(x, y):
                        return True
                return False

            return dfs(0, 0)

        vals = []
        for row in grid:
            for col in row:
                vals.append(col)
        vals = sorted(vals)

        left, right = 0, len(vals) - 1
        while left <= right:
            mid = (left + right) // 2
            if canPass(vals[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return vals[right]



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
            self.parent[rootA] = rootB

class Solution:
    def maximumMinimumPath(self, grid) -> int:
        # smilar to swim in rising water

        positions = collections.defaultdict(set)
        m, n = len(grid), len(grid[0])
        start = (0, 0)
        end = (m - 1, n - 1)

        uf = UnionFind()
        for i in range(m):
            for j in range(n):
                positions[grid[i][j]].add((i, j))

        for height in sorted(positions.keys(), reverse=True):
            pos = positions[height]

            for (i, j) in pos:
                for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] >= height:
                        uf.union((i, j), (x, y))

            if uf.find(start) == uf.find(end):
                return height



