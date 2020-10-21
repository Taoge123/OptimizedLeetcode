
class Solution:
    def findDerangement(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % mod

        return dp[-1]



class SolutionStackOverflow:
    def findDerangement(self, n):
        memo = {}
        self.mod = 1000000007
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        print(n)
        if n == 0:
            return 1
        if n == 1:
            return 0

        if n in memo:
            return memo[n]

        memo[n] = (n - 1) * (self.dfs(n - 1, memo) + self.dfs(n - 2, memo)) % self.mod
        return memo[n]


n = 990
a = SolutionStackOverflow()
print(a.findDerangement(n))

