
class Solution:
    def kWeakestRows(self, mat, k: int):
        m, n = len(mat), len(mat[0])
        row = []
        for i in range(m):
            row.append([sum(mat[i]), i])

        row.sort()
        res = []
        for i in range(k):
            res.append(row[i][1])
        return res


