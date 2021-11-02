
"""
https://www.youtube.com/watch?v=HTnIFivp0aw

这是一道简单但是比较有趣的题目。DP的方法还是比较容易想到的。令dp[k]表示当前拨号数字为ｋ的方案数，显然它取决于在按ｋ之前的那个数字的拨号方案数之和。

举个例子，第i次拨号时的dp[4]就等于第i-1次拨号时的dp[0]+dp[3]+dp[9]，这是因为在盘面上骑士只能从０，３，９这三个位置跳跃到４．
"""


class SolutionTD:
    def knightDialer(self, n):
        table = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4],
                 0: [4, 6]}
        self.mod = 10 ** 9 + 7
        res = 0
        memo = {}
        for i in range(10):
            res += self.dfs(n - 1, i, table, memo)
            res %= self.mod
        return res

    def dfs(self, n, node, table, memo):
        if (n, node) in memo:
            return memo[(n, node)]
        if n == 0:
            return 1

        res = 0
        for nei in table[node]:
            res += self.dfs(n - 1, nei, table, memo)
            res %= self.mod
        memo[(n, node)] = res
        return res



class Solution:
    def knightDialer(self, N):

        table = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4],
                 0: [4, 6]}
        mod = 10 ** 9 + 7
        dp = [1] * 10
        for _ in range(N - 1):
            newDP = [0] * 10
            for i in range(10):
                for j in table[i]:
                    newDP[j] += dp[i]
            dp = newDP

        return sum(dp) % (mod)




