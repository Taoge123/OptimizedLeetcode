
class Solution:
    def isToeplitzMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i> 0 and j > 0 and matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True

class SolutionLee:
    def isToeplitzMatrix(self, m):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True




