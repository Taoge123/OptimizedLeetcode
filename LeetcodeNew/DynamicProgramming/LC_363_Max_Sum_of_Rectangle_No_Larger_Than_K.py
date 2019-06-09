
"""
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
Note:

The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""

# Convert the problem to 1-D and them find max subarray no larger than K.
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        maxSum = -9999999
        horizontalSum = [[0 for j in range(0, len(matrix[0]) + 1)] for i in range(0, len(matrix))]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                horizontalSum[i][j] = horizontalSum[i][j - 1] + matrix[i][j]
        for cola in range(0, len(matrix[0])):
            for colb in range(cola, len(matrix[0])):
                bilist, vsum = [0], 0
                for i in range(0, len(matrix)):
                    vsumj = horizontalSum[i][colb] - horizontalSum[i][cola - 1]
                    vsum += vsumj
                    i = bisect.bisect_left(bilist, vsum - k)
                    if i < len(bilist):
                        maxSum = max(maxSum, vsum - bilist[i])
                    bisect.insort(bilist, vsum)
        return maxSum

"""
M = # of rows, N= # of cols
M > N
O(N^2 M^2)
bisect.bisect() takes O(logM) but bisect.insort() takes O(M)
"""


class Solution2:
    def maxSumSubmatrix(self, matrix, k):

        n_row, n_col = len(matrix), len(matrix[0])
        ans = float('-inf')
        for l in range(n_col):
            sums = [0] * n_row
            for r in range(l, n_col):
                for i in range(n_row):
                    sums[i] += matrix[i][r]
                ans = max(ans, self.maxSubArray(sums, k))
        return ans

    def maxSubArray(self, nums, k):
        cur_sum, max_sum = 0, float('-inf')
        sums = [0]
        for i, n in enumerate(nums, 1):
            cur_sum += n
            idx = bisect.bisect_left(sums, cur_sum - k)
            if idx != i:
                max_sum = max(max_sum, cur_sum - sums[idx])
            bisect.insort(sums, cur_sum)
        return max_sum







