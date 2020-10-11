
import heapq

class Solution:
    def swimInWater(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        heap = []
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited = set()
        visited.add((0, 0))
        res = 0

        while heap:
            node, i, j = heapq.heappop(heap)
            res = max(res, node)

            if i == j == n - 1:
                return res

            for dx, dy in self.directions:
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited:
                    continue

                heapq.heappush(heap, (grid[x][y], x, y))
                visited.add((x, y))




class SolutionBS:
    def swimInWater(self, grid) -> int:
        n = len(grid)
        left = 0
        right = n * n - 1
        while left < right:
            mid = (right - left) // 2 + left
            visited = [[0 for i in range(n)] for j in range(n)]
            if self.helper(grid, visited, 0, 0, grid[n - 1][n - 1], mid):
                right = mid
            else:
                left = mid + 1
        return left

    def helper(self, grid, visited, i, j, target, time):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visited[i][j] or grid[i][j] > time:
            return False
        visited[i][j] = True
        if grid[i][j] == target:
            return True
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            x = i + dx
            y = j + dy
            if self.helper(grid, visited, x, y, target, time):
                return True
        return False

