import functools


"""
https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/discuss/898847/Python-top-down-DP-n*k-w-explanation

dp[i][k] : for the first i points, the number of wayss to construct k line segments


dp0[i][k] : for the first i points, we do not use ith point for a line segment, the number of wayss to construct k line segments
dp1[i][k] : for the first i points, we do use ith point for a line segment, the number of wayss to construct k line segments



X X X X X X X X i
              ---  dp[i-1][k-1]
            -----  dp[i-2][k-1]
        ---------  dp[][]
     ...

----------------- dp[0][k-1]
dp[i][k] = sum {dp[j][k-1]} for j=0,1,2,...,i-1

X X X X X X X X i
        ....____*  dp1[i-1][k]
      ....____* *  dp1[i-2][k]
    ....____* * *  dp1[i-3][k]

* * * * * * * * *  dp1[0][k]


dp[i][k] = sum{dp1[j][k]} j = 0,1,2,3,...,i-1

sum1[i][k] -> presum of dp1[i][k]
sum0[i][k] -> presum of dp1[i][k]


"""


class SolutionTLE:
    def numberOfSets(self, n: int, K: int) -> int:

        mod = 10 ** 9 + 7
        dp0 = [[0 for i in range(1001)] for j in range(1001)]
        dp1 = [[0 for i in range(1001)] for j in range(1001)]
        sum0 = [[0 for i in range(1001)] for j in range(1001)]
        sum1 = [[0 for i in range(1001)] for j in range(1001)]

        for i in range(n):
            dp0[i][0] = 1
            sum0[i][0] = i + 1


        for i in range(1, n+ 1):
            for k in range(1, min(i, K) + 1):
                dp1[i][k] = sum0[i - 1][k - 1] + sum1[i - 1][k - 1]
                dp0[i][k] = sum1[i - 1][k]

                sum0[i][k - 1] = sum0[i - 1][k - 1] + dp0[i][k - 1]
                sum1[i][k] = sum1[i - 1][k] + dp1[i][k]

                sum0[i][k - 1] %= mod
                sum1[i][k] %= mod

        return (dp0[n - 1][K] + dp1[n - 1][K]) % mod



class Solution1:
    def numberOfSets(self, n: int, K: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for i in range(1001)] for j in range(1001)]
        sum = [[0 for i in range(1001)] for j in range(1001)]

        for i in range(n):
            dp[i][0] = 1
            sum[i][0] = i + 1

        for i in range(1, n + 1):
            for k in range(1, min(i, K) + 1):
                dp[i][k] += sum[i - 1][k - 1]
                dp[i][k] += dp[i - 1][k]
                dp[i][k] %= mod

                sum[i][k] = sum[i - 1][k] + dp[i][k]
                sum[i][k] %= mod

        return dp[n - 1][K] % mod


class Solution2:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dp(i, k, isStart):
            # Found a way to draw k valid segment
            if k == 0:
                return 1
            # reach the end of points
            if i == n:
                return 0
            res = dp(i + 1, k, isStart)
            if isStart:
                res += dp(i + 1, k, False)
            else:
                res += dp(i, k - 1, True)
            return res % mod

        return dp(0, k, True)


class SolutionHuahuaTLE:
    def numberOfSets(self, n: int, k: int) -> int:

        mod = 10 ** 9 + 7
        @functools.lru_cache(None)
        def dp(n, k):
            if k >= n:
                return 0
            if k == 1:
                return n * (n - 1) // 2

            if k == n - 1:
                return 1

            res = 0
            for i in range(2, n):
                res += (i - 1) * dp(n - i + 1, k - 1)
                res %= mod
            return res

        return dp(n, k)


class SolutionHuahua2:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for j in range(1, k + 1):
            summ = 0
            for i in range(1, n + 1):
                dp[i][j] = (summ + dp[i - 1][j]) % mod
                summ = (summ + dp[i][j - 1]) % mod
        return dp[n][k]

