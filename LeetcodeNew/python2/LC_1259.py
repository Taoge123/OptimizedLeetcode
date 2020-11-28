"""

Solution 1: DP
dp[n] is the number of shaking ways of n pairs people
In the the view of first people in these n pairs,
he/she can choose anyone, split i pairs on his left and n - 1 - i pairs on his right.

So here comes the equation of dynamic programme:
dp[n + 1] = dp[0] * dp[n] + dp[1] * dp[n - 1] + ..... + dp[n] * dp[0]

The first person and the person he shakes hand with divide the group into two parts.
These two parts are the sub-problems. Let dp[n] be the number of ways they handshakes,
base case: dp[0] = dp[2] = 1,
recurrece relation: dp[n] = sum(dp[i] * dp[n - 2 - i] for i in [0, 2, ..., n - 2]).

"""


class SolutionBottomUp:
    def numberOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        # dp[i] 表示有n对握手
        # dp[n] = dp[0] * dp[n-1] + dp[1] * dp[n-2] + ... + dp[n-1] * dp[0]
        dp = [0] * (n // 2 + 1)
        dp[0] = 1

        for k in range(1, n // 2 + 1):
            for i in range(k):
                dp[k] = (dp[k] + dp[i] * dp[k - 1 - i]) % mod

        return dp[n // 2]



class Solution:
    def numberOfWays(self, num_people: int) -> int:
        self.memo = {0 : 1}
        return self.dp(num_people)

    def dp(self, n):
        if n in self.memo:
            return self.memo[n]
        else:
            res = 0
            for i in range(2, n+1, 2):
                res += self.dp(i - 2) * self.dp(n - i) % (10 ** 9 + 7)
        self.memo[n] = res % (10 ** 9 + 7)
        return self.memo[n]


class SolutionSame:
    def numberOfWays(self, num_people: int) -> int:
        self.memo = {0: 1, 2: 1}
        return self.helper(num_people)

    def helper(self, n):
        mod = 10 ** 9 + 7
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = 0
        for i in range(0, n, 2):
            self.memo[n] = (self.memo[n] + self.helper(i) * self.helper(n - 2 - i)) % mod
        return self.memo[n]




