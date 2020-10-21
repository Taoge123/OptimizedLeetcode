class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        coins.sort()
        dp[0] = 0
        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1




class SolutionTopDown:
    def coinChange(self, coins, amount):
        memo = {0: 0}
        coins.sort()
        res = self.dfs(coins, amount, memo)
        if res == float('inf'):
            return -1
        return res

    def dfs(self, coins, amount, memo):
        if amount in memo:
            return memo[amount]

        res = float('inf')

        for coin in coins:
            if amount - coin < 0:
                break
            res = min(res, self.dfs(coins, amount - coin, memo) + 1)

        memo[amount] = res
        return res

