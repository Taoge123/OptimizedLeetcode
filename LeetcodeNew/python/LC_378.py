"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""


import bisect, heapq

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (low + high) // 2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                low = mid + 1
            else:
                high = mid
        return low



class Solution2:
    def kthSmallest(self, matrix, k: int) -> int:

        heap = [(matrix[0][0], 0, 0)]
        n = len(matrix)
        res = 0
        for k in range(1, k + 1):
            res, row, col = heapq.heappop(heap)
            if not row and col < n - 1:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            if row < n - 1:
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
        return res



class Solution3:
    def kthSmallest(self, matrix, k):
        heap = [(row[0], i, 0) for i, row in enumerate(matrix) if row]
        res = 0
        heapq.heapify(heap)
        for k in range(1, k + 1):
            res, row, col = heapq.heappop(heap)
            if col + 1 < len(matrix[row]):
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        return res


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8


a = Solution()
print(a.kthSmallest(matrix, k))



