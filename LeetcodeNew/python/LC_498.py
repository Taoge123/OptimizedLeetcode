
import collections

class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []

        res = []
        m, n = len(matrix), len(matrix[0])
        lines = collections.defaultdict(list)

        for i in range(m):
            for j in range(n):
                lines[i + j].append(matrix[i][j])

        for k in range(m + n - 1):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]
        return res





matrix = [[ 1, 2, 3 ],
          [ 4, 5, 6 ],
          [ 7, 8, 9 ]]

a = Solution()
print(a.findDiagonalOrder(matrix))




