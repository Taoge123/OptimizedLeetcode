
import heapq
import functools



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
