import collections

class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        table = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                table[i - j].append(mat[i][j])

        for k in table:
            table[k].sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = table[i - j].pop()

        return mat


