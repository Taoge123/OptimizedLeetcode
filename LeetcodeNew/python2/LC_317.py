
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

                            if 0 <= r < m and 0 <= c < n and grid[r][c] == 0 and not visited[r][c]:
                                distance[r][c] += dist + 1
                                reach[r][c] += 1
                                visited[r][c] = True
                                queue.append((r, c, dist + 1))

        shortest = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == buildingNum:
                    shortest = min(shortest, distance[i][j])

        return shortest if shortest < float("inf") else -1


grid = [[1,0,2,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0]]

a = Solution()
print(a.shortestDistance(grid))



