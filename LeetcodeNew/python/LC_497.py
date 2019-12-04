
"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.



Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:



Note:

The total number of elements of the given matrix will not exceed 10,000.
"""

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
                lines[i+j].append(matrix[i][j])

        for k in range(m + n - 1):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]
        return res


class Solution2:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []

        res = []
        m, n = len(matrix), len(matrix[0])
        lines = collections.defaultdict(list)

        for i in range(m):
            for j in range(n):
                lines[i + j].append(matrix[i][j])

        for k, val in lines.items():
            if k % 2 == 0:
                res += val[::-1]
            else:
                res += val

        return res








