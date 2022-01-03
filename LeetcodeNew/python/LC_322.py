

"""You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

import functools


class SolutionDFS:
    def coinChange(self, coins, amount: int) -> int:
        if amount < 1:
            return 0

        @functools.lru_cache(None)
        def dfs(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return float('inf')

            res = float('inf')
            for coin in coins:
                res = min(res, dfs(remain - coin) + 1)

            return res

        res = dfs(amount)
        return res if res != float('inf') else -1




class SolutionDFS2:
    def coinChange(self, coins, amount: int) -> int:
        if amount < 1:
            return 0

        memo = {}
        res = self.dfs(coins, amount, memo)
        return res if res != float('inf') else -1

    def dfs(self, coins, remain, memo):
        if remain in memo:
            return memo[remain]

        if remain == 0:
            return 0

        if remain < 0:
            return float('inf')

        res = float('inf')
        for coin in coins:
            res = min(res, self.dfs(coins, remain - coin, memo) + 1)

        memo[remain] = res
        return res



class Solution2:
    def coinChange(self, coins, amount: int) -> int:
        cache = {}
        cache[0] = 0
        return self.helper(coins, amount, cache)

    def helper(self, coins, amount, cache):
        if amount in cache:
            return cache[amount]
        mini = amount + 1
        for coin in coins:
            if amount >= coin:
                count = 1
                left = self.helper(coins, amount - coin, cache)
                if left != -1:
                    count += left
                    mini = min(mini, count)
        cache[amount] = mini if mini != amount + 1 else -1
        return cache[amount]


class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]



coins = [6,12,2,5]
amount = 11
a = SolutionDFS2()
print(a.coinChange(coins, amount))




