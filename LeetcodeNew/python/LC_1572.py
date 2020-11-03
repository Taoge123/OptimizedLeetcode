class Solution:
    def diagonalSum(self, mat) -> int:
        visited = set()

        n = len(mat)
        for i in range(n):
            visited.add((i, i))
            visited.add((i, n - i - 1))

        res = 0
        for i, j in visited:
            res += mat[i][j]
        return res

