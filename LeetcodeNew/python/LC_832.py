
class Solution:
    def flipAndInvertImage(self, A):
        self.flip(A)
        self.invert(A)
        return A

    def flip(self, A):
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n // 2):
                A[i][j], A[i][n - j - 1] = A[i][n - j - 1], A[i][j]
        return A

    def invert(self, A):
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                A[i][j] ^= 1
        return A


