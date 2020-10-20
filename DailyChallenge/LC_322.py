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


