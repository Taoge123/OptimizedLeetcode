import heapq


class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        heap = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heapq.heappush(heap, (0, 0, 0))

        visited = set()

        while heap:
            cost, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == m - 1 and j == n - 1:
                return cost
            for num, (dx, dy) in enumerate(directions):
                x = i + dx
                y = j + dy
                if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visited:

                    if grid[i][j] == (num + 1):
                        heapq.heappush(heap, (cost, x, y))
                    else:
                        heapq.heappush(heap, (cost + 1, x, y))



