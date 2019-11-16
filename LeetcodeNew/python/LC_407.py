
"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.



Note:

Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.



Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.





After the rain, water is trapped between the blocks. The total volume of water trapped is 4.
"""
import heapq

class Solution:
    def trapRainWater(self, heightMap):
        m, n, heap, trapped = len(heightMap), len(heightMap and heightMap[0]), [], 0
        for i in range(m):
            for j in range(n):
                if i in {0, m - 1} or j in {0, n - 1}:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 < x < m - 1 and 0 < y < n - 1 and heightMap[x][y] != -1:
                    trapped += max(h - heightMap[x][y], 0)
                    heapq.heappush(heap, (max(heightMap[x][y], h), x, y))
                    heightMap[x][y] = -1
        return trapped







