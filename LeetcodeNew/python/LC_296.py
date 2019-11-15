"""
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input:

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance
             of 2+2+2=6 is minimal. So return 6.

"""

class Solution:
    def minTotalDistance(self, grid):

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        pos = []
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    pos.append([i, j])

        pos = sorted(pos, key=lambda point: point[0])
        x = pos[len(pos) // 2][0]
        for point in pos:
            res += abs(point[0] - x)

        pos = sorted(pos, key=lambda point: point[1])
        y = pos[len(pos) // 2][1]
        for point in pos:
            res += abs(point[1] - y)

        return res







