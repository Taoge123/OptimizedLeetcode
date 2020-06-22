
"""
dp[i][j] - i个数有j个全排列的方案

[6 X X X X X ]
dp[6][j] j = 0,1,2,3,...,k
dp[S][j] j = 0,1,2,3,...,k

dp[6][j] = dp[5][j-5] + dp[5][j-4] + .. + dp[5][j]


dp[i][j] = dp[i-1][j-0] + dp[i-1][j-1] + dp[i-1][j-2].. + dp[i-1][j-(i-2)] + dp[i-1][j-(i-1)]

dp[i][j-1] = dp[i-1][j-1] + dp[i-1][j-2] + dp[i-1][j-3].. + dp[i-1][j-(i-1)] + dp[i-1][j-(i)]

dp[i][j] = dp[i][j-1] + dp[i-1][j-0] - dop[i-1][j-(i)]



"""
import collections


class SolutionTLE:
    def kInversePairs(self, n: int, k: int) -> int:

        dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
        mod = 10 ** 9 + 7
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for m in range(min(j, i - 1) + 1):
                    dp[i][j] += dp[i - 1][j - m]
                    dp[i][j] %= mod

        return dp[n][k]




class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
        mod = 10 ** 9 + 7
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if j >= i:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 0] - dp[i - 1][j - i]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 0]
                dp[i][j] %= mod

        return dp[n][k]




class Solution2:
    memo = collections.defaultdict(int)
    mod = 10 ** 9 + 7

    def kInversePairs(self, n: int, k: int) -> int:
        print(n, k)
        if n == 0:
            return 0
        if k == 0:
            return 1
        if (n, k) in self.memo:
            return self.memo[(n, k)]
        res = 0
        for i in range(min(k, n - 1) + 1):
            res = (res + self.kInversePairs(n - 1, k - i)) % self.mod
        self.memo[(n, k)] = res
        return res

a = Solution2()
print(a.kInversePairs(1000, 1000))

