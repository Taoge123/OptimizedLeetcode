
class Solution:
    def transpose(self, A):
        m, n = len(A), len(A[0])
        res = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = A[i][j]
        return res


