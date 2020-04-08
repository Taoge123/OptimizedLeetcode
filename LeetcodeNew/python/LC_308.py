"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""


class NumMatrix:
    def __init__(self, matrix):
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return
        self.nums = [[0 for j in range(n)] for i in range(m)]
        self.BIT = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def _lowbit(self, a):
        return a & -a

    def update(self, row, col, val):
        m, n = len(self.nums), len(self.nums[0])
        diff = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row + 1
        while i <= m:
            j = col + 1
            while j <= n:
                self.BIT[i][j] += diff
                j += (self._lowbit(j))
            i += (self._lowbit(i))

    def getSum(self, row, col):
        res = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.BIT[i][j]
                j -= (self._lowbit(j))
            i -= (self._lowbit(i))
        return res

    def sumRegion(self, row1, col1, row2, col2):
        return self.getSum(row2, col2) - self.getSum(row2, col1 - 1) \
               - self.getSum(row1 - 1, col2) + self.getSum(row1 - 1, col1 - 1)






class NumMatrix2:
    def __init__(self, matrix):
        self.tree = matrix
        for row in matrix:
            for i in range(1, len(row)):
                row[i] += row[i - 1]

    def update(self, row, col, val):
        row = self.tree[row]
        orig = row[col] - (row[col - 1] if col else 0)
        for i in range(col, len(row)):
            row[i] += val - orig

    def sumRegion(self, row1, col1, row2, col2):
        res = 0
        for i in range(row1, row2 + 1):
            res += self.tree[i][col2] - (self.tree[i][col1 - 1] if col1 else 0)
        return res





