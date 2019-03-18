

"""
https://leetcode.com/problems/trapping-rain-water-ii/discuss/185437/python3-BFS-%2B-Heap-1D-case-and-2D-case

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map,
compute the volume of water it is able to trap after raining.



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

After the rain, water is trapped between the blocks.
The total volume of water trapped is 4.

"""
"""
The idea is that we maintain all the points of the current border in a min heap 
and always choose the point with the lowest length. 
This is actually an optimized searching strategy over the trivial brute force method: 
instead of dfs each point to find the lowest "border" of its connected component, 
we can always start a search from the lowest border and update the points adjacent to it.
"""


import heapq


class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        import heapq
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0] * n for _ in range(m)]

        # Push all the block on the border into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1

        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height - heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = 1
        return result


class Solution1:
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


"""1D case"""
from heapq import *


class element(object):
    def __init__(self, index, height):
        self.index = index
        self.height = height

    def __lt__(self, other):
        return self.height < other.height


class Solution1D:
    def trap(self, height):
        L = len(height)
        if L <= 2: return 0

        heap, visited = [], set()
        for i in 0, L - 1:
            heap.append(element(i, height[i]))
            visited.add(i)
        heapify(heap)
        max_visited, water = 0, 0

        while heap:
            node = heappop(heap)
            i, h = node.index, node.height
            if h > max_visited:
                max_visited = h
            else:
                water += max_visited - h
            for ni in i - 1, i + 1:
                if 0 <= ni < L and ni not in visited:
                    heappush(heap, element(ni, height[ni]))
                    visited.add(ni)

        return water


"""2D case"""
from heapq import *


class element(object):
    def __init__(self, row, col, height):
        self.row = row
        self.col = col
        self.height = height

    def __lt__(self, other):
        return self.height < other.height


class Solution2D:
    def trapRainWater(self, heightMap):
        H = len(heightMap)
        if H <= 2: return 0
        W = len(heightMap[0])
        if W <= 2: return 0

        heap, visited = [], set()
        for r in 0, H - 1:
            for c in range(W):
                heap.append(element(r, c, heightMap[r][c]))
                visited.add((r, c))
        for c in 0, W - 1:
            for r in range(1, H - 1):
                heap.append(element(r, c, heightMap[r][c]))
                visited.add((r, c))
        heapify(heap)
        max_visited, water = 0, 0

        while heap:
            node = heappop(heap)
            r, c, h = node.row, node.col, node.height
            if h > max_visited:
                max_visited = h
            else:
                water += max_visited - h
            for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in visited:
                    heappush(heap, element(nr, nc, heightMap[nr][nc]))
                    visited.add((nr, nc))

        return water




