
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range( n +1)] for j in range( m +1)]
        dp[0][1] = 1
        for i in range(1, m+ 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 0:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m][n]






