
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


import functools


class Solution1:  # top down dp - faster
    def maxProductPath(self, grid) -> int:
        # 求 非负数max product
        # non negative vs negative
        mod = 10 ** 9 + 7
        memo = {}
        maxval, minval = self.dfs(grid, 0, 0, memo)
        if maxval >= 0:
            return maxval % mod
        else:
            return -1

    def dfs(self, grid, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # over the range
        if i == len(grid) or j == len(grid[0]):
            return float('-inf'), float('inf')

        # base case
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j], grid[i][j]

        # recursive --> two values
        max1, min1 = self.dfs(grid, i + 1, j, memo)
        max2, min2 = self.dfs(grid, i, j + 1, memo)

        # two values defines
        if grid[i][j] >= 0:
            maxval = max(max1, max2) * grid[i][j]
            minval = min(min1, min2) * grid[i][j]
        else:
            maxval = min(min1, min2) * grid[i][j]
            minval = max(max1, max2) * grid[i][j]

        memo[(i, j)] = maxval, minval
        return memo[(i, j)]



class Solution2:  # top down dp - slower
    def maxProductPath(self, grid) -> int:
        mod = 10 ** 9 + 7
        memo = {}
        maxval, minval = self.dfs(grid, 0, 0, memo)
        if maxval >= 0:
            return maxval % mod
        else:
            return -1

    def dfs(self, grid, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(grid) or j == len(grid[0]):
            return float('-inf'), float('inf')

        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j], grid[i][j]

        maxval, minval = float('-inf'), float('inf')
        for dx, dy in ((1, 0), (0, 1)):
            big, small = self.dfs(grid, i + dx, j + dy, memo)
            if grid[i][j] >= 0:
                if grid[i][j] * big > maxval:
                    maxval = grid[i][j] * big
                if grid[i][j] * small < minval:
                    minval = grid[i][j] * small
            else:
                if grid[i][j] * small > maxval:
                    maxval = grid[i][j] * small
                if grid[i][j] * big < minval:
                    minval = grid[i][j] * big

        memo[(i, j)] = maxval, minval
        return memo[(i, j)]


class Solution:  # bottom down dp
    def maxProductPath(self, grid):
        memo = {}
        m = len(grid)
        n = len(grid[0])
        MOD = 10 ** 9 + 7

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == 0 and j == 0:
                res = grid[i][j], grid[i][j]
            else:
                candidates = []
                if i > 0:
                    top = dp(i - 1, j)
                    candidates.extend([top[0] * grid[i][j], top[1] * grid[i][j]])
                if j > 0:
                    left = dp(i, j - 1)
                    candidates.extend([left[0] * grid[i][j], left[1] * grid[i][j]])
                res = max(candidates), min(candidates)

            memo[(i, j)] = res
            return res

        res = dp(m - 1, n - 1)
        return res[0] % MOD if res[0] >= 0 else -1


class SolutionTD3:
    def maxProductPath(self, grid) -> int:
        mod = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])

        self.res = float('-inf')
        @functools.lru_cache(None)
        def dfs(i, j, prod):
            if i >= 0 and i < m and j >= 0 and j < n:
                prod *= grid[i][j]
                if i == m - 1 and j == n - 1:
                    self.res = max(self.res, prod)
                    return
                dfs(i + 1, j, prod)
                dfs(i, j + 1, prod)

        dfs(0, 0, 1)
        return self.res % mod if self.res >= 0 else -1


class Solution4:
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



