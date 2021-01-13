class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))

        visited = set()
        visited.add((0, 0))
        res = 0

        while heap:
            node, i, j = heapq.heappop(heap)
            res = max(res, node)

            if i == n - 1 and j == n - 1:
                return res

            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if x < 0 or x >= n or y < 0 or y >= n:
                    continue
                if (x, y) in visited:
                    continue

                heapq.heappush(heap, (grid[x][y], x, y))
                visited.add((x, y))




