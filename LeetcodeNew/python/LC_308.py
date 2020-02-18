

class NumMatrix:
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





