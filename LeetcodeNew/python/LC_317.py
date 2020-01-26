
"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""


class Solution:
    def shortestDistance(self, grid):
        m = len(grid)
        n = len(grid[0])

        distance = [[0 for _ in range(n)] for _ in range(m)]
        reach = [[0 for _ in range(n)] for _ in range(m)]

        buildingNum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildingNum += 1
                    queue = [(i, j, 0)]

                    visited = [[False for _ in range(n)] for _ in range(m)]
                    for x, y, dist in queue:
                        for dirs in (-1, 0), (1, 0), (0, -1), (0, 1):
                            r = x + dirs[0]
                            c = y + dirs[1]

                            if 0 <= r < m and 0 <= c < n and grid[r][c] == 0 \
                                    and not visited[r][c]:
                                distance[r][c] += dist + 1
                                reach[r][c] += 1
                                visited[r][c] = True
                                queue.append((r, c, dist + 1))

        res = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == buildingNum:
                    res = min(res, distance[i][j])

        return res if res < float("inf") else -1



class Solution2:
    def shortestDistance(self, grid) -> int:
        if not grid or len(grid) == 0:
            return -1

        m, n = len(grid), len(grid[0])

        dist = [[0 for i in range(n)] for j in range(m)]
        nums = [[0 for i in range(n)] for j in range(m)]

        buildingNum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildingNum += 1
                    self.bfs(grid, i, j, dist, nums)

        res = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dist[i][j] != 0 and nums[i][j] == buildingNum:
                    res = min(res, dist[i][j])
        print(dist)
        if res == float('inf'):
            return -1
        else:
            return res

    def bfs(self, grid, row, col, dist, nums):
        m, n = len(grid), len(grid[0])
        queue = []
        queue.append([row, col])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = [[0 for i in range(n)] for j in range(m)]
        distance = 0

        while queue:
            distance += 1
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)
                for k in range(len(dirs)):
                    x = cur[0] + dirs[k][0]
                    y = cur[1] + dirs[k][1]
                    if (x >= 0 and x < m and y >= 0 and y < n) and not visited[x][y] and grid[x][y] == 0:
                        visited[x][y] = True
                        dist[x][y] += distance
                        nums[x][y] += 1
                        queue.append([x, y])




grid = [[1,0,2,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0]]

a = Solution()
print(a.shortestDistance(grid))



