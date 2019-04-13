
"""
https://leetcode.com/problems/range-sum-query-2d-immutable/solution/
https://www.youtube.com/watch?v=PwDqpOMwg6U

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined
by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

"""
Construct a 2D array sums[row+1][col+1]

(notice: we add additional blank row sums[0][col+1]={0} and blank column sums[row+1][0]={0} to remove the edge case checking), so, we can have the following definition

sums[i+1][j+1] represents the sum of area from matrix[0][0] to matrix[i][j]

To calculate sums, the ideas as below

+-----+-+-------+     +--------+-----+     +-----+---------+     +-----+--------+
|     | |       |     |        |     |     |     |         |     |     |        |
|     | |       |     |        |     |     |     |         |     |     |        |
+-----+-+       |     +--------+     |     |     |         |     +-----+        |
|     | |       |  =  |              |  +  |     |         |  -  |              |
+-----+-+       |     |              |     +-----+         |     |              |
|               |     |              |     |               |     |              |
|               |     |              |     |               |     |              |
+---------------+     +--------------+     +---------------+     +--------------+

   sums[i][j]      =    sums[i-1][j]    +     sums[i][j-1]    -   sums[i-1][j-1]   +  

                        matrix[i-1][j-1]
So, we use the same idea to find the specific area's sum.

+---------------+   +--------------+   +---------------+   +--------------+   +--------------+
|               |   |         |    |   |   |           |   |         |    |   |   |          |
|   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |          |
|   +------+    |   |         |    |   |   |           |   +---------+    |   +---+          |
|   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)    |
|   |      |    |   |         |    |   |   |           |   |              |   |              |
|   +------+    |   +---------+    |   +---+           |   |              |   |              |
|        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |              |
+---------------+   +--------------+   +---------------+   +--------------+   +--------------+
And we can have the following code
"""

class NumMatrix1:

    def __init__(self, matrix):
        self.sums = [[0] * (len(matrix and matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix and matrix[0])):
                self.sums[i + 1][j + 1] = self.sums[i][j + 1] + self.sums[i + 1][j] - self.sums[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.sums[row2 + 1][col2 + 1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1] + self.sums[row1][col1]



class NumMatrix2:
    def __init__(self, matrix):
        if not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                self.sum[i+1][j+1] = self.sum[i+1][j] + self.sum[i][j+1] + matrix[i][j] - self.sum[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.sum[row2+1][col2+1]-self.sum[row1][col2+1] - self.sum[row2+1][col1] + self.sum[row1][col1]


"""
# (0,0)
# ---------------------------
# |                         |
# |           (r1,c1)       |
# |             |-----------|(r1,c2)
# |             |  RegionA  |
# | ------------------------|(r2,c2)
# |           (r2,c1)       |
#  --------------------------
#  RegionA = region(0,0 to r2,c2) - 
#       region(0,0 to r2,c1) - 
#       region(0,0 to r1,c2) + 
#       region(0,0 to r1,c1)
"""


class NumMatrix3:

    def __init__(self, matrix):

        if not matrix or not matrix[0]:
            M, N = 0, 0
        else:
            M, N = len(matrix), len(matrix[0])
        self.sumM = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                self.sumM[i + 1][j + 1] = self.sumM[i][j + 1] + self.sumM[i + 1][j]  - self.sumM[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):

        return self.sumM[row2 + 1][col2 + 1] - self.sumM[row2 + 1][col1] - self.sumM[row1][col2 + 1] + self.sumM[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

"""
题目大意：
给定一个二维矩阵，计算从(row1, col1) 到 (row2, col2)的子矩阵的和。

测试用例见题目描述。

注意：

你可以假设矩阵不会改变
sumRegion函数会调用很多次
你可以假设row1 ≤ row2， 并且 col1 ≤ col2。
解题思路：
构造辅助二维数组sums

sums[x][y]表示从0,0到x,y的子矩阵的和

利用容斥原理，可知：

sumRange(row1, col1, row2, col2) = sums[row2][col2] + sums[row1 - 1][col1 - 1] - sums[row1 - 1][col2] - sums[row2][col1 - 1]
将辅助矩阵的行数和列数+1，可以简化对矩阵边界的处理。
"""

class NumMatrix(object):
    def __init__(self, matrix):

        m = len(matrix)
        n = len(matrix[0]) if m else 0
        self.sums = [[0] * (n + 1) for x in range(m + 1)]
        for x in range(1, m + 1):
            rowSum = 0
            for y in range(1, n + 1):
                self.sums[x][y] += rowSum + matrix[x - 1][y - 1]
                if x > 1:
                    self.sums[x][y] += self.sums[x - 1][y]
                rowSum += matrix[x - 1][y - 1]

    def sumRegion(self, row1, col1, row2, col2):

        return self.sums[row2 + 1][col2 + 1] + self.sums[row1][col1] \
                 - self.sums[row1][col2 + 1] - self.sums[row2 + 1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)




