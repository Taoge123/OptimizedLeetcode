

"""
    1  2
 6        3
    5  4

    1-6 => 2
    []  [2 3 4 5 6]

    1-6 => 3
    [1 2 3]  [3 4 5 6]

    1-6 => 4
    [1 2 3 4]  [4 5 6]

    1-6 => 5
    [1 2 3 4 5]  []


"""


class Solution:
    def minScoreTriangulation(self, A) -> int:
        n = len(A)
        dp = [[0 for i in range(n)] for j in range(n)]

        for step in range(2, n):
            for i in range(n - step):
                j = i + step
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + A[i] * A[j] * A[k] + dp[k][j])

        return dp[0][n - 1]







