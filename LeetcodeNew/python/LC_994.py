"""
Idea: We do BFS simultaneously from all rotten oranges, while using a counter to keep track of the number of fresh oranges that has become rotten.
Once the counter is equal to the total number of fresh oranges, we return the number of days elapsed.
If after the BFS, the counter is less than the total number of fresh oranges, we return -1.

Time complexity: O(n), space complexity: O(n), where n is the total number of cells.
"""


class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        fresh = 0
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                # fresh
                if grid[i][j] == 1:
                    fresh += 1
                # we start with rotten
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))
        visited = set()
        while queue:
            i, j, step = queue.popleft()
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                    visited.add((x, y))
                    fresh -= 1
                    if fresh == 0:
                        return step + 1
                    queue.append((x, y, step + 1))
        return 0 if fresh == 0 else -1





