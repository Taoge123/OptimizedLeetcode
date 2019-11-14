
class Solution:
    def setZeroes(self, matrix):

        rownum = len(matrix)
        colnum = len(matrix[0])

        row = [False for i in range(rownum)]
        col = [False for i in range(colnum)]

        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(rownum):
            for j in range(colnum):
                if row[i] or col[j]:
                    matrix[i][j] = 0




