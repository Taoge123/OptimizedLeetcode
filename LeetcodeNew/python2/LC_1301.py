"""
https://www.youtube.com/watch?v=WwdjLkWmDPs

1301.Number-of-Paths-with-Max-Score
此题仍然是经典的走迷宫的DP套路。只不过嵌套了两个DP小问题。第一个问题比较简单，设计状态变量dp[i][j]表示从右下角走到(i,j)位置的最大权重路径的权值和。大致的状态转移方程是

dp[i][j] = max(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + board[i][j]-'0'
当然coding的过程中要查验这三个前驱状态是否都存在，也就是处理好边界的情况。

第二个问题和第一个问题息息相关。我们知道dp[i][j]代表了从右下角走到(i,j)位置的最大权重路径，
其本质是在三个前驱状态dp[i+1],dp[i][j+1],dp[i+1][j+1]中取最大的那一个。假设这三个前驱状态中dp[i+1][j]最大，
说明(i,j)要取得最大权值路径，必须要先使得(i+1,j)取得最大权值路径。
因此，从右下角到(i+1,j)的最大权重路径的条数paths[i+1][j]，就对应了有相同多数目的从右下角到(i,j)的最大权重路径，也就是paths[i][j]。

特别的，如果三个前驱状态中有若干个并列最大的，
那么paths[i][j]就是这些前驱状态paths[i+1],paths[i][j+1],paths[i+1][j+1]的加和。
"""


class Solution:
    def pathsWithMaxScore(self, board):
        if not board:
            return [0, 0]
        n = len(board)
        mod = 10 ** 9 + 7
        # dp[i][j][0] is the max value from 'S' to this cell
        # dp[i][j][1] is the number of paths
        dp = [[[-1, 0] for i in range(n + 1)] for j in range(n + 1)]
        dp[0][0] = [0, 0]
        dp[n - 1][n - 1] = [0, 1]

        for i in range(n)[::-1]:
            for j in range(n)[::-1]:
                if board[i][j] in 'XS':
                    continue
                for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                    x = i + dx
                    y = j + dy
                    if dp[i][j][0] < dp[x][y][0]:
                        dp[i][j] = [dp[x][y][0], 0]

                    if dp[i][j][0] == dp[x][y][0]:
                        dp[i][j][1] += dp[x][y][1]
                        dp[i][j][1] %= mod

                # if there exits some path from 'E' to current position, update info of current position
                if dp[i][j][0] != -1 and (i or j):
                    dp[i][j][0] += int(board[i][j])
                    dp[i][j][0] %= mod

        return dp[0][0]




