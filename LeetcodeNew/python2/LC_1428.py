# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
   def get(self, row: int, col: int) -> int:
       pass
   def dimensions(self):
       pass

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        res = n
        for row in range(m):
            left = 0
            right = n - 1
            while left < right:
                mid = (left + right) // 2
                if binaryMatrix.get(row, mid) == 0:
                    left = mid + 1
                else:
                    right = mid

            if binaryMatrix.get(row, left) == 1:
                res = min(res, left)

        if res == n:
            return -1
        else:
            return res



