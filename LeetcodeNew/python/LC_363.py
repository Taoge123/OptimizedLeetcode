
"""
560. Subarray Sum Equals K
974. Subarray Sums Divisible by K
325. Maximum Size Subarray Sum Equals k
1074. Number of Submatrices That Sum to Target
363. Max Sum of Rectangle No Larger Than K

"""
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
"""
   0  1  2  3  4
0  2  1 -3 -4  5
1  0  6  3  4  1
2  2 -2 -1  4 -5
3 -3  3  1  0  3

0- 2  3  0 -4  1 
1- 0  6  9 13  14
2- 2  0 -1  3 -2
3--3  0  1  1  4


L
R
currSum
maxSum
maxLeft
maxRight
maxUp
maxDown

"""


import bisect

class SolutionBetter:
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(n):
            nums = [0] * m
            for right in range(left, n):
                for i in range(m):
                    nums[i] += matrix[i][right]
                res = max(res, self.kadane(nums, k))
        return res


    def kadane(self, nums, k):
        curSum, maxSum = 0, float('-inf')
        dp = [0]
        for i, num in enumerate(nums):
            curSum += num
            idx = bisect.bisect_left(dp, curSum - k)
            if idx != len(dp):
                maxSum = max(maxSum, curSum - dp[idx])
            bisect.insort(dp, curSum)
        return maxSum




class SolutionTLE:
    def maxSumSubmatrix(self, matrix, k):
        if not matrix or not matrix[0]:
            return 0
        curSum, maxSum = float('-inf'), float('-inf')
        M, N = len(matrix), len(matrix[0])
        for left in range(N):
            curArr = [0] * M
            for right in range(left, N):
                for m in range(M):
                    curArr[m] += matrix[m][right]
                curSum = self.getSumArray(curArr, M, k)
                if curSum > maxSum:
                    maxSum = curSum
        return maxSum

    def getSumArray(self, arr, M, k):
        sums = [0] * (M + 1)
        for i in range(M):
            sums[i + 1] = arr[i] + sums[i]
        res = float('-inf')
        for i in range(M):
            for j in range(i + 1, M + 1):
                curSum = sums[j] - sums[i]
                if curSum <= k and curSum > res:
                    res = curSum
        return res





# matrix = [[1,0,1],[0,-2,3]]
# k = 2
# matrix = [[2, 1,-3,-4, 5],
#           [0, 6, 3, 4, 1],
#           [2,-2,-1, 4,-5],
#           [-3, 3, 1, 0, 3]]
# k = 100

# matrix = [[2],[0],[3],[4],[4]]
# k = 4
matrix = [[1,0,1],[0,-2,3]]
k = 2
a = SolutionBetter()
print(a.maxSumSubmatrix(matrix, k))










