
class Solution:
    def numSubmat(self, mat) -> int:
        m, n = len(mat), len(mat[0])
        count = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in reversed(range(n)):
                if mat[i][j] == 1:
                    if j < n - 1:
                        count[i][j] += 1 + count[i][ j +1]
                    else:
                        count[i][j] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                min_width = float('inf')
                for k in range(i, m):
                    if mat[i][j] == 1:
                        min_width = min(min_width, count[k][j])
                        res += min_width

        return res






