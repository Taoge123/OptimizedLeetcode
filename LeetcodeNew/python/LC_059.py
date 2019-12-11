"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    def generateMatrix(self, n):

        matrix = [[0 ] * n for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        i, j = 0, 0
        for k in range(1, n ** 2 + 1):
            matrix[i][j] = k
            x, y = i + dirs[d][0], j + dirs[d][1]
            if x < 0 or y < 0 or x >= n or y >= n or matrix[x][y] != 0:
                d = (d + 1) % 4
            i, j = i + dirs[d][0], j + dirs[d][1]
            print(i, j)
        return matrix



n = 5
a = Solution()
print(a.generateMatrix(n))



