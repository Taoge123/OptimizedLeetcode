"""
https://www.youtube.com/watch?v=n4KHWvjfVx8
https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-1223-dice-roll-simulation/

1223.Dice-Roll-Simulation
本题属于一类常规的DP题。这类题目的特征就是“不能出现联系多少个XXX”。

以前做过一类更简化的版本，就是“不能出现连续两个相同的XXX”。那种情况下，定义dp[i][j]表示第i轮选择状态j，则dp[i][j] = sum(dp[i-1][j'])其中j'是所有的状态选择但不能是j。

这个题目更general，不能连续出现的次数是个变量，而且与j有关。于是我们可以定义dp[i][j][k]表示“第i轮选择状态j、并且结尾已经出现了连续k个状态j的方案数目”。显然我们可以分两种情况讨论：

k==1，说明第i-1轮的时候可以选任何不同于j的状态j'，并且第三个下标没有限制（只要不超过rollMax[j']的限制即可）。
k>1，说明第i-1轮的时候必须任然是j的状态，且第三个下标只能是k-1（表示结尾连续出现了k-1次）
最终的结果就是dp[n][j][k]对于任意j和k的情况的总和。

"""


class Solution:
    def dieSimulator(self, n, rollMax):

        mod = 10 ** 9 + 7
        dp = [[[0 for _ in range(16)] for _ in range(6)] for _ in range(n)]
        for j in range(6): dp[0][j][1] = 1

        for i in range(1, n):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    for jj in range(6):
                        if j == jj:
                            if k + 1 <= rollMax[j]:
                                dp[i][jj][k + 1] += dp[i - 1][j][k]
                        else:
                            dp[i][jj][1] += dp[i - 1][j][k]

        return sum(sum(row) for row in dp[-1]) % mod


class Solution1:
    def dieSimulator(self, n, rollMax):
        dp = [[[0] * (16) for _ in range(6)] for _ in range(n + 1)]
        MOD = 10 ** 9 + 7
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                for pre in range(6):
                    for k in range(1, rollMax[pre] + 1):
                        if pre != j:
                            dp[i][j][1] += dp[i - 1][pre][k]
                        elif k < rollMax[pre]:
                            dp[i][j][k + 1] += dp[i - 1][j][k]

        res = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                res = (res + dp[n][j][k]) % MOD

        return res

class SolutionLee:
    def dieSimulator(self, n, rollMax):
        mod = 10 ** 9 + 7
        dp = [[0, 1] + [0] * 15 for i in range(6)]
        for _ in range(n - 1):
            dp2 = [[0] * 17 for i in range(6)]
            for i in range(6):
                for k in range(1, rollMax[i] + 1):
                    for j in range(6):
                        if i == j:
                            if k < rollMax[i]:
                                dp2[j][k + 1] += dp[i][k] % mod
                        else:
                            dp2[j][1] += dp[i][k] % mod
            dp = dp2
        return sum(sum(row) for row in dp) % mod



