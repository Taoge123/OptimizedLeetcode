
"""

本题的思想与 152.Maximum-Product-Subarray 相同。

和传统的最优路径题一样，令dp[i][j]表示从左上角走到(i,j)的最优代价（即路径乘积最大）。根据规则，dp[i][j]仅由dp[i-1][j]和dp[i][j-1]转移而来。但是不同于以往的套路：

dp[i][j] = max(dp[i][j-1]*nums[i][j], dp[i-1][j]*nums[i][j])
在这里，如果nums[i][j]为负数的话，我们希望已知的反而是走到(i-1,j)和(i,j-1)的最小乘积路径，这样与nums[i][j]相乘之后才能得到的是最大乘积路径。这就提醒我们要维护两个状态变量，dp1[i][j]和dp2[i][j]来分别记录到当前的最大乘积路径和最小乘积路径。

dp1[i][j] = max(max(dp1[i][j-1]*nums[i][j], dp1[i-1][j]*nums[i][j]), max(dp2[i][j-1]*nums[i][j], dp2[i-1][j]*nums[i][j]));
dp2[i][j] = min(min(dp1[i][j-1]*nums[i][j], dp1[i-1][j]*nums[i][j]), min(dp2[i][j-1]*nums[i][j], dp2[i-1][j]*nums[i][j]))'

dp[i][j] : tje optimal cosr if we travel from top-left to (i, j)

the minimum sum path :
dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + nums[i][j]

the maximum sum path :
dp[i][j] = max(dp[i-1][j], dp[i][j-1]) * nums[i][j]

max = max(min(i-1,j) * nums[i][j], max(i-1, j) * nums[i][j],
           1                -1           2            -1
          min(i,j-1) * nums[i][j], max(i, j-1) * nums[i][j])

min = min(min(i-1,j) * nums[i][j], max(i-1, j) * nums[i][j],
           1                -1           2            -1
          min(i,j-1) * nums[i][j], max(i, j-1) * nums[i][j])

max(m-1, n-1)

"""



class Solution:
    def maxProductPath(self, grid) -> int:
        # dp1 is the max product path from top left to (i, j)
        # dp2 is the min product path from top left to (i, j)
        dp1 = [[0 for i in range(16)] for j in range(16)]
        dp2 = [[0 for i in range(16)] for j in range(16)]

        m, n= len(grid), len(grid[0])
        mod = 10 ** 9 + 7

        dp1[0][0] = grid[0][0]
        dp2[0][0] = grid[0][0]

        for i in range(1, m):
            dp1[i][0] = dp1[i - 1][0] * grid[i][0]
            dp2[i][0] = dp2[i - 1][0] * grid[i][0]

        for j in range(1, n):
            dp1[0][j] = dp1[0][j - 1] * grid[0][j]
            dp2[0][j] = dp2[0][j - 1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp1[i][j] = max(max(dp1[i - 1][j] * grid[i][j], dp2[i - 1][j] * grid[i][j]),
                                max(dp1[i][j - 1] * grid[i][j], dp2[i][j - 1] * grid[i][j]))

                dp2[i][j] = min(min(dp1[i - 1][j] * grid[i][j], dp2[i - 1][j] * grid[i][j]),
                                min(dp1[i][j - 1] * grid[i][j], dp2[i][j - 1] * grid[i][j]))

        if dp1[m - 1][n - 1] < 0:
            return -1
        else:
            return dp1[m - 1][n - 1] % mod



