
"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]


Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""


# class Solution:
#     def updateMatrix(self, matrix):
#         m, n = len(matrix), len(matrix and matrix[0])
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] != 0:
#                     matrix[i][j] = float("inf")
#                     if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
#                         matrix[i][j] = matrix[i - 1][j] + 1
#                     if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
#                         matrix[i][j] = matrix[i][j - 1] + 1
#         for i in range(m - 1, -1, -1):
#             for j in range(n - 1, -1, -1):
#                 if matrix[i][j] != 0:
#                     if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
#                         matrix[i][j] = matrix[i + 1][j] + 1
#                     if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
#                         matrix[i][j] = matrix[i][j + 1] + 1
#         return matrix

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        queue = collections.deque()
        m, n = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = float('inf')

        while queue:
            node = queue.popleft()
            for dir in directions:
                x, y = node[0] + dir[0], node[1] + dir[1]
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[node[0]][node[1]] + 1:
                    matrix[x][y] = matrix[node[0]][node[1]] + 1
                    queue.append((x, y))

        return matrix







