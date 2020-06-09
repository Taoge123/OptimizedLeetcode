"""
不断地从1向0扩散，扩散过程中最后一次遇到0那个就是
"""


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = collections.deque()
        water, land = 0, 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])
                    land += 1
                elif grid[i][j] == 0:
                    water += 1

        # 全是水或者全是陆地, 不用搜索
        if not land or not water:
            return -1
        step = -1
        res = 0
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                i, j = queue.popleft()
                for dx, dy in self.directions:
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= n or y < 0 or y >= n:
                        continue

                    # already visited
                    if grid[x][y] == 2:
                        continue

                    if grid[x][y] == 0:
                        res = max(res, step + 1)
                        grid[x][y] = 2
                        queue.append([x, y])
        return res



