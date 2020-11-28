
"""
1463.Cherry-Pickup-II
相比于741.Cherry-Pickup，这题的解法对于DP的倾向性更加明显，因为这题有非常显著的“轮次”的特点：每走一步就下降一行。
这一行（两个机器人）的选择，取决于上一行（两个机器人）的选择。因此我们设计dp[i][j]表示在当前行、
两个机器人分别在横坐标位置i和j时，此时的最大收益。我们接下来只需要考虑上一行里，哪些dp[a][b]可以转移到这一行的dp[i][j]。因为每次横向移动的氛围只有-1到1，所以枚举一下就行啦。


dp[i][j] : for a given row, the maximum number of cherries collections using both both robots at i and at j

dp[r][i][j] = min(dp[r-1][a][b] + grid[r][i] + grid[r][j])


"""

import copy

class Solution:
    def cherryPickup(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('-inf') for i in range(n)] for j in range(n)]
        dp[0][n - 1] = grid[0][0] + grid[0][n - 1]

        for row in range(1, m):
            dp_old = copy.deepcopy(dp)
            for i in range(n):
                for j in range(n):
                    for a in range(i - 1, i + 2):
                        for b in range(j - 1, j + 2):
                            if a < 0 or a >= n or b < 0 or b >= n:
                                continue
                            if i != j:
                                dp[i][j] = max(dp[i][j], dp_old[a][b] + grid[row][i] + grid[row][j])
                            else:
                                dp[i][j] = max(dp[i][j], dp_old[a][b] + grid[row][i])

        res = float('-inf')
        for i in range(n):
            for j in range(n):
                res = max(res, dp[i][j])

        return res



