"""
https://www.youtube.com/watch?v=S-fUTfqrdq8

dp[i][0] : ways to cover i cols, both rows of col i are covered
dp[i][1] : ways to cover i cols, top rows of col i are covered
dp[i][2] : ways to cover i cols, bottom rows of col i are covered

dp[0][0] = dp[1][0]

dp[i][0] = dp[i-1][0] + dp[i-1][1] +  dp[i-1][2] + dp[i-2][0]
dp[i][1] = dp[i-1][2] + dp[i-2][0]
dp[i][2] = dp[i-1][1] + dp[i-2][0]

dp[i][1] is always equals to dp[i][2], we can simply

dp[i][0] = dp[i-1][0] + 2 * dp[i-1][1] + dp[i-2][0]
dp[i][1] = dp[i-1][1] + dp[i-2][0]


"""


class Solution:
    def numTilings(self, N: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * 2 for i in range(N + 1)]
        dp[0][0] = dp[1][0] = 1

        for i in range(2, N + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + 2 * dp[i - 1][1]) % mod
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][1]) % mod

        return dp[N][0]




class Solution2:
    def numTilings(self, N):
        mod = 10 ** 9 + 7
        dp = [1, 0, 0, 0]
        for _ in range(N):
            newDP = [0, 0, 0, 0]
            newDP[0b00] = (dp[0b00] + dp[0b11]) % mod
            newDP[0b01] = (dp[0b00] + dp[0b10]) % mod
            newDP[0b10] = (dp[0b00] + dp[0b01]) % mod
            newDP[0b11] = (dp[0b00] + dp[0b01] + dp[0b10]) % mod
            dp = newDP

        return dp[0]

