"""

1292.Maximum-Side-Length-of-a-Square-with-Sum-Less-than-or-Equal-to-Threshold
本题可以遍历每个方阵，查看方阵的和sum是否满足条件。这样的时间复杂度是o(N^3)，其中遍历每个元素作为方阵的右下角需要o(N^2)，探索不同的边长需要o(N)。

本题更高效的方法就是二分搜值。猜测一个边长len，查看是否有一个方阵的sum满足条件。这样的时间复杂度是o(logN*N^2).

注意，本题中计算一个方阵的sum的方法可以是o(1)，只要提前计算所有(0,0)到(i,j)的矩阵和presum[i][j]。

presum[i][j] : sum of rectangle (0,0) (i,j)
sum[i][j] of len : presum[i][j] - presum[i][j-len] - presum[i-len][j] + presum[i-len][j-len]

O(N^2) * O(N) = O(N^3)

Binary Search is better

len : O(N^2)


"""


class Solution:
    def maxSideLength(self, mat, threshold: int) -> int:
        self.m, self.n = len(mat), len(mat[0])
        preSum = [[0 for i in range(self.n + 1)] for j in range(self.m + 1)]
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1] + mat[i - 1][j - 1]

        left, right = 1, min(self.m, self.n)
        while left < right:
            mid = right - (right - left) // 2
            if self.check(mid, threshold, preSum):
                left = mid
            else:
                right = mid - 1

        if self.check(left, threshold, preSum):
            return left
        else:
            return 0

    def check(self, num, threshold, preSum):
        for i in range(num, self.m + 1):
            for j in range(num, self.n + 1):
                summ = preSum[i][j] - preSum[i][j - num] - preSum[i - num][j] + preSum[i - num][j - num]
                if summ <= threshold:
                    return True
        return False


